import numpy as np
import pytest


@pytest.mark.parametrize(
    "first,second",
    [
        (
                np.array([[1.73, 1.68], [65.4, 59.2]], dtype=object),
                np.array([[1.73, 1.68], [65.4, 59.2]], dtype=object)),
        (
                np.array([[43, 43, 1312], [65.41, 123.2, 44, 1]], dtype=object),
                np.array([[43, 43, 1312], [65.41, 123.2, 44, 1]], dtype=object)),
        (
                np.array([[1, 1, 1], [1, 1, 1], [1, 2, 3]], dtype=object),
                np.array([[1, 1, 1], [1, 1, 1], [1, 2, 3]], dtype=object)
        )
    ]
)
def test_equality(first: np.array, second: np.array):
    """
    Test equality of matrices
        :param np.array() first: First matrix
        :param np.array() second: Second matrix
    """
    assert (first == second).all()


def test_multiplication(matrix: np.array):
    """
    Test multiplying a matrix by a scalar
        :param np.array() matrix: Matrix fixture
    """
    multiplier = np.random.randint(0, high=100)
    multiplied = matrix * multiplier
    for (x, y), value in np.ndenumerate(multiplied):
        assert multiplied[x, y] == matrix[x, y] * multiplier


def test_addition(matrix: np.array):
    """
    Test addition of matrices
        :param np.array() matrix: Matrix fixture
    """
    second = np.random.rand(*np.shape(matrix))
    result = matrix + second
    for (x, y), value in np.ndenumerate(result):
        assert result[x, y] == matrix[x, y] + second[x, y]


@pytest.mark.parametrize(
    "first,second,result",
    [
        (
                np.array([[1, 2], [3, 4]]),
                np.array([[5, 6], [7, 8]]),
                np.array([[19, 22], [43, 50]])
        ),
        (
                np.array([[2, 1], [-3, 0], [4, -1]]),
                np.array([[5, -1, 6], [-3, 0, 7]]),
                np.array([[7, -2, 19], [-15, 3, -18], [23, -4, 17]])
        )
    ]
)
def test_matrix_multiplication(first: np.array, second: np.array, result: np.array):
    """
    Test numpy.array().dot() method
        :param np.array() first: First multiplier
        :param np.array() second: Second multiplier
        :param np.array() result: Result of multiplication.
    """
    assert (first.dot(second) == result).all()


@pytest.mark.parametrize(
    "source,transposed",
    [
        (
                np.array([[0, 3], [1, 4], [2, 5]]),
                np.array([[0, 1, 2], [3, 4, 5]])
        ),
        (
                np.array([[1, 2, 3], [4, 5, 0], [-1, 3, 4]]),
                np.array([[1, 4, -1], [2, 5, 3], [3, 0, 4]])
        )
    ]
)
def test_matrix_transpose(source: np.array, transposed: np.array):
    """
    Test numpy.array().T method
        :param np.array() source: Original matrix to call .T method
        :param np.array() transposed: Transposed matrix.
    """

    assert (source.T == transposed).all()
