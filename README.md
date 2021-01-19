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
