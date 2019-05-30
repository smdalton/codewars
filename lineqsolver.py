





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
        print('number of zeros present in row != 1', row)
        return -1


# test to see if the matrix is in rref
def is_reduced(matx):
    indexes = [0,0,0]
    for row in matx:
        index = get_non_zero_index(row)
        if index:
            pass
    return indexes == [1,1,1]

def test_get_non_zero_index():
    test_matx = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    results = []
    for row in test_matx:
        results.append(get_non_zero_index(row))

    assert results == [0,1,2,-1,-1]

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
        [True,False, False, False],
        [False,False,False,False],
        [False,False,False,False],
        [False,False,False,False],
    ]

def test_add_row():
    test_matx = [
        [1, 1, 1],
        [5, 5, 5],
        [8, 8, 8],
    ]

    add_row(matx, 0, 1)
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
    #test_swap()
    #test_mult()
    #test_add_row()
    #test_num_zeros_in_row()
    #print('tests complete')
    #test_is_reduced()
    test_get_non_zero_index()

tests()
# def mat3solve(matx):
# all operations are assumed to be zero indexed
# swap two rows of the matrix

