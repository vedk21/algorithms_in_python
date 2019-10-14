import array as arr
import bubble_sort as bSort

if __name__ == '__main__':
    arr = arr.array('i', [14, 9, 18, 4, 3, 2, 8])
    arr = bSort.bubble_sort(arr)
    print(arr)
