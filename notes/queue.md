- [Queue (video)](https://www.coursera.org/lecture/data-structures/queues-EShpq)
    - Abstract datatype with the following operations
        - Eqneueue (Key): adds key to the collection
        - Key Dequeue(): removes and returns least recently added key
        - Empty(): true or false 
    - FIFO: First in first out
        - First come first serve (like a grocery store line to pay)

    - Queue implementation with linked list (with head and tail pointer):
        - Equeue happens via PushBack operation
        - Dequeue() happens via PopFront operatio
        - Empty: List.Empty


    - Queue implementation with an array:
        - Keep ttrack of read index and write index. Initially both at 0
        - Enqueue: update write index  (increment by 1)
        - Empty(): only empty when read == write index
        - Dequeue(): update read index (increment by 1) 
        - Note:
            - Write index can wrap back around when the array is full, and there is space at the front (front items have been dequeued)
                - This means read index can be greater than write index
                - However there must be a buffer of at least 1 between read and write because otherwise read index and write index would be the same (and we reserve that for only when the queue is empty)

    - Each operation is O(1)
    - Linked list implementation dioffers from array implementation because in the array there is an upper bound on queue length and unused space may be allocated

- [Circular buffer/FIFO](https://en.wikipedia.org/wiki/Circular_buffer)    
    - Like buffer in onboard thrust tool

- [[Review] Queues in 3 minutes (video)](https://youtu.be/D6gu-_tmEpQ)