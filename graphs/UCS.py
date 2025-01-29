# UCS - Uniform Cost Search
import os

from queue import PriorityQueue
from utils import build_adjacency_list_uw

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


def traverse_UCS(nodes,edges,start:str,goal:str):
    adjacency_list = build_adjacency_list_uw(nodes,edges)

    pq = PriorityQueue()
    pq.put((0,start))
    
    visited_costs = {}
    visited = ""
    while not pq.empty():
        cost,c_node = pq.get()
        if c_node in visited_costs and visited_costs[c_node] <= cost:
            continue
        visited_costs[c_node] = cost
        visited += c_node
        if c_node == goal:
            return [cost,visited]
        for neighbor in adjacency_list[c_node]:
          n_cost, n_node = neighbor
          new_cost = cost + n_cost
          if neighbor.node not in visited_costs or new_cost < visited_costs[neighbor.node]:
            pq.put((new_cost,n_node))



print(traverse_UCS(nodes,edges,"S","G"))