#!/usr/bin/python3
""" a module that checks unlockabily"""
def canUnlockAll(boxes):
    """ a function that checks if a box is unlockable"""
    if not boxes or len(boxes) == 1:
        return True
    locks = len(boxes) * [0]
    pool = [0, *boxes[0]]

    for tries in range(len(boxes)):
        for pl in pool:
            pool.extend(boxes[pl])
            pool = list(set(pool))
    for lp in range(len(boxes)):
        if lp in pool:
            locks[lp] = 1
        else:
            locks[lp] = 0

    if 0 in locks:
        return False
    else:
        return True
