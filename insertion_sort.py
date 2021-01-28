import time


def insertion_sort(input_data):
    start = time.time()

    num_of_comparisons = 0

    for j in range(1, len(input_data)):
        key = input_data[j]
        i = j - 1
        while i >= 0 and input_data[i] > key:
            num_of_comparisons += 1
            input_data[i + 1] = input_data[i]
            i = i - 1
        input_data[i+1] = key
    end = time.time()
    execution_time = (end-start) * 1000  # time in milliseconds
    with open('insertion_sort_output_data.csv', 'a') as writer_1:
        writer_1.write(f'{len(input_data)}, {num_of_comparisons}, {execution_time}\n')
    output = {'sorted_array': input_data, 'execution_time': execution_time, 'num_of_comparisons': num_of_comparisons}
    return output

