def printMatrix(l):
    block = 5*" "
    space = 2*" "
    matrix = [[block for i in range(10)] for j in range(10)]
    for row, col in l:
        matrix[row][col] = f"({row},{col})"
    print(len(block)*10*"*"+len(space)*9*"*")
    for row in matrix:
        print(space.join(row))
    print(len(block)*10*"*"+len(space)*9*"*")


if __name__ == "__main__":
    l = [(i, j) for i in range(10) for j in range(10)]
    printMatrix(l)
    l = [(i, j) for i in range(10) for j in range(i)]
    printMatrix(l)
