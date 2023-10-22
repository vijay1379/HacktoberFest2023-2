def recursive_insertion_sort(arr, n):
    if n <= 1:
        return
    
    # Sort the first n-1 elements
    recursive_insertion_sort(arr, n - 1)
    
    # Insert the last element into the sorted subarray
    key = arr[n - 1]
    j = n - 2
    
    # Move elements of arr[0..n-1] that are greater than key
    # to one position ahead of their current position
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key

# Example usage:
arr = [12, 11, 13, 5, 6]
recursive_insertion_sort(arr, len(arr))
print("Sorted array:", arr)
