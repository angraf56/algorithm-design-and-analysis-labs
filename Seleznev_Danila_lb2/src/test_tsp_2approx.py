import pytest
from tsp_2approx import (
    prim_mst,
    dfs_preorder,
    tsp_2approximation,
    INF
)

class TestPrimMST:
    def test_simple_graph(self):
        matrix = [
            [INF, 1, 2],
            [1, INF, 3],
            [2, 3, INF]
        ]
        mst = prim_mst(matrix, 3)

        total_edges = sum(len(neighbors) for neighbors in mst)
        assert total_edges == 4  # 2 ребра * 2 направления

        # Оптимальное MST: 0-1 (вес 1) + 0-2 (вес 2) = 3
        total_weight = sum(weight for neighbors in mst for _, weight in neighbors) / 2
        assert total_weight == 3.0

class TestDFSPreorder:
    def test_sorted_neighbors(self):
        mst = [
            [(1, 10), (2, 5), (3, 7)],
            [(0, 10)],
            [(0, 5)],
            [(0, 7)]
        ]
        path = dfs_preorder(mst, 0, 4)
        # После 0 должна идти вершина с минимальным весом (2 с весом 5)
        assert path[0] == 0
        assert path[1] == 2
    
    def test_sorted_by_vertex_number(self):
        mst = [
            [(3, 5), (1, 5), (2, 5)],
            [(0, 5)],
            [(0, 5)],
            [(0, 5)]
        ]
        path = dfs_preorder(mst, 0, 4)
        # При равных весах должна быть сортировка по номеру
        assert path[0] == 0
        assert path[1] == 1  # Минимальный номер при равных весах

class TestSolveTSP:
    def test_sample_input_1(self):
        matrix = [
            [INF, 18.97, 22.36, 19.42, 3.61],
            [18.97, INF, 35.61, 38.01, 17.0],
            [22.36, 35.61, INF, 16.28, 21.19],
            [19.42, 38.01, 16.28, INF, 21.02],
            [3.61, 17.0, 21.19, 21.02, INF]
        ]
        length, path = tsp_2approximation(2, matrix)

        assert path == [2, 3, 0, 4, 1, 2]
        assert abs(length - 91.92) < 0.01
    
    def test_sample_input_2(self):
        matrix = [
            [INF, 9.22, 23.32, 8.49, 16.76, 30.0, 26.02, 13.89, 3.61, 13.15, 21.4, 8.06, 4.12],
            [9.22, INF, 32.2, 17.69, 25.5, 39.2, 33.38, 13.93, 12.73, 21.02, 30.48, 5.1, 11.66],
            [23.32, 32.2, INF, 15.23, 15.52, 12.17, 25.24, 27.29, 19.72, 12.21, 3.16, 29.0, 20.62],
            [8.49, 17.69, 15.23, INF, 10.05, 21.63, 21.19, 18.03, 5.0, 8.06, 13.04, 15.65, 7.28],
            [16.76, 25.5, 15.52, 10.05, INF, 15.26, 11.66, 28.07, 14.14, 16.12, 12.37, 24.74, 17.03],
            [30.0, 39.2, 12.17, 21.63, 15.26, INF, 19.1, 37.64, 26.63, 22.56, 11.05, 37.22, 28.65],
            [26.02, 33.38, 25.24, 21.19, 11.66, 19.1, INF, 38.83, 24.33, 27.78, 22.2, 34.0, 27.46],
            [13.89, 13.93, 27.29, 18.03, 28.07, 37.64, 38.83, INF, 14.56, 15.23, 26.93, 8.94, 11.4],
            [3.61, 12.73, 19.72, 5.0, 14.14, 26.63, 24.33, 14.56, INF, 10.0, 17.8, 10.77, 3.16],
            [13.15, 21.02, 12.21, 8.06, 16.12, 22.56, 27.78, 15.23, 10.0, INF, 11.7, 17.2, 9.49],
            [21.4, 30.48, 3.16, 13.04, 12.37, 11.05, 22.2, 26.93, 17.8, 11.7, INF, 27.66, 19.1],
            [8.06, 5.1, 29.0, 15.65, 24.74, 37.22, 34.0, 8.94, 10.77, 17.2, 27.66, INF, 8.6],
            [4.12, 11.66, 20.62, 7.28, 17.03, 28.65, 27.46, 11.4, 3.16, 9.49, 19.1, 8.6, INF]
        ]
        length, path = tsp_2approximation(10, matrix)

        assert path == [10, 2, 5, 9, 3, 8, 12, 0, 11, 1, 7, 4, 6, 10]
        assert abs(length - 147.25) < 0.01

class TestEdgeCases:
    def test_two_cities(self):
        matrix = [
            [INF, 10],
            [10, INF]
        ]
        length, path = tsp_2approximation(0, matrix)
        assert len(path) == 3
        assert length == 20
    
    def test_single_city(self):
        matrix = [[INF]]
        length, path = tsp_2approximation(0, matrix)
        assert len(path) == 2
        assert path == [0, 0]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
