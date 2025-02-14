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
from List_linked import List
from Sorts_List_linked import Sorts


a = List()
b = [654, 67, 789, 678, 56, 34, 90]

for n in b:
    a.append(n)

Sorts.radix_sort(a)

print("sorted array: {}".format([x for x in a]))
