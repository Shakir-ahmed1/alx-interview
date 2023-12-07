#!/usr/bin/python3
""" a module that checks unlockabily"""
def canUnlockAll(boxes):
    """ a function that checks if a box is unlockable"""
    n = len(boxes)
    if n <= 1:
        return True
    opened_boxes = [0, *boxes[0]]
    # A key with the same number as a box opens that box
    for box in range(n):
        if box in boxes and box not in opened_boxes:
            opened_boxes.append(box)
    
    for box in range(n):
        for b in opened_boxes:
            if b < n:
                opened_boxes = list(set(opened_boxes.extend(boxes[b])))
    
    correct_keys = n * [0]
    for box in range(n):
        if box in opened_boxes:
            correct_keys[box] = 1
    
    if 0 in correct_keys:
        return False
    else:
        return True



    # Return True if all boxes can be opened, else return False