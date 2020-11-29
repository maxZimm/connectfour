
class GameIO():

    def __init__(self):
        pass

    def get_name(self):
        user_inp = input('Player Name: ').strip()
        user_inp = self.nameValidation(user_inp)
        return user_inp

    def name_validation(self, name):
        if len(name) < 3:
            name = input('Name must be at least 3 letters: ').strip()
            return self.nameValidation(name)
        else:
            return name

    def print_board(self, board):
        for row in board.state:
            for item in board.state[row]:
                if board.state[row][item]:
                    print('|'+ board.state[row][item] + '|', end='')
                else:
                    print('|_|', end='')
            print('')

