import pytest
from wagner_fischer_path import wagner_fischer_with_path

def test_empty_strings():
    assert wagner_fischer_with_path(1, 1, 1, "", "") == ""
    assert wagner_fischer_with_path(1, 1, 1, "abc", "") == "DDD"
    assert wagner_fischer_with_path(1, 1, 1, "", "abc") == "III"

def test_identical_strings():
    result = wagner_fischer_with_path(1, 1, 1, "hello", "hello")
    assert result == "MMMMM"

def test_single_operations():
    result = wagner_fischer_with_path(1, 1, 1, "cat", "bat")
    assert 'R' in result and result.count('M') == 2
    
    result = wagner_fischer_with_path(1, 1, 1, "cat", "cats")
    assert 'I' in result and result.count('M') == 3

def test_path_correctness():
    result = wagner_fischer_with_path(1, 1, 1, "kitten", "sitting")
    assert len(result) == 7
    assert all(op in 'MRID' for op in result)
