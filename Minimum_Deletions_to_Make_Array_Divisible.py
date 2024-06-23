from functools import reduce
import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        res = reduce(math.gcd, numsDivide)
        # for i in range(len(nums)):

        #     if res % nums[i] == 0:
        #         return i
            
        for i, num in enumerate(nums):
            if res % num == 0:
                return i
        return -1