from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm  : {algorithm}")
    print("Total data : 10000")
    print("Range data : 0 - 1000")
    print(f"Minimum execution time: {min(times)}")


def bubble_sort(array):
    for i in range(len(array)):
        already_sorted = True
        
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+1], array[j]
                already_sorted = False
                
        if already_sorted:
            break
        
    return array

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(10000)]

    run_sorting_algorithm(algorithm="bubble_sort", array=array)
    

