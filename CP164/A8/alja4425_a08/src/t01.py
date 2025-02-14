"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sara Aljaafari
ID:      169044425
Email:   alja4425@mylaurier.ca
__updated__ = '2023-03-27'
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

tree = BST()
tree.insert(5)
tree.insert(6)
tree.insert(3)
tree.insert(1)
tree.insert(4)
tree.insert(8)


'''
print(tree.is_valid())
tree._root._right._value = 4
print(tree.is_valid())
'''
'''
tree2 = BST()
for i in range(1,7):
    tree2.insert(i)
'''
print(tree.levelorder())
tree.remove(3)
print(tree.levelorder())
