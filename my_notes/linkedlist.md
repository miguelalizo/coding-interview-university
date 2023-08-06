# Linked List
op[]
- [x] [[Review] Linked lists in 4 minutes (video)](https://youtu.be/F8AbOfQwl1c)

- [ ] [Linked Lists CS50 Harvard University](https://www.youtube.com/watch?v=2T-A_GFuoTo&t=650s) - this builds the intuition.

    - Linked Lists solve some of the problems of Arrays
        - Arrays take O(n) to add to an array (when you need to increase the size)
    - LinkedLists are more dynamic as you can grow and shrink the data stored in the Linked list without to touch all of the original data and move it from old location to new

    - How linkedlists are stored in memory:
        - The values in the linked list can be spread out in computers memory! (Without having to be continuous memory storage as arrays)
    - Linked lists relate the elements to eaqch other via pointers
        - Each element has a value, and a pointer to the next or previous node
        - OX0 indicates "NULL" the is the absense of a pointer
        - Usually this is implemented underneath the hood

    Terminology:
    - Linked lists have nodes
        - Each node has a value and a pointer

    Cannot rely on binary seach to find something 
    - Tradeoff from using pointers (linked list) rather than continuous memory (arrays)

    - You should always check if a pointer returned from a function is null

    - Insertion takes BigO(n) at an arbitrary location, and BigO(1) at the start

    - Searching takes bigO(n)

- [Singly Linked Lists (video)](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)
    - Some linked lists have a tail pointer
    - Retrieving last element (Top back operation) also takes O(1)
    - Pop back operaation (remove last element of the list) takes O(n) because you have to point the tail pointer to the second to last element, and to do that youi need to traverse the entire list from the front, which takes O(n)

    ## Operation runtimes
    
    ### Singly Linked List with no tail:
    - PushFront(Key): O(1)
    - TopFront(): O(1)
    - PopFront(): O(1)
    - PushBack: O(n)
    - TopBack: O(n)
    - PopBack(): O(n)
    - Find(Key): O(n)
    - Erase(Key): O(n)
    - Empty(): O(1)
    - AddBefore(Node, Key): O(n)

    ### Singly Linked List with tail:
    - PushBack: O(1)
    - TopBack: O(1)
