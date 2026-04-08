import re
from config import settings


class Normalizer:
    """Normalize input text and replace russian numeral written digits on word written numbers"""

    def __init__(self, device="cpu") -> None:
        self.device = device

    def norm_text(self, text: str) -> str:
        """Основной метод нормализации текста"""
        # Очистка текста
        text = self._clean_text(text)
        # Преобразование чисел в текст
        text = self._convert_numbers_to_text(text)
        return text

    def _clean_text(self, text: str) -> str:
        """Очистка текста от лишних символов"""
        # Оставляем только русские буквы, цифры, пробелы и основные знаки препинания
        allowed_chars = r"[^а-яёА-ЯЁ0-9\s\.,!?;:\-\(\)\"\'«»—]"
        text = re.sub(allowed_chars, " ", text)
        # Заменяем множественные пробелы на один
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def _convert_numbers_to_text(self, text: str) -> str:
        """Преобразует числа в текстовое представление"""

        def replace_number(match):
            number_str = match.group()
            try:
                number = int(number_str)
                return self._number_to_words(number)
            except ValueError:
                return number_str

        # Ищем и заменяем все целые числа в тексте
        return re.sub(r"\b\d+\b", replace_number, text)

    def _number_to_words(self, n: int) -> str:
        """Конвертирует число в текст на русском языке"""
        if n == 0:
            return "ноль"

        # Единицы
        units = [
            "",
            "один",
            "два",
            "три",
            "четыре",
            "пять",
            "шесть",
            "семь",
            "восемь",
            "девять",
        ]
        # 10-19
        teens = [
            "десять",
            "одиннадцать",
            "двенадцать",
            "тринадцать",
            "четырнадцать",
            "пятнадцать",
            "шестнадцать",
            "семнадцать",
            "восемнадцать",
            "девятнадцать",
        ]
        # Десятки
        tens = [
            "",
            "",
            "двадцать",
            "тридцать",
            "сорок",
            "пятьдесят",
            "шестьдесят",
            "семьдесят",
            "восемьдесят",
            "девяносто",
        ]
        # Сотни
        hundreds = [
            "",
            "сто",
            "двести",
            "триста",
            "четыреста",
            "пятьсот",
            "шестьсот",
            "семьсот",
            "восемьсот",
            "девятьсот",
        ]

        if n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (" " + units[n % 10] if n % 10 != 0 else "")
        elif n < 1000:
            return hundreds[n // 100] + (
                " " + self._number_to_words(n % 100) if n % 100 != 0 else ""
            )
        else:
            # Для чисел больше 1000 используем упрощенный вариант
            return self._large_number_to_words(n)

    def _large_number_to_words(self, n: int) -> str:
        """Обработка больших чисел (тысячи и больше)"""
        if n < 1000000:
            # Тысячи
            thousands = n // 1000
            remainder = n % 1000

            if thousands == 1:
                thousand_text = "тысяча"
            elif 2 <= thousands <= 4:
                thousand_text = self._number_to_words(thousands) + " тысячи"
            else:
                thousand_text = self._number_to_words(thousands) + " тысяч"

            if remainder > 0:
                return thousand_text + " " + self._number_to_words(remainder)
            else:
                return thousand_text
        else:
            # Для очень больших чисел возвращаем как строку
            return str(n)


# Альтернативная версия с улучшенной обработкой склонений
class AdvancedNormalizer(Normalizer):
    """Улучшенный нормалайзер с лучшей обработкой числительных"""

    def _number_to_words(self, n: int) -> str:
        """Улучшенная конвертация чисел с правильными склонениями"""
        if n == 0:
            return "ноль"

        # Базовые словари
        units_female = [
            "",
            "одна",
            "две",
            "три",
            "четыре",
            "пять",
            "шесть",
            "семь",
            "восемь",
            "девять",
        ]
        units_male = [
            "",
            "один",
            "два",
            "три",
            "четыре",
            "пять",
            "шесть",
            "семь",
            "восемь",
            "девять",
        ]
        teens = [
            "десять",
            "одиннадцать",
            "двенадцать",
            "тринадцать",
            "четырнадцать",
            "пятнадцать",
            "шестнадцать",
            "семнадцать",
            "восемнадцать",
            "девятнадцать",
        ]
        tens = [
            "",
            "",
            "двадцать",
            "тридцать",
            "сорок",
            "пятьдесят",
            "шестьдесят",
            "семьдесят",
            "восемьдесят",
            "девяносто",
        ]
        hundreds = [
            "",
            "сто",
            "двести",
            "триста",
            "четыреста",
            "пятьсот",
            "шестьсот",
            "семьсот",
            "восемьсот",
            "девятьсот",
        ]

        def convert_triplet(num, is_female=False):
            """Конвертирует трехзначное число"""
            units_dict = units_female if is_female else units_male
            result = []

            if num >= 100:
                result.append(hundreds[num // 100])
                num %= 100

            if num >= 20:
                result.append(tens[num // 10])
                num %= 10
                if num > 0:
                    result.append(units_dict[num])
            elif num >= 10:
                result.append(teens[num - 10])
            elif num > 0:
                result.append(units_dict[num])

            return " ".join(result)

        # Обработка тысяч
        if n < 1000:
            return convert_triplet(n)
        elif n < 1000000:
            thousands = n // 1000
            remainder = n % 1000

            thousand_text = convert_triplet(thousands, is_female=True)
            if thousands % 10 == 1 and thousands % 100 != 11:
                thousand_text += " тысяча"
            elif 2 <= thousands % 10 <= 4 and not 12 <= thousands % 100 <= 14:
                thousand_text += " тысячи"
            else:
                thousand_text += " тысяч"

            if remainder > 0:
                return thousand_text + " " + convert_triplet(remainder)
            else:
                return thousand_text
        else:
            return str(n)
