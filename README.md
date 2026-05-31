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

### Comparisions for different datasets

`Algorithm    | Dataset         | Time (ms)        | Peak Memory (KiB)`
---------------------------------------------------------------------------

--- `Dataset size: 500` ---
Merge Sort   | Sorted          |        5.252 ms |        10.507812 KiB
Quick Sort   | Sorted          |       62.553 ms |        15.125000 KiB
Merge Sort   | Reverse Sorted  |        2.471 ms |         9.796875 KiB
Quick Sort   | Reverse Sorted  |       99.521 ms |        12.093750 KiB
Merge Sort   | Random          |        3.421 ms |         8.281250 KiB
Quick Sort   | Random          |        0.833 ms |         0.000000 KiB

--- `Dataset size: 1000` ---
Merge Sort   | Sorted          |        7.396 ms |        19.531250 KiB
Quick Sort   | Sorted          |      878.855 ms |        43.343750 KiB
Merge Sort   | Reverse Sorted  |        9.775 ms |        19.531250 KiB
Quick Sort   | Reverse Sorted  |     1609.299 ms |        43.343750 KiB
Merge Sort   | Random          |        5.087 ms |        16.757812 KiB
Quick Sort   | Random          |        1.656 ms |         0.000000 KiB

--- `Dataset size: 2000` ---
Merge Sort   | Sorted          |       15.827 ms |        39.062500 KiB
Quick Sort   | Sorted          |     9553.995 ms |       105.843750 KiB
Merge Sort   | Reverse Sorted  |        9.519 ms |        39.062500 KiB
Quick Sort   | Reverse Sorted  |    11328.217 ms |       105.843750 KiB
Merge Sort   | Random          |       15.823 ms |        33.140625 KiB
Quick Sort   | Random          |       12.404 ms |         0.000000 KiB



## Usage

Run any script with Python, for example:

```bash
python benchmark.py
```

Or execute one of the algorithm files directly to test sorting behavior and compare results.

