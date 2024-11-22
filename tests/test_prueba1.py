import pytest
from src.prueba1 import num_mayor


@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (0, 0, 0),
        (2, 1, 2),
        (1, 2, 2)
    ]

)
def test_num_mayor(input_x, input_y, expected):
        assert num_mayor(input_x, input_y) == expected