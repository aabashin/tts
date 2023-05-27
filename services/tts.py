import os
import torch
import uuid

from config import settings


class TTS:
    """
    synthesize audio from text by neural model
    -------
    Methods:
    -------

        __init__ - load model to RAM an save parameters out stream\n
        synthesize - take text and save audio file\n
    """

    def __init__(self) -> None:
        self.device = torch.device(settings.DEVICE)
        torch.set_num_threads(4)
        torch.backends.quantized.engine = "qnnpack"
        self.local_file = settings.PATH_TTS_MODEL
        self.model = torch.package.PackageImporter(self.local_file).load_pickle(
            "tts_models", "model"
        )
        self.model.to(self.device)
        self.speaker = settings.SPEAKER
        self.sample_rate = int(settings.SAMPLE_RATE)
        self.put_accent = settings.PUT_ACCENT
        self.put_yo = settings.PUT_YO

    def synthesize(self, text: str) -> str:
        if not os.path.exists(settings.LOCAL_OUT_DIR):
            os.mkdir(settings.LOCAL_OUT_DIR)

        temp_file = self.model.save_wav(
            text=text,
            speaker=self.speaker,
            audio_path=f"{settings.LOCAL_OUT_DIR}{uuid.uuid4()}.wav",
            sample_rate=self.sample_rate,
            put_accent=self.put_accent,
            put_yo=self.put_yo,
        )

        return temp_file
