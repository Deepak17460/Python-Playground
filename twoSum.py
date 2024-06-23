from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

# Main code to handle input and call the function
if __name__ == "__main__":
    n = int(input())
    if 2 <= n <= 10**4:
        nums = [int(item) for item in input().split()]
        target = int(input())
        if all(-10**9 <= x <= 10**9 for x in nums) and -10**9 <= target <= 10**9:
            solution = Solution()
            # Call the twoSum method and print the result
            print(solution.twoSum(nums, target))
        else:
            print("Oops!")
    else:
        print("Oops!")
