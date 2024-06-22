from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 \
                or self.missionaries > 3 or self.cannibals > 3 \
                or (self.cannibals > self.missionaries and self.missionaries > 0) \
                or (3 - self.cannibals > 3 - self.missionaries and 3 - self.missionaries > 0):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and \
               self.cannibals == other.cannibals and \
               self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def successors(state):
    children = []
    if state.boat == 1:
        new_state = State(state.missionaries - 2, state.cannibals, 0, state)
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries, state.cannibals - 2, 0, state)
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries - 1, state.cannibals - 1, 0, state)
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries - 1, state.cannibals, 0, state)
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries, state.cannibals - 1, 0, state)
        if new_state.is_valid():
            children.append(new_state)
    else:
        new_state = State(state.missionaries + 2, state.cannibals, 1, state)
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries, state.cannibals + 2, 1, state)
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries + 1, state.cannibals + 1, 1, state)
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries + 1, state.cannibals, 1, state)
        if new_state.is_valid():
            children.append(new_state)
        new_state = State(state.missionaries, state.cannibals + 1, 1, state)
        if new_state.is_valid():
            children.append(new_state)
    return children

def breadth_first_search():
    initial_state = State(3, 3, 1)
    if initial_state.is_goal():
        return initial_state
    frontier = deque([initial_state])
    explored = set()
    while frontier:
        state = frontier.popleft()
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if child not in explored and child not in frontier:
                frontier.append(child)
    return None

def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    for t in range(len(path)):
        state = path[t]
        if state.parent:
            print(f"Move: {t + 1}, Boat: {'Left' if state.boat == 0 else 'Right'}, "
                  f"Missionaries: {abs(state.missionaries - state.parent.missionaries)}, "
                  f"Cannibals: {abs(state.cannibals - state.parent.cannibals)}")
        print(f"Left side: {state.missionaries} Missionaries, {state.cannibals} Cannibals | "
              f"Right side: {3 - state.missionaries} Missionaries, {3 - state.cannibals} Cannibals")
        print("--------------------------------------------------")

solution = breadth_first_search()
print("Solution Steps in Ascending Move Count:")
print_solution(solution)
