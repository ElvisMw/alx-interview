#!/usr/bin/python3

"""
Check if all the boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Check if all the boxes can be unlocked

    Args:
        boxes (list): list of lists of keys, where each sublist represents
            the keys in a particular box

    Returns:
        bool: True if all the boxes can be unlocked, False otherwise
    """
    if not boxes:
        """ No boxes, no way to unlock them all """
        return False

    e = len(boxes)
    visited = {0}
    keys_queue = list(boxes[0])

    while keys_queue:
        """
        Breadth-first search through the graph of keys

        The graph is represented as a list of lists, where each sublist
        represents the keys in a particular box. The visited set is used to
        keep track of which boxes have already been visited.

        The algorithm starts by adding all the keys in the first box to the
        queue, and then repeatedly dequeues a key and adds all the keys in
        that box to the visited set and the queue, until the queue is empty.
        If at any point the visited set size is equal to the total number of
        boxes, then all the boxes can be unlocked.
        """
        key = keys_queue.pop(0)
        if key < e and key not in visited:
            visited.add(key)
            keys_queue.extend(set(boxes[key]) - visited)

    return len(visited) == e
