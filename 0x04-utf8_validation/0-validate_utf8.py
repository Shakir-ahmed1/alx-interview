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
    invalid_numbers = [0xC1, 0xC0, 0xF5, 0XF6, 0XF7, 0XF8, 0XF9, 0XFA,
                       0XFB, 0XFC, 0XFD, 0XFE, 0XFF]
    temp = []
    temp_count = 0
    for d in data:
        d = d % 256
        st = status(d)
        if st == 5:
            return False
        if st == 0 and not temp:
            continue

        if not temp:
            if st == 1 or temp_count:
                return False
            temp_count = st
        else:
            if st != 1 or not temp_count:
                return False
        temp_count -= 1
        temp.append(d)
        if temp_count == 0:
            temp = []
    if temp_count != 0:
        return False
    return True
