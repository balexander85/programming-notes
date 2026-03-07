from typing import List

import pytest


def sum_builtin(numbers: List[int]) -> int:
    return sum(numbers)


def sum_for_loop(numbers: List[int]) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


def sum_while_loop(numbers: List[int]) -> int:
    total = 0
    count = 0
    while count < len(numbers):
        total += numbers[count]
        count += 1
    return total


def sum_recursion_pop(numbers: List[int]) -> int:
    total = 0
    if len(numbers) <= 0:
        return total

    index = numbers.pop()

    total = index + sum_recursion_pop(numbers)

    return total


def sum_recursion_pythonic(numbers: List[int]) -> int:
    if not numbers:
        return 0
    return numbers[0] + sum_recursion_pythonic(numbers[1:])


@pytest.mark.parametrize(
    'sum_function',
    [
        sum,
        sum_builtin,
        sum_for_loop,
        sum_while_loop,
        sum_recursion_pop,
        sum_recursion_pythonic
    ]
)
def test_sum_functions(sum_function):
    assert 55 == sum_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert 5 == sum_function([10, -5])
