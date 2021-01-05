import os
import gui

class GameIO():

    def __init__(self, viz):
        self.viz = viz
        if self.viz == 'y':
            gui.Main()

    def get_name(self, i):
        user_inp = input(f'Player {i} Name: ').strip()
        user_inp = self.name_validation(user_inp)
        return user_inp

    def name_validation(self, name):
        if len(name) < 3:
            name = input('Name must be at least 3 letters: ').strip()
            return self.name_validation(name)
        else:
            return name

    def get_move(self, player):
        inp = input(f'{player.name} select column 1 - 7: ').strip()
        inp = self.move_validation(inp, player)
        return inp

    def move_validation(self, move, player):
        '''Validate move can be converted to an int 
           betwee 1 and 7. Then convert and - 1'''
        valid_nums = list(range(1,8))
        if int(move) and int(move) in valid_nums:
            return int(move) - 1
        else:
            print('Selection out of range')
            return self.get_move(player)

    def print_board(self, board):
        for row in board.state:
            for item in board.state[row]:
                if board.state[row][item]:
                    print('|'+ str(board.state[row][item]) + '|', end='')
                else:
                    print('|_|', end='')
            print('')

    def cli_clrscrn(self):
        os.system('clear')
