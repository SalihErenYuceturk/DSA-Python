From the book "Problem Solving with Algorithms and Data Structures using Python". 

# Linear Data Structures

## Stack
Ordered. Last in, first out.

Methods:
- Stack() - Create and return and empty stack.
- push(item_in) - Add item_in to the top of the stack. 
- pop() - Remove the top item from the stack and return that item.
- peek() - Return the top item.
- is_empty() - Return true if the stack is empty. Else false.
- size() - Return the number of items in the stack. 

## Queue
Ordered. First in, first out.

Methods:
- Queue() - Create and return an empty queue.
- enqueue(item_in) - Add item_in to the rear of the queue.
- dequeue() - Remove the front item from the queue and return that item.
- is_empty() - Return true if the queue is empty. Else false.
- size() - Return the number of items in the queue.

## Deque
Ordered. Elements can be added to the rear and front. They can also be removed from either side.

Methods:
- Deque() - Create and return an empty deque.
- add_front(item_in) - Add item_in to the front of the deque.
- add_rear(item_in) - Add item_in to the rear of the deque.
- remove_front() - Remove the front item from the deque and return that item.
- remove_rear() - Remove the rear item from the deque and return that item.
- is_empty() - Return true if the deque is empty. Else false.
- size() - Return the number of items in the deque.

## Unordered List
Collection of related items that have no special order or sequence.

Methods:
- UnorderedList() - Create and return an empty list.
- add(item_in) - Add item_in to the list. Assume item_in is not already in the list.
- remove(item_in) - Remove item_in from the list. Assume item_in is present in the list.
- search(item_in) - Return true if the item is in the list. Else false.
- is_empty() - Return true if the list is empty. Else false.
- size() - Return the number of items in the list.
- append(item_in) - Add item_in to the front of the list. Assume item_in is not present in the list.
- index(item_in) - Return the position of item_in in the list. Assume item_in is present in the list.
- insert(index_in, item_in) - Add item_in to the list at index_in. Assume item_in is not present in the list.
- pop() - Remove the front item from the list and return that item. Assume the list is not empty.
- pop(index_in) - Remove and return the item at index_in. Assume the item is in the list.

## Ordered List
Collection of related items where each item holds a relative position that is based upon some underlying 
characteristic. Typically either ascending or descending.

Methods:
- OrderedList() - Create and return an empty ordered list.
- add(item_in) - Add item_in to the list. Assume item_in is not already in the list.
- remove(item_in) - Remove item_in from the list. Assume item_in is present in the list.
- search(item) - Return true if the item is in the list. Else false.
- is_empty() - Return true if the list is empty. Else false.
- size() - Return the number of items in the list.
- index(item_in) - Return the position of item_in in the list. Assume item_in is present in the list.
- pop() - Remove the front item from the list and return that item. Assume the list is not empty.
- pop(index_in) - Remove and return the item at index_in. Assume the item is in the list.

# The Three Laws Of Recursion
1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.

# Searching And Sorting

## Searching

### Sequential Search
For each item in the list, compare it to the search item. If they match, return true, else look at the next item. If 
all items have been checked and there is no match, return false. The time complexity is O(n).

### Binary Search
Assuming that the list is ordered, check the middle term. If the item is the correct one, return true, else 
depending on the nature of ordering, eliminate half of the list and check the middle item of that. Time complexity 
is O(log(n)).

### Hashing
Through the use of hashing, a data structure that can be searched in O(1) can be built. A hash table is used for 
this. A hash table is a collection of items which are stored in such a way as to make it easy to find them later. 
Each position has a key and value. Retrieving the value assigned to a key takes only a time complexity of O(1). For 
this to be done successfully, the correct key and value must be mapped together. This is done through a hash 
function. 

If two values end up having the same key, this is called a collusion. It is possible to write a function 
that avoids this if we know the value set beforehand, and that it will not change.

## Sorting

