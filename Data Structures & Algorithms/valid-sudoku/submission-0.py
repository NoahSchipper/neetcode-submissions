class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seenNums = set()
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                elif num in seenNums:
                    return False
                else:
                    seenNums.add(num)
        for col in range(9):
            seenNums = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                elif num in seenNums:
                    return False
                else:
                    seenNums.add(num)
        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                seenNums = set()
                for row in range(startRow, startRow + 3):
                    for col in range(startCol, startCol + 3):
                        num = board[row][col]
                        if num == ".":
                            continue
                        elif num in seenNums:
                            return False
                        else:
                            seenNums.add(num)
        return True

