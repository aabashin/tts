import os


def test_tts(tts_service):
    serv = tts_service
    test_file = serv.synthesize("пример произношения текста")
    check_file = os.path.exists(f"{test_file}")
    assert check_file == 1

    os.remove(test_file)
