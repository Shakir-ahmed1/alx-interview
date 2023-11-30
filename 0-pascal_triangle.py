""" a module for the implementation of pascal's triangle """


def pascal_triangle(n):
    """ pascals triangle with for nth step"""
    if n <= 0:
        return []
    temp = []
    result = []
    for a in range(n):

        tm = temp.copy()
        temp = []
        for b in range(len(tm) + 1):

            if b == 0:
                temp.append(1)
            elif b != len(tm) and len(tm) > 1:
                temp.append(tm[b - 1] + tm[b])
            else:
                temp.append(1)
        result.append(temp)
    return result
