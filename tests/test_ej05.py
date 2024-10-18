import pytest
from src.ej05_def2 import calcula_precio

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (14, 25, "El precio final del artículo con IVA (25.00) es 17.50€."),
        (10, 25, "El precio final del artículo con IVA (25.00) es 12.50€."),
        (27, 10, "El precio final del artículo con IVA (10.00) es 29.70€.")
    ]

)
def test_calcula_precio(input_x, input_y, expected):
        assert calcula_precio(input_x, input_y) == expected

