# third party packages and modules

# standard library packages and modules
import array as arr

# internal packages and modules
import algorithms.bubble_sort as bSort
import algorithms.selection_sort as sSort

# create a dictionary to save all available sorting funations options
sorting_algorithms_dict = {
    'bubble': bSort.bubble_sort,
    'selection': sSort.selection_sort
}

# get options from created dictionary
sorting_options_available = tuple(sorting_algorithms_dict.keys())

# sample array for testing
arr = arr.array('i', [14, 9, 18, 4, 3, 2, 8])

if __name__ == '__main__':

    while True:
        selected_sorting_option = input(f"Please choose sorting algorithm from given list: [{', '.join(sorting_options_available)}]: ")

        try:
            sort_function = sorting_algorithms_dict[selected_sorting_option.strip()]
            print(f'Array before sorting: {arr}')
            arr = sort_function(arr)
            print(f'Sorted Array: {arr}')
            break;
        except KeyError:
            print('Please enter valid sorting algorithm option from given list')
