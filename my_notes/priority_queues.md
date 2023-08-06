# Priority Queues

# [Introduction (video)](https://www.coursera.org/lecture/data-structures/introduction-2OpTs)
## Queue review: 
- Allows for PushBack() (add new element to back of queue) and PopFront() (remove front most element)
    - Uses FIFO (first in first out)
## Priority Queues:
- No such thing as beginning or end of queue
- Supports:
    - Insert(p): insert a new element
    - ExtractMax(): pop element whos priority is maximum
- Use Case:
    - Scheduling Jobs
        - Want to process jobs with max priority
        - Need to be able to processs jobs of highest priority first
        - Need to be able to insert jobs into priority queue

# [CS 61B Lecture 24: Priority Queues (video)](https://archive.org/details/ucberkeley_webcast_yIUFT6AKBGE)

## Priority queues:
- Data structure, little bit like a dictionary in that it stores entries, every entry consists of a key and an associated value
- However, a dict is used when you want to look up a particular queue
-  priority queue is used when you want to specify a particular order
    - A total order is defined on the keys
- Operations:
    - Identify or remove entry whose key is the lowest (this is the only entry you can remove quickly)
    - Any key may be inserted at any time
- Suppose we use integers as our key:
    - Say we want to insert 5: hoot
    - [4: womp, 7: gong] --> insert(k, v) --> [4: womp, 5, hoot, 7 gong]
    - Say we want to removeMin()
        - removeMin() --> [4, womp]
    - You can also return min without removing it
        - Min() --> [ 4: womp]

- Priority queues are commonly used as "event queues" in simulations
    - Key is the time the event takes place
    - Value is description of event
    - To perform the simulation you can take vents off the queue with the minimum time of time of event
    - Events can have the same time but can only be taken off the queue one at a time
    
## Implemenation: Binary Heap
- **Binary heap: an implementation of priority queues**
- Binary heaps is a complete binary tree
    - A complete binary tree is one such that every row (level) of the tree is filled up except the bottom row (which may be partially full, filled in from left to right)
- Example of complete binary tree
    -  `[[2], [5, 3], [9, 6, 11, 4], [17, 10, 8, null, null, null]]`
        - notice every node in first two levels have both left and right child, the bottom row is incomplete but filled in from left to right
- To be a binary heap, a tree must satisfy:
    - Must be a complete binary trees
    - Must satisfy the heap-order property:
        - No child has a key less than its parents key
- Note: every subtree of a binary heap, is a binary heap
### Binary Heap:
-  `[null, 2, 5, 3, 9, 6, 11, 4, 17, 10, 8]` 
    - Note: They keys are stored in the array
- Often stored as arrays of the level order traversal (BFS) of the binary heap 
- Intebntionally leaving index 0 because it makes indexes work out more nicely
- Mapping of nodes to indices: **Level numbering**
    - Makes it easy to point out who are the parents and children of a node
        - Node i's children are 2i and 2i+1
        - Node i's parent is i/2
            - Say we are looking for parent and children of node with key 9 (index 4 of array)
                - Parent: 4/2 = 2,  arr[2] = 5
                - Children: 4*2 = 8, 4*2 +1= 9, therefore children are arr[8]-> 17 and arr[9] -> 10
- Array implementation is really fast and very commonly used
    - You always know where the last value is because it is the last filled value in the array
