import random
import os


if not os.path.exists('input_data'):
    os.mkdir('input_data')

input_data_sizes = [20000, 40000, 60000, 80000, 100000]

input_data_types = ['random_data', 'sorted_random_data', 'reverse_sorted_random_data', 'identical_data']


def generate_random_numbers(count, data_type='random_data'):
    """function is used to generate random numbers.
    :param count: number of random numbers to generate
    :param data_type: Type of random data you want. default is random numbers.
    :return: list of random numbers"""
    start = 0
    end = 1000000  # max number is 1 million as given in instructions
    result = []
    if data_type == 'identical_data':
        number = random.randint(start, end)
        result = [number for _ in range(count)]

    elif data_type == 'random_data':
        result = [random.randint(start, end) for _ in range(count)]

    elif data_type == 'sorted_random_data':
        result = sorted([random.randint(start, end) for _ in range(count)])

    elif data_type == 'reverse_sorted_random_data':
        result = sorted([random.randint(start, end) for _ in range(count)], reverse=True)

    return result


def create_input_data_files():
    for input_data_size in input_data_sizes:
        file_name = 'input_data/{}'.format(input_data_size)
        if not os.path.exists(file_name):
            os.mkdir(file_name)
        for input_data_type in input_data_types:
            with open(file_name+'/{}.txt'.format(input_data_type), 'w+') as writer:
                for num in generate_random_numbers(count=input_data_size, data_type=input_data_type):
                    writer.write('{}\n'.format(num))
