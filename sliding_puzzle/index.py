puzzle = [[2,3],
          [0,1]]
puzzle2 = [[1,2],
          [3,0]]

puzzle3 = [[3,0],
           [2,1]]
# solution is [[1,2],
#              [3,0]]

def solve(puzzle):
    if isValid(puzzle): return 0
    IR = len(puzzle) - 1
    IC = len(puzzle[0]) - 1
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    r,c  = find(0,puzzle)
    can_move = []
    for dr,dc in directions:
        nr,nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr > IR or nc > IC:continue
        print(nr,nc)
        value = puzzle[nr][nc]
        if value:
            can_move.append(value)
    to_move = min(can_move)
    to_r,to_c = find(to_move,puzzle)
 
    same_row = r == to_r
    same_col = r == to_r
    isClockwise = ((same_row and r == 1 and c - to_c > 0) or
                    (same_row and r == 0 and c - to_c < 0) or 
                    (same_col and c == 0 and r - to_r > 0) or
                    (same_col and c == 1 and r - to_r < 0))
    movements = 0
    direction = [to_r - r,to_c - c]
    while True:
        dr,dc = direction
        print(r,c,direction)
        puzzle[r][c] = puzzle[r+dr][c+dc]
        r,c = r + dr, c + dc
        puzzle[r][c] = 0
        #clockwise -1j counterclockwise 1j
        n_direction = complex(*direction) * (-1j if isClockwise else 1j)
        direction =  [int(n_direction.real), int(n_direction.imag)] 
        movements += 1
        if isValid(puzzle):
            return movements
        # if iteration == 5:
        #     break

def isValid(puzzle):
    num = 1
    IR = len(puzzle)
    IC = len(puzzle[0])
    for r in range(0,IR):
        for c in range(0,IC):
            # print( (r == (IR - 1) and (IC - 1) == c))
            # print(r,c,puzzle[r][c],(0 if (r != (IR - 1) and (IC - 1) != c) else num))
            if puzzle[r][c] != (0 if (r == (IR - 1) and (IC - 1) == c) else num):
                return False
            num += 1
    return True

def find(num,puzzle):
    IR = len(puzzle)
    IC = len(puzzle[0])
    for r in range(0,IR):
        for c in range(0,IC):
            if puzzle[r][c] == num:
                return (r,c)
    return (-1,-1)
# print(solve(puzzle))
# print(solve(puzzle2))
# print(solve(puzzle3))

#recorrer los grafos por ciudad
#https://mega.nz/folder/fpVBTYDb#AhWVJ-CFyUA5mFHKIMZJjQ/folder/jpk1jAwR



def navigate_p2( grid, position ):
    R, C = len(grid), len(grid[0])
    
    visited = set()
    direction = 0 - 1j
    
    while True:
        r, c = int( position.imag ), int( position.real )
        dr, dc = int( direction.imag), int( direction.real)
        assert not( r >= R or r < 0 or c < 0 or c >= C )
     
        if (r,c,dr,dc) in visited:
            #print( 'Cycle detected' )
            return True
        visited.add( (r,c,dr,dc) )
            
        nr, nc = r + dr, c + dc
        if nr >= R or nr < 0 or nc < 0 or nc >= C:
            #print( 'EXIT', (nr, nc) )
            return False
    
        if grid[nr][nc] in '#O':
            direction *= 1j
        else:
            position += direction

print(0 - 1j)