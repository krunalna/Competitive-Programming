#36. Valid Sudoku


    #Create 3 dictionarys to keep track of rows, columns and squares.
    #Traverse the list and update each of these dictionaries with new values while checking if the current row, column or square have seen the value before.
    #If the entire sudoku is traverse and no issue is found then the sudoku is valid.


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = {i:set() for i in range(len(board))}
        cols = {i:set() for i in range(len(board[0]))}
        squares = {i:set() for i in range(9)}
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                value = board[row][col]
                
                if value != ".":
                    square = (row // 3) * 3 + col // 3
                    if value in rows[row] or value in cols[col] or value in squares[square]:
                        return False
                    
                    rows[row].add(value)
                    cols[col].add(value)
                    squares[square].add(value)
                    
        return True


#