from random import randint
import random

class Player():
    def __init__(self, name="Player"):
        self.name = name

    def move(self, game, time_left):
        pass

    def get_name(self):
        return self.name


class RandomPlayer(Player):
    """Player that chooses a move randomly."""
    def __init__(self, name="RandomPlayer"):
        super().__init__(name)

    def move(self, game, time_left):
        
        move = random.choice(game.get_player_moves(self))
        return move

    def get_name(self):
        return self.name


class HumanPlayer(Player):
    """
    Player that chooses a move according to user's input. 
    (Useful if you play in the terminal)
    """
    def __init__(self, name="HumanPlayer"):
        super().__init__(name)

    def __get_moves(self, moves):
        moves_list = list(moves.values())
        legal_moves = []
        for move1 in moves_list[0]:
            for move2 in moves_list[1]:
                if move1 == move2:
                    continue
                for move3 in moves_list[2]:
                    if move1 == move3 or move2 == move3:
                        continue
                    legal_moves.append((move1, move2, move3))

        return legal_moves

    def move(self, game, time_left):
        queen_moves = game.get_player_moves(self)
        legal_moves = self.__get_moves(queen_moves)
        choice = {}

        if not len(legal_moves):
            print("No more moves left.")
            return None, None, None

        counter = 1
        for move in legal_moves:
            choice.update({counter: move})
            print('\t'.join(['[%d] %s' % (counter, move)]))
            counter += 1

        print("-------------------------")
        print(game.print_board(legal_moves))
        print("-------------------------")
        print(">< - impossible, o - valid move")
        print("-------------------------")

        valid_choice = False

        while not valid_choice:
            try:
                index = int(input('Select move index [1-' + str(len(legal_moves)) + ']:'))
                valid_choice = 1 <= index <= len(legal_moves)

                if not valid_choice:
                    print('Illegal move of queen! Try again.')
            except Exception:
                print('Invalid entry! Try again.')

        return choice[index]

    def get_name(self):
        return self.name
