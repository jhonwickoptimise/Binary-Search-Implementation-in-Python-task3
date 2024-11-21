def binary_search(arr, target):
    # Define the starting and ending indices of the list
    left, right = 0, len(arr) - 1

    # Loop until the search interval is empty
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2
        # Compare the middle element with the target
        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    # If we reach here, the target is not in the list
    return -1

# Example
if __name__ == "__main__":
    # A sorted list
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target_value = 7

    # Perform binary search
    result = binary_search(sorted_list, target_value)

    if result != -1:
        print(f"Element {target_value} found at index {result}.")
    else:
        print(f"Element {target_value} not found in the list.")
