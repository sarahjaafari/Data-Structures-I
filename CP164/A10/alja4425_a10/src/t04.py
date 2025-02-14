"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sara Aljaafari
ID:      169044425
Email:   alja4425@mylaurier.ca
__updated__ = '2023-04-10'
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts

a = Deque()

b = [345, 56, 678, 76, 456, 87, 67, 765]

for n in b:
    a.insert_rear(n)
    
Sorts.gnome_sort(a)

print("sorted linked: {}".format([x for x in a]))
