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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run insertion sort algorithm on a set of input data')

    parser.add_argument('-fp', '--filepath',
                        action='store',
                        nargs='?',
                        help='File path to input data',
                        dest='file_path',
                        metavar='path/to/file',
                        )

    parser.add_argument('--default',
                        help='Run insertion sort on the input data provided',
                        action='store_true',
                        dest='default_mode',
                        )
    args = parser.parse_args()

    if args.default:
        input_dirs = os.listdir('input_data')
        for folder in input_dirs:
            n_n = os.listdir('input_data/{}'.format(folder))
            for file in n_n:
                print(f'Current file is: input_data/{folder}/{file}')
                insertion_sort(f'input_data/{folder}/{file}')

    if args.file_path is not None:
        insertion_sort(args.file_path)
