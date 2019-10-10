import math
import time


num_of_comparisons = 0


def three_way_merge(input_data, p, mid1, mid2, r):
    global num_of_comparisons
    left_array = input_data[p - 1: mid1]
    mid_array = input_data[mid1: mid2 + 1]
    right_array = input_data[mid2 + 1: r]

    left_array.append(math.inf)
    mid_array.append(math.inf)
    right_array.append(math.inf)

    i = 0
    j = 0
    k = 0
    for num in range(p - 1, r):
        minimum = min([left_array[i], mid_array[j], right_array[k]])
        if minimum == left_array[i]:
            num_of_comparisons += 1
            input_data[num] = left_array[i]
            i += 1
        elif minimum == mid_array[j]:
            num_of_comparisons += 1
            input_data[num] = mid_array[j]
            j += 1
        else:
            num_of_comparisons += 1
            input_data[num] = right_array[k]
            k += 1


def three_way_merge_sort(input_data, p, r):
    """

    :param input_data: input array to be sorted
    :param p: starting index. Note that it should start from 1
    :param r: length of the input data i.e len(input_data)
    :return: output, a dictionary with summary of the data
    """
    start = time.time()
    if len(input_data[p - 1: r]) < 2:
        pass
    else:
        mid1 = p + ((r - p) // 3)
        mid2 = p + 2 * ((r - p) // 3)

        three_way_merge_sort(input_data, p, mid1)
        three_way_merge_sort(input_data, mid1 + 1, mid2 + 1)
        three_way_merge_sort(input_data, mid2 + 2, r)
        three_way_merge(input_data, p, mid1, mid2, r)

    end = time.time()
    execution_time = (end-start) * 1000  # time in milliseconds
    with open('three_way_merge_sort_output_data.csv', 'a') as writer:
        writer.write(f'{len(input_data)}, {num_of_comparisons}, {execution_time}\n')

    output = {'sorted_array': input_data, 'execution_time': execution_time, 'num_of_comparison': num_of_comparisons}
    return output
