"""def dls(graph, node, limit):
    if limit < 0:
        return False
    print(node, end=' ')  # Shows the order of visited nodes
    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, limit - 1):
            return True
    return False

def ids(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth limit: {depth}")
        if dls(graph, start, depth):
            return True
    return False

# ---- User Input Section ----
graph = {}
num_nodes = int(input("How many nodes are there? "))

for _ in range(num_nodes):
    entry = input("Enter a node followed by its children (space-separated): ").split()
    node = entry[0]
    children = entry[1:]
    graph[node] = children

start_node = input("Enter the start node: ")
depth_limit_dls = int(input("Enter depth limit for DLS: "))
depth_limit_ids = int(input("Enter maximum depth for IDS: "))

# ---- Run DLS ----
print("\n--- Depth-Limited Search (DLS) ---")
dls(graph, start_node, depth_limit_dls)

# ---- Run IDS ----
print("\n\n--- Iterative Deepening Search (IDS) ---")
ids(graph, start_node, depth_limit_ids)"""



def get_graph_input():
    graph = {}   # Initializes an empty dictionary called graph.
    print("Enter the graph (e.g., A B C means A -> B and C). Type 'done' to finish.")
    while True:
        line = input("Enter node and its neighbors: ")
        if line.lower() == 'done':
            break
        parts = line.strip().split()    # "A B C " -> ['A','B','C']
        if parts:
            node = parts[0]       # 1st item is the node
            neighbors = parts[1:] # remaining items are neighbors
            graph[node] = neighbors
    return graph

def dls(graph, node, limit):
    if limit < 0:
        return False
    print(node, end=' ')
    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, limit - 1):
            return True
    return False

def ids(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth limit: {depth}")
        if dls(graph, start, depth):
            return True
    return False

# ---- Main Program ----
graph = get_graph_input()
start_node = input("\nEnter the start node: ")
depth_limit_dls = int(input("Enter depth limit for DLS: "))
depth_limit_ids = int(input("Enter maximum depth for IDS: "))

print("\n--- Depth-Limited Search (DLS) ---")
dls(graph, start_node, depth_limit_dls)

print("\n\n--- Iterative Deepening Search (IDS) ---")
ids(graph, start_node, depth_limit_ids)
