class Node:
    def __init__(self, value=None, children=None):
        self.value = value  # For leaf nodes
        self.children = children if children else []

def minimax(node, is_maximizing):
    if not node.children:  # Leaf node
        return node.value

    if is_maximizing:
        return max(minimax(child, False) for child in node.children)
    else:
        return min(minimax(child, True) for child in node.children)

# Take user input
print("Building a tree...")

num_leaves = int(input("Enter number of leaf nodes (must be a power of 2, like 2, 4, 8, 16, etc.): "))

leaf_values = []
for i in range(num_leaves):
    val = int(input(f"Enter value for leaf {i + 1}: "))
    leaf_values.append(Node(value=val))

# Function to build tree recursively
def build_tree(nodes, is_maximizing):
    if len(nodes) == 1:
        return nodes[0]

    next_level = []
    for i in range(0, len(nodes), 2):
        parent = Node(children=[nodes[i], nodes[i + 1]])
        next_level.append(parent)
    
    return build_tree(next_level, not is_maximizing)

# Build the tree
root = build_tree(leaf_values, is_maximizing=True)

# Run minimax
result = minimax(root, is_maximizing=True)
print("Minimax result:", result)

