
#a function that prints a prefix sum of 1d list
def prefix_sum(numbers:list)->None:
    b = []
    b.append(numbers[0])
    for x in range(1,len(numbers)):
         b.append(b[x-1] + numbers[x])
    print(b)

#a function that returns the diagonal elements of a 2d list
def diagonal(numbers:list)->list:
    b = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                b.append(numbers[i][j])
    return b
#a function that checks if the matrix is symmetric or not and returns true or false
def symmetric(numbers:list)->bool:
    symmetric = True;
    for x in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[x][j] != numbers[j][x]:
                symmetric = False
    return symmetric
def transpose(numbers:list)->list:
    #zero all the matrix elements
    a = [[0 for y in range(len(numbers))]for x in range(len(numbers[0]))]
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):#max([len(items) for items in numbers])):
            a[j][i] = numbers[i][j]
    return a
#a function that returns a 2d list which is result of two 2d multiplication
def multiply(matrix_1,matrix_2)->list:
    #a = [[0 for y in range(len(matrix_1))]for x in range(len(matrix_1))]
    a = [ [0] * len(matrix_1[0]) for _ in range(len(matrix_1))]
    #return a
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[i])):
            a[i][j] = matrix_1[i][j] * matrix_2[i][j]
    return a

    

            
#prefix_sum([1,7,2,3,4,5])
#m8 = [[1,2,3],[4,5,6],[7,8,9]]
