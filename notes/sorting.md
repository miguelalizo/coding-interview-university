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
Divide and conquer algorithm
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


### Runtime
- O(n*log(n))
    - Optimal runtime for comparison based algorithms

## [1. Mergesort](https://www.coursera.org/lecture/algorithms-part1/mergesort-ARWDq)
Steps:
1. Divide array in two halves
2. Recursively sort each half
3. Merge two halves

Idea is based on the idea of merging


# [Sedgewick - Mergesort (5 videos)](https://www.coursera.org/learn/algorithms-part1/home/week/3)

    - [ ] [2. Bottom up Mergesort](https://www.coursera.org/learn/algorithms-part1/lecture/PWNEl/bottom-up-mergesort)
    - [ ] [3. Sorting Complexity](https://www.coursera.org/lecture/algorithms-part1/sorting-complexity-xAltF)
    - [ ] [4. Comparators](https://www.coursera.org/lecture/algorithms-part1/comparators-9FYhS)
    - [ ] [5. Stability](https://www.coursera.org/learn/algorithms-part1/lecture/pvvLZ/stability)