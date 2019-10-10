import argparse
import time
import os
from merge_sort import call_merge_sort
from three_way_merge_sort import call_three_way_merge_sort
from heap_sort import heap_sort
from insertion_sort import insertion_sort


def covert_input_file_to_arr(file_path):
    with open(file_path, 'r') as reader:
        arr = [int(num) for num in reader]
    return arr


def run_algorithm(input_arr):
    sorting_algorithms = [call_merge_sort, call_three_way_merge_sort, insertion_sort, heap_sort]
    for algorithm in sorting_algorithms:
        print('Running {} on array of length {}'.format(algorithm.__name__, len(input_arr)))
        algorithm(input_arr)

    # insertion_sort(input_arr)
    # print('Running {} on array of length {}'.format(merge_sort.__name__, len(input_arr)))
    # merge_sort(input_arr, 0, len(input_arr)-1)
    # print('Running {} on array of length {}'.format(heap_sort.__name__, len(input_arr)))
    # heap_sort(input_arr)
    # print('Running {} on array of length {}'.format(three_way_merge_sort.__name__, len(input_arr)))
    # three_way_merge_sort(input_arr, 1, len(input_arr))


if __name__ == '__main__':
    help_message = """
    Run insertion sort algorithm on a set of input data. To run insertion sort on only custom data, you have to use the
    --no-default flag unless it would run on both the sample data and custom data
    """
    parser = argparse.ArgumentParser(description=help_message)

    parser.add_argument('-fp', '--filepath',
                        action='store',
                        nargs='?',
                        help='File path to input data',
                        dest='file_path',
                        metavar='path/to/file',
                        )

    parser.add_argument('-cv', '--custom-values',
                        action='store',
                        nargs='*',
                        type=int,
                        help='List of numbers to sorted separated by space e.g 8 1 4',
                        dest='custom_values',
                        )

    parser.add_argument('--no-default',
                        help='Do not insertion sort on the input data provided',
                        action='store_false',
                        dest='default_mode',
                        )
    args = parser.parse_args()

    if args.default_mode:
        input_dirs = os.listdir('input_data')
        for folder in input_dirs:
            n_n = os.listdir('input_data/{}'.format(folder))
            for file in n_n:
                file_name = f'input_data/{folder}/{file}'
                default_input_data = covert_input_file_to_arr(file_name)
                run_algorithm(default_input_data)

    if args.file_path:
        custom_arr = covert_input_file_to_arr(args.file_path)
        run_algorithm(custom_arr)

    if args.custom_values:
        file_name = 'custom_values_{0:.0f}.txt'.format(time.time())
        with open(file_name, 'w+') as writer:
            for val in args.custom_values:
                writer.write('{}\n'.format(val))

        custom_value_arr = covert_input_file_to_arr(file_name)
        run_algorithm(custom_value_arr)

