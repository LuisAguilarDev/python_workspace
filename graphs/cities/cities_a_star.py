import heapq
import math
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from utils.index import euclidean_distance,haversine_h,coordinates


cities = {
    "New York": [(200, "Philadelphia"), (300, "Boston"), (350, "Washington DC")],
    "Philadelphia": [(200, "New York"), (150, "Baltimore"), (250, "Washington DC")],
    "Boston": [(300, "New York"), (350, "Albany"), (400, "Providence")],
    "Washington DC": [(350, "New York"), (250, "Philadelphia"), (200, "Richmond")],
    "Baltimore": [(150, "Philadelphia"), (180, "Richmond"), (250, "Pittsburgh")],
    "Albany": [(350, "Boston"), (200, "Syracuse"), (300, "Hartford")],
    "Providence": [(400, "Boston"), (100, "Hartford"), (250, "New Haven")],
    "Richmond": [(200, "Washington DC"), (180, "Baltimore"), (300, "Charlotte")],
    "Pittsburgh": [(250, "Baltimore"), (200, "Columbus"), (300, "Cleveland")],
    "Charlotte": [(300, "Richmond"), (200, "Greensboro"), (400, "Atlanta")],
    "Columbus": [(200, "Pittsburgh"), (250, "Cleveland"), (300, "Cincinnati")],
    "Cleveland": [(300, "Pittsburgh"), (250, "Columbus"), (350, "Detroit")],
    "Detroit": [(350, "Cleveland"), (300, "Chicago"), (400, "Indianapolis")],
    "Chicago": [(300, "Detroit"), (400, "Indianapolis"), (350, "Milwaukee")],
    "Indianapolis": [(400, "Detroit"), (400, "Chicago"), (300, "Louisville")],
    "Milwaukee": [(350, "Chicago"), (300, "Madison"), (400, "Minneapolis")],
    "Louisville": [(300, "Indianapolis"), (350, "Nashville"), (400, "Cincinnati")],
    "Nashville": [(350, "Louisville"), (300, "Memphis"), (400, "Knoxville")],
    "Memphis": [(300, "Nashville"), (400, "Little Rock"), (500, "Jackson")],
    "Atlanta": [(400, "Charlotte"), (300, "Knoxville"), (350, "Birmingham")],
    "Cincinnati": [(300, "Columbus"), (400, "Louisville"), (350, "Indianapolis")],
    "Madison": [(300, "Milwaukee"), (350, "Minneapolis"), (400, "Chicago")],
    "Minneapolis": [(400, "Milwaukee"), (350, "Madison"), (450, "Des Moines")],
    "Knoxville": [(400, "Nashville"), (300, "Atlanta"), (350, "Birmingham")],
    "Greensboro": [(200, "Charlotte")],
    "Little Rock": [(400, "Memphis")],
    "Birmingham": [(350, "Knoxville"), (350, "Atlanta")],
    "Jackson": [(500, "Memphis")],
    "Syracuse": [(200, "Albany")],
    "Hartford": [(300, "Albany"), (100, "Providence")],
    "New Haven": [(250, "Providence")],
    "Des Moines": [(450, "Minneapolis")]  # ✅ Added Des Moines!
}




def a_star(graph, start: str, goal: str) -> int:
    pq  = []
    heapq.heappush(pq, (euclidean_distance(start, goal), 0, start))  # (priority, cost, node)
    # print(pq)
    visited = set()
    
    visited_costs = {start: 0}
    parent = {start: None}
    while pq:
        _, c_cost, c_node = heapq.heappop(pq)
        visited.add(c_node)
        if c_node == goal:
            path = []
            while c_node is not None:
                path.append(c_node)
                c_node = parent[c_node]
            return [",".join(path[::-1]), c_cost]

        for cost, n_node in graph[c_node]:
            n_cost = c_cost + cost
            if n_node not in visited or n_cost < visited_costs[n_node]:
                parent[n_node] = c_node
                visited_costs[n_node] = n_cost
                priority = n_cost + euclidean_distance(n_node, goal)
                heapq.heappush(pq, (priority, n_cost, n_node))
            
    return None  # No path found

print(a_star(cities,"Detroit","Greensboro"))
print(a_star(cities,"Little Rock","Syracuse"))
print(a_star(cities,"Little Rock","New York"))