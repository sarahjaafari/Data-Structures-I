"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sara Aljaafari
ID:      169044425
Email:   alja4425@mylaurier.ca
__updated__ = '2023-03-13'
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

d = Deque()
d.insert_rear(0)
d.insert_rear(1)
d.insert_rear(2)
d.insert_rear(3)
d.insert_rear(4)
for i in d:
    print(i)
d._swap(d._rear._prev,d._front._next)
print()
for i in d:
    print(i)
