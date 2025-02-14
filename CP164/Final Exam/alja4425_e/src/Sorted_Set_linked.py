"""
-------------------------------------------------------
Linked version of the Sorted_Set ADT.
-------------------------------------------------------
Author: Sara Aljaafari
ID:     169044425
Email:  alja4425@mylaurier.ca
__updated__ = "2023-04-14"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class _Set_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a Sorted_Set node that contains a copy of value
        and a link to another Sorted_Set node.
        Use: node = _Set_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (*)
            next_ - another Sorted_Set node (_Set_Node)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            a new _Set_Node object (_Set_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_

class Sorted_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_Set.
        Use: source = Sorted_Set()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            A new linked Sorted_Set object (Sorted_Set)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    # ---------------------------------------------------------
    # Helper Methods

    def _append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the rear of self.
        Private helper method.
        Use: self._append(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            None
        -------------------------------------------------------
        """
        new_node = _Set_Node(value, None)
        if self._rear is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the occurrence of key in self.
        Private helper method.
        Use: prev, curr, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            prev - pointer to node previous to node containing key (_Set_Node)
            curr - pointer to node containing key (_Set_Node)
            index - index of key in self (int)
        -------------------------------------------------------
        """
        index = 0
        prev = None
        curr = self._front
        while curr is not None and curr._value < key:
            index += 1
            prev = curr
            curr = curr._next     
        if curr is None or curr._value > key:
            index = -1
            curr = None
        return prev, curr, index
    
    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        previous, current, index = self._linear_search(key)
        if index >= 0:
            value = current._value
            if previous is None:
                self._front = current._next
            else:
                previous._next = current._next
            if current._next is None:
                self._rear = previous
        else:
            value = None
        return value


    # ---------------------------------------------------------
    # Magic Methods
    
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            the number of values in source (int)
        -------------------------------------------------------
        """
        
        return self._count


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: contains = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            True if source contains key, False otherwise. (bool)
        -------------------------------------------------------
        """

        _, _, index = self._linear_search(key)

        return index > -1
    
    def __eq__(self, target):
        """
        -------------------------------------------------------
        Determines whether two Sorted_Sets are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        -------------------------------------------------------
        Parameters:
            target - a sorted set (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        Examples:
            {1,2,3} == {1,2,3}: True
            {1,2,3} == {1,2,4}: False
            {1,2,3} == {1,2,3,4}: False
        -------------------------------------------------------
        """

        if len(self) != len(target):
            return False
        current_self = self._front
        current_target = target._front
        while current_self is not None:
            if current_self.value != current_target.value:
                return False
            current_self = current_self.next
            current_target = current_target.next
        return True

    # ---------------------------------------------------------
    # Set Manipulation Methods

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            True if source is empty, False otherwise. (bool)
        -------------------------------------------------------
        """
        return self._front is None
    
    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            value - a copy of the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """
        _, current, index = self._linear_search(key)
        
        if index >= 0:
            value = deepcopy(current._value)
            
        else:
            value = None

        return value

    def add(self, value):
        """
        ---------------------------------------------------------
        Adds value to source, allows only one copy of value.
        Contents of source remain sorted.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            added - True if value is added to source, False otherwise (boolean)
        -------------------------------------------------------
        """
        if value in self._value:
            return False

        index = 0
        while index < len(self._value) and self._value[index] < value:
            index += 1

        self._value.insert(index, value)
        return True 

    def discard(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Returns None if no matching value.
        Use: value = source.discard(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            value - the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """
        for value in self._value:
            if value == key:
                self._items.remove(value)
                return value
        return None

    def clear(self):
        """
        -------------------------------------------------------
        Removes all values from source.
        Use: source.clear()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            None
        -------------------------------------------------------
        """
        self._values = []

    # ---------------------------------------------------------
    # Set Creation Methods

    def difference(self, source2):
        """
        -------------------------------------------------------
        Return a new Sorted_Set with copies of values in source1 that are not in source2.
        Values may appear only once in target. Values must be sorted.
        source1 and source2 are unchanged.
        Use: target = source1.difference(source2)
        -------------------------------------------------------
        Parameters:
            source2 - a linked Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            target - the difference of source1 and source2 (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.difference({3,4,5}): {1,2}
            {1,2,3,7,9}.difference({3,4,5}): {1,2,7,9}
            {2,3,4}.difference({1,2,3,4,5}): {}
        -------------------------------------------------------
        """
        target = Sorted_Set()
        node = self._front
        while node is not None:
            if node.value not in source2:
                target.add(node.value)
            node = node.next

        return target

    def isdisjoint(self, target):
        """
        -------------------------------------------------------
        Return True if source has no values in common with target.
        Use: disjoint = source.isdisjoint(target)
        -------------------------------------------------------
        Parameters:
            target - a Sorted_Set to compare against source. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            disjoint - True if source has no values in common with target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.isdisjoint({4,5,6,7}): True
            {1,2,3}.isdisjoint({1,4,5,6,7}): False
        -------------------------------------------------------
        """
        for value in self._value:
            if value in target._value:
                return False
        return True

    def issuperset(self, target):
        """
        ---------------------------------------------------------
        Test whether every value in target is also in source.
        Use: superset = source.issuperset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            superset - True if all values in target are also in source,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issuperset({0,1,2,3,4}): False
            {1,2,3,4,5}.issuperset({1,2,4,5}): True
        -------------------------------------------------------
        """
        for value in target._value:
            if value not in self._value:
                return False
        return True

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the set
        from first to last items.
        Use: for v in set:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌‌‌​​‌​​‌:
            yields
            value - the next value in the set (*)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next
