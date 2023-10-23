# frozen set cum e tupla pentru liste

def GetOperationSetsOverLists(a: list, b: list) -> list[set]:
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    difference_a = set(a) - set(b)
    difference_b = set(b) - set(a)
    return [intersection, union, difference_a, difference_b]


# print(GetOperationSetsOverLists([1, 2, 3], [2, 3, 4]))

def GetNumberOfLettersInWordDictionary(word: str) -> dict[str, int]:
    return {letter: word.count(letter) for letter in set(word)}

# print(GetNumberOfLettersInWordDictionary("ana are mere"))
