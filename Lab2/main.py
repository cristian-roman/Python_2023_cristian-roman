# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from typing import Tuple


def GetFirstNNumberFromFibonacci(n: int) -> list[int]:
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


def FindPrimeNumbers(numbers: list[int]) -> list[int]:
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
    if number % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def ListExtractor(a: list[int], b: list[int]) -> list[list[int]]:
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


def ComposeSong(music_syllabus: list[str], steps: list[int], startingPosition: int) -> list[str]:
    result = [music_syllabus[startingPosition]]
    position = startingPosition
    for step in steps:
        position = (position + step) % len(music_syllabus)
        result.append(music_syllabus[position])
    return result


def ReplaceElementsUnderFirstDiagonal(matrx: list[list[int]]) -> list[list[int]]:
    for i in range(len(matrx)):
        for j in range(len(matrx[i])):
            if i > j:
                matrx[i][j] = 0
    return matrx


def GetNumbersAppearingXTimes(*collection: list[int], x: int) -> list[int]:
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


def GetPalindromeData(numbers: list[int]) -> Tuple[int, int]:
    count = 0
    max_palindrome = 0
    for number in numbers:
        reversed_number = GetReversedNumber(number)
        if number == reversed_number:
            count += 1
            if number > max_palindrome:
                max_palindrome = number
    return count, max_palindrome


def GetReversedNumber(number: int) -> int:
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number // 10
    return reversed_number


def GetCharactersBasedOnAsciiCodeDivideRule(x: int = 1, strings: list[str] = None, flag: bool = True) -> list[
    list[str]]:
    result = []
    string_index = 0
    for string in strings:
        result.append(None)
        for character in string:
            if flag:
                if ord(character) % x == 0:
                    to_add = True
                else:
                    to_add = False
            else:
                if ord(character) % x != 0:
                    to_add = True
                else:
                    to_add = False

            if to_add:
                if result[string_index] is None:
                    result[string_index] = []
                result[string_index].append(character)
        string_index += 1
    return result


def GetUnableToViewGameSpectators(matrx: list[list[int]]) -> list[Tuple[int, int]]:
    result = []
    for i in range(1, len(matrx)):
        for j in range(len(matrx[i])):
            if matrx[i - 1][j] > matrx[i][j]:
                result.append((i, j))
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(GetFirstNNumberFromFibonacci(10))
    # print(FindPrimeNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 31]))
    # print(ListExtractor([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    # print(ComposeSong(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    # print(ReplaceElementsUnderFirstDiagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(GetNumbersAppearingXTimes([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))
    # print(GetPalindromeData([123, 121, 989, 989, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123]))
    # print(GetCharactersBasedOnAsciiCodeDivideRule(2, ["test", "hello", "lab002"],False))
    #print(GetUnableToViewGameSpectators([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]]))
