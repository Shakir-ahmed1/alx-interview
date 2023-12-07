#!/usr/bin/python3
""" a module that checks unlockabily"""


def canUnlockAll(boxes):
    """ a function that checks if a box is unlockable"""
    opened_boxes = {0}
    new_boxes = {0}
    while new_boxes:
        current_boxes = new_boxes.copy()
        new_boxes.clear()

        for box in current_boxes:
            for key in boxes[box]:
                if key < len(boxes) and key not in opened_boxes:
                    opened_boxes.add(key)
                    new_boxes.add(key)

    return len(opened_boxes) == len(boxes)