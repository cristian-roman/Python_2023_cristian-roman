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


if __name__ == '__main__':
    # GreatestCommonDivisor()
    VowelsCalculator()