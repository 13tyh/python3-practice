from exercises.basics_repetition.round_27 import (
    find_largest_row,
    matrix_row_sums,
    matrix_total,
    transpose_2x2,
)


def test_round_27() -> None:
    matrix = [[1, 2], [3, 4]]
    assert matrix_total(matrix) == 10
    assert matrix_row_sums(matrix) == [3, 7]
    assert transpose_2x2(matrix) == [[1, 3], [2, 4]]
    assert find_largest_row([[1], [2, 3], [4]]) == [2, 3]
    assert find_largest_row([]) == []
