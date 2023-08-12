import random

def insertion_sort(nums: list[int]):
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

    for i in range(1, len(nums)):
        insert(nums, i)

def insert(nums, p):
    """
    Insert nums[idx] into nums in the correct place, left of the partition
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
    if nums[p] >= nums[p-1]:
        return
    
    for i in range(p-1, -1, -1):
        if nums[p] >= nums[i]:
            return
        else:
            nums[i], nums[p] = nums[p], nums[i]
            p-=1

if __name__=="__main__":
    random.seed("ABC")
    nums_test = [random.randint(0, 1000) for _ in range(30)]
    insertion_sort(nums_test)
    print(nums_test)
    nums_test = [0, 1, 2, 3, 4, 5, 7, 6, 8, 9]
    insertion_sort(nums_test)
    print(nums_test)

