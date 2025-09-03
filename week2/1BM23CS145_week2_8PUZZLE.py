from collections import deque
import copy

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  

moves = [(-1,0), (1,0), (0,-1), (0,1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def is_goal(state):
    return state == goal_state

def print_state(state):
    for row in state:
        print(row)
    print()

def dfs(start_state, limit=50):
    stack = [(start_state, [])] 
    visited = set()

    while stack:
        state, path = stack.pop()
        state_tuple = tuple(tuple(row) for row in state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if is_goal(state):
            return path + [state]

        if len(path) >= limit:  
            continue

        for neighbor in get_neighbors(state):
            stack.append((neighbor, path + [state]))
    return None

def dls(state, depth, path, visited):
    if is_goal(state):
        return path + [state]
    if depth == 0:
        return None

    state_tuple = tuple(tuple(row) for row in state)
    visited.add(state_tuple)

    for neighbor in get_neighbors(state):
        neighbor_tuple = tuple(tuple(row) for row in neighbor)
        if neighbor_tuple not in visited:
            result = dls(neighbor, depth - 1, path + [state], visited)
            if result:
                return result
    return None

def ids(start_state, max_depth=50):
    for depth in range(max_depth):
        visited = set()
        result = dls(start_state, depth, [], visited)
        if result:
            return result
    return None


if __name__ == "__main__":
    start_state = [[1, 2, 3],
                   [4, 0, 6],
                   [7, 5, 8]]

    print("DFS Solution:")
    sol_dfs = dfs(start_state, limit=20)
    if sol_dfs:
        for step in sol_dfs:
            print_state(step)
    else:
        print("No solution found with DFS")

    print("\nIDS Solution:")
    sol_ids = ids(start_state, max_depth=20)
    if sol_ids:
        for step in sol_ids:
            print_state(step)
    else:
        print("No solution found with IDS")


