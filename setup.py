from distutils.core import setup

from DBAPI import APP_NAME, APP_VERSION

setup(
    name=APP_NAME,
    version=APP_VERSION,
    description='Shell API for SQLAlchemy',
    author='Chris Coe',
    author_email='chrcoe@ieee.org',
    packages=[
        'DBAPI',
    ],
)
