from one_hot_encoder import fit_transform
import pytest


def test_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    transformed_cities = fit_transform(cities)
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert transformed_cities == exp_transformed_cities


def test_exception():
    with pytest.raises(TypeError):
        fit_transform(12)


def test_exception_error():
    with pytest.raises(ValueError):
        fit_transform(12)


def test_moscow():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    transformed_cities = fit_transform(cities)
    assert ('Moscow', [0, 0, 1]) in transformed_cities


def test_moscow_error():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    transformed_cities = fit_transform(cities)
    assert ('Moscow', [0, 0, 1]) not in transformed_cities
