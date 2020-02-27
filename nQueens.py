NQueens = 5
Queens = [None] * NQueens


def possible(x, y):
    for i in range(0, x):
        if Queens[i] == y: # check rows
            return False
        if abs(y - Queens[i]) == abs(x - i):  # check diagonals
            return False
    return True


def solve():
    for x in range(0, NQueens):
        if Queens[x] is None:
            for i in range(0, NQueens):
                if possible(x, i):
                    Queens[x] = i
                    solve()
                    Queens[x] = None
            return
    print(Queens)


solve()
