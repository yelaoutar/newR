import pytest

from src.main import calculer_moyenne


def test_calculer_moyenne():
    assert calculer_moyenne([10, 15, 20]) == 15


def test_liste_vide():
    with pytest.raises(ValueError):
        calculer_moyenne([])
