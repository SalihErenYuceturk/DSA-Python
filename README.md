From the book "Problem Solving with Algorithms and Data Structures using Python".

# 1 - Linear Data Structures

## 1.1 - Stack
Ordered. Last in, first out.

Methods:
- Stack() - Create and return an empty stack.
- push(item_in) - Add item_in to the top of the stack. 
- pop() - Remove the top item from the stack and return that item.
- peek() - Return the top item.
- is_empty() - Return True if the stack is empty. Else False.
- size() - Return the number of items in the stack. 

## 1.2 - Queue
Ordered. First in, first out.

Methods:
- Queue() - Create and return an empty queue.
- enqueue(item_in) - Add item_in to the rear of the queue.
- dequeue() - Remove the front item from the queue and return that item.
- is_empty() - Return True if the queue is empty. Else False.
- size() - Return the number of items in the queue.

## 1.3 - Deque
Ordered. Elements can be added to the rear and front. They can also be removed from either side.

Methods:
- Deque() - Create and return an empty deque.
- add_front(item_in) - Add item_in to the front of the deque.
- add_rear(item_in) - Add item_in to the rear of the deque.
- remove_front() - Remove the front item from the deque and return that item.
- remove_rear() - Remove the rear item from the deque and return that item.
- is_empty() - Return True if the deque is empty. Else False.
- size() - Return the number of items in the deque.

## 1.4 - Unordered List
Collection of related items that have no special order or sequence.

Methods:
- UnorderedList() - Create and return an empty list.
- add(item_in) - Add item_in to the list. Assume item_in is not already in the list.
- remove(item_in) - Remove item_in from the list. Assume item_in is present in the list.
- search(item_in) - Return True if the item is in the list. Else False.
- is_empty() - Return True if the list is empty. Else False.
- size() - Return the number of items in the list.
- append(item_in) - Add item_in to the front of the list. Assume item_in is not present in the list.
- index(item_in) - Return the position of item_in. Assume item_in is present in the list.
- insert(index_in, item_in) - Add item_in to the list at index_in. Assume item_in is not present in the list.
- pop() - Remove the front item from the list and return that item. Assume the list is not empty.
- pop(index_in) - Remove and return the item at index_in. Assume the item is in the list.

## 1.5 - Ordered List
Collection of related items where each item holds a relative position that is based upon some underlying 
characteristic. Often either ascending or descending.

Methods:
- OrderedList() - Create and return an empty ordered list.
- add(item_in) - Add item_in to the list. Assume item_in is not already in the list.
- remove(item_in) - Remove item_in from the list. Assume item_in is present in the list.
- search(item) - Return True if the item is in the list. Else False.
- is_empty() - Return True if the list is empty. Else False.
- size() - Return the number of items in the list.
- index(item_in) - Return the position of item_in in the list. Assume item_in is present in the list.
- pop() - Remove the front item from the list and return that item. Assume the list is not empty.
- pop(index_in) - Remove and return the item at index_in. Assume the item is in the list.

# 2 - The Three Laws Of Recursion
1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.

# 3 - Searching And Sorting

## 3.1 - Searching Algorithms

### 3.1.1 - Sequential Search
For each item in the list, compare it to the search item. If they match, return True, else look at the next item. If 
all items have been checked and there is no match, return False. The time complexity is O(n).

### 3.1.2 - Binary Search
Assuming that the list is ordered, check the middle term. If the item is the correct one, return True, else 
depending on the nature of ordering, eliminate half of the list and check the middle item of that. Time complexity 
is O(log(n)).

### 3.1.3 - Hashing
Hashing is the process of converting a given key into a value. Through hashing, a data structure that can be 
searched in O(1) can be built. A hash table need to be created for this. A hash table is a collection of items which 
are stored in such a way as to make it easy to find them later. Each position has a key and value. Retrieving the 
value assigned to a key takes only a time complexity of O(1). For this to be done successfully the correct key and 
value must be mapped together. This is done through a hash function. 

If two values end up having the same key, this is called a collusion. It is possible to write a function that avoids 
this if we know the value set beforehand, and that it will not change.

Methods:
- Map(size_in) - Create a new empty map with a given size. Returns an empty map collection.
- put(key_in, value_in) - Add a new key-value pair to the map. If the key is already in the map replace the old 
  value with the new value.
- get(key_in) - Given a key, return the value stored in the map or None otherwise.
- del - Delete the key-value pair from the map using a statement of the form del map[key].
- len() - Return the number of key-value pairs stored in the map.
- in - Return True for a statement of the form key in map, if the given key is in the map, else False.

## 3.2 - Sorting Algorithms

### 3.2.1 - Bubble Sort
Compare every item with the one after it. Swap if the item is bigger than the one after it. Go on to the next. Keep 
scanning the list as such until every item is in the correct order. The time complexity is O(n^2).

### 3.2.2 - Selection Sort
Scan through the list, select the highest value, and swap it with the end of the list. Repeat the process for the 
list, without the sorted parts with ever iteration. The time complexity is O(n^2), but this algorithm performs 
better than bubble sort.

### 3.2.3 - Insertion Sort
Starting from one side of the list, a sublist of sorted items is made. Each new item is put in the correct position, 
and the sublist grows until the entire list is sorted. The time complexity is O(n^2), but like the last one, it 
tends  to perform better than the prior two.

### 3.2.4 - Shell Sort
An optimisation of insertion sort. Break the list into smaller lists of items of a certain increment. Sort these 
lists using insertion sort. Merge them and sort the final list using insertion sort. Although the worst case time 
complexity of this algorithm is O(n^2), it often performs close to O(n^(3/2)).

### 3.2.5 - Merge Sort
A recursive algorithm that continually splits the list in half. If the list is empty or has one item, it is sorted 
(base case). If the list has multiple items, merge sort is invoked on them. Once both halves are sorted, they are 
merged. The time complexity is O(n*log(n)).

### 3.2.6 - Quick Sort
Select a pivot item. Put this item in the correct position in the list. Divide the list on the pivot and apply the 
same algorithm on those lists. The average time complexity is O(n*log(n)).

# 4 - Trees And Tree Algorithms

## Binary Heap
Methods:
- BinaryHeap() - Create a new, empty binary heap.
- insert(item_in) - Add a new item to the heap.
- find_min() - Return the item with the minimum key value.
- del_min() - Return the item with the minimum key value, removing the item from the heap.
- is_empty() - Return True if the heap is empty, else False.
- size() - Return the number of items in the heap.
- build_heap(list_in) - Build a new heap from a list of keys.

## Search Tree
Methods:
- Map() - Create a new, empty map.
- put(key_in, value_in) - Add a new key-value pair to the map. If the key is already in the map then replace the old 
  value with the new value.
- get(key_in) - Given a key, return the value stored in the map, else None.
- del - Delete the key-value pair from the map using a statement of the form del map[key].
- len() - Return the number of key-value pairs stored in the map.
- in - Return True for a statement of the form key in map, if the given key is in the map.

## AVL Tree
