# third party packages and modules

# standard library packages and modules
import array as arr

# internal packages and modules

def insertion_sort(arr):
    for i in range(1, len(arr)):
        # pivot value
        index_to_check = i
        while(index_to_check > 0
        and arr[index_to_check - 1] > arr[index_to_check]):
            arr[index_to_check - 1], arr[index_to_check] = arr[index_to_check], arr[index_to_check - 1]
            index_to_check -= 1

    return arr


if __name__ == '__main__':
    arr = arr.array('i', [14, 9, 18, 4, 3, 2, 18])
    arr = insertion_sort(arr)
    print(arr)
