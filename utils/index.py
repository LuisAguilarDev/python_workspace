import math
from typing import List, Dict

class Edge:
    def __init__(self, node: str, cost: int):
        self.node = node
        self.cost = cost
    def __iter__(self):
        yield self.cost
        yield self.node

def build_adjacency_list_uu(nodes, edges) -> Dict[str,List[str]]:
    """
    Build an adjacency list for an undirected, unweighted graph.

    :param nodes: A list of node identifiers.
    :param edges: A list of pairs [start, end].
    :return: A dictionary where each key is a node, and each value is a list of adjacent nodes.
    """
    adjacency_list = {node: [] for node in nodes}
    for start, end in edges:
        adjacency_list[start].append(end)
        adjacency_list[end].append(start)
    return adjacency_list


def build_adjacency_list_uw(nodes, edges) -> Dict[str,List[Edge]]:
    """
    Build an adjacency list for an undirected, weighted graph.

    :param nodes: A list of node identifiers.
    :param edges: A list of tuples (from_node, to_node, cost).
    :return: A dictionary where each key is a node, and each value is a list of dictionaries
             with 'node' and 'cost' keys.
    """
    adjacency_list = {node: [] for node in nodes}
    for from_node, to_node, cost in edges:
        adjacency_list[from_node].append(Edge(to_node,cost))
        adjacency_list[to_node].append(Edge(from_node,cost))
    return adjacency_list


def build_adjacency_matrix_uu(nodes, edges):
    """
    Build an adjacency matrix for an undirected, unweighted graph.

    :param nodes: A list of node identifiers.
    :param edges: A list of pairs (start, end).
    :return: A 2D list (matrix), where matrix[i][j] = 1 if there's an edge between nodes[i] and nodes[j], else 0.
    """
    n = len(nodes)
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
    index_map = {node: i for i, node in enumerate(nodes)}

    for start, end in edges:
        i, j = index_map[start], index_map[end]
        adjacency_matrix[i][j] = 1
        adjacency_matrix[j][i] = 1

    return adjacency_matrix


def build_adjacency_matrix_uw(nodes, edges):
    """
    Build an adjacency matrix for an undirected, weighted graph.

    :param nodes: A list of node identifiers.
    :param edges: A list of tuples (start, end, cost).
    :return: A 2D list (matrix), where matrix[i][j] = weight of the edge, or 0 if no edge exists.
    """
    n = len(nodes)
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
    index_map = {node: i for i, node in enumerate(nodes)}

    for start, end, cost in edges:
        i, j = index_map[start], index_map[end]
        adjacency_matrix[i][j] = cost
        adjacency_matrix[j][i] = cost

    return adjacency_matrix


coordinates = {
    "New York": (40.7128, -74.0060),
    "Philadelphia": (39.9526, -75.1652),
    "Boston": (42.3601, -71.0589),
    "Washington DC": (38.9072, -77.0369),
    "Baltimore": (39.2904, -76.6122),
    "Albany": (42.6526, -73.7562),
    "Providence": (41.8240, -71.4128),
    "Richmond": (37.5407, -77.4360),
    "Pittsburgh": (40.4406, -79.9959),
    "Charlotte": (35.2271, -80.8431),
    "Columbus": (39.9612, -82.9988),
    "Cleveland": (41.4993, -81.6944),
    "Detroit": (42.3314, -83.0458),
    "Chicago": (41.8781, -87.6298),
    "Indianapolis": (39.7684, -86.1581),
    "Milwaukee": (43.0389, -87.9065),
    "Louisville": (38.2527, -85.7585),
    "Nashville": (36.1627, -86.7816),
    "Memphis": (35.1495, -90.0490),
    "Atlanta": (33.7490, -84.3880),
    "Cincinnati": (39.1031, -84.5120),
    "Madison": (43.0731, -89.4012),
    "Minneapolis": (44.9778, -93.2650),
    "Knoxville": (35.9606, -83.9207),
    "Greensboro": (36.0726, -79.7920),
    "Little Rock": (34.7465, -92.2896),
    "Birmingham": (33.5186, -86.8104),
    "Jackson": (32.2988, -90.1848),
    "Syracuse": (43.0481, -76.1474),
    "Hartford": (41.7658, -72.6734),
    "New Haven": (41.3083, -72.9279),
    "Des Moines": (41.5868, -93.6250)  # ✅ Added Des Moines!
}




def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two latitude/longitude points."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 111

def haversine_h(city1, city2, radius=6371):
    """Calculate the great-circle distance between two points on Earth (default in kilometers)."""
    lat1, lon1 = coordinates[city1]
    lat2, lon2 = coordinates[city2]
    
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Calculate the differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Apply the Haversine formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Return the distance
    return radius * c  # Distance in kilometers (change radius to 3958.8 for miles)