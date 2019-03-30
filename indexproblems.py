


def column_containing_a_point(i,j):

    list_of_indices=[]

    for index in range(9):
        list_of_indices.append([index,j])

    return list_of_indices


def row_containing_a_point(i, j):
    list_of_indices = []

    for index in range(9):
        list_of_indices.append([i,index])

    return list_of_indices

def three_by_three_matrix_containing_a_point(i,j):

    # there are 9 possible 3 by 3 matrices in 9 by 9 sudoku matrix

    a=(i//3)*3
    b=(j//3)*3   # indices of corner entry

    list_of_indices=[]

    for r in range(3):
        for s in range(3):
            list_of_indices.append([a+r,b+s])

    return list_of_indices

list_of_three_by_three_matrices=[]
list_of_columns= []
list_of_rows= []

for i,j in [[0,r] for r in range(9)]:

    list_of_columns.append(column_containing_a_point(i,j))

for i,j in [[r,0] for r in range(9)]:

    list_of_rows.append(row_containing_a_point(i,j))

for i,j in [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]:

    list_of_three_by_three_matrices.append(three_by_three_matrix_containing_a_point(i,j))


