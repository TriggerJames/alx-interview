#!/usr/bin/python3
"""Lockboxes Module"""


def canUnlockAll(boxes):
    # Start with the first box unlocked
    unlocked = set([0])
    keys = set(boxes[0])
    stack = list(keys)

    while stack:
        current_box = stack.pop()

        if current_box not in unlocked and current_box < len(boxes):
            unlocked.add(current_box)
            for key in boxes[current_box]:
                if key not in unlocked:
                    stack.append(key)

    # Check if we were able to unlock all boxes
    return len(unlocked) == len(boxes)
