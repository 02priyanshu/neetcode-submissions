class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenC = defaultdict(list)
        seenB = defaultdict(list)

        for i in range(len(board)):
            seenR=[]
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seenR:
                    return False
                seenR.append(board[i][j])
                if board[i][j] in seenC[j]:
                    return False
                seenC[j].append(board[i][j])
                if board[i][j] in seenB[i//3,j//3]:
                    return False
                seenB[i//3,j//3].append(board[i][j])
        return True