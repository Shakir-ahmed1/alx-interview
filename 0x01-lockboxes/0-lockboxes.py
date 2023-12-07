#!/usr/bin/python3
""" a module that checks unlockabily"""


def canUnlockAll(boxes):
    """ a function that checks if a box is unlockable"""
    opened_boxes = {0}

    # Iterate through opened boxes and add new keys to the set
    for box in opened_boxes:
        for key in boxes[box]:
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)