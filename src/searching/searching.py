import math

def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = math.floor((high + low)/2)
        guessed = arr[mid]

        if guessed == target:
            return mid

        elif guessed > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found

