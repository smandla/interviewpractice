def countIslands(binaryMatrix):
    outerLength = len(binaryMatrix)
    innerLength = len(binaryMatrix[0])
    counter = 0 
    for i in range(0,outerLength):
        for j in range(0,innerLength):
            if (binaryMatrix[i][j] == 1):
                dfs(binaryMatrix, i, j, outerLength, innerLength)
                counter += 1
    return counter



    print(binaryMatrix[1][1])
    return(outerLength)
def dfs(binaryMatrix, i, j, outerLength, innerLength):
    if ( i < 0 or j < 0 or i >= outerLength or j >= innerLength or binaryMatrix[i][j] != 1):
        return 
    binaryMatrix[i][j] = -1
    dfs(binaryMatrix, i - 1, j, outerLength, innerLength)
    dfs(binaryMatrix, i, j - 1, outerLength, innerLength)
    dfs(binaryMatrix, i + 1, j, outerLength, innerLength)
    dfs(binaryMatrix, i, j + 1, outerLength, innerLength)


binaryMatrix = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0],[0, 0, 0, 0, 0]]
print(countIslands(binaryMatrix))
