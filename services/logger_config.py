import logging
import os
from config import settings
from logging.handlers import RotatingFileHandler


class LoggerConfig:
    @classmethod
    def get_logger(cls):
        # check if log file not create for local start
        if not os.path.isfile(settings.LOG_FILE):
            if not os.path.exists(settings.LOG_DIR):
                os.mkdir(settings.LOG_DIR)
            else:
                with open(settings.LOG_FILE, "x"):
                    print("log file exists")

        log_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", "%H:%M:%S %d-%m-%Y"
        )
        file_handler = RotatingFileHandler(
            filename=settings.LOG_FILE,
            mode="a",
            maxBytes=5 * 1024 * 1024,
            backupCount=2,
            encoding="utf8",
            delay=0,
        )
        file_handler.setFormatter(log_formatter)
        logger = logging.getLogger()
        logger.addHandler(file_handler)

        if settings.LOG_LEVEL == "debug":
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

        return logger
