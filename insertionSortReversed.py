
#!/usr/bin/env python3

from typing import List, Optional



def insertion_sort_reversed(arr: Optional[List[float]]) -> Optional[List[float]]:
	# Sorts arr in-place in descending order using insertion sort.
	if arr is None:
		return None

	# Work in-place
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		# For descending order, shift elements that are smaller than key to the right
		while j >= 0 and arr[j] < key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key

	return arr


if __name__ == "__main__":
	# Simple demonstration and quick checks
	samples = [
		[],
		[1],
		[3, 2, 1],
		[1, 2, 3],
		[5, 3, 8, 1, 2, 9],
		[5, 5, 5, 1],
		[0, -1, 3, -2, 3],
	]

	for s in samples:
		a = s.copy()
		insertion_sort_reversed(a)
		print(f"input: {s} -> sorted descending: {a}")

