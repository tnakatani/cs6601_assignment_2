#!/usr/bin/env python
import traceback
from isolation import Board, game_as_text
from test_players import RandomPlayer, HumanPlayer, Player
import platform

if platform.system() != 'Windows':
    import resource

from time import time, sleep

def correctOpenEvalFn(yourOpenEvalFn):
    print()
    try:
        sample_board = Board(RandomPlayer(), RandomPlayer())
        # setting up the board as though we've been playing
        board_state = [
            ["11", " ", " ", "22", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ["12", " ", " ", "21", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            ["12", " ", " ", " ", " ", " ", "23"]
        ]
        sample_board.set_state(board_state, True)
        #test = sample_board.get_legal_moves()
        h = yourOpenEvalFn()
        print('OpenMoveEvalFn Test: This board has a score of %s.' % (h.score(sample_board, sample_board.get_active_player())))
    except NotImplementedError:
        print('OpenMoveEvalFn Test: Not implemented')
    except:
        print('OpenMoveEvalFn Test: ERROR OCCURRED')
        print(traceback.format_exc())

    print()

def beatRandom(yourAgent):

    """Example test you can run
    to make sure your AI does better
    than random."""

    print("")
    try:
        r = RandomPlayer()
        p = yourAgent()
        game = Board(r, p, 7, 7)
        output_b = game.copy()
        winner, move_history, termination = game.play_isolation(time_limit=1000, print_moves=True)
        print("\n", winner, " has won. Reason: ", termination)
        # Uncomment to see game
        # print game_as_text(winner, move_history, termination, output_b)
    except NotImplementedError:
        print('CustomPlayer Test: Not Implemented')
    except:
        print('CustomPlayer Test: ERROR OCCURRED')
        print(traceback.format_exc())

    print()

def minimaxTest(yourAgent, minimax_fn):
    """Example test to make sure
    your minimax works, using the
    OpenMoveEvalFunction evaluation function.
    This can be used for debugging your code
    with different model Board states.
    Especially important to check alphabeta
    pruning"""

    # create dummy 5x5 board
    print("Now running the Minimax test.")
    print()
    try:
        def time_left():  # For these testing purposes, let's ignore timeouts
            return 10000

        player = yourAgent() #using as a dummy player to create a board
        sample_board = Board(player, RandomPlayer())
        # setting up the board as though we've been playing
        board_state = [
            ["X", "X", "12", "X", "13", "X", " "],
            [" ", "X", "X", " ", " ", "X", "X"],
            ["X", " ", "11", "X", " ", "X", " "],
            [" ", "X", "X", "X", " ", "X", " "],
            [" ", "X", "22", " ", "X", " ", "X"],
            [" ", " ", "X", "X", "21", "X", " "],
            ["X", "23", "X", "X", "X", "X", "X"]
        ]
        sample_board.set_state(board_state, p1_turn = True)

        test_pass = True

        expected_depth_scores = [(1, -3), (2, 1), (3, 4)]

        for depth, exp_score in expected_depth_scores:
            move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=True)
            print(score)
            if exp_score != score:
                print("Minimax failed for depth: ", depth)
                test_pass = False
            else:
                print("Minimax passed for depth: ", depth)

        if test_pass:
            player = yourAgent()
            sample_board = Board(RandomPlayer(), player)
            # setting up the board as though we've been playing
            board_state = [
                ["X", "X", " ", "X", " ", "X", " "],
                [" ", "", "X", " ", " ", "X", "X"],
                ["X", "11", " ", "22", " ", "X", " "],
                [" ", "X", "X", "X", " ", "X", " "],
                ["12", "X", " ", " ", " ", "13", "X"],
                [" ", " ", "21", "X", " ", "X", " "],
                ["X", "23", "X", "X", "", "X", "X"]
            ]
            sample_board.set_state(board_state, p1_turn=False)

            test_pass = True

            expected_depth_scores = [(1, 24), (2, 8), (3, float("inf"))]

            for depth, exp_score in expected_depth_scores:
                move, score = minimax_fn(player, sample_board, time_left, depth=depth, my_turn=True)
                print(score)
                if exp_score != score:
                    print("Minimax failed for depth: ", depth)
                    test_pass = False
                else:
                    print("Minimax passed for depth: ", depth)

        if test_pass:
            print("Minimax Test: Runs Successfully!")

        else:
            print("Minimax Test: Failed")

    except NotImplementedError:
        print('Minimax Test: Not implemented')
    except:
        print('Minimax Test: ERROR OCCURRED')
        print(traceback.format_exc())

def alphabeta_ID_test(yourAgent, algorithm, algorithm_name):
    """Example test to make sure
    your minimax works, using the
    OpenMoveEvalFunction evaluation function.
    This can be used for debugging your code
    with different model Board states.
    Especially important to check alphabeta
    pruning"""

    # create dummy 5x5 board
    print(f"Now running the {algorithm_name} test.")
    print()
    try:
        def time_left():  # For these testing purposes, let's ignore timeouts
            return 10000

        player = yourAgent() #using as a dummy player to create a board
        sample_board = Board(player, RandomPlayer())
        # setting up the board as though we've been playing
        board_state = [
            ["X", "X", "12", "X", "13", "X", " "],
            [" ", " ", "X", " ", " ", "X", "X"],
            ["X", " ", "11", " ", " ", "X", " "],
            [" ", " ", "X", "X", " ", "X", " "],
            [" ", "X", "22", " ", " ", " ", "X"],
            [" ", "X", " ", " ", "21", "X", " "],
            ["X", "23", "X", "X", "X", "X", "X"]
        ]
        sample_board.set_state(board_state, p1_turn = True)

        test_pass = True

        expected_depth_scores = [(1, 42), (2, 20), (3, 4), (4, 9)]

        for depth, exp_score in expected_depth_scores:
            move, score = algorithm(player, sample_board, time_left, depth=depth, my_turn=True)
            print(score)
            if exp_score != score:
                print(f"{algorithm_name} failed for depth: ", depth)
                test_pass = True
            else:
                print(f"{algorithm_name} passed for depth: ", depth)

        if test_pass:
            player = yourAgent()
            sample_board = Board(RandomPlayer(), player)
            # setting up the board as though we've been playing
            board_state = [
                ["X", "X", " ", "X", "13", "X", " "],
                [" ", " ", "X", " ", " ", "X", "X"],
                ["X", " ", "11", " ", "12", "X", "21"],
                ["X", " ", "X", "X", " ", " ", " "],
                [" ", "X", "X", " ", "22", "23", "X"],
                [" ", " ", "X", " ", " ", " ", "X"],
                ["X", " ", "X", " ", "X", "X", "X"]
            ]
            sample_board.set_state(board_state, p1_turn=False)

            test_pass = True

            expected_depth_scores = [(1, -6), (2, -2), (3, -3), (4, float("-inf"))]

            for depth, exp_score in expected_depth_scores:
                move, score = algorithm(player, sample_board, time_left, depth=depth, my_turn=True)
                print(score)
                if exp_score != score:
                    print(f"{algorithm_name} failed for depth: ", depth)
                    test_pass = False
                else:
                    print(f"{algorithm_name} passed for depth: ", depth)

        if test_pass:
            print(f"{algorithm_name} Test: Runs Successfully!")

        else:
            print(f"{algorithm_name} Test: Failed")

    except NotImplementedError:
        print(f'{algorithm_name} Test: Not implemented')
    except:
        print(f'{algorithm_name} Test: ERROR OCCURRED')
        print(traceback.format_exc())