- Each TreeNode has 2 references, (key, value) OR reference "Entry" object, and can have reference "entry" object which has references to a key and a value
- Operations:
    1. Entry `min()`;
        - Return entry at the root (root is the has the min key)
    2. Entry `insert(Object k, Object v) `
        - Key and value can be any object
        - Need to take an arbitrary key and insert it such that the heap order property is satisfied
        - Let x be new entry (k,v)
            - Place x in bottom level of tree, at first free spot from the left, i.e. first free location in the array
                - The problem is the new key might violate heap order property. How do we fix it? Lets insert key 2
            -  `[null, 2, 5, 3, 9, 6, 11, 4, 17, 10, 8]` -> -  `[null, 2, 5, 3, 9, 6, 11, 4, 17, 10, 8, 2]`
            - Entry bubbles up the tree until heap order property is satisfied
                - Bubbling: 
                    - Compare x's key with its parent key. If x's key is less, then exchange with parent
                - `[null, 2, 5, 3, 9, 6, 11, 4, 17, 10, 8, 2]` => `[null, 2, 5, 3, 9, 2, 11, 4, 17, 10, 8, 6]`
                    => `[null, 2, 2, 3, 9, 5, 11, 4, 17, 10, 8, 6]`

                - Time complexity: log(n) 
                    - Length depth location of insertion of the new key
    3. Entry `removeMin()`; 
        - Removes key and returns it
        - Start by removing entry at root; save it for return value
            - Before we return we have to fix the hole we left
        - Fill the hole with last entry in the tree, lets call it "x"
        - Bubble it down through the heap
            - Repeat:
                - If x > one or both of its children
                    then swap x with its minimum child
            -  `[null, 2, 5, 3, 9, 6, 11, 4, 17, 10, 8]` => `[null, 8, 5, 3, 9, 6, 11, 4, 17, 10]`
                => `[null, 3, 5, 8, 9, 6, 11, 4, 17, 10]` => `[null, 3, 5, 4, 9, 6, 11, 8, 17, 10]`
    4. Bottom-Up heap constructions
        - Given a bunch of entries, make a heap out of them
        - We could Insert them one by one: $\Theta$(n*log(n)) but turns out we can do it in linear time
        - void bottomupheap();
            - Make a complete tree out of entries in any order
            - Walk backwars from last internal node (internal node is a node that is not a leaf); i.e. reverse order in array
            - When we visit a node, bubble it down as in removeMin()
            - Example:
                - `[9, 4, 7, 2, 8, 2, 6]` => `[9, 4, 2, 2, 8, 7, 6]` => `[9, 2, 2, 4, 8, 7, 6]` => `[2, 4, 2, 9, 8, 7, 6]`
            - Runing time: O(n) (not proven in this lecture)


### Running times
| Operations            | Binary Heap       | Sorted List | Unsorted List |
| --------------------- | ----------------- | ----------- | ------------- |                       
| min()                 | $\Theta$(1)       | $\Theta$(1) | $\Theta$(n)   |
| insert() (worst case) | $\Theta$(log(n))  | $\Theta$(n) | $\Theta$(1)   |
| insert (best case)    | $\Theta$(1)       | $\Theta$(1) | $\Theta$(1)   |
| removeMin() (worst)   | $\Theta$(log(n))  | $\Theta$(1) | $\Theta$(n)   |
| removeMin() (best)    | $\Theta$(1)       | $\Theta$(1) | $\Theta$(n)   |

- Insert and remove for Binary Heap takes $\Theta$(log(n)) because:
    - Takes O(1) time to compare x with parent
    - Complete binary tree has as most 1+log(n) levels
        - Where n is the number of elements
        - Thus, $\Theta$(log(n)) worst-case time     

    

# [MIT: Heaps and Heap Sort (video)](https://www.youtube.com/watch?v=B7hVxCmfPtM&index=4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)

## Priority Queue
- Implements a set S of elements, each of these element is a associated with a key
- Operations:
    - Insert(S, x): insert element x into set S
    - Max(S): return element of S with the largest key
    - ExtractMax(S): return element of S with the largest key and remove from the queue
    - Increment(S, x, k): Increase the value of x's key to new value k

## Heap
An array visualized as a nearly complete binary tree (all levels of tree full except lowest level, can be partially complete from left to right)

Example:
- `[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]`

Heap on a Tree:
- Root of tree: first element (i=1)
- Parent(i) = i/2
- Left(i) = 2*i
- Right(i) = 2*i +1

### Max Heap
**Max-Heap Property:**
The key of a node is >= the keys of its children (recursive, must be true for every node)

How do we maintain Max-Heap Property?

- **Operations:**
    - BuildMaxHeap: produces a max heap from an unordered array
    - maxHeapify: correct a single violation of the heap property in a subtree's root
        - Assume that the trees rooted at left(i) and right(i) are max heaps
            - Leafs are max heap so this is performed bottom up
        - Example: `A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]` #not a max heap initially
            - MaxHeapify(A, 2)
                heapsize(A) = 10
                Exchange A[2] with A[4]
                Call MaxHeapify(A, 4)
                    Exchange A[4] with A[8]
                    Done.
        - Time complexity: O(log(n)) because the height of a complete binary tree is log(n) and we are bubbling down at most the depth of the tree
    - buildMaxHeap:
        - Convert an array `A[1...N]` into a max heap
        ```
        for i=n/2 down to 1:
            do maxHeapify(A, i)
        ```
        - Elements A[n/2+ 1...n] are all leaves
        - Time complexity: O(n)
            - Analysis:
                - Observation 1: MaxHeapify takes O(1) for nodes that are one level above leaves and in general O(l) time for nodes l levels above the leaves
                - Observation 2: n/4 nodes with level 1, n/8 nodes with level 2, ... and 1 node at log(n) level
                - Total amount of work in the for loop:
                    - n/4(1*c) + n/2(2*c) + n/16(3c) + ... + 1(log(n)*c)
                    - Set n/4=2^k, and simplfy
                    c(2^k)(1/(2^0) + 2/(2^1) + 3/(2^2) + ... (k+1)/(2^k))
                        - (1/(2^0) + 2/(2^1) + 3/(2^2) + ... (k+1)/(2^k))~=3
                            - Bounded by a constant
                    - 3c(2^k) => 2^k, which 2^k = n/4 => becomes $\Theta$(n) 
