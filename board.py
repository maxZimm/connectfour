
class Board():

    def __init__(self):
        self.state = {
          0: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None },
          1: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None },
          2: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None },
          3: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None },
          4: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None },
          5: {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None }
         }

    def accept_move(self, move):
        '''Move is tuple with 2 elments 
           index 0 is player index 1 is column'''    
        rows = list(range(6))
        rows.reverse()
        for row in rows:
            if not self.state[row][move[1]]:
                self.state[row][move[1]] = move[0]
                break

    def check_winner(self):
        # check rows, check columns, check diagonals
        for row in range(6):
            if self.check_row_win(self.state[row]):
                return self.check_row_win(self.state[row])
        for col in range(7):
            if self.check_col_win(col):
                return self.check_col_win(col)
        if self.check_diag_win():
            return self.check_diag_win()

    def check_row_win(self, row):
        # count the number of times the same valid value occurs in a dict
        count = 1
        items = list(range(1,7))
        for item in items:
            if (row[item] == row[item - 1]) and row[item] is not None:
                count += 1
                if count == 4:
                    return row[item]
            else:
                count = 1 

    def check_col_win(self, col):
        count = 1
        items = list(range(1,6))
        for item in items:
            if (self.state[item][col] == self.state[item - 1][col]) and self.state[item][col] is not None:
                count += 1
                if count == 4:
                    return self.state[item][col]
            else:
                count = 1

    def check_diag_win(self):
        descend_points = [[5,6], [5,5], [5,4], [5,3], [4,6], [3,6]] 
        ascend_points = [[5,0], [5,1], [5,2], [5,3], [4,0], [3,0]]
        for point in descend_points:
            if self.diag_decrement(point):
                return self.diag_decrement(point)

        for point in ascend_points:
            if self.diag_increment(point):
                return self.diag_increment(point)

    def diag_decrement(self, point):
        count = 1
        r,c = point[0], point[1]
        index = r if r < c else c
        index = range(index)
        for i in index:
            if (self.state[r][c] == self.state[r - 1][c - 1]) and self.state[r][c] is not None:
                count += 1
                if count == 4:
                    return self.state[r][c]
            else:
                count = 1        
            r -= 1
            c -= 1

    def diag_increment(self, point):
        count = 1
        r,c = point[0], point[1]
        index = r if c < 2 else 6 - c
        index = range(index)
        for i in index:
            if (self.state[r][c] == self.state[r - 1][c + 1]) and self.state[r][c] is not None:
                count += 1
                if count == 4:
                    return self.state[r][c]
            else:
                count = 1        
            r -= 1
            c += 1
