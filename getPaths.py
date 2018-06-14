
def getPaths(A):

    power = [[[A[row][col],] for row in range(len(A))] for col in range(len(A))]
    final = [[['',] for row in range(len(A))] for col in range(len(A))]
    for i in range(len(A)):
        final[i][i] = ['X']
    for row in range(len(final)) :
        for col in range(len(final)):
            if A[row][col] != '-':
                final[row][col] = A[row][col]
    while (not isFull(final)) :
        power = multiply(power,A)
        for row in range(len(final)) :
            for col in range(len(final)):
                if final[row][col][0] == '' and power[row][col]:
                    final[row][col] = power[row][col]
    return final

def isFull(A):
    full = True
    for row in A:
        for col in row:
            if col[0] == '':
                full = False
    return full

# Matrix Multiplication
def multiply(A, B):
    result = [[[] for row in range(len(A))] for col in range(len(A))]
    for row in range(len(A)):
        for col in range(len(A)): # for each matrix entry
            for k in range(len(A)): # for each term in the dot product
                for a in range(len(A[k][col])): # for each term in the first part of the dot product
                    for b in range(len(B[row][k])): # for each term in the second part of the dot product
                        new = A[k][col][a] + B[row][k][b]
                        if (('-' not in new) and ('yy' not in new) and ('pp' not in new)) :
                            result[row][col].append(new)
    return result

# turns adjacency matrix into list of dicts mapping
def matrixToList(A):
    adjacencyList = [None]
    for row in A:
        print(row)
        dict = {}
        for index, entry in enumerate(row):
            # if want to label vertices starting at 1, add , start=1 to enumerate params
            if entry not in dict:
                dict[entry] = [None]
            dict[entry].append(index)
        adjacencyList.append(dict)

x = [['-','-','-','y','p','y'],
    ['-','-','-','y','y','p'],
    ['-','-','-','y','p','y'],
    ['y','y','y','-','-','-'],
    ['p','y','p','-','-','-'],
    ['y','p','y','-','-','-']]

for row in x :
    print(row)

print('')

result = getPaths(x)
for row in result :
    print(row)

print(matrixToList(x))