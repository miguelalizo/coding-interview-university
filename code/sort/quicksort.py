import random

def quicksort(nums: list[int], low: int, high: int):
    """
    In-place quicksort for an Array nums.
    Runs on average in: O(nlogn) but worst case is quadratic
    Space complexity: O(1)

    Parameters
    ----------
    nums: list[int]
        Array of numbers in to be sorted
    low: int
        Lower bound index of the nums subarray to be partitioned
    high: int
        Upper bound index of the nums subarray to be partitioned
    """
    if low<high:
        pivot_idx = partition(nums, low, high)
        quicksort(nums, low, pivot_idx-1)
        quicksort(nums, pivot_idx+1, high)

def partition(nums: list[int], low: int, high: int):
    """
    Find partition index and place all elements greater than pivot to the right of pivot,
    and all elements less than puvot to the left.
    Pivot is chosen as the right most element (so that it is out of the way)

    Parameters
    ----------
    nums: list[int]
        List of nums to be partitioned
    low: int
        Lower bound index of the nums subarray to be partitioned
    high: int
        Upper bound index of the nums subarray to be partitioned

    Returns
    -------
    None
    """
    # choose rightmost element as pivot (this is kind of randomly choosing pivot)
    pivot = nums[high]

    # pointer for the leftmost element in the list that is greater than pivot
    i = low-1
    # look for elements smaller than pivot and if found then swap with current i
    # note: as we go through the loop, as long as elements are all smaller than pivot then
    # the i and j will be the same at the swap (and nothing happens)
    for j in range(low, high):
        if (nums[j]<pivot):
            i+=1
            (nums[i], nums[j]) = (nums[j], nums[i])

    # swap first element greater than pivot with pivot
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1

if __name__=="__main__":
    random.seed()
    nums = [random.randint(0, 1000) for _ in range(15)]
    print(nums)
    quicksort(nums, 0, len(nums)-1)
    print(nums)