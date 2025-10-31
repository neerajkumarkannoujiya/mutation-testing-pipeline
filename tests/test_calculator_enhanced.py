import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator
import pytest

class TestCalculatorEnhanced:
    def setup_method(self):
        self.calc = Calculator()
    
    def test_add_positive(self):
        assert self.calc.add(2, 3) == 5
    
    def test_add_negative(self):
        assert self.calc.add(-1, -1) == -2
    
    def test_add_mixed(self):
        assert self.calc.add(-1, 1) == 0
    
    def test_subtract_positive(self):
        assert self.calc.subtract(5, 3) == 2
    
    def test_subtract_negative(self):
        assert self.calc.subtract(3, 5) == -2
    
    def test_multiply_positive(self):
        assert self.calc.multiply(2, 3) == 6
    
    def test_multiply_by_zero(self):
        assert self.calc.multiply(2, 0) == 0
        assert self.calc.multiply(0, 5) == 0
    
    def test_multiply_negative(self):
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(2, -3) == -6
        assert self.calc.multiply(-2, -3) == 6
    
    def test_divide_positive(self):
        assert self.calc.divide(6, 3) == 2
    
    def test_divide_fraction(self):
        assert self.calc.divide(5, 2) == 2.5
    
    def test_divide_negative(self):
        assert self.calc.divide(-6, 3) == -2
        assert self.calc.divide(6, -3) == -2
        assert self.calc.divide(-6, -3) == 2
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
    
    def test_is_even_positive(self):
        assert self.calc.is_even(4) == True
        assert self.calc.is_even(5) == False
    
    def test_is_even_negative(self):
        assert self.calc.is_even(-4) == True
        assert self.calc.is_even(-5) == False
    
    def test_is_even_zero(self):
        assert self.calc.is_even(0) == True
    
    # Edge case tests to kill more mutants
    def test_add_floats(self):
        assert self.calc.add(2.5, 3.5) == 6.0
    
    def test_subtract_same_number(self):
        assert self.calc.subtract(5, 5) == 0
    
    def test_divide_by_one(self):
        assert self.calc.divide(7, 1) == 7
