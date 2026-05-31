# MSCS532_Assignment2

This repository contains Python implementations of Merge Sort and Quick Sort using both static and dynamic approaches, plus a benchmark script to compare performance.

## Files

- `merge_sort_static.py`: A static implementation of Merge Sort with a fixed-size recursion or input handling style.
- `merge_sort_dynamic.py`: A dynamic implementation of Merge Sort that adapts to arbitrary list sizes and uses flexible recursion.
- `quick_sort_static.py`: A static implementation of Quick Sort using a fixed pivot selection or array partitioning style.
- `quick_sort_dynamic.py`: A dynamic implementation of Quick Sort that adapts to varying list sizes and performs recursive partitioning.
- `benchmark.py`: A script to run timing comparisons between the sort implementations and evaluate performance.

## Algorithms included

- Merge Sort: divides the list into halves, recursively sorts each half, then merges the two sorted halves.
- Quick Sort: partitions the array around a pivot, then recursively sorts the partitions.

## Example benchmark results

### Dataset size: 500

| Algorithm   | Dataset         | Time (ms) | Peak Memory (KiB) |
|------------|-----------------|----------:|------------------:|
| Merge Sort | Sorted          | 5.252     | 10.507812         |
| Quick Sort | Sorted          | 62.553    | 15.125000         |
| Merge Sort | Reverse Sorted  | 2.471     | 9.796875          |
| Quick Sort | Reverse Sorted  | 99.521    | 12.093750         |
| Merge Sort | Random          | 3.421     | 8.281250          |
| Quick Sort | Random          | 0.833     | 0.000000          |

### Dataset size: 1000

| Algorithm   | Dataset         | Time (ms) | Peak Memory (KiB) |
|------------|-----------------|----------:|------------------:|
| Merge Sort | Sorted          | 7.396     | 19.531250         |
| Quick Sort | Sorted          | 878.855   | 43.343750         |
| Merge Sort | Reverse Sorted  | 9.775     | 19.531250         |
| Quick Sort | Reverse Sorted  | 1609.299  | 43.343750         |
| Merge Sort | Random          | 5.087     | 16.757812         |
| Quick Sort | Random          | 1.656     | 0.000000          |

### Dataset size: 2000

| Algorithm   | Dataset         | Time (ms) | Peak Memory (KiB) |
|------------|-----------------|----------:|------------------:|
| Merge Sort | Sorted          | 15.827    | 39.062500         |
| Quick Sort | Sorted          | 9553.995  | 105.843750        |
| Merge Sort | Reverse Sorted  | 9.519     | 39.062500         |
| Quick Sort | Reverse Sorted  | 11328.217 | 105.843750        |
| Merge Sort | Random          | 15.823    | 33.140625         |
| Quick Sort | Random          | 12.404    | 0.000000          |

## Usage

Run any script with Python, for example:

```bash
python benchmark.py
```

Or execute one of the algorithm files directly to test sorting behavior and compare results.
