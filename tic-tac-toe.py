# Tic Tac Toe checker


def isSolved(board):
    l = [[] for i in range(0,8)]
    for i, v in enumerate(board):
        for a, b in enumerate(v):
            l[i%3].append(b)
            l[a%3+3].append(b)
            if i==a: l[6].append(b)
            if i+a == 2 : l[7].append(b)
    for each in l:
        if len(set(each)) == 1 and each[0] != 0 : return each[0]
    if [item for sublist in board for item in sublist].count(0) != 0 : return -1
    else : return 0


b= [[1,2,0],[1,1,2],[0,1,2]]

#print isSolved(b)
