#!/usr/bin/python3
""" utf validation module """


def validUTF8(data):
    """ UTF-8 validator """
    invalid_numbers = [0xC1, 0xC0, 0xF5, 0XF6, 0XF7, 0XF8, 0XF9, 0XFA,
                       0XFB, 0XFC, 0XFD, 0XFE, 0XFF]
    for d in data:
        if not 256 > d >= 0 or d in invalid_numbers:
            return False
    return True
