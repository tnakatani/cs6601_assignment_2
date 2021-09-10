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

    def move(self, game, time_left):
        player_moves = game.get_player_moves(self)
        
        print("-------------------------")
        print(game.print_board(player_moves))
        print("-------------------------")
        print()

        if not len(player_moves):
            print("No more moves left.")
            return None, None, None

        active_queens = game.get_active_players_queens()
        choice = []
        
        disp_cols = 4
        color_black, color_red = '\033[0m', '\033[91m'
        
        for queen in active_queens:
            counter = 1
            legal_moves = game.__get_moves__(game.__last_queen_move__[queen])
            for move in legal_moves:
                end = "\n" if counter % disp_cols == 0 else ""
                color = color_black if move not in choice else color_red
                print('\t'.join([color + '%d. %s \t' % (counter, move)]), end=end)                    
                counter += 1        
            
            if end != '\n':
                print()
                
            valid_choice = False

            while not valid_choice:
                try:
                    index = int(input(color_black + 'Select ' +  queen[-2:] + ' move: [1-' + str(len(legal_moves)) + ']:'))
                    valid_choice = 1 <= index <= len(legal_moves)
                    
                    if not valid_choice:
                        print('Illegal move of queen or invalid entry! Try again.')
                except Exception:
                    print('Invalid entry! Try again.')
                    
            choice.append(legal_moves[index - 1])
            print()
        return choice
    
    def get_name(self):
        return self.name
