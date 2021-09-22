import unittest
import numpy as np

from algorithms.sorting.sorts import *
from copy import deepcopy

class TestSorts(unittest.TestCase):
    def setUp(self) -> None:        
        self.test_arr = list(np.random.randint(1,101,5))
        self.result = sorted(self.test_arr)
        return super().setUp()

    def test_selection_sort(self) -> None:
        sorted_arr = selection_sort(deepcopy(self.test_arr))
        self.assertListEqual(sorted_arr, self.result)

    def test_bubble_sort(self) -> None:
        sorted_arr = bubble_sort(deepcopy(self.test_arr))
        self.assertListEqual(sorted_arr, self.result)
    
    def test_insertion_sort(self) -> None:
        sorted_arr = insertion_sort(deepcopy(self.test_arr))
        self.assertListEqual(sorted_arr, self.result)

    def test_merge_sort(self) -> None:
        arr = deepcopy(self.test_arr)
        merge_sort(arr)
        self.assertListEqual(arr, self.result)

    def test_heap_sort(self) -> None:
        arr = deepcopy(self.test_arr)
        heap_sort(arr)
        self.assertListEqual(arr, self.result)

    def test_quick_sort(self) -> None:
        arr = deepcopy(self.test_arr)
        quick_sort(arr, 0, len(arr)-1)
        self.assertListEqual(arr, self.result)

if __name__ == "__main__":
    unittest.main()
    