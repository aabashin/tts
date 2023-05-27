import pytest
from config import settings

INVALID_FILE_NAME = "-1"


@pytest.fixture(scope="session")
def create_test_file():
    test_file = open("TestFile.txt", "w+")
    test_file.write("Test")
    test_file.close()


def test_success_remove_file(test_file_service, create_test_file):
    result = test_file_service.remove_temp_file("TestFile.txt")
    assert result == settings.RM_FILE_OK


def test_success_remove_file(test_file_service):
    result = test_file_service.remove_temp_file(INVALID_FILE_NAME)
    assert (
        result
        == f"Error with remove temp file:  [Errno 2] No such file or directory: '{INVALID_FILE_NAME}'"
    )
