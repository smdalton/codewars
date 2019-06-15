





def swap_rows(matx, row1, row2):
    temp = matx[row1]
    matx[row1] = matx[row2]
    matx[row2] = temp

# multiply a specified row by a coefficient
def mult_row(matx, row1, coef):
    if row1 > 3: return 'Row outside bounds mult'
    matx[row1] = [x * coef for x in matx[row1]]

# adds row1 to row2
def add_row(matx, row1, row2):
    if row1 > 3 or row2 > 3: return 'Row outside bounds add_row'
    matx[row2] = [x + y for x, y in zip(matx[row1], matx[row2])]

def add_mult_row(matx, row1, row2, coef):
    '''
    adds multiple of first row index to second row index
    '''
    row_to_add = [x * coef for x in matx[row1]]
    matx[row2] = [x + y for x, y in zip(row_to_add, matx[row2])]
def add_mult_row(matx, row1, row2, coef):
    '''
    adds multiple of first row index to second row index
    '''
    row_to_add = [x * coef for x in matx[row1]]
    matx[row2] = [x + y for x, y in zip(row_to_add, matx[row2])]

def num_zeros_in_row(row):
    return row[:3].count(0)
    # want to skip the numeric value as a zero

# returns the index of all values that are not zero
def get_non_zero_index(row):
    # check to see if the solution has non-zero solutions
    if num_zeros_in_row(row) == 2:
        for i in range(len(row)-1):
            if row[i] == 1:
                return i
    else:
        print('number of non-zero values present in row != 1', row)
        return -1

# test to see if the matrix is in rref
def is_reduced(matx):
    result = []
    for i in range(len(matx)):
        result.append(matx[0][i]+matx[1][i]+matx[2][i])
    return result == [1,1,1]

def test_get_non_zero_index():
    test_matx = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
    ]
    results = []
    for row in test_matx:
        results.append(get_non_zero_index(row))
    print(results)
    assert results == [0,1,2,-1,-1, 2, -1]

def test_is_reduced():
    matx1 = [[1,0,0,0], [0,1,0,0], [0,0,1,0]]
    matx2 = [[1,1,1,1], [1,2,3,4], [4,5,4,2]]
    matx3 = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
    matx4 = [[-1,-2,-3,-4], [-7,-5,-3,-12], [5,4,1,2]]

    test_matrices = [matx1,matx2,matx3,matx4]
    results = []
    for matrix in test_matrices:
        results.append(is_reduced(matrix))

    assert results == [
        True,
        False,
        False,
        False,
    ]

def test_add_row():
    test_matx = [
        [1, 1, 1],
        [5, 5, 5],
        [8, 8, 8],
    ]

    add_row(test_matx, 0, 1)
    assert test_matx == [
        [1, 1, 1],
        [6, 6, 6],
        [8, 8, 8],
    ]

def test_mult():
    test_matx = [
        [1, 1, 1],
        [5, 5, 5],
        [8, 8, 8],
    ]

    mult_row(test_matx, 2, 4)
    assert test_matx == [
        [1, 1, 1],
        [5, 5, 5],
        [32, 32, 32],
    ]

def test_swap():
    test_matx = [
        [1, 1, 1],
        [5, 5, 5],
        [8, 8, 8],
    ]
    swap_rows(test_matx, 1, 0)
    assert test_matx == [
        [5, 5, 5],
        [1, 1, 1],
        [8, 8, 8],
    ]

def test_num_zeros_in_row():
    row = [2,3,0,0]
    print(num_zeros_in_row(row), row)
    assert num_zeros_in_row(row) == 1

    row = [0,0,0,0]
    print(num_zeros_in_row(row), row)
    assert num_zeros_in_row(row) == 3

    row = [1,1,1,1]
    print(num_zeros_in_row(row), row)
    assert num_zeros_in_row(row) == 0

def tests():
    test_swap()
    test_mult()
    test_add_row()
    test_num_zeros_in_row()
    test_is_reduced()
    test_get_non_zero_index()
    test_is_reduced()
    print('tests complete')

#tests()



#def mat3solve(matx):
# all operations are assumed to be zero indexed


test_matx = [
    [2,1,1,8],
    [0,1,4,7],
    [5,0,3,13]
]
solution = [2,3,1]

def sort_by_zeros(matx):
    matx.sort(key=lambda x: x[:3].count(0))

def test_mat3_solve(matx):

    # get the largest value in the matrix to the top row
    matx.sort(key=lambda x: x[0], reverse=True)
    # get the second row and see if it's first value is not = zero



    print(matx)

    # select a non leading zero row and perform operations to zero it out


test_mat3_solve(test_matx)


def move_zeros(array):
    zero_count = array.count(int(0))
    array = [x for x in array if x != 0]

    for i in range(0, zero_count):
        array.append(0)

    return array