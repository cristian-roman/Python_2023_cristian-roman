import numpy as np
def GreatestCommonDivisor():
    # reading section
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")

        if user_input == "":
            break
        try:
            read_number = int(user_input)
            numbers.append(read_number)
        except ValueError:
            print("Invalid input")

    # processing section
    if len(numbers) == 0:
        print("No numbers to process")
        return
    if (len(numbers) == 1):
        print("GCD is " + str(numbers[0]))
        return

    a = numbers[0]
    b = numbers[1]
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

    for i in range(2, len(numbers)):
        a = b
        b = numbers[i]
        while r != 0:
            a = b
            b = r
            r = a % b

    # output section
    print("GCD is " + str(b))


def VowelsCalculator():
    # reading section
    user_input = input("Enter a string: ")

    # processing section
    vowels = 0
    for i in range(len(user_input)):
        if user_input[i] in "aeiouAEIOU":
            vowels += 1

    # output section
    print("The number of vowels is " + str(vowels))


def StringOccurrenceCalculator(str1, str2):
    if len(str2) < len(str1):
        return 0
    count = 0
    for i in range(len(str2)):
        if str2[i] == str1[0]:
            for j in range(len(str1)):
                if str2[i + j] != str2[j]:
                    break
                if j == len(str1) - 1:
                    count += 1
    return count


def TurnTo_lowercase_with_underscore(UpperCamelCaseString):
    lower_case_string = ""
    for i in range(len(UpperCamelCaseString)):
        if UpperCamelCaseString[i].isupper():
            if i != 0:
                lower_case_string += "_" + UpperCamelCaseString[i].lower()
            else:
                lower_case_string += UpperCamelCaseString[i].lower()
        else:
            lower_case_string += UpperCamelCaseString[i]
    return lower_case_string


def MatrixRunner(matrx):
    begin = 0
    end = len(matrx)

    while 1:
        for j in range(begin, end):
            print(matrx[begin][j], end="")
        for i in range(begin + 1, end):
            print(matrx[i][end - 1], end="")
        for j in range(end - 2, begin - 1, -1):
            print(matrx[end - 1][j], end="")
        for i in range(end - 2, begin, -1):
            print(matrx[i][begin], end="")
        begin += 1
        end -= 1
        if begin >= end:
            break

def IsNumberPalindrome(n):
    if n < 0:
        return False
    if n < 10:
        return True
    if n % 10 == 0:
        return False
    reverse = 0
    cn = n
    while n > reverse:
        reverse = reverse * 10 + n % 10
        n //= 10
    return n == reverse or n == reverse // 10

def ExtractNumberFromString(str):
    number = ""
    for i in range(len(str)):
        if str[i].isdigit():
            while str[i].isdigit():
                number += str[i]
                i += 1
            break
    return int(number)

def CountBitsOf1FromNumber(nr):
    count = 0
    while nr > 0:
        if nr & 1:
            count += 1
        nr >>= 1
    return count

def GetTheMostImportantLetter_CaseInsensitive(str):
    dict = {}
    for i in range(len(str)):
        if str[i].isalpha():
            if str[i].lower() in dict:
                dict[str[i].lower()] += 1
            else:
                dict[str[i].lower()] = 1

    max = 0
    for key in dict:
        if dict[key] > max:
            max = dict[key]
            letter = key
    return letter

def CountWords(str):
    count = 0
    for i in range(len(str)):
        if str[i] == " ":
            count += 1
    return count + 1

if __name__ == '__main__':
    # GreatestCommonDivisor()
    # VowelsCalculator()
    # str1 = input("Enter str1: ")
    # str2 = input("Enter str2: ")
    # print("number of occurrences: ", StringOccurrenceCalculator(str1, str2))
    # print(TurnTo_lowercase_with_underscore("UpperCamelCaseString"))
    # matrix = [
    #     ['f', 'i', 'r', 's'],
    #     ['n', '_', 'l', 't'],
    #     ['o', 'b', 'a', '_'],
    #     ['h', 't', 'y', 'p']
    # ]
    # MatrixRunner(matrix)
    # print(IsNumberPalindrome(12321))
    # print(ExtractNumberFromString("abc123def"))
    #print(CountBitsOf1FromNumber(24))
    #print(GetTheMostImportantLetter_CaseInsensitive("aAAbbbb"))
    print(CountWords("I have Python exam"))

