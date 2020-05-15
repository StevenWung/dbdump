from optparse import OptionParser


class Configuration:
    parser = OptionParser(usage="Usage: program [options]")

    def __init__(self):
        self.build_parser()

    def build_parser(self):
        self.parser.add_option("-f", "--config", dest="config", help="Configuration file")
        self.parser.add_option("-s", "--host", dest="db_host", help="Database host")
        self.parser.add_option("-u", "--user", dest="db_user", help="Database user")
        self.parser.add_option("-p", "--password", dest="db_password", help="Database password")
