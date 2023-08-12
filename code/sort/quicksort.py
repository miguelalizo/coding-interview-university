import random

def quicksort(nums: list[int], low: int, high: int):
    """
    """
    if low<high:
        pivot_idx = partition(nums, low, high)
        quicksort(nums, low, pivot_idx-1)
        quicksort(nums, pivot_idx+1, high)

def partition(nums: list[int], low: int, high: int):
    """
    """
    # rightmost element as pivot
    pivot = nums[high]
    # pointer for greatest element
    i = low-1

    for j in range(low, high):
        print(i, j)
        print(nums)
        if (nums[j]<pivot):
            i+=1
            (nums[i], nums[j]) = (nums[j], nums[i])
        print(nums)
            # left_wall+=1
    # print(low, left_wall)
    # print(nums[low], nums[left_wall])
    nums[i+1], nums[high] = nums[high], nums[i+1]
    # print(nums[low], nums[left_wall])
    # print(nums)
    
    return i+1

if __name__=="__main__":
    random.seed("ABC")
    nums = [random.randint(0, 1000) for _ in range(15)]
    print(nums)
    quicksort(nums, 0, len(nums)-1)
    print(nums)