import logging
from services.logger_config import LoggerConfig

from config import settings


def test_logger():
    test_logger = LoggerConfig.get_logger()
    expected_logger = logging.Logger(settings.LOG_FILE)
    expected_logger.setLevel(logging.INFO)
    expected_events = expected_logger.level
    result_events = test_logger.level
    assert expected_events == result_events