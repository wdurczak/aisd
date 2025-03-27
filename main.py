from input import generate_data, DataType
from heap_sort import heap_sort
from quick_sort import quick_sort
from shell_sort import shell_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

while True:
    try:
        n = int(input("Podaj liczbę elementów: "))
        if n > 0:
            break
        else:
            print("n musi być > 0")
    except ValueError:
        print("podaj liczbe całkowitą")

data_types = list(DataType)
for i, dtype in enumerate(data_types):
    print(f"{i+1}. {dtype.value}")

while True:
    try:
        choice = int(input("Wybierz typ danych: "))
        if 1 <= choice <=len(data_types):
            selected_data_type = data_types[choice - 1]
            break
        else:
            print("podaj poprawny numer")
    except ValueError:
        print("podaj poprawna liczbe")

data = generate_data(n, selected_data_type)
sorting_algorithms = {
    "Heap Sort": heap_sort,
    "Quick Sort (Left Pivot)": lambda arr: quick_sort(arr, 0, len(arr) - 1, pivot_type="left"),
    "Quick Sort (Random Pivot)": lambda arr: quick_sort(arr, 0, len(arr) - 1, pivot_type="random"),
    "Shell Sort": shell_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
}

for i, alg in enumerate(sorting_algorithms.keys()):
    print(f"{i+1}. {alg}")

while True:
    try:
        choice = int(input("Wybór algorytmu sortowania (numer): "))
        if 1 <= choice <= len(sorting_algorithms):
            selected_algorithm = list(sorting_algorithms.values())[choice - 1]
            break
        else:
            print("wpisz poprawny numer")
    except ValueError:
        print("wpisz liczbe")

selected_algorithm(data)

print("Wynik:", data)