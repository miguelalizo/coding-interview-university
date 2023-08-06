[Stacks (video)](https://www.coursera.org/lecture/data-structures/stacks-UdKzQ)
- Abstract data type with the following operations:
    - Push(Key): adds key to collection
    - Key Top(): returns the most recently added key
    - Key Pop(): removes and returns the most recently-added key
    - Boolean Empty(): are there any elements in stack?

- Can think of it like a stack of books:
    - Add a book, Push(), can only do this to the top of the stack of books
    - Remove a book, Pop(), can only do this by removing all the books before the desired book to be removed
    - Grab top book Top()

- **Follows: LIFO: "Last in First Out"**

- **Array implementation of stack:** Stack implementation using an Array of some length n for th elength of the stack
    - numElements: Need to keep a variable for the num of elements currently in the stack (starts at 0 when nothing is in the array)
    - When we Push, we are going to append the element at the end of the array O(1) operation
        - Also add 1 to the numElements
        
    - Operations:
        - Push(): add value to stack, O(1)
        - Empty(): return the arr.length O(1)(
        - Top(): return the value at arr[numElements - 1] O(1)
        - Pop(): remove the element at arr[numElements - 1] and numElements--

    - Limitations of using an array implementation: 
        - Limited stack size
        - Risk of wasted space if arr is instantiated and not all length is used
    - Advantages of array implementation:
        - All operations are O(1)

- **Linked List implementation of stack:**
    - Push(): add value to beginning of stack (add to beginning of list): O(1)
    - Pop(): remove first value in list: O(1)
    - Top(): return first element in list: O(1)
    - Empty(): if list is empty O(1)

    - Advantages:
        - Not limited in size like array implementation


    

 
[[Review] Stacks in 3 minutes (video)](https://youtu.be/KcT3aVgrrpU)