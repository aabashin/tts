import pytest
import sys
import os

# Добавляем корневую директорию проекта в Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.file_service import FileService
from services.normalizer import AdvancedNormalizer
from services.tts import TTS


@pytest.fixture(scope="session")
def tts_service():
    return TTS()


@pytest.fixture(scope="session")
def test_normalizer():
    return AdvancedNormalizer()


@pytest.fixture(scope="session")
def test_text():
    return "Hello!!! Это тестовая строка! Она для модульного тестирования., 4:; 45"


@pytest.fixture(scope="session")
def test_file_service():
    return FileService()
