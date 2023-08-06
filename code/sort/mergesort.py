from typing import Union, List

Num = Union[int, float]

def mergesort(nums: List[Num]) -> None:
    """
    Sort a list of numbers in place

    Parameters
    ----------
    nums: List[Num]

    Returns
    -------
    None
    """
    if len(nums) <=1:
        return nums
    if len(nums) > 1:
        left_nums = nums[:len(nums)//2]
        right_nums = nums[len(nums)//2:]

    # recursion
    mergesort(left_nums)
    mergesort(right_nums)

    # merge
    i = 0 # left nums index
    j = 0 # right nums index
    k = 0 # merged nums idx
    while i<len(left_nums) and j<len(right_nums):
        if left_nums[i] <= right_nums[j]:
            nums[k] = left_nums[i]
            i+=1
        else:
            nums[k] = right_nums[j]
            j+=1
        k+=1

    while i<len(left_nums):
        nums[k] = left_nums[i]
        i+=1
        k+=1
    while j<len(right_nums):
        nums[k] = right_nums[j]
        j+=1
        k+=1

if __name__=="__main__":
    nums_test = [2, 3.1, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
    mergesort(nums_test)
    print(nums_test)