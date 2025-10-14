class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost

# Initialize the graph as a dictionary with Node objects
graph = {
    'A': Node('A', None, ['B', 'C', 'E'], 0),
    'B': Node('B', None, ['A', 'D', 'E'], 0),
    'C': Node('C', None, ['A', 'F', 'G'], 0),
    'D': Node('D', None, ['B', 'E'], 0),
    'E': Node('E', None, ['A', 'B', 'D'], 0),
    'F': Node('F', None, ['C'], 0),
    'G': Node('G', None, ['C'], 0)
}

def DFS(initialState, goalState):
    # Initialize frontier (stack) with the initial state
    frontier = [initialState]
    # Initialize explored set to keep track of visited nodes
    explored = []
    
    # Continue while there are nodes to explore
    while len(frontier) > 0:
        # Remove the last node (LIFO)
        currentNode = frontier.pop()
        # Add the current node to explored
        explored.append(currentNode)
        
        # Explore all actions (neighbors) of the current node
        for child in graph[currentNode].actions:
            # If child is not in frontier or explored
            if child not in frontier and child not in explored:
                # Set the parent of the child node
                graph[child].parent = currentNode
                # If child is the goal state, reconstruct and return the path
                if graph[child].state == goalState:
                    return actionSequence(graph, initialState, goalState)
                # Add child to frontier for further exploration
                frontier.append(child)
        # If frontier is empty and goal not found, return failure (implicitly handled by loop end)
    
    return None  # No path found (though not explicitly shown in the image)

def actionSequence(graph, initialState, goalState):
    # Start with the goal state
    solution = [goalState]
    # Backtrack from goal to initial state using parent pointers
    currentParent = graph[goalState].parent
    
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    
    # Reverse the solution to get path from initial to goal
    solution.reverse()
    # Return the sequence of actions (path)
    return solution

# Test the DFS
initialState = 'A'  # As specified in the activity
goalState = 'F'    # As specified in the activity
solution = DFS(initialState, goalState)

# Print the solution
print("Solution:", solution)

# Example call as per the image note
# Calling DFS() will return the following solution: ['A', 'C', 'F']