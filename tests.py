import pytest
from big_number_computation import big_number_computation, to_int
from string_and_words import word_count, word_replacement, grep_line


# Big Number Computation

def test_to_int_normal_positive():
    assert to_int("1") == 1

def test_to_int_big_positive():
    assert to_int("100000000000000000000000000000000000000000") \
        == 100000000000000000000000000000000000000000

def test_to_int_normal_negative():
    assert to_int("-1") == -1

def test_to_int_big_negative():
    assert to_int("-100000000000000000000000000000000000000000") \
        == -100000000000000000000000000000000000000000

def test_to_int_zero():
    assert to_int("0") == 0

def test_big_number_computation_normal_addition():
    assert big_number_computation("2", "+", "1") == "3"

def test_big_number_computation_normal_subtraction():
    assert big_number_computation("2", "-", "1") == "1"

def test_big_number_computation_normal_multiplication():
    assert big_number_computation("2", "*", "1") == "2"

def test_big_number_computation_big_addition():
    assert big_number_computation("200000000000000000000000000000000000000000", "+", "100000000000000000000000000000000000000000") \
        == "300000000000000000000000000000000000000000"

def test_big_number_computation_big_subtraction():
    assert big_number_computation("200000000000000000000000000000000000000000", "-", "100000000000000000000000000000000000000000") \
        == "100000000000000000000000000000000000000000"

def test_big_number_computation_big_multiplication():
    assert big_number_computation("200000000000000000000000000000000000000000", "*", "100000000000000000000000000000000000000000") \
        == "20000000000000000000000000000000000000000000000000000000000000000000000000000000000"

