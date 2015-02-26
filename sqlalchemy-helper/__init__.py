'''
Allows setting up the DB connection by the code using this shell API.

@author: chrcoe
'''
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa


APP_NAME = "DBAPI"
__versionnum__ = ('0', '0', '1')
APP_VERSION = '.'.join([i for i in __versionnum__])
__session__ = sessionmaker(expire_on_commit=False)
__engine__ = None


def get_version():  # pragma: no cover
    return APP_VERSION


@contextmanager
def transaction_scope():
    ''' Builds a scope to manage a series of DB operations. '''
    session = __session__()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_engine():
    '''
    Singleton method to return the existing engine or create it if it does
    not already exist.
    '''
    if __engine__:
        return __engine__
    else:
        __setup_engine__()
        return __engine__


def __setup_engine__():
    ''' Sets up the engine for this module. '''
    # pylint: disable=global-statement
    # this is needed in this module specifically to create the engine globally
    global __engine__
    from DBAPI.settings import DATABASE

    if not DATABASE['host']:
        raise AttributeError(
            "DB Settings must be passed to DBAPI.settings.DATABASE"
        )

    # TODO: handle multiple DB types somehow... currently this PostgreSQL
    conn_string = 'postgresql+psycopg2://{}:{}@{}/{}'.format(
        DATABASE['uid'],
        DATABASE['pwd'],
        DATABASE['host'],
        DATABASE['name'],
#         DATABASE['driver'] # for MSSQL via pyodbc
    )
#     __engine__ = sa.create_engine(conn_string, echo=True)
    __engine__ = sa.create_engine(conn_string)
    __session__.configure(bind=__engine__)
