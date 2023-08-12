import pytest
import random
import sys

sys.path.append('../')
import insertionsort

@pytest.fixture(scope="module")
def nums():
    random.seed("ABC")
    return [random.randint(0, 1000) for _ in range(20)]

def test_insertionsort(nums):
    print(nums)
    ans = sorted(nums.copy())
    insert_sorted = nums.copy()
    insertionsort.insertion_sort(insert_sorted)
    # print(ans)
    print(insert_sorted)
    assert ans == insert_sorted
    