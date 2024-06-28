
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connections = [0] * n
        for road in roads:
            connections[road[0]] += 1
            connections[road[1]] += 1
        for i, num in enumerate(connections):
            print(i,num)
        sorted_cities = sorted(range(n), key=lambda x: connections[x], reverse=True)
        print("After")
        for i, num in enumerate(sorted_cities):
            print(i,num)
        importance = [0] * n
        for i, city in enumerate(sorted_cities):
            importance[city] = n - i

        total_importance = 0
        for road in roads:
            total_importance += importance[road[0]] + importance[road[1]]
        
        return total_importance
