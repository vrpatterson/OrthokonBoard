# OrthokonBoard

This program contains a class called OrthokonBoard that represents the board for a two-player 
game that is played on a 4x4 grid. This class does not do everything needed to play a game -
it's just responsible for handling the rules concerning the game board. Things like asking the 
user for moves, printing results for the user, keeping track of whose turn it is, and running the 
game loop would be the responsibility of one or more other classes. The board starts with four
red pieces on row 0 and four yellow pieces on row 3. A valid move consists of a player moving 
one of their pieces orthogonally or diagonally as far as it can go until it hits another piece 
or the edge of the board (it must move at least one space). After the piece stops, any opponent 
pieces on orthogonally adjacent squares are flipped over to its color. The OrthokonBoard class 
doesn't keep track of whose turn it is, so it will allow multiple moves by the same player 
consecutively. A player wins upon making a move that either flips over the remaining opponent 
pieces or leaves the opponent without a move.

# How to play:
Initialize game:  
&nbsp; &nbsp; &nbsp; game = OrthokonBoard()  
    
Red will make first move:  (either player can make first move)  
&nbsp; &nbsp; &nbsp; game.make_move(0,0,2,0)  (first two values are row, column for piece to move - last two values is location to move to)  
  
Yellow can make the next move:    (there is no requirement to alternate turns)  
&nbsp; &nbsp; &nbsp; game.make_move(3,2,1,0)  
  
Continue until either player wins or there is a draw  
Results are printed to the console  
