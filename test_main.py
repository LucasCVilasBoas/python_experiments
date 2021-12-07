import pytest
import adder

# Testing sum function
def test_add_two_positive_numbers():
    assert adder.add_two_numbers(1, 1) == 2

def test_add_two_negative_numbers():
    assert adder.add_two_numbers(-1, -1) == -2

def test_add_two_numbers_positive_and_negative():
    assert adder.add_two_numbers(-1, 1) == 0

def test_add_two_numbers_positive_and_zero():
    assert adder.add_two_numbers(1, 0) == 1

def test_add_two_numbers_negative_and_zero():
    assert adder.add_two_numbers(-1, 0) == -1


# Testing subtraction function
def test_subtract_two_positive_numbers():
    assert adder.subtract_two_numbers(1, 1) == 0

def test_subtract_two_negative_numbers():
    assert adder.subtract_two_numbers(-1, -1) == 0

def test_subtract_two_numbers_positive_and_negative():
    assert adder.subtract_two_numbers(-1, 1) == -2

def test_subtract_two_numbers_positive_and_zero():
    assert adder.subtract_two_numbers(1, 0) == 1

def test_subtract_two_numbers_negative_and_zero():
    assert adder.subtract_two_numbers(-1, 0) == -1