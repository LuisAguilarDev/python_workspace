import heapq
import time
def find_zero(matrix):
    """Finds and returns the (i, j) position of the element 0 in the matrix."""
    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col == 0:
                return r, c
    raise ValueError("Matrix does not contain a zero.")

# no heuristic
def find_solution(matrix,solution):
    IR = len(matrix)
    IC = len(matrix[0])
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = [matrix]
    queue = [(matrix,0)]
    while queue:
        cm,steps = queue.pop(0)
        if(cm == solution):
            return (cm,steps)
        # Find the position of zero
        r, c = find_zero(cm)
        for dr,dc in directions:
            nr, nc = r + dr, c + dc
            if nr >= IR or nr < 0 or nc < 0 or nc >= IC: continue
            # Convert to a mutable list of lists
            mut = [list(row) for row in cm]
            # Swap the element 0 with the element at the new position
            mut[r][c], mut[nr][nc] = mut[nr][nc], mut[r][c]
            next_m = tuple(tuple(row) for row in mut)
            if(next_m not in visited):
                visited.append(next_m)
                queue.append((next_m,steps+1))
    return (None,-1)

# Example matrix as a tuple of tuples
matrix = (
    (5, 6, 4),
    (3, 2, 7),
    (8, 1, 0)
)

start_time = time.time()
_,steps = find_solution(matrix,((1, 2, 3),(4, 5, 6), (7, 8, 0)))
print("find_solution:",steps)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.5f} seconds")

# Example matrix as a tuple of tuples
matrix = (
    (0, 1),
    (3, 2),
)

solution = (
    (1, 2),
    (3, 0),
)

puzzle = ((2,3),(0,1))
puzzle2 = ((1,2),(3,0))

puzzle3 = ((3,0),(2,1))
unsolvable = ((0,2),(3,1))
solution = ((1,2),(3,0))
print(find_solution(puzzle,solution))
print(find_solution(puzzle2,solution))
print(find_solution(puzzle3,solution))
print(find_solution(unsolvable,solution))

def heuristic(puzzle):
    # check the movements to reach its place
    goal_position = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 0: (2, 2)
    }

    distance = 0
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            c_value = puzzle[r][c]
            if c_value != 0:  # Skip the empty tile
                gr, gc = goal_position[c_value]
                distance += abs(r - gr) + abs(c - gc)
    
    return distance

# with heutistic
def find_solution_a_star(matrix,solution):
    IR = len(matrix)
    IC = len(matrix[0])
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    pq = []
    visited_cost = {matrix:0}
    heapq.heappush(pq,(heuristic(matrix),matrix,0))
    while pq:
        _,cm,steps = heapq.heappop(pq)
        if(cm == solution):
            return (cm,steps)
        # Find the position of zero
        r, c = find_zero(cm)
        for dr,dc in directions:
            nr, nc = r + dr, c + dc
            if nr >= IR or nr < 0 or nc < 0 or nc >= IC: continue
            # Convert to a mutable list of lists
            mut = [list(row) for row in cm]
            # Swap the element 0 with the element at the new position
            mut[r][c], mut[nr][nc] = mut[nr][nc], mut[r][c]
            next_m = tuple(tuple(row) for row in mut)
            if (steps + 1) < visited_cost.get(next_m,float('inf')):
                visited_cost[next_m] = steps + 1
                priority = steps + 1 + heuristic(next_m)
                heapq.heappush(pq,(priority,next_m,steps+1))
    return (None,-1)

matrix = (
    (5, 6, 4),
    (3, 2, 7),
    (8, 1, 0)
)

start_time = time.time()
_,steps = find_solution_a_star(matrix,((1, 2, 3),(4, 5, 6), (7, 8, 0)))
print("find_solution_a_star:",steps)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.5f} seconds")