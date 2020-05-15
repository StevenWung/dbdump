from libs.db import Db


class DbConfig:
    type = Db.MySQL
    host = None
    user = None
    password = None
    database = None
    port = 0

    def __init__(self, type, host, user, password, database, port=None):
        self.type = type
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        if port is None:
            self.port = 5243 if type == Db.Postgresql else 3306
