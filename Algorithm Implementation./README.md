# Artificial Intelligence Algorithms – 

This document contains an overview of various Artificial Intelligence algorithms we studied during the course, including how they work, their real-life applications, and their complexities.

---

## 🔍 Uninformed Search Algorithms

### 1. Breadth-First Search (BFS)
- **How it works:** Explores all nodes level by level using a queue (FIFO).
- **Applications:** Shortest path in unweighted graphs, social network analysis.
- **Complexity:**
  - Time: O(b^d)
  - Space: O(b^d)
  - (b = branching factor, d = depth of solution)

### 2. Depth-First Search (DFS)
- **How it works:** Explores as deep as possible before backtracking; uses a stack or recursion.
- **Applications:** Puzzle solving, pathfinding in mazes.
- **Complexity:**
  - Time: O(b^m)
  - Space: O(b*m)
  - (m = maximum depth)

### 3. Iterative Deepening Search (IDS)
- **How it works:** Combines DFS and BFS by increasing depth limit step-by-step.
- **Applications:** Game trees, memory-efficient pathfinding.
- **Complexity:**
  - Time: O(b^d)
  - Space: O(b*d)

### 4. Bidirectional Search
- **How it works:** Runs two simultaneous BFS searches—from the start and from the goal—and meets in the middle.
- **Applications:** GPS navigation, robot motion planning.
- **Complexity:**
  - Time: O(b^(d/2))
  - Space: O(b^(d/2))

### 5. Depth-Limited Search
- **How it works:** DFS with a fixed maximum depth.
- **Applications:** Large search trees with known depth limits.
- **Complexity:**
  - Time: O(b^l)
  - Space: O(b*l)
  - (l = depth limit)

---

## 🧠 Informed Search Algorithms

### 6. Heuristic Search
- **How it works:** Uses a heuristic function to estimate cost from current node to goal.
- **Applications:** Pathfinding in games, robotics, planning.
- **Complexity:** Depends on heuristic quality; generally improves over uninformed search.

### 7. Best-First Search
- **How it works:** Expands the node with the lowest heuristic value.
- **Applications:** Pathfinding, AI planning.
- **Complexity:**
  - Time: O(b^m)
  - Space: O(b^m)

### 8. A* Search
- **How it works:** Uses `f(n) = g(n) + h(n)` (actual cost + heuristic) to find the optimal path.
- **Applications:** Google Maps, game AI, robotics.
- **Complexity:**
  - Time: O(b^d)
  - Space: O(b^d) (depends on heuristic accuracy)

### 9. AO* Algorithm
- **How it works:** Works on AND-OR graphs to find optimal solutions by expanding paths that are most promising.
- **Applications:** Problem solving in decision trees with subgoals, diagnostics.
- **Complexity:** Varies; depends on graph structure and heuristics.

---

## ⚙️ Optimization Algorithms

### 10. Hill Climbing
- **How it works:** Starts with a random solution and makes small changes to improve it.
- **Applications:** Feature selection, scheduling, configuration problems.
- **Complexity:**
  - Time: O(n) to O(n^2) depending on steps and evaluation cost
  - Space: O(1)

### 11. Beam Search
- **How it works:** Keeps only top `k` best nodes at each level instead of all; limits memory.
- **Applications:** Speech recognition, machine translation.
- **Complexity:**
  - Time: O(k * b * d)
  - Space: O(k * d)

---

## 🎮 Game Playing Algorithms

### 12. Min-Max Algorithm
- **How it works:** Assumes both players play optimally and chooses moves to maximize the minimum gain.
- **Applications:** Chess, tic-tac-toe, checkers, other 2-player games.
- **Complexity:**
  - Time: O(b^m)
  - Space: O(m)

### 13. Alpha-Beta Pruning
- **How it works:** Improves Min-Max by cutting off branches that won’t affect the result.
- **Applications:** Chess engines, game AI.
- **Complexity:**
  - Time: O(b^(m/2)) (with good ordering)
  - Space: O(m)

---
