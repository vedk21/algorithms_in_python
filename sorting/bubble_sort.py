import array as arr

import utils.utility as util

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        is_swapped = False
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr = util.swap(arr, i, j)
                is_swapped = True
        if not is_swapped:
            break
    return arr


if __name__ == '__main__':
    arr = arr.array('i', [14, 9, 18, 4, 3, 2, 8])
    arr = bubble_sort(arr)
    print(arr)
