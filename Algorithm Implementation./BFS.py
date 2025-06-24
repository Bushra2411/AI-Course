"""graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])

# Example usage:
bfs(graph, 'A')"""



from collections import deque

def get_graph_input():
    graph = {}   #Initializes an empty dictionary called graph.
    print("Enter the graph (e.g., A B C means A -> B and C). Type 'done' to finish.")
    while True:
        line = input("Enter node and its neighbors: ")
        if line.lower() == 'done':
            break
        parts = line.strip().split()    # "A B C " -> ['A','B','C']
        if parts:
            node = parts[0]       #1st item of node
            neighbors = parts[1:] #except the 1st item 
            graph[node] = neighbors
    return graph

def bfs(graph, start): 
    visited = set()         #Initializes an empty set called visited.This set will store the nodes that have already been visited during the traversal to prevent revisiting nodes.
    queue = deque([start])  #Initializes a queue (using deque), starting with the start node.The queue is used to keep track of nodes to be explored.The start node is added as the first element of the queue, and the traversal will begin from here

    print("\nBFS Traversal:", end=' ')
    while queue:
        node = queue.popleft()  #FIFO
        if node not in visited:
            print(node, end=' ')  #The end=' ' ensures that the nodes are printed on the same line, separated by spaces
            visited.add(node)     #Adds the current node to the visited set to mark it as visited.
            queue.extend(graph.get(node, []))   #This means all unvisited neighbors of the current node will be added to the queue for future exploration.

graph = get_graph_input()
start_node = input("Enter the start node for BFS: ")
bfs(graph, start_node)
