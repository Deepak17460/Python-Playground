from itertools import count
from typing import List


class Solution:
    def minKBitFlips(self, n: List[int], k: int) -> int:
        q,o=set(),0
        for l,v,r in zip(count(),n,count(k-1)):
            if (1-v+len(q))%2:
                o+=1
                q.add(r)
            q.discard(l)
        return -1 if q else o
    
    #When the for loop iterates over the list n, it uses zip to create a tuple (l, v, r) for each element in the list, where: