def even_number_of_evens(numbers):
    """
    Should there be a need for a reminder;
    1) raise a typeerror is no list is passed into function
    2) if numbers is empty - return False
    3) if number of evens is odd - return False
    4) if number of evens is 0 - return False
    5) if number of evens is even - return True
    """

    if isinstance(numbers, list):
        evens = 0

        print(n for n in numbers)

        for n in numbers:
            if n % 2 == 0:
                evens += 1

        if evens:
            return evens % 2 == 0
        else:
            return False
    else:
        raise TypeError("A list was not passed into tehe function!")


if __name__ == '__main__':
    even_number_of_evens([2, 1, 4])