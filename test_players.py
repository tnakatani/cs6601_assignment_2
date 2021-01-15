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
        if not game.get_player_moves(self):
            return None
        repeat_move = True
        while repeat_move:
            
            queen1_moves = game.get_player_moves(self)[game.get_queen_name(game.__active_players_queen1__)]
            #print(queen1_moves)
            if len(queen1_moves):
                move1 = queen1_moves[randint(0,len(queen1_moves)-1)]
            else:
                move1 = None

            queen2_moves = game.get_player_moves(self)[game.get_queen_name(game.__active_players_queen2__)]
            #print(queen2_moves)
            if len(queen2_moves):
                move2 = queen2_moves[randint(0,len(queen2_moves)-1)]
            else:
                move2 = None

            queen3_moves = game.get_player_moves(self)[game.get_queen_name(game.__active_players_queen3__)]
            #print(queen3_moves)
            if len(queen3_moves):
                move3 = queen3_moves[randint(0,len(queen3_moves)-1)]
            else:
                move3 = None

            if move1 == None or move2 == None or move3 == None:
                return move1,move2,move3

            if move1 != move2 and move2!= move3 and move3 != move1:
                repeat_move = False
                return move1,move2,move3
            if move1 == move2:
                if len(queen1_moves) <= 1 and len(queen2_moves) <= 1:
                    return None,None,move3
            elif move2 == move3:
                if len(queen2_moves) <= 1 and len(queen3_moves) <= 1:
                    return move1,None,None
            elif move3 == move1:
                if len(queen1_moves) <= 1 and len(queen3_moves) <= 1:
                    return None,move2,None
            elif move1 == move2 == move3:
                if len(queen1_moves) <= 1 and len(queen2_moves) <= 1 and len(queen3_moves) <= 1:
                    return None,None,None

    def get_name(self):
        return self.name


class HumanPlayer(Player):
    """
    Player that chooses a move according to user's input. 
    (Useful if you play in the terminal)
    """
    def __init__(self, name="HumanPlayer"):
        super().__init__(name)

    def move(self, game, time_left):
        legal_moves = game.get_player_moves(self)
        choice = {}

        if not len(legal_moves):
            print("No more moves left.")
            return None, None

        counter = 1
        for move in legal_moves:
            choice.update({counter: move})
            print('\t'.join(['[%d] (%d,%d)' % (counter, move[0], move[1])]))
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
