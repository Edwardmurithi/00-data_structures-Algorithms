def insertion_sort(arr):
    for j in range(1, len(arr)): # Start from index 1 (since index 0 is considered sorted)
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:  # Shift elements to the right
            arr[i + 1] = arr[i]
            i = i - 1

        arr[i + 1] = key # Insert the key at the correct position


arr = [5, 3, 8, 6, 2]
print("Before sorting:", arr)
insertion_sort(arr)
print("After sorting:", arr)