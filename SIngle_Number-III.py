from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dict={}
        res=[]
        for num in nums:
            if num in dict:
               dict[num]+=1
            else:
                dict[num]=1
        for num, count in dict.items():
            if count == 1:
               res.append(num)
        return res
    
# Main code to handle input and call the function
if __name__ == "__main__":
    n = int(input())
    nums = [int(item) for item in input().split()]
    solution = Solution()
    # Call the twoSum method and print the result
    print(solution.singleNumber(nums))
