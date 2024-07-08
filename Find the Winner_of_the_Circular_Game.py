class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        index = 0
        # for i in range(len(friends)):
        #     print(friends[i])
        while len(friends) > 1:
            index = (index + k - 1) % len(friends)
            friends.pop(index)
        
        return friends[0]

[https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/?envType=daily-question&envId=2024-07-08]
