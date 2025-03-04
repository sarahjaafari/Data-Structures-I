"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sara Aljaafari
ID:      169044425
Email:   alja4425@mylaurier.ca
__updated__ = '2023-04-02'
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set
from functions import insert_words,comparison_total
fn = "gibbon.txt"
fv = open(fn, "r", encoding="utf-8")
hs = Hash_Set(20)
insert_words(fv,hs)
total,max_word = comparison_total(hs)
fruits = {"apple":"green","banana":"yellow"}
x = list(fruits.values())
fruits["apple"] = "hip"
print(fruits.pop("apple"))
print("Using array-based list Hash_Set")
print()
print("Total Comparisons: {:,}".format(total))
print("Word with maximum comparisons '{}': {:,}".format(max_word.word,max_word.comparisons))
hs.debug()
