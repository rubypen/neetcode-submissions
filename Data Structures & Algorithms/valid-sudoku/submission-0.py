class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Game Plan: iterate through rows and columns in the same 2 for loops
        # compare sets of cols and rows with themselves
        # for the 3x3 boxes we can take care of them by
        # ensure if i_new <= i + 2 board[i][j] compare to new 
        # j_new <= j + 2 board[i][j] compare to new

        # First Implementation
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        ''' rows & cols'''
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3, j//3)]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])
        return True

