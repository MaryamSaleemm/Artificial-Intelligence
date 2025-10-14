class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

# Initialize the graph as a dictionary with Node objects
graph = {
    'A': Node('A', None, ['B', 'E', 'C'], 0),  # A is the root, no parent, connects to B, E, C
    'B': Node('B', None, ['A', 'D', 'E'], 0),  # B connects to A, D, E
    'C': Node('C', None, ['A', 'F', 'G'], 0),  # C connects to A, F, G
    'D': Node('D', None, ['B', 'E'], 0),       # D connects to B, E
    'E': Node('E', None, ['A', 'B', 'D'], 0),  # E connects to A, B, D
    'F': Node('F', None, ['C'], 0),            # F connects to C
    'G': Node('G', None, ['C'], 0)             # G connects to C
}

# Optional: Print the graph structure to verify
for node_state, node in graph.items():
    print(f"Node {node_state}: Parent = {node.parent}, Actions = {node.actions}, Total Cost = {node.totalCost}")