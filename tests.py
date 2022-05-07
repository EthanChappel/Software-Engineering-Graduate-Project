import pytest
from big_number_computation import big_number_computation, to_int
from date_time_transformation import transform_datetime
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


# String and words

test_text = "The cosmos is all that is...\n...or ever was or ever will be."

def test_word_count():
    assert word_count(test_text) \
        == {
            'The': 1,
            'cosmos': 1,
            'is': 2,
            'all': 1,
            'that': 1,
            'or': 2,
            'ever': 2,
            'was': 1,
            'will': 1,
            'be': 1
        }

def test_word_replacement():
    assert word_replacement('cosmos', 'universe', test_text) \
        == "The universe is all that is...\n...or ever was or ever will be."

def test_grep_line():
    assert grep_line("cosmos", test_text) == [' 1:  The cosmos is all that is...']
