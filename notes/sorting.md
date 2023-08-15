# Stability in sorting algorithms ("Is Quicksort stable?")
## [Sorting Algorithm Stability](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability)
-  If two items compare as equal (like the two 5 cards), then their relative order will be preserved, i.e. if one comes before the other in the input, it will come before the other in the output.
- Unstable sorting algorithms can be specially implemented to be stable. One way of doing this is to artificially extend the key comparison, so that comparisons between two objects with otherwise equal keys are decided using the order of the entries in the original input list as a tie-breaker. Remembering this order, however, may require additional time and space.
## [Stability In Sorting Algorithms](http://stackoverflow.com/questions/1517793/stability-in-sorting-algorithms)

A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted. Some sorting algorithms are stable by nature like Insertion sort, Merge Sort, Bubble Sort, etc. And some sorting algorithms are not, like Heap Sort, Quick Sort, etc.

Background: a "stable" sorting algorithm keeps the items with the same sorting key in order. Suppose we have a list of 5-letter words:

```
peach
straw
apple
spork
```
If we sort the list by just the first letter of each word then a stable-sort would produce:
```
apple
peach
straw
spork
```
In an unstable sort algorithm, straw or spork may be interchanged, but in a stable one, they stay in the same relative positions (that is, since straw appears before spork in the input, it also appears before spork in the output).

We could sort the list of words using this algorithm: stable sorting by column 5, then 4, then 3, then 2, then 1. In the end, it will be correctly sorted. Convince yourself of that. (by the way, that algorithm is called radix sort)

Now to answer your question, suppose we have a list of first and last names. We are asked to sort "by last name, then by first". We could first sort (stable or unstable) by the first name, then stable sort by the last name. After these sorts, the list is primarily sorted by the last name. However, where last names are the same, the first names are sorted.

You can't stack unstable sorts in the same fashion.

## [Stability In Sorting Algorithms](http://www.geeksforgeeks.org/stability-in-sorting-algorithms/)

### Do we care for simple arrays like the array of integers? 
When equal elements are indistinguishable, such as with integers, or more generally, any data where the entire element is the key, stability is not an issue. Stability is also not an issue if all keys are different.

### Can we make any sorting algorithm stable? 
Any given sorting algorithm which is not stable can be modified to be stable. There can be algorithm-specific ways to make it stable, but in general, any comparison-based sorting algorithm which is not stable by nature can be modified to be stable by changing the key comparison operation so that the comparison of two keys considers position as a factor for objects with equal keys.

## [Sorting Algorithms - Stability](http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/stability.pdf)
Unfortunately, many of the (otherwise) best sorting algorithms are
not stable.
    - For example, quicksort and heapsort are not stable. (Mergesort
property implemented is stable.)

Any sorting algorithm may be made stable, at a price: The price is
Θ(n) extra space, and moderately increased running time (less than
doubled, most likely).
    - We have to (temporarily) append a sequence number to the key of
each element of the array. The sequence number serves as a tie-
breaker.

# Mergesort
## [Merge Sort In Python Explained (with example and code)](https://www.youtube.com/watch?v=cVZMah9kEjI)
### Overview
Recursive Divide and conquer algorithm
    - A problem is divided into subproblems recursively until the problem is very simple to solve
    - Solutions are combined to solve original problem

### General Principle
Merge Sort:
    1. Divide array in two halves
    2. Recursively sort each half
    3. Merge two halves

Example:
- Sort:
    - `[2, 6, 5, 1, 7, 4, 3]`
    - `[2, 6, 5, 1] [7, 4, 3]`
    - `[2, 6, 5, 1] [7, 4, 3]`
    - `[2, 6] [5, 1] [7, 4] [3]`
    - `[2] [6] [5] [1] [7] [4] [3]` # sorted
- Now merge:
    - `[2] [6]` => `[2, 6]`
    - `[5] [1]` => `[1, 5]`
    - `[7] [4]` => `[4, 7]`
    - `[3]`
    - `[2, 6] [1, 5]` => `[1, 2, 5, 6]`
    - `[4, 7] [3]` => `[3, 4, 7]`
    - `[1, 2, 5, 6] [3, 4, 7]` => `[1, 2, 3, 4, 5, 6, 7]`

