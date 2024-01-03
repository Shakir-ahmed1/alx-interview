#!/usr/bin/python3
""" utf validation module """
def is_btwn(data, bounds):
    if bounds[0] <= data <= bounds[1]:
        return True
    return False

def validUTF8(data):
    """ UTF-8 validator """
    invalid_numbers = [0xC1, 0xC0, 0xF5, 0XF6, 0XF7, 0XF8, 0XF9, 0XFA,
                       0XFB, 0XFC, 0XFD, 0XFE, 0XFF]
    asc = (0x00, 0x7f)
    cont = (0x80, 0xbf)
    len2 = (0xc2, 0xdf)
    len31 = (0xe1, 0x3c)
    len32 = (0x3e, 0x3f)
    temp = []
    for d in data:
        if not 256 > d >= 0:
            return False
        if not temp:
            if is_btwn(d, asc):
                continue
            if is_btwn(d, cont):
                return False
            if is_btwn(d, len2) or is_btwn(d, len31) or is_btwn(d, len32):
                temp.append(d)
        else:
            if is_btwn(d, asc):
                temp = []
                continue
            if is_btwn(d, cont):
                temp.append(d)
                continue
            if is_btwn(d, len2) or is_btwn(d, len31) or is_btwn(d, len32):
                continue
            if d in invald:
                return False
    return True
