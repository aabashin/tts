import pytest

from services.file_service import FileService
from services.normalizer import Normalizer
from services.tts import TTS

@pytest.fixture(scope="session")
def tts_service():
    return TTS()

@pytest.fixture(scope="session")
def test_normalizer():
    return Normalizer()

@pytest.fixture(scope="session")
def test_text():
    return "Hello!!! Это тестовая строка! Она для модульного тестирования., 4:; 45"

@pytest.fixture(scope="session")
def test_file_service():
    return FileService()
