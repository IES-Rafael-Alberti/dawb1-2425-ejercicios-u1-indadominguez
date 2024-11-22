import pytest
from src.ej11_def import suma_enteros

@pytest.mark.parametrize(
    "input_x, expected",
    [
        (10, "La suma de los enteros desde 1 hasta (10) es: (55)"),
        (7, "La suma de los enteros desde 1 hasta (7) es: (28)")
        
    ]

)
def test_suma_enteros(input_x, expected):
        assert suma_enteros(input_x) == expected
