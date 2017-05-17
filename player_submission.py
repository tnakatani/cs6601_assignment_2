#!/usr/bin/env python
from isolation import Board, game_as_text
from test_players import RandomPlayer


# This file is your main submission that will be graded against. Do not
# add any classes or functions to this file that are not part of the classes
# that we want.

# Submission Class 1
class OpenMoveEvalFn():
    """Evaluation function that outputs a 
    score equal to how many moves are open
    for AI player on the board minus
    the moves open for opponent player."""

    def score(self, game, maximizing_player_turn=True):
        # TODO: finish this function!
        raise NotImplementedError
        return eval_func


# Submission Class 2
class CustomEvalFn():
    """Custom evaluation function that acts
    however you think it should. This is not
    required but highly encouraged if you
    want to build the best AI possible."""

    def score(self, game, maximizing_player_turn=True):
        # TODO: finish this function!
        raise NotImplementedError
        return eval_func


class CustomPlayer():
    # TODO: finish this class!
    """Player that chooses a move using 
    your evaluation function and 
    a depth-limited minimax algorithm 
    with alpha-beta pruning.
    You must finish and test this player
    to make sure it properly uses minimax
    and alpha-beta to return a good move
    in less than 5 seconds."""

    def __init__(self, search_depth=3, eval_fn=OpenMoveEvalFn()):
        # if you find yourself with a superior eval function, update the
        # default value of `eval_fn` to `CustomEvalFn()`
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, legal_moves, time_left):
        best_move, best_queen, utility = self.minimax(game, time_left, depth=self.search_depth)
        # change minimax to alphabeta after completing alphabeta part of assignment
        return best_move, best_queen

    def utility(self, game):
        """TODO: Update this function to calculate the utility of a game state"""
        return self.eval_fn.score(game)

    def minimax(self, game, time_left, depth=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        raise NotImplementedError
        return best_move, best_queen, best_val

    def alphabeta(self, game, time_left, depth=float("inf"), alpha=float("-inf"), beta=float("inf"),
                  maximizing_player=True):
        # TODO: finish this function!
        raise NotImplementedError
        return best_move, best_queen, val


def main():

    try:
        sample_board = Board(RandomPlayer(), RandomPlayer())
        # setting up the board as though we've been playing
        sample_board.move_count = 4
        sample_board.__board_state__ = [
            [11, 0, 0, 0, 21, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 22, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 12, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        sample_board.__last_queen_move__ = {sample_board.queen_11: (0, 0), sample_board.queen_12: (4, 5),
                                            sample_board.queen_21: (0, 4), sample_board.queen_22: (2, 2)}
        h = OpenMoveEvalFn()
        print('OpenMoveEvalFn Test: This board has a score of %s.' % (h.score(sample_board)))
    except NotImplementedError:
        print 'OpenMoveEvalFn not implemented'

    try:
        """Example test to make sure
        your minimax works, using the
        #computer_player_moves - opponent_moves evaluation function."""
        # create dummy 3x3 board

        p1 = RandomPlayer()
        p2 = RandomPlayer()
        # p2 = CustomPlayer2( search_depth=3)
        # p2 = HumanPlayer()
        b = Board(p1, p2, 5, 5)
        b.__board_state__ = [
            [0, 21, 0, 0, 0],
            [0, 0, 11, 0, 0],
            [0, 0, 12, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 22, 0, 0, 0]
        ]
        b.__last_queen_move__["queen11"] = (1, 2)
        b.__last_queen_move__["queen21"] = (0, 1)
        b.__last_queen_move__["queen12"] = (2, 2)
        b.__last_queen_move__["queen22"] = (4, 1)

        b.move_count = 4

        output_b = b.copy()
        winner, move_history, queen_history, termination = b.play_isolation()
        print 'Minimax Test: runs successfully'
        # Uncomment to see example game
        # print game_as_text(winner, move_history, queen_history, termination, output_b)
    except NotImplementedError:
        print 'Minimax not implemented'

    """Example test you can run
    to make sure your AI does better
    than random."""
    try:
        r = CustomPlayer()
        h = RandomPlayer()
        game = Board(r, h, 7, 7)
        output_b = game.copy()
        winner, move_history, queen_history, termination = game.play_isolation()
        if 'CustomPlayer' in str(winner):
            print 'CustomPlayer Test: CustomPlayer Won'
        else:
            print 'CustomPlayer Test: CustomPlayer Lost'
        # Uncomment to see game
        # print (game_as_text(winner, move_history, queen_history, termination, output_b))
    except NotImplementedError:
        print 'CustomPlayer not implemented'

if __name__ == "__main__":
    main()
