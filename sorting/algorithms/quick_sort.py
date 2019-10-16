# third party packages and modules

# standard library packages and modules
import array as ar

# internal packages and modules

def findPivotIndex(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    pivot = arr[start]
    pivotIndex = start
    # find the appropriate pivot index and return
    for i in range(start + 1, end + 1):
        if arr[i] < pivot:
            # increase pivot index until we find numbers less than pivot element
            pivotIndex += 1
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]

    return pivotIndex

def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivotIndex = findPivotIndex(arr, left, right)

        # put the pivot element at pivot index
        arr[left], arr[pivotIndex] = arr[pivotIndex], arr[left]

        arr = quick_sort(arr, left, pivotIndex)
        arr = quick_sort(arr, pivotIndex+1, right)

    return arr


if __name__ == '__main__':
    arr = ar.array('i', [4, 9, 5, 4, 3, 2, 8])
    arr = quick_sort(arr)
    print(arr)
