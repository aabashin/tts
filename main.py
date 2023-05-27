from services.logger_config import LoggerConfig
from services.web_service import WebService

if __name__ == "__main__":
    logger = LoggerConfig.get_logger()
    web_service = WebService()
