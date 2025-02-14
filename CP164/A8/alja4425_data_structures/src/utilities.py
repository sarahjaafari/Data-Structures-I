"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sara Aljaafari
ID:      169044425
Email:   alja4425@mylaurier.ca
__updated__ = '2023-02-04'
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source) - 1, -1, -1):
        value = source.pop()
        stack.push(value)
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        Numbers = stack.pop()
        target.insert(0, Numbers)
    return

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    for value in source:
        stack.push(value)
    if stack.is_empty():
        print("Stack is empty")
    else:
        print("Stack is not empty")
        value = stack.peek()
        print(value)
        value = stack.pop()
        print(value)
    return

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        value = source.pop()
        queue.insert(value)
    return None

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(queue) > 0:
        value = queue.remove()
        target.append(value)
    return None

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    print("Test is_empty method on an empty queue:", q.is_empty())
    print("Test len method on an empty queue:", len(q))
    
    for value in a:
        q.insert(value)
        print("Inserting value:", value)
        print("Test is_empty method on a non-empty queue:", q.is_empty())
        print("Test len method on a non-empty queue:", len(q))
        print("Test peek method on a non-empty queue:", q.peek())
        
    while not q.is_empty():
        value = q.remove()
        print("Removing value:", value)
        print("Test is_empty method on a non-empty queue:", q.is_empty())
        print("Test len method on a non-empty queue:", len(q))
        
    print("Test is_empty method on an empty queue:", q.is_empty())
    print("Test len method on an empty queue:", len(q))
    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for value in source:
        pq.insert(value)
    source.clear()
    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        value = pq.remove()
    target.append(value)
    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print("Priority Queue is empty:", pq.is_empty())
    for value in a:
        pq.insert(value)
        print("\nPriority Queue after inserts:")
    for value in pq._values:
        print(value)
        print("\nPeek value:", pq.peek())
    while not pq.is_empty():
        value = pq.remove()
        print("\nRemove value:", value)
        print("Priority Queue after remove:")
    for item in pq._values:
        print(item)
    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in source:
        llist.append(i)
    source.clear()
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) > 0:
        target.append(llist.pop(0))
    return

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print("List is empty: ", lst.is_empty())
    print("List length: ", len(lst))

    for movie in source:
        lst.append(movie)

    print("List is empty: ", lst.is_empty())
    print("List length: ", len(lst))
    print("List front: ", lst.front())
    print("List rear: ", lst.rear())
    print("List max: ", lst.max())
    print("List min: ", lst.min())
    print("List count of movie 'The Godfather': ", lst.count('The Godfather'))
    print("List index of movie 'The Godfather': ", lst.index('The Godfather'))
    print("List contents: ", lst)
    lst.remove('The Godfather')
    print("List contents after remove of movie 'The Godfather': ", lst)

    return
    