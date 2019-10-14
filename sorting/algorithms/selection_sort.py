# third party packages and modules

# standard library packages and modules
import array as arr

# internal packages and modules
import utils.utility as util

def selection_sort(arr):
    for i in range(len(arr)):
        # saving minimum element as first element of new iteration
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # don't swap if min_index is same as we started with
        if min_index != i:
            arr = util.swap(arr, i, min_index)

    return arr


if __name__ == '__main__':
    arr = arr.array('i', [14, 9, 18, 4, 3, 2, 18])
    arr = selection_sort(arr)
    print(arr)
