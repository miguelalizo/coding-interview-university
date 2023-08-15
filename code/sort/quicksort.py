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
    # choose rightmost element as pivot (this is kind of randomly choosing pivot)
    pivot = nums[high]
    # pointer for greatest element
    i = low-1
    print("pivot: ",pivot, " nums: ",nums[low:high])
    for j in range(low, high):
        if (nums[j]<pivot):
            i+=1
            (nums[i], nums[j]) = (nums[j], nums[i])
    nums[i+1], nums[high] = nums[high], nums[i+1]
    print("pivot: ",pivot, " nums: ",nums[low:high+1], " idx: ",i+1)
    return i+1

if __name__=="__main__":
    random.seed("ABC")
    # nums = [random.randint(0, 1000) for _ in range(15)]
    nums = [3,1,2,6,4,5,3]
    print(nums)
    quicksort(nums, 0, len(nums)-1)
    print(nums)