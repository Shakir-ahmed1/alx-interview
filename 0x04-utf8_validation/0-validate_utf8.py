#!/usr/bin/python3
""" utf validation module """


def status(number):
    if number < 0b10000000:
        return 0
    if 0b10000000 <= number < 0b11000000:
        return 1
    if 0b11000000 <= number < 0b11100000:
        return 2
    if 0b11100000 <= number < 0b11110000:
        return 3
    if 0b11110000 <= number < 0b11111000:
        return 4
    return 5


def validUTF8(data):
    """ UTF-8 validator """
    temp_count = 0
    for d in data:
        d = d % 256
        st = status(d)
        if st == 5:
            return False
        if st == 0 and not temp_count:
            continue

        if not temp_count:
            if st == 1 or temp_count:
                return False
            temp_count = st
        else:
            if st != 1 or not temp_count:
                return False
        temp_count -= 1
    if temp_count != 0:
        return False
    return True
