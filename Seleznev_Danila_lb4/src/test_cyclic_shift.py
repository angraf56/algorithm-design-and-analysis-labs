import pytest
from cyclic_shift import compute_prefix_function, kmp_search_cyclic, find_cyclic_shift

class TestCyclicShift:
    def test_basic_case(self):
        assert find_cyclic_shift("defabc", "abcdef") == 3

    def test_identical_strings(self):
        assert find_cyclic_shift("abcdef", "abcdef") == 0
    
    def test_another_shift(self):
        assert find_cyclic_shift("bcdefa", "abcdef") == 5
    
    def test_not_cyclic_shift(self):
        assert find_cyclic_shift("abcxyz", "abcdef") == -1
    
    def test_different_lengths(self):
        assert find_cyclic_shift("abc", "abcdef") == -1
    
    def test_empty_strings(self):
        assert find_cyclic_shift("", "") == 0
