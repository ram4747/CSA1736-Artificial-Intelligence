class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.current_position = (0, 0)
        self.path_cost = 0

    def move_up(self):
        if self.current_position[0] > 0:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
            self.path_cost += 1

    def move_down(self):
        if self.current_position[0] < len(self.grid) - 1:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
            self.path_cost += 1

    def move_left(self):
        if self.current_position[1] > 0:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
            self.path_cost += 1

    def move_right(self):
        if self.current_position[1] < len(self.grid[0]) - 1:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
            self.path_cost += 1

    def clean(self):
        while True:
            if self.grid[self.current_position[0]][self.current_position[1]] == 'dirty':
                self.grid[self.current_position[0]][self.current_position[1]] = 'clean'
                print(f"Cleaning cell {self.current_position}")
            if self.is_clean():
                print("All cells are clean!")
                break
            else:
                self.move_to_nearest_dirty_cell()

    def move_to_nearest_dirty_cell(self):
        dirty_cells = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'dirty':
                    dirty_cells.append((i, j))
        nearest_dirty_cell = min(dirty_cells, key=lambda x: abs(x[0] - self.current_position[0]) + abs(x[1] - self.current_position[1]))
        if nearest_dirty_cell[0] < self.current_position[0]:
            self.move_up()
            print("Moving up")
        elif nearest_dirty_cell[0] > self.current_position[0]:
            self.move_down()
            print("Moving down")
        elif nearest_dirty_cell[1] < self.current_position[1]:
            self.move_left()
            print("Moving left")
        else:
            self.move_right()
            print("Moving right")

    def is_clean(self):
        for row in self.grid:
            if 'dirty' in row:
                return False
        return True


grid = [['clean', 'dirty', 'clean', 'clean'],
        ['clean', 'clean', 'dirty', 'clean'],
        ['dirty', 'clean', 'clean', 'dirty']]

vacuum_cleaner = VacuumCleaner(grid)
vacuum_cleaner.clean()
print("Total path cost:", vacuum_cleaner.path_cost)
