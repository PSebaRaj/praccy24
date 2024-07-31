# 1. Two Sum, w/ Kev!
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        if target - num in seen:
           return [seen[target - num], i]

        seen[num] = i

    return []


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
