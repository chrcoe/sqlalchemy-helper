'''
DB settings would go here.

@author: chrcoe
'''

# this should be overwritten by the application such as:
# from DPABPI.settings import DATABASE
#
# DATABASE = myNewDB {
#     'driver': None,
#     'name': db_name,
#     'host': db_host,
#     'uid': db_userid,
#     'pwd': db_passwd,
# }
#
# This needs to be done before calling DBAPI.get_engine()

DATABASE = {
    'driver': None,
    'name': None,
    'host': None,
    'uid': None,
    'pwd': None,
}
