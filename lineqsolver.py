matx = [
    [1, 1, 1],
    [5, 5, 5],
    [8, 8, 8],
]


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


# adds multiple of first row index to second row index
def add_mult_row(matx, row1, row2, coef):
    row_to_add = [x * coef for x in matx[row1]]
    matx[row2] = [x + y for x, y in zip(row_to_add, matx[row2]]

    # check if matrix is in RREF
    # def is_reduced(matx):
    # return False

    # solve for the
    # def back_substitue(matx):
    # return False


def test_mult_row(matx, row1, row2, coef):


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


def tests():
    test_swap()
    test_mult()
    test_add_row()


tests()
# def mat3solve(matx):
# all operations are assumed to be zero indexed
# swap two rows of the matrix

