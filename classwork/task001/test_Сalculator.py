from unittest import TestCase

import pytest

from Сalculator import Calculator


class TestCalculator(TestCase):
    calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, -1) == -2
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 5) == -4

    def test_multiply(self):
        assert self.calc.multiply(3, 4) == 12

    def test_divide(self):
        assert self.calc.divide(8, 4) == 2
        with pytest.raises(ValueError):
            self.calc.divide(1, 0)
