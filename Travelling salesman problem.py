import itertools

def calculate_distance(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]  # return to the start point
    return distance

def travelling_salesman_problem(graph):
    nodes = list(graph.keys())
    min_path = None
    min_distance = float('inf')

    for permutation in itertools.permutations(nodes):
        current_distance = calculate_distance(graph, permutation)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = permutation

    return min_path, min_distance

# Example usage
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

path, distance = travelling_salesman_problem(graph)
print(f"Minimum path: {path}")
print(f"Minimum distance: {distance}")
