#!/usr/bin/env python

# This file is your main submission that will be graded against. Only copy-paste
# code on the relevant classes included here from the IPython notebook. Do not
# add any classes or functions to this file that are not part of the classes
# that we want.

# Submission Class 1
class OpenMoveEvalFn():
    """Evaluation function that outputs a 
    score equal to how many moves are open
    for your computer player on the board."""
    def score(self, game, maximizing_player_turn=True):
        # TODO: finish this function!
        if maximizing_player_turn:
            moves=game.get_legal_moves()
            eval_func =len(moves)
            return eval_func
        else:
            moves=game.get_opponent_moves() #here opponent chan choose any queen.. thus its addition of both
            eval_func =len(moves)            
            return eval_func
        

# Submission Class 2
class CustomEvalFn():
    """Custom evaluation function that acts
    however you think it should. This is not
    required but highly encouraged if you
    want to build the best AI possible."""
    def score(self, game, maximizing_player_turn=True):
        # TODO: finish this function!
        return eval_func

# Submission Class 3
class CustomPlayer():
    # TODO: finish this class!
    """Player that chooses a move using 
    your evaluation function and 
    a depth-limited minimax algorithm 
    with alpha-beta pruning.
    You must finish and test this player
    to make sure it properly uses minimax
    and alpha-beta to return a good move
    in less than 1000 milliseconds."""
    def __init__(self,  search_depth=3, eval_fn=OpenMoveEvalFn()):
        # if you find yourself with a superior eval function, update the
        # default value of `eval_fn` to `CustomEvalFn()`
        self.eval_fn = eval_fn
        self.search_depth = search_depth
        
    def choose_queen(self, game, queen1, queen2):
        #n=randint(queen1,queen2)  
        #return n
        game.set_active_queen(queen1)
        queen1_moves=game.get_legal_moves()
        num_queen1_moves=len(queen1_moves)
        
        game.set_active_queen(queen2)
        queen2_moves=game.get_legal_moves()
        num_queen2_moves=len(queen2_moves)
        
        if num_queen1_moves >= num_queen2_moves:
            return queen1
        else:
            return queen2

    
    def move(self, game, legal_moves, time_left):
        best_move, utility, queen = self.minimax(game,time_left, depth=self.search_depth)
        return best_move, queen


    def utility(self, game, maximizing):
        #queen1, queen2 = game.get_active_players_queen()
        #queen=self.choose_queen(game, queen1, queen2)
        #game.set_active_queen(queen)
        
        if maximizing:
            if not game.get_opponent_moves():
                return float("inf")
            if not game.get_legal_moves():
                return float("-inf")

            return self.eval_fn.score(game)

        else:
            if not game.get_legal_moves():
                return float("inf")
            if not game.get_opponent_moves():
                return float("-inf")

            return self.eval_fn.score(game)


    def minimax(self, game,time_left, depth=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        queen1, queen2 =game.get_active_players_queen()
        queen=self.choose_queen(game, queen1, queen2)
        game.set_active_queen(queen)
        legal_moves = game.get_legal_moves()
        
        if not depth or not legal_moves:              
            return None, self.utility(game, maximizing_player), queen

        if maximizing_player:
            best_move = None
            best_val =  float("-inf")
            
            
            for move in legal_moves:
                _, val, q = self.minimax(game.forecast_move(move), time_left, depth -1, False ) #forecast move has a problem
                if val > best_val:
                    best_val = val
                    best_move = move

        else:
            best_move = None
            best_val = float("inf")            

            for move in legal_moves:
                _, val,q = self.minimax(game.forecast_move(move), time_left, depth -1, True)
                if val < best_val:
                    best_val = val
                    best_move = move

        return best_move, best_val, queen
    
    
    def alphabeta(self, game,time_left, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        queen1, queen2 =game.get_active_players_queen()
        queen=self.choose_queen(game, queen1, queen2)
        game.set_active_queen(queen)
        legal_moves = game.get_legal_moves()
        
        if not depth or not legal_moves :            
            return None, self.utility(game, maximizing_player), queen
        
        if maximizing_player:
            val = float("-inf")
            best_move = None
            
            for move in legal_moves:
                node = game.forecast_move(move)

                _, new_val,q = self.alphabeta(node, time_left, depth-1, alpha, beta, False)

                if new_val > val:
                    val = new_val
                    best_move = move

                alpha = max( alpha, val)

                if beta <= alpha:
                    return best_move, beta, q
            return best_move, val, queen

        else:
            val = float("inf")
            best_move = None
            
            for move in legal_moves:
                node = game.forecast_move(move)
                _, new_val,q = self.alphabeta(node, time_left, depth -1 , alpha, beta, True)

                if new_val < val:
                    val = new_val
                    best_move = move

                beta = min(beta, val)

                if beta <= alpha:
                    return best_move, alpha,q

            return best_move, val, queen
