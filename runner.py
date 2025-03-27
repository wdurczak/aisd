
import time
import csv
from input import generate_data, DataType
from heap_sort import heap_sort
from quick_sort import quick_sort
from shell_sort import shell_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

class SortBenchmark:
    def __init__(self):
        self.algorithms = {
            1: ("Insertion Sort", insertion_sort),
            2: ("Shell Sort", shell_sort),
            3: ("Selection Sort", selection_sort),
            4: ("Heap Sort", heap_sort),
            5: ("Quick Sort (Left Pivot)", lambda arr: quick_sort(arr, 0, len(arr) - 1, pivot_type="left")),
            6: ("Quick Sort (Random Pivot)", lambda arr: quick_sort(arr, 0, len(arr) - 1, pivot_type="random"))
        }
        self.data_types = [
            ("Random", DataType.RANDOM),
            ("Increasing", DataType.ASCENDING),
            ("Decreasing", DataType.DESCENDING),
            ("Constant", DataType.CONSTANT),
            ("A-Shaped", DataType.A_SHAPED)
        ]

    def run(self, algorithm_number, data):
        if algorithm_number not in self.algorithms:
            raise ValueError("Nieznany numer algorytmu")
        _, sort_function = self.algorithms[algorithm_number]
        sort_function(data)

    def benchmark_all(self, sizes, output_csv="benchmark_results.csv"):
        with open(output_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Algorithm", "DataType", "InputSize", "Time"])
            for alg_num, (alg_name, sort_func) in self.algorithms.items():
                for dtype_name, dtype in self.data_types:
                    for size in sizes:
                        data = generate_data(size, dtype)
                        start = time.perf_counter()
                        sort_func(data.copy())
                        elapsed = time.perf_counter() - start
                        writer.writerow([alg_name, dtype_name, size, f"{elapsed:.6f}"])
                        print(f"{alg_name} | {dtype_name} | n={size} | {elapsed:.6f}s")

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10000)
    sizes = [2**i for i in range(4, 14)]
    benchmark = SortBenchmark()
    benchmark.benchmark_all(sizes)
