import logging


class Logger:
    def __init__(self, filename='dbdump.log'):
        logging.basicConfig(
            filename=filename,
            level=logging.DEBUG,
            format='[%(asctime)s] %(levelname)s  {%(filename)s:%(lineno)d} - %(message)s',
            datefmt='%H:%M:%S'
        )
        logging.getLogger("requests").setLevel(logging.WARNING)

        stderr_logger = logging.StreamHandler()
        stderr_logger.setFormatter(
            logging.Formatter('[%(asctime)s] %(levelname)s  {%(filename)s:%(lineno)d} - %(message)s')
        )
        logging.getLogger().addHandler(stderr_logger)
        logging.getLogger('requests').setLevel(logging.WARNING)
