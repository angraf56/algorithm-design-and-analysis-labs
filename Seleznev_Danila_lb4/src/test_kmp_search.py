import pytest
from kmp_search import compute_prefix_function, kmp_search

class TestPrefixFunction:    
    def test_simple_pattern(self):
        assert compute_prefix_function("abc") == [0, 0, 0]
    
    def test_pattern_with_repetition(self):
        assert compute_prefix_function("abab") == [0, 0, 1, 2]
    
    def test_pattern_all_same(self):
        assert compute_prefix_function("aaaa") == [0, 1, 2, 3]

class TestKMPSearch:
    def test_basic_case(self):
        assert kmp_search("ab", "abab") == [0, 2]
    
    def test_multiple_occurrences(self):
        assert kmp_search("abc", "abcabcabc") == [0, 3, 6]
    
    def test_no_occurrences(self):
        assert kmp_search("xyz", "abcdef") == []
    
    def test_overlapping_occurrences(self):
        assert kmp_search("aa", "aaaa") == [0, 1, 2]
    
    def test_pattern_longer_than_text(self):
        assert kmp_search("abcdef", "abc") == []
    
    def test_empty_pattern(self):
        assert kmp_search("", "abc") == []
    
    def test_empty_text(self):
        assert kmp_search("abc", "") == []
