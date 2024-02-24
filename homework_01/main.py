"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int, div: int = 2) -> bool:
    """
    Функция, которая определяет - просто число или нет
    :param number: число
    :param div: делитель, который нужен для рекурсии (по-умолчанию равен 2)
    :return: True/False
    """
    if number < 2:
        return False
    if div == number:
        return True
    if number % div == 0:
        return False
    return is_prime(number, div + 1)


def filter_numbers(numbers: list, filter_types: str) -> list[int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
