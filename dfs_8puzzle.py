from copy import deepcopy

# Goal state
goal_state = [[1,2,3], [4,5,6], [7,8,0]]

# Moves: up, down, left, right
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def dfs(start):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        state_tuple = tuple(map(tuple, state))

        if state == goal_state:
            return path + [state]

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        x, y = find_zero(state)

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_state = deepcopy(state)
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                stack.append((new_state, path + [state]))

    return None

# Example Start State
start = [[1,2,3], [4,0,6], [7,5,8]]
result = dfs(start)

# Print result
if result:
    for step in result:
        for row in step:
            print(row)
        print("------")
else:
    print("No solution found")
