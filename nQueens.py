NQueens = 5
Queens = [None] * NQueens

def possible(x,y):
#     global Queens
    for i in range(0,x): # check rows
        if Queens[i] == y:
            return False
        if abs(y - Queens[i]) == abs(x-i): #check diagonals
            return False
    return True

def solve():
#     global Queens
    for x in range(0,NQueens):
        if Queens[x] is None:
            for i in range(0,NQueens):
                if possible(x,i):
                    Queens[x] = i
                    solve()
                    Queens[x] = None
            return
    print(Queens)

solve()

