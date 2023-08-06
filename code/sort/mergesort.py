from typing import Union, List
import random

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

if __name__=="__main__":
    random.seed("ABC")
    nums_test = [random.randint(0, 1000) for _ in range(100)]
    print(nums_test)
    mergesort(nums_test)
    print(nums_test)