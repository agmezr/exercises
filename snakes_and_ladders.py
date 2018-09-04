"""
Rules:

All players start at the 1 tile.
Each turn, the player rolls the die and advances their piece by whatever number was rolled.
If the tile you land on contains the base of a ladder, you instantly ascend to the top of the ladder.
If the tile contains the head of a snake, you instantly descend to the end of the snake's tail.
If you roll a 6, you get another turn after completing the current one (ie: another die roll and move)
The game ends when one of the players reaches the 100 tile.
You must land exactly on the tile; if you overshoot it, you'll 'bounce' back by however many tiles you exceeded it.
For example, if you're currently on the 97 tile and you roll a 5, you'll move 3 tiles forward to the 100, and then you'll travel the remaining 2 tiles back, landing on 98.
The game board in this case is represented by the matrix board, where each tile that has the base of a ladder or head of a snake on it simply contains the number of the tile that it leads to. All other tiles contain -1.

There's also an array diceRolls which contains the outcomes of all the die rolls in the game (for all players), in order. 
There may have been extra die rolls after one of the players already won, so you'll need to check when someone wins.

Given board, dieRolls, and integer players (representing how many players are in the game), 
your task is to return an array of each player's final position when the game ends.
"""


def snakesAndLadders(board, dieRolls, players):
    positions = [1] * players
    player_turn = 0
    
    # play the game by iterating over the die rolls
    for turn, roll in enumerate(dieRolls):
        pos = positions[player_turn % players] + roll
        positions[player_turn % players] = pos
        
        # if tile number > 100 rebound 
        if pos > 100:
            pos = 100 - (pos - 100)
            positions[player_turn % players] = pos
            
        # if player wins stop
        elif pos == 100:
            break
        
        # advance to new position
        x, y = warp(pos)
        tile = board[x][y]        

        # if tile is a ladder or snake set to new tile
        if tile > 0:
            positions[player_turn % players] = tile
            
        #if not 6 change to next player
        player_turn += (roll < 6)

    return positions

# from a given tile number obtain the row and col from the board
def warp(n):
    n -= 1
    row = (10 - (n // 10)) - 1
    col = n % 10
    
    # if row is not odd reverse the numeration
    if row % 2 == 0:
        col = (10 - col) - 1
        
    return row, col

board = [[-1,28,-1,-1,-1,-1,82,-1,-1,-1],
         [-1,-1,-1,67,-1,-1,-1,-1,-1,-1],
         [56,-1,-1,-1,-1,-1,-1,55,-1,36],
         [-1,-1,-1,-1,87,-1,-1,-1,-1,-1],
         [75,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,30,-1,-1,-1,61,-1,-1,-1],
         [-1,-1,-1,-1,-1,18,-1,-1,-1,-1],
         [-1,44,-1,32,-1,-1,-1,-1,45,-1],
         [-1,-1,-1,-1,-1,-1,26,-1,-1,-1],
         [-1,-1,-1,12,-1,-1,-1,-1,-1,-1]]

dieRolls = [2, 1, 3]
players = 4

r = snakesAndLadders(board, dieRolls, players)
print(r)
