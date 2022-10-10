from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoding(unittest.TestCase):
    def test_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed_cities = fit_transform(cities)
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(transformed_cities, exp_transformed_cities)
        self.assertNotIn(('Moscow', [1, 0, 1]), transformed_cities)
        self.assertIn(('Moscow', [0, 0, 1]), transformed_cities)

    def test_exception(self):
        with self.assertRaises(TypeError):
            fit_transform(12)

    def test_exception_error(self):
        with self.assertRaises(ValueError):
            fit_transform(12)

    def test_moscow(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed_cities = fit_transform(cities)
        self.assertIn(('Moscow', [0, 0, 1]), transformed_cities)

    def test_moscow_error(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed_cities = fit_transform(cities)
        self.assertNotIn(('Moscow', [0, 0, 1]), transformed_cities)
