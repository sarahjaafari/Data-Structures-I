"""
-------------------------------------------------------
Midterm Queue Functions
-------------------------------------------------------
Author: Sara Aljaafari
ID:     169044425
Email:  alja4425@mylaurier.ca
__updated__ = "2023-03-02"
-------------------------------------------------------
"""
from Queue_array import Queue


def queue_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of values in source. When finished, values
    in source are rotated n positions to the right.
    Use: queue_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the Queue to rotate (Queue)
        n - amount to rotate Queue values (int)
    Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
        None
    -------------------------------------------------------
    """
    if n <= 0:
        return
    queue = Queue()
    for i in range(n):
        if source.is_empty():
            break
        value = source.remove()
        queue.insert(value)
    while not source.is_empty():
        value = source.remove()
        source.insert(value)
    while not queue.is_empty():
        value = queue.remove()
        source.insert(value)
