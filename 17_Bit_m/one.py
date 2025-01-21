from typing import List

def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res = num ^ res
    
    return res
    
print(singleNumber(nums = [3,2,3]))