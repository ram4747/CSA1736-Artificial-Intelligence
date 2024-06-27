from heapq import heappop, heappush

def a_star(graph, start, goal, heuristic):
    open_set = []
    heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]
    
    while open_set:
        current_f, current = heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                if neighbor not in [i[1] for i in open_set]:
                    heappush(open_set, (f_score[neighbor], neighbor))
    
    return None

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

start = 'A'
goal = 'D'
path = a_star(graph, start, goal, heuristic)
print(f"Path from {start} to {goal}: {path}")
