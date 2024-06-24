class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        Sum=sum(nums)
        n=len(nums)
        res= n*(n+1)//2 # expected~sum
        return res-Sum
