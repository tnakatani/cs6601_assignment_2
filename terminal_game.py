from test_players import HumanPlayer
from isolation import Board

player1 = HumanPlayer("player1")
player2 = HumanPlayer("player2")

game = Board(player1, player2)
game.play_isolation(120000)

