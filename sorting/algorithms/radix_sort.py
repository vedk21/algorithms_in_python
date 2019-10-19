# third party packages and modules

# standard library packages and modules
import array as arr
import math

# internal packages and modules

def get_digit(num, i):
    return math.floor(abs(num) / (10**i)) % 10

def get_digit_count(num):
    if num == 0:
        return 1
    return math.floor(math.log10(abs(num))) + 1

def max_digits(nums):
    max_digit = [get_digit_count(i) for i in nums]
    return max(max_digit)

def radix_sort(arr):
    max_digit_count = max_digits(arr)

    for index in range(max_digit_count):
        # create bucket to store all digits number
        bucket = {i:[] for i in range(10)}
        # check for every numbers digit in array
        # and push into appropriate bucket index
        for num in arr:
            digit = get_digit(num, index)
            bucket[digit].append(num)
        # collect all numbers from 0 -> 9 from bucket
        # and assign them to arr
        arr = sum(bucket.values(), [])
    return arr


if __name__ == '__main__':
    arr = arr.array('i', [144, 9, 110, 4, 30, 2, 86])
    arr = radix_sort(arr)
    print(arr)
