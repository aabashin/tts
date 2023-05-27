import os

from config import settings


class FileService:
    """
    Service for make action with files
    -------
    Methods:
    -------

    remove_temp_file - delete file by path and return result - string type
    """

    def remove_temp_file(self, file_path: str) -> str:
        try:
            os.remove(file_path)
            return settings.RM_FILE_OK
        except Exception as e:
            return " ".join([settings.RM_FILE_ERROR, str(e)])
