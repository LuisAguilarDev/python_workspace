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
