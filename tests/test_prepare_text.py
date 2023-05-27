from services.web_service import preprocessing_text

def test_preprocessing_text(test_text):
    expected_text = "хелло!!! Это тестовая строка! Она для модульного тестирования., четыре:; сорок пять"
    result_text = preprocessing_text(test_text)
    assert expected_text == result_text