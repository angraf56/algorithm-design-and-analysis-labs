import pytest
from levenshtein import levenshtein_distance

def test_empty_strings():
    assert levenshtein_distance("", "") == 0
    assert levenshtein_distance("abc", "") == 3
    assert levenshtein_distance("", "abc") == 3

def test_identical_strings():
    assert levenshtein_distance("hello", "hello") == 0

def test_single_operation():
    assert levenshtein_distance("cat", "bat") == 1
    assert levenshtein_distance("cat", "cats") == 1
    assert levenshtein_distance("cats", "cat") == 1

def test_multiple_operations():
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("saturday", "sunday") == 3

