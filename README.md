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

## Usage

Run any script with Python, for example:

```bash
python benchmark.py
```

Or execute one of the algorithm files directly to test sorting behavior and compare results.