```python
Num = Union[int, float]

def mergesort(nums: List[Num], left: int = 0, right: int = None) -> None:
    """
    Sort a list of numbers in place

    Parameters
    ----------
    nums: List[Num]

    Returns
    -------
    None
    """
    if right is None:
        right = len(nums)-1

    if left >= right:
        return
    
    mid = (left+right)//2

    # recursion
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)

    merge(nums, left, right, mid)
    
def merge(nums: List[Num], left: int, right: int, mid: int) -> None:
    """
    Merge two lists in sorted order

    Parameters
    ----------
    nums: List[Num]
        List of numbers to be merged
    left: int
        Left bound index of nums
    right: int
        Right boudn index of nums
    mid: int
        Midpoint index of nums

    Returns
    -------
    None
    """
    # merge
    l_copy = nums[left:mid+1]
    r_copy = nums[mid+1:right+1]

    l_counter, r_counter = 0, 0
    k = left # sorted counter

    while l_counter<len(l_copy) and r_counter<len(r_copy):
        if l_copy[l_counter] <= r_copy[r_counter]:
            nums[k] = l_copy[l_counter]
            l_counter+=1
        else:
            nums[k] = r_copy[r_counter]
            r_counter+=1
        k+=1

    while l_counter<len(l_copy):
        nums[k] = l_copy[l_counter]
        l_counter+=1
        k+=1
    while r_counter<len(r_copy):
        nums[k] = r_copy[r_counter]
        r_counter+=1
        k+=1
```

#### Callstack
```
mergesort([7,5,2,1,3]) 
	mergesort([7,5])				// left 
		mergesort([7])			// left 
			return [7] 
		mergesort([5])			// right 
			return [5] 
		return merge([7],[5])		// returns [5, 7] 
	mergesort([2,1,3])			// right 
		mergesort([2])			// left 
			return [2] 
		mergesort([1,3])			// right 
			mergesort([1])  		// left	 
				return [1] 
			mergesort([3])		// right 
				return [3] 
			return merge([1],[3])	// returns [1, 3] 
		return merge([2], [1,3])		// returns [1,2,3] 
	return merge([5,7], [1,2,3])		// returns [1,2,3,5,7] 
```
### Runtime (Best and Wost Case are the same!)
- $\Theta$(n*log(n))
    - Optimal runtime for comparison based algorithms

## [1. Mergesort](https://www.coursera.org/lecture/algorithms-part1/mergesort-ARWDq)
Steps:
1. Divide array in two halves
2. Recursively sort each half
3. Merge two halves

Idea is based on the idea of merging

# Quicksort

## [Quicksort in 4 minutes](https://www.youtube.com/watch?v=Hoixgm4-P4M)
### Recursive algorithm
- Think pivot
- A pivot is one of the items in the array that meets the following 3 conditions after we sorted it
    1. Correct final position in sorted array
    2. Items to the left are smaller
    3. Items to the right are larger
    - Example: `[ 2 6 5 3 8 7 1 0]`
        - First, move the pivot to the end to get it oput of the way `[2 6 5 0 8 7 1 3]`
        - Look for first instance of (both) thesetwo items
            - itemFromLeft: first item starting from the left that is larger than pivot
            - itemFromRight: first item starting from the right that is less than pivot
        - `6` is itemFromLeft and `1` is item from right. Swap them
            - => `[2 1 5 0 8 7 6 3]`
        - Now, `5` is itemFromLeft and `0` is item from right. Swap them
            - => `[2 1 0 5 8 7 6 3]`
        - Now itemFromLeft has a greater index than itemFromRight so we know we are done
        - Now simply swap itemFromLeft with our pivot
            - => `[2 1 0 3 8 7 6 5]` and now our pivot is in the right spot! And we now have 2 partitions (everything left of 3 and everything right of 3)
        - So now we recursively do the same thing on the two partitions
### How to choose pivot? 
-The pivot makes a big difference in the performance of the algorithm
- One popular method is `Median of 3`:
    - In this method we look at the first middle and last element of the array
    - we sort them and use the middle element as the pivot
        - We are making the guess that the middle of these 3 items could be close to the median of the array
        
### Time complexity:
- Worst case: O(n^2)
    - When does worst case happen?
- Average case: O(nlog(n))

#### Best Case
- If the pivot always lands in the middle, then we end up with 2 subproblems that are roughly half the size of the original problem
    - If the pivots of those are roughly at the middle, then you end up with 4 subproblems with roughly a quarter of the size of the original problem 
    - and so on..
