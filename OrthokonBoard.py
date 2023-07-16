# Victoria Patterson
# Portfolio Project for OSU Computer Science II
# Description: This program contains a class called OrthokonBoard that represents the board for a two-player 
#              game that is played on a 4x4 grid. This class does not do everything needed to play a game -
#              it's just responsible for handling the rules concerning the game board. Things like asking the 
#              user for moves, printing results for the user, keeping track of whose turn it is, and running the 
#              game loop would be the responsibility of one or more other classes. The board starts with four
#              red pieces on row 0 and four yellow pieces on row 3. A valid move consists of a player moving 
#              one of their pieces orthogonally or diagonally as far as it can go until it hits another piece 
#              or the edge of the board (it must move at least one space). After the piece stops, any opponent 
#              pieces on orthogonally adjacent squares are flipped over to its color. The OrthokonBoard class 
#              doesn't keep track of whose turn it is, so it will allow multiple moves by the same player 
#              consecutively. A player wins upon making a move that either flips over the remaining opponent 
#              pieces or leaves the opponent without a move.

class OrthokonBoard:
    """ Represents a 2 person game played on a 4x4 grid. This class handles the rules concerning the game board,
        including moving the pieces as allowed """

    def __init__(self):
        """ Initalizes the board and current state of the game """
        self._board = [["Red", "Red", "Red", "Red"], 
                       [" ", " ", " ", " "], 
                       [" ", " ", " ", " "], 
                       ["Yellow", "Yellow", "Yellow", "Yellow"]]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """ Returns current state of the board """
        return self._current_state
    
    def print_board(self):
        """ Prints the board """
        print(self._board)
    
    def make_move(self, row_cur, col_cur, row_move_to, col_move_to):
        """ Method responsible for making a move, first calls helper methods to ensure move
        is valid, records valid moves, then calls helper methods to update board and check
        if game is completed """
        
        self.print_board()

        # Check if move is valid
        if not self.check_valid_move(row_cur, col_cur, row_move_to, col_move_to):
            return False
        
        # Checks that piece moved as far as it can
        if not self.check_piece_moved_max_distance(row_cur, col_cur, row_move_to, col_move_to):
            return False

        # Record move
        if self._board[row_cur][col_cur] == "Yellow":
            self._board[row_move_to][col_move_to] = "Yellow"
            self._board[row_cur][col_cur] = " "
            self.print_board()
        else:
            self._board[row_move_to][col_move_to] = "Red"
            self._board[row_cur][col_cur] = " "
            self.print_board()

        # Check for pieces to capture
        self.update_board(row_move_to, col_move_to)

        # Check if game is complete
        if self.check_game_over():
            print("Game is over!", self._current_state)
            return True

        return True

    def check_valid_move(self, row_cur, col_cur, row_move_to, col_move_to):
        """ Method responsible for validating moves, uses helper methods for validation """

        # Check if piece to move is present in space
        if self._board[row_cur][col_cur] == " ":
            return False

        # Check move is within board limits
        if not self.check_out_of_bounds(row_move_to, col_move_to):
            return False
        
        # Check move moves at least one space
        if row_cur == row_move_to and col_cur == col_move_to:
            return False

        # Checks that new location is empty
        if not self.check_if_empty_space(row_move_to, col_move_to):
            return False
        
        if not self.check_road_block(row_cur, col_cur, row_move_to, col_move_to):
            return False
        
        return True
    
    def check_road_block(self, row_cur, col_cur, row_move_to, col_move_to):
        """ Method ensures that the player is moving piece according to game rules (vertically, horizontally
        or diagonally only) and checks to make sure there are no 'roadblocks' along the path to the new space """
        
        # Checks for roadblock along path to new space
        if row_cur == row_move_to:      # moving piece horizontally
            row = row_cur
            col = col_cur
            if col_cur > col_move_to:   # moving piece horizontally left
                while col != col_move_to:
                    col -= 1
                    if not self.check_out_of_bounds(row, col) or not self.check_if_empty_space(row, col):
                        return False
            else:
                while col < col_move_to:    # moving piece horizontally right
                    col += 1
                    if not self.check_out_of_bounds(row, col) or not self.check_if_empty_space(row, col):
                        return False
            return True
            
        elif col_cur == col_move_to:      # moving piece vertically
            row = row_cur            
            col = col_cur
            if row_cur > row_move_to:     # moving piece up
                while row != row_move_to:
                    row -= 1
                    if not self.check_if_empty_space(row, col):
                        return False
            else:
                while row != row_move_to: # moving piece down
                    row += 1
                    if not self.check_if_empty_space(row, col):
                        return False
            return True
        
        elif abs(row_cur - row_move_to) == abs(col_cur - col_move_to):      # ensures player is moving piece diagonally
            row = row_cur
            col = col_cur
            if row_cur > row_move_to:       # moving diagonally up  
                if col_cur > col_move_to:   # moving up to the left
                    while row > row_move_to and col > col_move_to:
                        row -= 1
                        col -= 1
                        if not self.check_out_of_bounds(row, col) or not self.check_if_empty_space(row, col):
                            return False
                else:                       # moving up to the right
                    while row > row_move_to and col < col_move_to:
                        row -= 1
                        col += 1
                        if not self.check_out_of_bounds(row, col) or not self.check_if_empty_space(row, col):
                            return False
            else:                           # moving diagonally down
                if col_cur > col_move_to:   # moving down to the left
                    while row < row_move_to and col > col_move_to:
                        row += 1
                        col -= 1
                        if not self.check_out_of_bounds(row, col) or not self.check_if_empty_space(row, col):
                            return False
                else:                       # moving down to the right
                    while row < row_move_to and col < col_move_to:
                        row += 1
                        col += 1
                        if not self.check_out_of_bounds(row, col) or not self.check_if_empty_space(row, col):
                            return False

                # Check space is within bounds first
                if self.check_out_of_bounds(row, col):
                    if not self.check_if_empty_space(row, col):
                        return False
                    
            return True
        else:
            print("INVALID MOVE")
            return False

    def check_piece_moved_max_distance(self, row_cur, col_cur, row_move_to, col_move_to):
        """ Method ensures that a player moves the piece as far across the board as possible """

        if row_cur == row_move_to:      # moving horizontally
            if col_cur > col_move_to:   # moving left
                next_col = col_move_to - 1
            else:                       # moving right
                next_col = col_move_to + 1
            
            if next_col >= 0 and next_col <= 3:    # checks if reached edge of board
                if self.check_if_empty_space(row_move_to, next_col): 
                    return False    # piece did not move as far as it should have

        elif col_cur == col_move_to:      # moving vertically
            if row_cur > row_move_to:     # moving up
                next_row = row_move_to - 1
            else:                         # moving down
                next_row = row_move_to + 1
            
            if next_row >= 0 and next_row <= 3:    # checks if reached edge of board
                if self.check_if_empty_space(next_row, col_move_to): 
                    return False    # piece did not move as far as it should have

        else:                           # moving diagonally 
            next_row = row_cur
            next_col = col_cur
            if row_cur > row_move_to:    # diagonally up
                next_row = row_move_to - 1
            else:                        # diagonally down
                next_row = row_move_to + 1
            
            if col_cur > col_move_to:    # diagonally left
                next_col = col_move_to - 1
            else:                        # diagonally down
                next_col = col_move_to + 1

            if next_row >= 0 and next_row <= 3:     # check if next row and column are beyond edge of board
                if next_col >= 0 and next_col <= 3:
                    if self.check_if_empty_space(next_row, next_col):
                        return False        # piece did not move as far as it should

        return True
    
    def check_out_of_bounds(self, row, col):
        """ Method checks if a space is out of bounds of the board"""

        if row < 0 or row > 3:
            return False        # out of bounds
        if col < 0 or col > 3:
            return False        # out of bounds
        return True     # space is in bounds of board


    def check_if_empty_space(self, row, col):
        """ Method checks if a space contains any pieces or if it's empty"""

        move_to = self._board[row][col]
        if move_to != " ":
            return False
        return True         # space is empty

    def update_board(self, row, col):
        """ Method that is called after a piece is moved. It checks surrounding spaces
         for opponents capturable pieces and calls capture_piece() when a capture can be made """
        
        # Check space above
        row_above = row - 1
        col_above = col
        if self.check_out_of_bounds(row_above, col_above):      # ensure space above is not out of bounds
            if not self.check_if_empty_space(row_above, col_above):     # space contains a piece
                self.capture_piece(row, col, row_above, col_above)

        # Check space below
        row_below = row + 1
        col_below = col
        if self.check_out_of_bounds(row_below, col_below):      # ensure space above is not out of bounds
            if not self.check_if_empty_space(row_below, col_below):     # space contains a piece
                self.capture_piece(row, col, row_below, col_below)

        # Check space to left
        row_left = row
        col_left = col - 1
        if self.check_out_of_bounds(row_left, col_left):      # ensure space above is not out of bounds
            if not self.check_if_empty_space(row_left, col_left):     # space contains a piece
                self.capture_piece(row, col, row_left, col_left)

        # Check space to right
        row_right = row
        col_right = col + 1
        if self.check_out_of_bounds(row_right, col_right):      # ensure space above is not out of bounds
            if not self.check_if_empty_space(row_right, col_right):     # space contains a piece
                self.capture_piece(row, col, row_right, col_right)

    def capture_piece(self, row, col, next_row, next_col):
        """ Method that flips game piece color when capturable by opponent """

        if self._board[row][col] == "Yellow" and self._board[next_row][next_col] == "Red":
            self._board[next_row][next_col] = "Yellow"        # Capture Red piece
            self.print_board()
        elif self._board[row][col] == "Red" and self._board[next_row][next_col] == "Yellow":
            self._board[next_row][next_col] = "Red"           # Capture Yellow piece
            self.print_board()
        else:
            return False    # adjacent piece is same player

    def check_game_over(self):
        """ Method used for determining when game is completed, it checks if """
        # Check if either player has no more available pieces to play
        yellow_pieces = 0
        red_pieces = 0

        for row in self._board:
            for piece in row:
                if piece == "Yellow":
                    yellow_pieces += 1
                if piece == "Red":
                    red_pieces += 1
        
        if yellow_pieces == 0 and red_pieces != 0:
            # Red wins
            self._current_state = "RED_WINS"
            return True

        elif red_pieces == 0 and yellow_pieces != 0:
            # Yellow wins
            self._current_state = "YELLOW_WINS"
            return True
        
        # Check if either player has no more available moves
        yellow_moves_available = False
        red_moves_available = False

        for cur_row in range(len(self._board)):
            for cur_col in range(len(self._board[cur_row])):
                cur_val = self._board[cur_row][cur_col]
                if cur_val != " ":
                    for nrow, ncol in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:  # indices of each space around piece 
                        new_row = cur_row + nrow
                        new_col = cur_col + ncol
                        if self.check_valid_move(cur_row, cur_col, new_row, new_col):
                            if cur_val == "Yellow":     # yellow has available moves
                                yellow_moves_available = True
                            else:                       # red has available moves
                                red_moves_available = True

        if not yellow_moves_available and red_moves_available:  # yellow has no available moves, red does
            self._current_state = "RED_WINS"
            return True
        
        elif yellow_moves_available and not red_moves_available:    # yellow does have available moves, red does not
            self._current_state = "YELLOW_WINS"
            return True

        elif not yellow_moves_available and not red_moves_available:    # neither player has any available moves left
            self._current_state = "DRAW"
            return True

        return False    # Both opponents still have available moves
