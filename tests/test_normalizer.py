def test_normalizer_with_text(test_normalizer):
    result_text = test_normalizer.norm_text("тест")

    assert result_text == "тест"


def test_normalizer_with_numbers(test_normalizer):
    result_text = test_normalizer.norm_text("вчера 23 сентября я выиграл 1 млн рублей")

    assert (
        result_text == "вчера двадцать третьего сентября я выиграл один миллион рублей"
    )
