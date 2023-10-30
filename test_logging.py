import logging
import sys

class MyFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        record.color =  "\033[31m"
        return True


def config_logging(file_name: str, console_level: int=logging.INFO, file_level: int=logging.DEBUG):
    file_handler = logging.FileHandler(file_name, mode='w', encoding="utf8")
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s\t[%(name)s %(levelname)s]\t(%(module)s: %(lineno)d):\t%(message)s'
        ))
    file_handler.setLevel(file_level)
    file_handler.addFilter(MyFilter())

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter('%(color)s[%(name)s %(levelname)s] %(message)s'))
    console_handler.setLevel(console_level)
    console_handler.addFilter(MyFilter())

    my_logger = logging.getLogger("AUTO_PWR")

    my_logger.setLevel(min(console_level, file_level))
    my_logger.addHandler(file_handler)
    my_logger.addHandler(console_handler)
        
    
    return my_logger

if __name__ == '__main__':
    logger = config_logging("test.log", logging.INFO, logging.DEBUG)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.critical("critical")

    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.critical("critical")
    
    b = 0
    try:
        a = 2/b
    except:
        logger.exception("exception occurred")