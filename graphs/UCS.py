# UCS - Uniform Cost Search
import os
import heapq
from typing import List, Dict

from utils.index import Edge,build_adjacency_list_uw

os.system("clear")

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'S']
edges = [
  ['A', 'S', 3],
  ['A', 'D', 3],
  ['S', 'B', 6],
  ['S', 'C', 2],
  ['C', 'E', 1],
  ['B', 'E', 2],
  ['B', 'D', 4],
  ['B', 'G', 9],
  ['D', 'F', 5],
  ['F', 'E', 6],
  ['E', 'H', 5],
  ['F', 'G', 5],
  ['H', 'G', 8],
]
# print(edges)


def traverse_UCS(graph:Dict[str, List[Edge]],start:str,goal:str):
    pq  = [(0,start)]
    visited = set([start])
    
    visited_costs = {start:0}
    parent = {start:None}
    while pq:
        c_cost,c_node = heapq.heappop(pq)
        if c_node == goal:
            path = []
            while c_node is not None:
              path.append(c_node)
              c_node = parent[c_node]
            return ["".join(path[::-1]),c_cost]
        for n_cost, n_node in graph.get(c_node,[]):
          new_cost = c_cost + n_cost
          if n_node not in visited or new_cost < visited_costs[n_node]:
            visited_costs[n_node] = new_cost
            visited.add(n_node)
            parent[n_node] = c_node
            heapq.heappush(pq,(new_cost,n_node))
    return float('inf')

graph = build_adjacency_list_uw(nodes,edges)

print(traverse_UCS(graph,"S","G"))