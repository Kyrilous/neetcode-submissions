import heapq
from typing import List, Dict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # 1. Build adjacency list: node -> [[neighbor, weight], ...]
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, w in edges:          # renamed so we don't overwrite src
            adj[s].append([d, w])

        # 2. Dijkstra
        shortest = {}                  # node -> final shortest distance
        minHeap = [[0, src]]           # [distance so far, node]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:         # already found a cheaper route
                continue
            shortest[n1] = w1          # first pop = shortest distance

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        # 3. Nodes we never reached get -1
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest