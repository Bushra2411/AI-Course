
def get_graph_input():
    graph = {}
    print("Enter the graph (e.g., A B C means A -> B and C). Type 'done' to finish.")
    while True:
        line = input("Enter node and its neighbors: ")
        if line.lower() == 'done':
            break
        parts = line.strip().split()
        if parts:
            node = parts[0]
            neighbors = parts[1:]
            graph[node] = neighbors
    return graph

def dfs(graph, start):
    visited = set()
    stack = [start]

    print("\nDFS Traversal:", end=' ')
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Add neighbors in reverse to maintain left-to-right order
            stack.extend(reversed(graph.get(node, [])))


graph = get_graph_input()
start_node = input("Enter the start node for DFS: ")
dfs(graph, start_node)
