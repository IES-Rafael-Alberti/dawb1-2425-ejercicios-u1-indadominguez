import pytest
from src.ej02_def import calcular_importe_total

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (4, 2, 8),
        (1, 3, 3),
        (2, 2, 4)
    ]

)
def test_calcular_importe_total(input_x, input_y, expected):
        assert calcular_importe_total(input_x, input_y) == expected



    