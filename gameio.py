import os

class GameIO():

    def __init__(self):
        pass

    def get_name(self):
        user_inp = input('Player Name: ').strip()
        user_inp = self.name_validation(user_inp)
        return user_inp

    def name_validation(self, name):
        if len(name) < 3:
            name = input('Name must be at least 3 letters: ').strip()
            return self.name_validation(name)
        else:
            return name

    def get_move(self):
        pass

    def print_board(self, board):
        for row in board.state:
            for item in board.state[row]:
                if board.state[row][item]:
                    print('|'+ board.state[row][item] + '|', end='')
                else:
                    print('|_|', end='')
            print('')

    def cli_clrscrn(self):
        os.system('clear')
