import inspect
import logging
import os

from elevate import elevate


class Logging(object):
    """Logging class"""

    def log(self, loglevel=logging.DEBUG):
        """logs functions"""
        # set class method from where its called

        try:
            logger_name = inspect.stack()[1][3]
            logger = logging.getLogger(logger_name)
            logger.setLevel(loglevel)

            # create console handler and set level to debug
            fh = logging.FileHandler("test.log")

            # create formatter
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(funcName)s - %(module)s - %(message)s - %(threadName)s')

            fh.setFormatter(formatter)
            logger.addHandler(fh)

        except Exception as e:
            print(e)

        return logger


class Events(object):
    """Events that comes with functions"""

    def elevate(self):
        elevate(show_console=True)


    def get_processes(self):
        pass

log = Logging()
Events = Events()
