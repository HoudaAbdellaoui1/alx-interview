#!/usr/bin/python3
def canUnlockAll(boxes):
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
