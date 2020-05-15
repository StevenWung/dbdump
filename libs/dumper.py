import enum
import psycopg2

from libs.db import Db


class Dumper:
    from_db_type = Db.Postgresql

    def __init__(self):
        pass
