import numpy as np
import pytest


@pytest.fixture(params=[(50, 40), (100, 123), (10, 10), (231, 231)])
def matrix(request):
    return np.random.rand(request.param[0], request.param[1])
