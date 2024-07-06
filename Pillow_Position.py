class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        PillowP=1
        forward=True

        while time:
            if forward:
                if PillowP==n:
                    forward=False
                    PillowP-=1
                else:
                    PillowP+=1
            else:
                if PillowP==1:
                    forward=True
                    PillowP+=1
                else:
                    PillowP-=1
            time-=1
        return PillowP


(QUestion link)[https://leetcode.com/problems/pass-the-pillow/?envType=daily-question&envId=2024-07-06]
