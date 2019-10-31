
def k_ary_string(arr, size, k):
    if (size < 1):
        print(arr, end='')
    else:
        for i in range(k):
            arr[size - 1] = i
            k_ary_string(arr, size - 1, k)
    print('')

if __name__ == '__main__':
    arr = [0, 1, 2]
    k_ary_string(arr, len(arr), 3)