- In this case, the problem breaks down in to a tree of `logn` depth
- Work done at each level:
    - Level 0: `n` work
    - Level 1: `n/2` work each partition so `2 * n/2 ~ n`
    - Level 3: `n/4' at each partition so `4 * n/4 ~ n`
    - And so on...
    - So at each level we have roughly `n` amount of work
- Therefore best case time complexity is $\Omega$(nlog(n))

#### Worst Case
Pivot lands always at the beginning of the array
- This means the first problem is divided into a 2 subproblems where the left is size 1 and the right is n-1
- At each subsequent level, the problem will be subdivided into 1+d and n-d where d is the depth of the callstack; therefore we will have n subproblems all which take n-d time
- Worst case is $\Theta$(n^2)

#### Average Case
Runtime complexity: $\Theta$(nlog(n))
Proof:
![Image](static/quicksort_average.png)

##### Despite this Worst Case, quicksort is actually better than mergesort

## [Sorting 2, Video 4 Quicksort Best and Worst Case](https://www.youtube.com/watch?v=PJnHzFypGaI
)

## [1. Quicksort](https://www.coursera.org/lecture/algorithms-part1/quicksort-vjvnC)
- Recusrive algorithm 
- Like mergesort except that it does the recursion after it does the work, whereas mergesort does it before it does the work

Steps:
1. Shuffle the array
2. Partition so that for some j:
    - entry a[j] is in place
    - No larger entry to the left of j
    - No smaller entry to the right of j
3. Sort each piece recursively


# [Sedgewick - Quicksort (4 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)
    - [ ] [1. Quicksort](https://www.coursera.org/lecture/algorithms-part1/quicksort-vjvnC)
    - [ ] [2. Selection](https://www.coursera.org/lecture/algorithms-part1/selection-UQxFT)
    - [ ] [3. Duplicate Keys](https://www.coursera.org/lecture/algorithms-part1/duplicate-keys-XvjPd)
    - [ ] [4. System Sorts](https://www.coursera.org/lecture/algorithms-part1/system-sorts-QBNZ7)

# UC Berkeley Sort Lectures:
## [CS 61B Lecture 29: Sorting I (video)](https://archive.org/details/ucberkeley_webcast_EiUvYS2DT6I)
### Insertion Sort
#### Runs in O(n^2)
#### Procedure:
Maintain the invariant that S is sorted
- start with emopty list S and unsorted list i of N items
```python
for x in i:
    # insert x into S in sorted order
```

#### Notes:
Linked lST
- If S is a linked list, then O(n) worst-case time to find the right position to insert
Array
- If S is an array then we can use binary search to find the insertion position which becomes O(logn) to ***find*** the right position to insert **BUT** it doestake O(n) time to shift higher items over after inserting

In place Sort
- Insertion sort is in place sort if S is an Array
    - This is done by 'partitioning' the array into S and I in place with indexing
- Space complexity O(1)

Inversions:
- if you start with an already almost sorted array then running time is proportional to the numbher of inversions

Balanced Search Tree:
- If S is a balanced search tree then running time can become O(nlogn)
    - This is not used in practiced because there are better sorting algorithms for balanced search trees that run faster (still O(nlogn) but with better coefficients)

For implementation: see `code/insertionsort.py`

### Selection
#### Runs in O(n^2) ALWAYS
#### Procedure:
Maintain the invariant that S is sorted
- start with emopty list S and unsorted list i of N items
```
for (i=0;i<n;i++){
    x <- item in I with smallest key
    remove x from I
    append x to end of S
}
```
Whether S is array or linked list:
- $\Theta$(n^2)

In place sort:
- This algorithm can be done in place

### Heapsort
- Runs in O(nlogn)
- Can be done in-place
- It is like selection sort where S is a heap
- Great for sorting arrays but it is clunky to perform for linkedlists
    - Best way to use it for linkedlists is by first making an array representation of the linked list and then using heapsort on the array and then making a new linkedlist from the sorted array
        - In practice, just dont use heapsort on linked lists

Already implemented see `heapsort.py` and [priority queue notes](priority_queues.md)


### Mergesort
Recursive divide and conquer alrgorithm:
- Divide first, then sort while merging
    - "Opposite" order than quicksort


Running time:
- Runs in O(nlogn)

Already implemented see `mergesort.py`

Idea:
- Merge 2 sorted lists into one sorted list in linear time

Linked Lists:
- Natural for sorting linked lists

Arrays:
- Not great because it is not an in-place sort and so it requires linear (extra) space to solve

## [CS 61B Lecture 30: Sorting II (video)](https://archive.org/details/ucberkeley_webcast_2hTY3t80Qsk)

### Quicksort - Fastest comparison based sort for arrays
Recursive divide and conquer algorithm:
- Do all the work before dividing, then merge is just concatenating two lists together
    - "Opposite" order than mergesort

Running time:
- Best and Worst case - $\Theta$(n^2)
- In practice, it virtually always happens in O(nlogn)
    - With a smaller constant hidden in the bigO notation than mergesort

- **Fastest known comparison based sort for arrays!**
    - Because constant factor in the O(nlogn)

Idea:
- We are given an unsorted list of items to sort
- We will pick one item from the array and call it the `pivot`
- We will put all the items less than the pivot on the left side of the array and put all items greater than the pivot on the right side of the array
- Then we sort those two stacks recursively
- Then we glue them both together with the pivot in the middle

#### Algorithm
1. Partition:
- Start with list I of n items
- Choose pivot item v from I
- Partition I into 2 unsorted lists I1 and I2
    - I1: All keys smaller than pivot's key
    - I2: All keys larger than the pivot's key
    - Items w/ same key as pivot can go into either list
        - Which side differs depending on the implementation
    - The pivot does not go into either list
2. 
Sort I1 recursively, yielding sorted list S1
Sort I2 recursively, yielding sorted list S2
3. Concatenate I1 and I2 with v in the middle

Example:`[4,7,1,5,9,3,0]`
Simple pivot rule for this example: Say pivot is always the first item in the list, we will start with 4
- Any items less than 4 will go on the L1 `[1,3,0]`; L2 becomes `[7,5,9]` with the pivot in between
Here is what the callstack looks like:
```
   [4,7,1,5,9,3,0]
