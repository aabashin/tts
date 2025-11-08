from services.logger_config import LoggerConfig
from services.web_service import WebService

if __name__ == "__main__":
    logger = LoggerConfig.get_logger()
    logger.info("Starting TTS Service...")
    
    try:
        web_service = WebService()
        web_service.run()
    except Exception as e:
        logger.error(f"Failed to start service: {e}")
        raise