import pytest
from maior_numero import maior_numero

@pytest.mark.parametrize("a,b,c,expected", [
    (1, 2, 3, 3),
    (3, 2, 1, 3),
    (5, 5, 2, 5),
    (-1, -3, -2, -1),
    (0, 0, 0, 0),
])
def test_maior_numero(a, b, c, expected):
    assert maior_numero(a, b, c) == expected
