#!/usr/bin/python3
""" utf validation module """


def validUTF8(data):
    """ UTF-8 validator """
    for d in data:
        if not 256 > d >= 0:
            return False
    return True
