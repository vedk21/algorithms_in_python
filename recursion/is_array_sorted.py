'''
    Solution to check if array is sorted ascending using recursion
'''

def is_array_sorted(arr, size):
    # if array is empty return False
    if (size == 0):
        return False
    # if there are only one element left in arr, return True
    if (size == 1):
        return True

    # solve problem for left n-1 elements if last 2 elements are sorted otherwise return False
    return False if arr[size - 1] < arr[size - 2] else is_array_sorted(arr, size - 1)

if __name__ == '__main__':
    arr = [i for i in range(21, 0, -1)]
    print(f'Array: {arr}')
    print(f"The given array is {'sorted.' if is_array_sorted(arr, len(arr)) else 'not sorted.'}")

    arr = [i for i in range(21)]
    print(f'Array: {arr}')
    print(f"The given array is {'sorted.' if is_array_sorted(arr, len(arr)) else 'not sorted.'}")
