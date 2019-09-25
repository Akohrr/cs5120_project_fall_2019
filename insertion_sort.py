# import argparse
# import time
# import os
#
# # parser = argparse.ArgumentParser(description='Run insertion sort algorithm on a set of input data')
# #
# # parser.add_argument('-fp, --file-path', action='store', nargs='?', type=open, metavar='File path to input data',
# #                     dest='file_path', required=True)
# #
# # print(parser.parse_args())
#
#
# def insertion_sort(input_data_file_path: str):
#
#     with open(input_data_file_path, 'r') as reader:
#         input_data = [int(num) for num in reader]
#     num_of_comparisons = 0
#     start = time.time()
#
#     for j in range(1, len(input_data)):
#         key = input_data[j]
#         i = j - 1
#         while i >= 0 and input_data[i] > key:
#             num_of_comparisons += 1
#             input_data[i + 1] = input_data[i]
#             i = i - 1
#         input_data[i+1] = key
#     end = time.time()
#     execution_time = (end-start) * 1000
#
#     with open('output_data.txt', 'a') as writer:
#         writer.write(f'{len(input_data)} {num_of_comparisons} {execution_time}\n')
#
#     print('Size of input: {}'.format(input_data))
#     print('Time taken in Milliseconds: {}'.format(execution_time))
#     print('NUmber of comparisons is {}'.format(num_of_comparisons))
#
#
# input_dirs = os.listdir('input_data')
# print(input_dirs)
# for folder in input_dirs:
#     if folder == '20000':
#         n_n = os.listdir('input_data/{}'.format(folder))
#         for file in n_n:
#             print(f'Current file is: input_data/{folder}/{file}')
#             insertion_sort(f'input_data/{folder}/{file}')
#
#
#
#
# # 69.58782505989075 67.60318493843079