class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        edge_1, edge_2=edges[0], edges[1]

        if edge_1[0] in edge_2:
            return edge_1[0]
        else :
            return edge_1[1]



            # edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
