import pytest
from src.ej01_def import dar_bienvenida

def test_dar_bienvenida():
    assert dar_bienvenida("Indalecio") == ("Hola, Indalecio")
