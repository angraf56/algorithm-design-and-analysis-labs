import pytest
from tsp_little import (
    reduce_matrix,
    find_best_zero,
    creates_small_cycle,
    remove_row_col,
    little_algorithm,
    INF
)

class TestReduceMatrix:
    def test_reduce_simple_matrix(self):
        matrix = [[INF, 2, 3], [4, INF, 5], [6, 7, INF]]
        cost = reduce_matrix(matrix)
        # Редукция строк: 2+4+6=12, редукция столбцов: 1, итого: 13
        assert cost == 13
        for row in matrix:
            assert 0 in row or all(x == INF for x in row)

class TestFindBestZero:
    def test_find_in_simple_matrix(self):
        matrix = [[INF, 0, 1], [0, INF, 2], [3, 4, INF]]
        pos, penalty = find_best_zero(matrix)
        # Два нуля: (0,1) со штрафом 1+4=5, (1,0) со штрафом 2+3=5
        # Выбирается первый найденный
        assert pos == (0, 1)
        assert penalty == 5

class TestCreatesSmallCycle:
    def test_small_cycle(self):
        edges = [(0, 1), (1, 2)]
        assert creates_small_cycle(edges, 2, 0, 5)
    
    def test_full_cycle(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
        assert not creates_small_cycle(edges, 4, 0, 5)

class TestRemoveRowCol:
    def test_remove_from_3x3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rows = [0, 1, 2]
        cols = [0, 1, 2]
        new_matrix, new_rows, new_cols = remove_row_col(matrix, rows, cols, 1, 1)
        assert len(new_matrix) == 2
        assert len(new_matrix[0]) == 2
        assert new_rows == [0, 2]
        assert new_cols == [0, 2]

class TestLittleAlgorithm:
    def test_sample_input_1(self):
        matrix = [
            [INF, 1, 3],
            [3, INF, 1],
            [1, 2, INF]
        ]
        path, cost = little_algorithm(matrix)

        assert path == [0, 1, 2]
        assert cost == 3.0
    
    def test_sample_input_2(self):
        matrix = [
            [INF, 3, 4, 1],
            [1, INF, 3, 4],
            [9, 2, INF, 4],
            [8, 9, 2, INF]
        ]
        path, cost = little_algorithm(matrix)

        assert path == [0, 3, 2, 1]
        assert cost == 6.0

class TestEdgeCases:    
    def test_two_cities(self):
        matrix = [
            [INF, 10],
            [15, INF]
        ]
        path, cost = little_algorithm(matrix)
        assert path == [0, 1]
        assert cost == 25.0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
