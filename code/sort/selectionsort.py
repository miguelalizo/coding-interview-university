import random

def selection_sort(nums: list[int]):
    """
    Insertion sort in-place
    Runtime: O(n^2)
    Space: Theta(1)

    Parameters
    ----------
    nums: list[int]
        Numbers list to be sorted

    Returns
    -------
    None
    """
    if not nums:
        return nums

    # i is the partition
    for i in range(0, len(nums)-1):
        swap(nums, i)

def swap(nums, p):
    """
    Find smallest element in nums that appears after index p, if the value
    is < than nums[p] then swap it.
    Runs in: O(n)
    Space: Theta(1)

    Parameters
    ----------
    nums: list[int]
        Nums list
    p: int
        Index of partition

    Returns
    -------
    None
    """
    smallest_idx = p
    for i in range(p+1, len(nums)):
        if nums[i] < nums[smallest_idx]:
            smallest_idx = i
    nums[p], nums[smallest_idx] = nums[smallest_idx], nums[p]

if __name__=="__main__":
    random.seed("ABC")
    nums_test = [random.randint(0, 1000) for _ in range(30)]
    selection_sort(nums_test)
    print(nums_test)
    nums_test = [0, 1, 2, 3, 4, 5, 7, 6, 8, 9]
    selection_sort(nums_test)
    print(nums_test)
