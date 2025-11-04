8-Puzzle Problem

This project demonstrates solving the classic 8-Puzzle Problem using two fundamental AI search algorithms:
Depth-First Search (DFS) and Breadth-First Search (BFS).

Problem Description

The 8-Puzzle consists of a 3×3 grid containing tiles numbered from 1 to 8 and one blank space (0).
The objective is to move the blank space to rearrange the tiles until the goal configuration is reached.

Example

Initial State

1 2 3
4 0 6
7 5 8


Goal State

1 2 3
4 5 6
7 8 0

DFS Approach – Depth-First Search
Aim

To solve the 8-puzzle problem using the Depth-First Search (DFS) algorithm, exploring deeper states before backtracking.

Algorithm

Start with the initial puzzle state.

Use a stack to store states and track visited configurations.

Generate all possible moves by sliding the blank tile (0) up, down, left, right.

Push unvisited child states onto the stack.

Continue exploring deeper paths recursively.

Stop when the goal state is found.

If all paths are explored without success → no solution exists.

Pseudocode
def dfs(start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path + [state]
        visited.add(tuple(state))
        for next_state in get_neighbors(state):
            if tuple(next_state) not in visited:
                stack.append((next_state, path + [state]))
    return None

Complexity

Time Complexity: O(b^m)
(b = branching factor, m = maximum depth)

Space Complexity: O(b × m)

BFS Approach – Breadth-First Search
Aim

To solve the 8-puzzle problem using the Breadth-First Search (BFS) algorithm to find the shortest path to the goal state.

Algorithm

Start with the initial state.

Use a queue to explore nodes level by level.

Generate all valid next moves (children).

Skip already visited states.

Stop when the goal state is reached.

If the queue becomes empty → no solution exists.

Pseudocode
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        visited.add(tuple(state))
        for next_state in get_neighbors(state):
            if tuple(next_state) not in visited:
                queue.append((next_state, path + [state]))
    return None

Complexity

Time Complexity: O(b^d)
(b = branching factor, d = depth of the solution)

Space Complexity: O(b^d)
Time Complexity:
* Worst-case: O(b^m) (b = branching factor, m = max depth)

* Space: O(b*m)



2. BFS Approach – Breadth-First Search
Aim:
   To solve the 8-puzzle problem using Breadth-First Search (BFS) algorithm to find the shortest path to the goal state.

Algorithm:
 1. Start with the initial puzzle state.

 2. Use a queue to store current state and path.

 3. Generate all possible valid next states (children).

 4. Check if the state is visited.

 5. Stop if goal is reached.

Time Complexity:
 * Worst-case: O(b^d) (b = branching factor, d = depth of solution)

 * Space: O(b^d)
