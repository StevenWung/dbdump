import psycopg2


class Db:
    MySQL = 1
    Postgresql = 2
    conn = None

    def __init__(self, cfg):
        self.config = cfg
        if cfg.type == Db.MySQL:
            pass
        if cfg.type == Db.Postgresql:
            self.conn = psycopg2.connect(user=cfg.user,
                                         password=cfg.password,
                                         host=cfg.host,
                                         port=cfg.port,
                                         database=cfg.database)
