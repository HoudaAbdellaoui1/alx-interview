#!/usr/bin/python3
"""
This module provides a function to determine whether all locked boxes can be
opened given a set of keys inside some of the boxes.

A box is opened using a key with the same number as the box. Initially, only
the first box (box 0) is unlocked. The goal is to determine if all the boxes
can eventually be unlocked.

The function uses a depth-first search (DFS) approach to simulate the process
of unlocking boxes and collecting keys.

Function:
    canUnlockAll(boxes): Determines if all the boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each index represents a box
        and each element is a list of keys contained in that box. The keys are
        represented by integers, and a key with value 'i' unlocks the box with
        the index 'i'.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    n = len(boxes)
    unlocked = [False] * n  # list to track which boxes are unlocked
    unlocked[0] = True  # first box is unlocked
    stack = [0]  # stack to iterate through the boxes

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
