import pytest
from wagner_fischer import wagner_fischer

def test_empty_strings():
    assert wagner_fischer(1, 1, 1, "", "") == 0
    assert wagner_fischer(1, 1, 1, "abc", "") == 3
    assert wagner_fischer(1, 1, 1, "", "abc") == 3

def test_identical_strings():
    assert wagner_fischer(1, 1, 1, "hello", "hello") == 0

def test_standard_costs():
    assert wagner_fischer(1, 1, 1, "kitten", "sitting") == 3

def test_real_example():
    assert wagner_fischer(1, 1, 1, "entrance", "reenterable") == 5

def test_high_costs():
    assert wagner_fischer(1, 10, 1, "", "abc") == 30
    assert wagner_fischer(1, 1, 10, "abc", "") == 30

