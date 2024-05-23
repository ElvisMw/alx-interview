#!/usr/bin/python3
"""
Module for validating UTF-8 data
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    """ Masks to check the first byte and the continuation bytes """
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            """ Count the number of leading 1's in the first byte """
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if num_bytes == 0:
                continue

            # Invalid scenarios for first byte
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check continuation bytes: they must start with '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
