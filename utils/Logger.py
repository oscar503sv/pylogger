import logging
import os
import traceback

class Logger():

    def __set_logger(self):
        log_directory = 'utils/logs'
        log_filename = 'app.log'

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # create a file handler
        log_path = os.path.join(log_directory, log_filename)
        handler = logging.FileHandler(log_path, encoding='utf-8')
        handler.setLevel(logging.DEBUG)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)

        if (logger.hasHandlers()):
            logger.handlers.clear()

        # add the handlers to the logger
        logger.addHandler(handler)

        return logger
    
    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__set_logger(cls)
            
            if level == 'critical':
                logger.critical(message)
            elif level == 'debug':
                logger.debug(message)
            elif level == 'error':
                logger.error(message)
            elif level == 'info':
                logger.info(message)
            elif level == 'warning':
                logger.warning(message)
            
        except Exception as ex:
            print(traceback.format_exc())
            print(ex)
