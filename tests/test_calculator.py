import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator
import pytest

class TestCalculator:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
    
    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(3, 5) == -2
    
    def test_multiply(self):
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(2, 0) == 0
    
    def test_divide(self):
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)
    
    def test_is_even(self):
        assert self.calc.is_even(4) == True
        assert self.calc.is_even(5) == False
