# frozen set cum e tupla pentru liste
# operatorul ** pentru dictionarii in functie

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


def CompareTwoLists(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    if len(a) == 0:
        return True

    if a[0] is dict:
        for i in range(len(a)):
            if not CompareTwoDictionaries(a[i], b[i]):
                return False
    elif a[0] is list:
        for i in range(len(a)):
            if not CompareTwoLists(a[i], b[i]):
                return False
    elif a[0] is set:
        for i in range(len(a)):
            if not CompareTwoSets(a[i], b[i]):
                return False
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
    return True


def CompareTwoSets(a: set, b: set) -> bool:
    if len(a) != len(b):
        return False
    for element in a:
        if element not in b:
            return False
    return True


def CompareTwoDictionaries(a: dict, b: dict) -> bool:
    if len(a) != len(b):
        return False
    ans: bool = True
    for key in a.keys():
        if key not in b.keys():
            return False
        if a[key] != b[key]:
            return False
        if a[key] is dict:
            ans &= CompareTwoDictionaries(a[key], b[key])
        elif a[key] is list:
            ans &= CompareTwoLists(a[key], b[key])
        elif a[key] is set:
            ans &= CompareTwoSets(a[key], b[key])
        else:
            ans &= a[key] == b[key]
    return ans


first_list = tuple[1, 2, 3, 4, 5]
second_list = tuple[1, 2, 3, 4, 5]

first_set = {1, 2, 3, 4, first_list}
second_set = {1, 2, 3, 4, second_list}

first_dict = {"a": 1, "b": first_set, "c": first_list}
second_dict = {"a": 1, "b": second_set, "c": second_list}

print(CompareTwoDictionaries(first_dict, second_dict))
