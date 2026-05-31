import random
import time
import tracemalloc
import sys
import io
import contextlib

# ---------------------------------------------------------
# Increase recursion limit so naive Quick Sort can handle
# larger sorted inputs without crashing immediately.
# ---------------------------------------------------------
sys.setrecursionlimit(10000)

# ---------------------------------------------------------
# Import existing sort files WITHOUT changing them.
# Their print statements will be suppressed during import.
# ---------------------------------------------------------
with contextlib.redirect_stdout(io.StringIO()):
    from merge_sort_static import merge_sort
    from quick_sort_static import quick_sort


# ---------------------------------------------------------
# Benchmark function
# ---------------------------------------------------------
def benchmark(algorithm, arr):
    """
    Measures execution time and peak memory usage.

    Parameters:
        algorithm (str): "Merge Sort" or "Quick Sort"
        arr (list): input dataset

    Returns:
        time_ms (float): execution time in milliseconds
        peak_kib (float): peak memory usage in KiB
        output (list): sorted array
    """

    # Copy input so original dataset is unchanged
    data = list(arr)

    tracemalloc.start()
    start = time.perf_counter()

    try:
        if algorithm == "Merge Sort":
            # Merge sort usually returns a new sorted list
            output = merge_sort(data)

        elif algorithm == "Quick Sort":
            # Quick sort often sorts in place
            result = quick_sort(data, 0, len(data) - 1)

            # If quick_sort returns None, use the modified data list
            output = data if result is None else result

        else:
            raise ValueError("Unknown algorithm")

        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return (end - start) * 1000, peak / 1024, output

    except RecursionError:
        # Handle worst-case recursion failure gracefully
        tracemalloc.stop()
        return None, None, None


# ---------------------------------------------------------
# Main driver
# ---------------------------------------------------------
if __name__ == "__main__":

    sizes = [500, 1000, 2000]

    print("\nAlgorithm    | Dataset         | Time (ms)        | Peak Memory (KiB)")
    print("-" * 75)

    for n in sizes:
        print(f"\n--- Dataset size: {n} ---")

        datasets = {
            "Sorted": list(range(n)),
            "Reverse Sorted": list(range(n, 0, -1)),
            "Random": [random.randint(0, 1000) for _ in range(n)]
        }

        for dataset_name, dataset in datasets.items():
            for algorithm in ["Merge Sort", "Quick Sort"]:

                time_ms, peak_kib, output = benchmark(algorithm, dataset)

                if time_ms is None:
                    print(
                        f"{algorithm:12s} | {dataset_name:15s} | "
                        f"RecursionError (worst-case recursion depth exceeded)"
                    )
                else:
                    print(
                        f"{algorithm:12s} | {dataset_name:15s} | "
                        f"{time_ms:12.3f} ms | {peak_kib:16.6f} KiB"
                    )
