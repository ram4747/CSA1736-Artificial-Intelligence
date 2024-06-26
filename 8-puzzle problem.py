import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous

    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def is_goal(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal

    def get_neighbors(self):
        neighbors = []
        x, y = next((i, j) for i, row in enumerate(self.board) for j, val in enumerate(row) if val == 0)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))

        return neighbors

def solve_puzzle(start_board):
    start_state = PuzzleState(start_board)
    priority_queue = []
    heapq.heappush(priority_queue, start_state)
    visited = set()
    visited.add(tuple(map(tuple, start_state.board)))

    while priority_queue:
        current_state = heapq.heappop(priority_queue)

        if current_state.is_goal():
            solution_path = []
            while current_state:
                solution_path.append(current_state.board)
                current_state = current_state.previous
            solution_path.reverse()
            return solution_path

        for neighbor in current_state.get_neighbors():
            if tuple(map(tuple, neighbor.board)) not in visited:
                heapq.heappush(priority_queue, neighbor)
                visited.add(tuple(map(tuple, neighbor.board)))

    return None

def print_solution(solution):
    for step in solution:
        for row in step:
            print(row)
        print()

if __name__ == "__main__":
    start_board = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    solution = solve_puzzle(start_board)

    if solution:
        print("Solution found in {} moves:".format(len(solution) - 1))
        print_solution(solution)
    else:
        print("No solution found.")
