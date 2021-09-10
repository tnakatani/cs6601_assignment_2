'''
Creates game of isolation through command line

usage: play_game.py [-h] [--print_moves] PLAYER PLAYER BOARD_SIZE

positional arguments:
  PLAYER         The two players e.g. (H, R, C)
  BOARD_SIZE     The board size e.g. (Entering 7 produces a 7x7 board)

optional arguments:
  -h, --help     show this help message and exit
  --print_moves  print moves
'''

import argparse
from isolation import Board
from test_players import HumanPlayer, RandomPlayer
try:
    from section2a.submission import CustomPlayer
    players_dict = {'H' : HumanPlayer(), 'R' : RandomPlayer(), 'C' : CustomPlayer()}  
except ImportError:
    players_dict = {'H' : HumanPlayer(), 'R' : RandomPlayer()}  

parser = argparse.ArgumentParser(description='Create Game')
parser.add_argument('players', metavar='PLAYER', type=str, nargs=2,
                   help='The two players e.g. (H, R, C)')
parser.add_argument('size', metavar='BOARD_SIZE', type=int, nargs=1,
                     help='The board size e.g. (Entering 7 produces a 7x7 board)')
parser.add_argument('--print_moves', dest='print_moves', action='store_const',
                    const=True, default=False, help='print moves')

args = parser.parse_args()

game = Board(players_dict[args.players[0]],
             players_dict[args.players[1]],
             args.size[0], args.size[0])

winner, move_history, loser_message = game.play_isolation(time_limit = 10000, print_moves=args.print_moves)
print(loser_message + "\nWinner: " + winner)
