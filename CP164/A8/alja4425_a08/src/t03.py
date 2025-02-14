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
from Letter import fill_letter_bst
from functions import do_comparisons, comparison_total, letter_table
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"


bst2 = BST()


fill_letter_bst(bst2, DATA2)


letter_table(bst2)
