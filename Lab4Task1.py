class Node:
    def __init__(self, state, parent, actions, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions  # List of (neighbor, distance) tuples
        self.totalCost = totalCost

# Define the graph with distances (undirected)
graph = {
    'Arad': Node('Arad', None, [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)], 0),
    'Zerind': Node('Zerind', None, [('Arad', 75), ('Oradea', 71)], 0),
    'Oradea': Node('Oradea', None, [('Zerind', 71), ('Sibiu', 151)], 0),
    'Timisoara': Node('Timisoara', None, [('Arad', 118), ('Lugoj', 111)], 0),
    'Lugoj': Node('Lugoj', None, [('Timisoara', 111), ('Mehadia', 70)], 0),
    'Mehadia': Node('Mehadia', None, [('Lugoj', 70), ('Dobreta', 75)], 0),
    'Dobreta': Node('Dobreta', None, [('Mehadia', 75), ('Craiova', 120)], 0),
    'Craiova': Node('Craiova', None, [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)], 0),
    'Sibiu': Node('Sibiu', None, [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)], 0),
    'Fagaras': Node('Fagaras', None, [('Sibiu', 99), ('Bucharest', 211)], 0),
    'Rimnicu Vilcea': Node('Rimnicu Vilcea', None, [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)], 0),
    'Pitesti': Node('Pitesti', None, [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)], 0),
    'Bucharest': Node('Bucharest', None, [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)], 0),
    'Giurgiu': Node('Giurgiu', None, [('Bucharest', 90)], 0),
    'Urziceni': Node('Urziceni', None, [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)], 0),
    'Hirsova': Node('Hirsova', None, [('Urziceni', 98), ('Eforie', 86)], 0),
    'Eforie': Node('Eforie', None, [('Hirsova', 86)], 0),
    'Vaslui': Node('Vaslui', None, [('Urziceni', 142), ('Iasi', 92)], 0),
    'Iasi': Node('Iasi', None, [('Vaslui', 92), ('Neamt', 87)], 0),
    'Neamt': Node('Neamt', None, [('Iasi', 87)], 0)
}

def DFS(initialState, goalState):
    frontier = [initialState]
    explored = []
    
    while len(frontier) > 0:
        currentNode = frontier.pop()
        if currentNode not in explored:
            explored.append(currentNode)
            for neighbor, distance in graph[currentNode].actions:
                if neighbor not in frontier and neighbor not in explored:
                    graph[neighbor].parent = currentNode
                    graph[neighbor].totalCost = graph[currentNode].totalCost + distance
                    if neighbor == goalState:
                        return actionSequence(graph, initialState, goalState), graph[neighbor].totalCost
                    frontier.append(neighbor)
    
    return None, float('inf')  # No path found

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

# Test the DFS
initialState = 'Arad'
goalState = 'Bucharest'
path, totalDistance = DFS(initialState, goalState)

if path:
    print(f"Path from {initialState} to {goalState}: {path}")
    print(f"Total Distance: {totalDistance} km")
else:
    print("No path found.")