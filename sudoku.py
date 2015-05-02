# check the sudoku
def done_or_not(board):
    sets = [[] for i in range(0,18)]
    for a, lis in enumerate(board):
        sets.insert(19,lis)
        for i, v in enumerate(lis):
            sets[i+9].append(v)
            sets[(a/3)*3+i/3].append(v)
    return all([len(set(each))==9 for each in sets])

sudoku1 = [[1, 3, 2, 5, 7, 9, 4, 6, 8],[4, 9, 8, 2, 6, 1, 3, 7, 5],[7, 5, 6, 3, 8, 4, 2, 1, 9],[6, 4, 3, 1, 5, 8, 7, 9, 2],[5, 2, 1, 7, 9, 3, 8, 4, 6],[9, 8, 7, 4, 2, 6, 5, 3, 1],[2, 1, 4, 9, 3, 5, 6, 8, 7],[3, 6, 5, 8, 1, 7, 9, 2, 4],[8, 7, 9, 6, 4, 2, 1, 5, 3]]
sudoku2 =[[1, 3, 2, 5, 7, 9, 4, 6, 8],[4, 9, 8, 2, 6, 1, 3, 7, 5],[7, 5, 6, 3, 8, 4, 2, 1, 9],[6, 4, 3, 1, 5, 8, 7, 9, 2],[5, 2, 1, 7, 9, 3, 8, 4, 6],[9, 8, 7, 4, 2, 6, 5, 3, 1],[2, 1, 4, 9, 3, 5, 6, 8, 7],[3, 6, 5, 8, 1, 7, 9, 2, 4],[8, 7, 9, 6, 4, 2, 1, 3, 5]]

print done_or_not(sudoku1)
