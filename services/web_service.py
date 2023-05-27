import re
from sanic import Sanic
from sanic.response import json
from sanic import response
from config import settings
from services.tts import TTS
from services.normalizer import Normalizer
from services.logger_config import LoggerConfig
from services.file_service import FileService

app = Sanic("tts")
tts_service = TTS()
norm = Normalizer()
logger = LoggerConfig.get_logger()
file_service = FileService()


def preprocessing_text(text: str) -> str:
    """
    prepare text: all numeral written digits changes on
    word written numbers and drop latin symbols
    """
    if set("1234567890") & set(text):
        text = norm.norm_text(text)
    return re.sub("[^А-Яа-яЁё+.,!?…:;_~ ]", "", text).strip()


class WebService:
    """
    Web-server by Sanic

    receive POST request with text, send to TTS service and
    send response with audio

    receive GET request and send the simple message, like ping-pong
    """

    def __init__(self) -> None:
        app.run(
            host=settings.HOST_IP,
            port=int(settings.HOST_PORT),
            auto_reload=settings.RELOAD,
        )

    @app.route("/tts", methods=["POST"])
    async def post_handler(self):
        if "text" in self.json:
            text = preprocessing_text(self.json["text"])

            regex = "^[+.,!?…:;_~ ]+$"
            pattern = re.compile(regex)
            find_symb = pattern.search(text) is not None

            if text == "" or find_symb:
                text = settings.ERROR_RUS_SYMBOL
                logger.error(f"settings.ERROR_RUS_SYMBOL text: {text}")

            logger.debug(f"{settings.MESSAGE_PREPARE}: {text}")
            temp_file = tts_service.synthesize(text)

            logger.debug(f"{settings.MESSAGE_SEND}")
            resp = await response.file(f"{temp_file}")

            if resp.status != 200:
                rm_file = file_service.remove_temp_file(temp_file)
                logger.debug(rm_file)
                logger.error(f"{settings.ERROR_POST_RESPONSE}")
                return json(settings.ERROR_POST_RESPONSE)
            else:
                rm_file = file_service.remove_temp_file(temp_file)
                logger.debug(rm_file)
                return resp

        else:
            logger.error(settings.POST_ERROR)
            return json(settings.POST_ERROR)
