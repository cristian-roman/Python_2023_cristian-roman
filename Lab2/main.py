# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from typing import List, Any


def GetFirstNNumberFromFibonacci(n: int) -> list:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result


def FindPrimeNumbers(numbers: list) -> list:
    result = []
    for number in numbers:
        if IsPrimeNumber(number):
            result.append(number)
    return result


def IsPrimeNumber(number: int) -> bool:
    if number == 0 or number == 1:
        return False
    if number == 2:
        return True
    if (number % 2 == 0):
        return False
    for i in range(3, int(np.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def ListExtractor(a: list, b: list) -> list[list[int]]:
    # A collection intersect with B collection
    lists = []
    intersect_result = []
    for i in a:
        for j in b:
            if i == j:
                intersect_result.append(i)
    lists.append(intersect_result)

    # a - b
    a_minus_b_result = []
    for i in a:
        if i not in intersect_result:
            a_minus_b_result.append(i)
    lists.append(a_minus_b_result)

    # b - a
    b_minus_a_result = []
    for i in b:
        if i not in intersect_result:
            b_minus_a_result.append(i)
    lists.append(b_minus_a_result)

    # a union b
    union_result = []
    for i in a:
        union_result.append(i)
    for i in b:
        if i not in union_result:
            union_result.append(i)
    lists.append(union_result)

    return lists


def ComposeSong(music_syllabus: list, steps: list, startingPosition: int) -> list:
    result = [music_syllabus[startingPosition]]
    position = startingPosition
    for step in steps:
        position = (position + step) % len(music_syllabus)
        result.append(music_syllabus[position])
    return result


def ReplaceElementsUnderFirstDiagonal(matrx: list[list]) -> list[list]:
    for i in range(len(matrx)):
        for j in range(len(matrx[i])):
            if i > j:
                matrx[i][j] = 0
    return matrx


def GetNumbersAppearingXTimes(*collection: list[Any], x: int) -> list[Any]:
    result = []
    first_list = collection[0]
    for comparison_element in first_list:
        count = 1
        for i in range(1, len(collection)):
            for element in collection[i]:
                if comparison_element == element:
                    count += 1
        if count == x:
            result.append(comparison_element)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(GetFirstNNumberFromFibonacci(10))
    # print(FindPrimeNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 31]))
    # print(ListExtractor([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    # print(ComposeSong(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    # print(ReplaceElementsUnderFirstDiagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(GetNumbersAppearingXTimes([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))
