def matrix(a,b):
    rowa, cola = len(a), len(a[0])
    rowb, colb = len(b), len(b[0])

    if cola != rowb:
        return -1

    result = [[0 for _ in range(colb)] for _ in range(rowa)]
    # print(result)

    for i in range(rowa):
        for j in range(colb):
            for k in range(cola):
                result[i][j] += a[i][k] * b[k][j]
    return result


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(matrix(A, B)) 
# -> [[19, 22], [43, 50]]