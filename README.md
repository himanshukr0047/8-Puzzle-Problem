# 8-Puzzle-Problem
This project demonstrates the solution to the classic 8 Puzzle Problem using two fundamental AI search algorithms: Depth-First Search (DFS) and Breadth-First Search (BFS).


1. DFS Approach – Depth-First Search
Aim:
    To solve the 8-puzzle problem using Depth-First Search (DFS) algorithm, exploring deeper states before backtracking.

Algorithm:
 1. Start with the initial puzzle state.

 2. Use a stack to store the path and visited states.

 3. Move the blank tile (0) in all possible directions (up, down, left, right).

 4. Continue exploring deeper nodes.

 5. Stop when the goal state is found.

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
