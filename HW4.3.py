#3.1

def create_2d_list():
    matrix = []
    value = 1
    for i in range(5):  
        row = []
        for j in range(5):  
            row.append(value)
            value += 1
        matrix.append(row)
    return matrix


#3.2
def modified_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0: 
                matrix[i][j] = '?'
    return matrix

#3.3
def sum_non_question_elements(matrix):
    total = 0
    for row in matrix:
        for element in row:
            if element != '?':  
                total += element
    return total


