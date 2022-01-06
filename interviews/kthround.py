def kthround(m,n):
    game = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            mod = (i + j + 1) % n
            game[i][j] = n if mod == 0 else mod
        


    return game[m-1]


m = 4
n = 5
print(kthround(m,n))
