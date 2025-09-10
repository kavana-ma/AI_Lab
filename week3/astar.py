import heapq

goal_state = [[1,2,3],
              [8,0,4],
              [7,6,5]]

moves = [(1,0), (-1,0), (0,1), (0,-1)]

def to_tuple(board):
    return tuple(tuple(row) for row in board)

def find_pos(board, value):
    for i in range(3):
        for j in range(3):
            if board[i][j] == value:
                return (i, j)

# Heuristic 1: misplaced tiles
def h_misplaced(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal_state[i][j]:
                count += 1
    return count

# Heuristic 2: manhattan distance
def h_manhattan(board):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                goal_i, goal_j = find_pos(goal_state, val)
                dist += abs(i - goal_i) + abs(j - goal_j)
    return dist

def get_neighbors(board):
    neighbors = []
    x, y = find_pos(board, 0)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [list(row) for row in board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(new_board)
    return neighbors

def print_board(board):
    for row in board:
        print(' '.join(str(x) for x in row))
    print()

def astar(start, heuristic):
    pq = []
    g = 0
    f = g + heuristic(start)
    heapq.heappush(pq, (f, g, start, []))
    visited = set()

    while pq:
        f, g, board, path = heapq.heappop(pq)
        if board == goal_state:
            return path + [board]

        visited.add(to_tuple(board))

        for neighbor in get_neighbors(board):
            if to_tuple(neighbor) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [board]))
    return None

start_state1 = [[1,2,3],
               [4,0,6],
               [7,5,8]]

start_state2 = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

start_state3 = [
    [8, 0, 3],
    [2, 1, 4],
    [7, 6, 5]
]

print("Using Misplaced Tiles:")
solution = astar(start_state3, h_misplaced)
print("Steps:", len(solution)-1)
for step, board in enumerate(solution):
    print(f"Step {step}:")
    print_board(board)

print("Using Manhattan Distance:")
solution = astar(start_state3, h_manhattan)
print("Steps:", len(solution)-1)
for step, board in enumerate(solution):
    print(f"Step {step}:")
    print_board(board)
