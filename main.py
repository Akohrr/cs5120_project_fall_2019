import argparse
import time
import os


def insertion_sort(input_data_file_path: str):

    with open(input_data_file_path, 'r') as reader:
        input_data = [int(num) for num in reader]

    num_of_comparisons = 0
    start = time.time()

    for j in range(1, len(input_data)):
        key = input_data[j]
        i = j - 1
        while i >= 0 and input_data[i] > key:
            num_of_comparisons += 1
            input_data[i + 1] = input_data[i]
            i = i - 1
        input_data[i+1] = key
    end = time.time()
    execution_time = (end-start) * 1000

    with open('output_data.txt', 'a') as writer:
        writer.write(f'{len(input_data)} {num_of_comparisons} {execution_time}\n')

    return input_data


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
                print(f'Current file is: input_data/{folder}/{file}')
                insertion_sort(f'input_data/{folder}/{file}')

    if args.file_path:
        insertion_sort(args.file_path)

    if args.custom_values:
        file_name = 'custom_values_{0:.0f}.txt'.format(time.time())
        with open(file_name, 'w+') as writer:
            for val in args.custom_values:
                writer.write('{}\n'.format(val))
        print('Running insertion sort on {} would give {}'.format(args.custom_values, insertion_sort(file_name)))