[1,3,0]  [4]  [7,5,9]
[0][1][3]    [5][7][9]
    [0,1,3,4,5,7,9]
```
Lets try to use this version of this sort to sort a sorted array
```
   [0,1,3,4,5,7,9]
   [0][1,3,4,5,7,9]
   [0][1][3,4,5,7,9]
   [0][1][3][4,5,7,9]
   [0][1][3][4][5,7,9]
   [0][1][3][4][5][7,9]
   [0][1][3][4][5][7][9]
   [0,1,3,4,5,7,9]
```

Point here being:
- If you choose your pivots well then you may have O(logn) levels in the revcursion tree where at each level you do n work and end up with O(nlogn) running time
- If you choose pivots incorrectly, then you can get worst case O(n^2) 
    - Worst case: sorted set and choosing first item as pivot

#### Choosing a Pivot Strategies
1. Randomly select an item from I as pivot.
- On average, 1/4, 3/4 split between I1 and LI2 which results in O(nlogn)
2. Median of 3 strategy
- Choose 3 random pivots and figure out which one of those 3 is the median of those 3 and choose that as the pivot
- In practice this only pays off if you have a lot of items in the list
- Even better probability of O(nlogn)

#### Quicksort on Linked Lists
When you have items that with equal keys, the answer to which side (I1 or I2) you put it in is different for Arrays than for linked lists.

Suppose we put all items with same key as v (pivot) into the first I1:
```
[5,5,5,5,5,5]
[5,5,5,5,5][5][]
```
This becomes quadratic!

Better strategy:
1. Partition I into 3 lists I1, I2, Iv
    - Iv contains pivot and all items with the same key
2. Sort I1 and I2, (dont sort Iv)
3. Concat S1, Iv and S2
- Example:
    ```
    [5, 7, 5, 0, 6, 5, 5] suppose we choose 5 as pivot
    [0] [5,5,5,5] [7,6]
    [0] [5,5,5,5] [6][7][]
    [0,5,5,5,5,6,7]
    ```
- This approach does not work well for arrays because if you want to sort in place, then where do you put the Iv elements? Gets messy!

#### Quicksort on Arrays - This is where quicksort shines!
In-Place quicksort is fast
- However a fast in place quicksort that is always fast is tricky

Algorithm:
- array a
- Sort items from a[low]...a[high]
    - We choose pivot v; swapt it wit last item in subarray array to get it out of the way
    ```
    [...3,8,0,9,5,7,4...] (choosing 5 as pivot)
      LOW       v   HIGH
    [3,8,0,9,4,7,5]
     i           j
    i <- low-1
    j <- high
    Invariants:
    - All items left of index i have a key <= pivot
    - All items to the right of index j have a key >=pivot
    Advance i until you find a key>=pivot
    Decrement j until you find a key<=pivot
    [3,8,0,9,4,7,5]
    i=8 and i=4
    swap i and j 
    [3,4,0,9,8,7,5]
    repeat this until i>=j
    Then swap pivot back to middle (take whatever key is at i and swap with pivot which is last thing in array)
    [3,4,0,5,8,7,9]
    ```
- Items with same key as pivot?
    - With this rule used above we stop at these and swap them (relating to part of algorithm that says "Advance i until you find a key>=pivot" and "Decrement j until you find a key<=pivot) but why?
        - If we didnt swap them (say by changing to Advance i until you find a key>pivot) then if we have an array where all elements are the same we get n^2 running 
            - i pointer will advance all the way to the end of the list and j never advances which will put all the values into the left
        - Instead if we keep incrementing i and decrementing j and keep swapping every time then we will partition the array in the middle into two halves