### Heap Sort - NOTE: TRY TO UNDERSTAND THIS LATER
1. BuildMaxHeap from unordered array
2. Find max element A[1]
3. Swap elements A[n] with A[1] 
    Now max element is at end of array
4. Discard node n from heap, by decrementing heap size
5. New root may violate Max Heap Property, but the children are max heaps => run maxHeapify() on new A[1] element

**Min-Heap Property:** 
The key of a node is <= the keys of its children (recursive, must be true for every node)



# [Linear Time BuildHeap (max-heap)](https://www.youtube.com/watch?v=MiyLo8adrWw)
## Building a binary heap in O(n)
- Works bottom up
- Every leaf is a binary heap, half of the nodes are leaf nodes
- Eventually we get to a node that is the parent of some other node
    - If the value of this node is not bigger than its child then we must bubble down the node (using maxHeapify)
    - For the next n/4 nodes we will do the same, for the n/4 nodes above that we will do it again, for the n/16.. etc (fewer and fewer nodes have a larger height)
- Use maxHeapify() 


# [[Review] Heap (playlist) in 13 minutes (video)](https://www.youtube.com/playlist?list=PL9xmBV_5YoZNsyqgPW-DNwUeT8F8uhWc6)
- Max heaps are used for HeapSort
- Min heaps are used for priority queues

- Max heapify: 
    - Creates max heap from unsorted array
    - Maintains max-heap property
        - Value of i<=value of parent
        - Value of i>= valu eof children
    - Inputs: array (a), heap size, index (i)
        - Note: heap size is a parameter because it useful during heap sort, in bulding our heap heapsize will be length of the array, but in heapsort, heap size decreases as you sort the array

    ```python
    def max_heapify(a, heap_size, i):
        """
        Runs in 0(log(n))
        """
        l = 2*i
        r = 2*i + 1

        largest = i

        if l < heap_size and a[l] > a[i]:
            largest = l
        
        if r < heap_size and a[r] > a[largest]:
            largest = r
        
        if largest != i:
            # swap elements
            a[i], a[largest] = a[largest], a[i]
            max_heapify(a, heap_size, largest)
    ```
- BuildMaxHeap():
    - Wrapper function that calls maxheapify
    - leaves = A[floor(n/2)+1] to a[n]
    - O(n)
    ```python
    def build_max_heap(a):
        """
        Build max heap, runs in O(n)
        """
        for i in range(heap_size//2, 0, -1):
            max_heapify(a, heap_size, i)
    ```
- Heap Sort:
    - Heap is an ordered binary tree
    - Max heap: parent > child
    - Max heapify: similar ot max-heap but assumes part of array is already sorterd
    - In a nutshell:
        1. Continuously create a max heap to find th elargest item
        2. Remove largest item 
        3. Place largest item into a sorted partition
    - Begin
        - Build max heap, which will tell us largest item, then we swap largest value with the last item in the array
        - now call heapify since 
    - Time complexity: O(nlogn)
        - heapify takes O(logn) and called n-1 times

    - Example:
        - a= `[2,8,5,3,9,1]`
        - call buildMaxHeap(a) => a=`[9,8,5,3,2,1]`
        - swap firt and last element => a=`[1, 8, 5, 3, 2, 9]`
        - remove 9 from tree and ocnsider it sorted, a=`[1, 8, 5, 3, 2]`
        - now we are back to having a tree and not a heap, so we call maxHeapify, a=`[8, 5, 3, 1, 2]` 
        - Now swap largest number and last number in array and remove largest and place in the sorted list => a=`[2, 3, 5, 1, 8]` then remove 8 annd consider it sorted
        a=`[2, 3, 5, 1]`
        - Now call Maxheapify again a=`[5, 3, 2, 1]`
        - Now swap again a=`[1, 3, 2, 5]` 
        - now remove again a=`[1, 3, 2]`
        - now max heapify a=`[3, 1, 2]`
        - swap a=`[2, 1, 3]`
        - remove a=`[2, 1]`
        - heapify a=`[2, 1]`
        - swap a=`[1, 2]`
        - remove a=`[1]`
        - heapofy and remove a=`[]` and resulting sorted list = `[1, 2, 3, 5, 8, 9]`
    ```python
    def heapsort(a):
        for i in range (n, 1, -1):
            swap(A[1], A[i])
            n = n-1
            max_heapify(a, i)
    ```
