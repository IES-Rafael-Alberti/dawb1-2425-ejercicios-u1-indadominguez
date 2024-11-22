import pytest
from src.ej04_def2 import grados_celsius

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (32, 0.0),
        (145, 62.78),
        (122, 50)
    ]

)
def test_grados_celsius(input_x, expected):
        assert grados_celsius(input_x) == expected


