# third party packages and modules

# standard library packages and modules
import array as ar

# internal packages and modules

def merge(arr1, arr2):
    result = ar.array('i', [])
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result = result + arr1[i:]
    result = result + arr2[j:]
    return result

def merge_sort(arr):

    if (len(arr) <= 1):
        return arr

    mid = (len(arr) // 2)
    leftArr = merge_sort(arr[:mid])
    rightArr = merge_sort(arr[mid:])
    arr = merge(leftArr, rightArr)
    return arr


if __name__ == '__main__':
    arr = ar.array('i', [4, 9, 5, 4, 3, 2, 8])
    arr = merge_sort(arr)
    print(arr)
