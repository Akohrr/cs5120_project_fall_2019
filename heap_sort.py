import time

num_of_comparisons = 0


def heapify(input_data, n, i):
    global num_of_comparisons
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and input_data[i] < input_data[left]:
        num_of_comparisons += 1
        largest = left

    if right < n and input_data[largest] < input_data[right]:
        num_of_comparisons += 1
        largest = right

    if largest != i:
        input_data[i], input_data[largest] = input_data[largest], input_data[i]
        heapify(input_data, n, largest)


def heap_sort(input_data):
    start = time.time()
    n = len(input_data)

    for i in range(n, -1, -1):
        heapify(input_data, n, i)

    for i in range(n-1, 0, -1):
        input_data[i], input_data[0] = input_data[0], input_data[i]
        heapify(input_data, i, 0)

    end = time.time()
    execution_time = (end - start) * 1000  # time in milliseconds

    with open('heap_sort_output_data.csv', 'a') as writer:
        writer.write(f'{len(input_data)}, {num_of_comparisons}, {execution_time}\n')

    output = {'sorted_array': input_data, 'execution_time': execution_time, 'num_of_comparisons': num_of_comparisons}
    return output
