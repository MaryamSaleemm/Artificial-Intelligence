# Regions of Australia
regions = [
    "Western Australia", "Northern Territory", "South Australia",
    "Queensland", "New South Wales", "Victoria", "Tasmania"
]

# Possible colors
colors = ["Red", "Green", "Blue"]

# Adjacency (who borders whom)
neighbors = {
    "Western Australia": ["Northern Territory", "South Australia"],
    "Northern Territory": ["Western Australia", "South Australia", "Queensland"],
    "South Australia": ["Western Australia", "Northern Territory",
                        "Queensland", "New South Wales", "Victoria"],
    "Queensland": ["Northern Territory", "South Australia", "New South Wales"],
    "New South Wales": ["Queensland", "South Australia", "Victoria"],
    "Victoria": ["South Australia", "New South Wales"],
    "Tasmania": []   # No borders
}

# Backtracking CSP solver
def is_valid(region, color, assignment):
    """Check if assigning this color to this region is valid"""
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(assignment):
    """Recursive backtracking solver"""
    # If all regions assigned → solution found
    if len(assignment) == len(regions):
        return assignment

    # Choose an unassigned region
    region = [r for r in regions if r not in assignment][0]

    # Try each color
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color  # choose
            result = solve(assignment)
            if result:
                return result
            del assignment[region]  # undo (backtrack)

    return None

# Run the solver
solution = solve({})

print("Map Coloring Solution:\n")
for region, color in solution.items():
    print(f"{region}: {color}")