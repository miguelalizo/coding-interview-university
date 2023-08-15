def max_heapify(a: list[int], i: int):
    """
    Ensures a[i] is >= its children recursively. 
    Maintains max-heap property forn an array implementation of a max heap

    Parameters
    ----------
    a: list[int]
        list representation of binary tree
    i: int
        index to ensure max-heap property

    Returns
    -------
    None
    """
    l = 2*i + 1
    r = 2*i + 2
    max_idx = i

    if l<len(a):
        if a[l] > a[i]:
            max_idx = l
    if r<len(a):
        if a[r] > a[l]:
            max_idx = r

    a[max_idx], a[i] = a[i], a[max_idx]

    if i != max_idx and max_idx <= len(a)//2 -1:
        max_heapify(a, max_idx)


def build_max_heap(a: list[int]):
    """
    Uses max_heapify to build a max-heap (array implementation)

    Parameters
    ----------
    a: list[int]
        Unordered list of integers
    
    Returns
    -------
    None
    """
    for i in range((len(a)//2)-1, -1, -1):
        max_heapify(a, i)

def heap_sort(a):
    """
    Heap-Sort algorithm. Uses build_max_heap and max_heapify to sort
    the input list and returns the sorted input list

    Runs in: O(nlogn)
    Space: O(n)

    Parameters
    ----------
    a: list[int]
        Unordered list of integers

    Returns
    -------
    a_sorted: list[int]
        Sorted list containing all elements in a
    """
    build_max_heap(a)
    a_sorted = []

    while(len(a)>1):
        # swap
        a[0], a[len(a)-1] = a[len(a)-1], a[0]

        # pop and add to a_sorted
        a_sorted = [a.pop(-1)] + a_sorted

        # heapify
        max_heapify(a, 0)

    a_sorted =  [a.pop(-1)] + a_sorted
    
    return a_sorted

if __name__=="__main__":
    a = [5, 8, 4, 3, 1, 9, 15, 20, 2, 67, 0]
    print(a)
    a_sorted = heap_sort(a)
    print(a_sorted)

    a = [5, 8, 4, 3, 0, 9, 15, 1, 20, 2, 67, 55,104, 1, 6, 44, 17, 18, 13, 2, 23, 4]
    print(a)
    a_sorted = heap_sort(a)
    print(a_sorted)

    a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(a)
    a_sorted = heap_sort(a)
    print(a_sorted)



