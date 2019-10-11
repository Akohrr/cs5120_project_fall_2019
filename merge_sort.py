import time


num_of_comparisons = 0


def merge(input_data, p, q, r):
    global num_of_comparisons
    n1 = q - p + 1
    n2 = r - q

    left_array = [0] * (n1 + 1)
    right_array = [0] * (n2 + 1)

    for i in range(0, n1):
        left_array[i] = input_data[p + i]

    for j in range(0, n2):
        right_array[j] = input_data[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            num_of_comparisons += 1
            input_data[k] = left_array[i]
            i += 1
        else:
            num_of_comparisons += 1
            input_data[k] = right_array[j]
            j += 1
        k += 1

    while i < n1:
        input_data[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        input_data[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(input_data, p, r):
    """

    :param input_data: array to be sorted
    :param p: index of start of the array i.e 0
    :param r: len(input_data) - 1
    :return: dict showing summary of results
    """

    if p < r:
        q = (p + (r - 1)) // 2
        merge_sort(input_data, p, q)
        merge_sort(input_data, q + 1, r)
        merge(input_data, p, q, r)


def call_merge_sort(arr):
    global num_of_comparisons
    start = time.time()
    merge_sort(arr, 0, len(arr)-1)
    end = time.time()
    execution_time = (end - start) * 1000  # time in milliseconds
    with open('merge_sort_output_data.csv', 'a') as writer:
        writer.write(f'{len(arr)}, {num_of_comparisons}, {execution_time}\n')
    output = {'sorted_array': arr, 'execution_time': execution_time, 'num_of_comparisons': num_of_comparisons}
    num_of_comparisons = 0
    return output

