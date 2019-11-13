from minimum_coin_change_algorithms import greedy_solution, recursive_solution, bottom_up_dynamic_solution
import sys
import time

algorithms = [recursive_solution, greedy_solution, bottom_up_dynamic_solution]


def run_all_algorithms(test_data, file_name):
    for algorithm in algorithms:
        for raw_data in test_data[:-1]:
            data = raw_data.split(' ')
            print(f'Running {algorithm.__name__} on {data}')
            if len(data) > 1:
                amount = int(data[0])
                coin_system = [int(num) for num in data[2:]]
                start_time = time.time()
                coins_used = algorithm(amount, coin_system)
                end_time = time.time()
                execution_time = (end_time - start_time) * 1000  # time in milliseconds
                if algorithm.__name__ == 'recursive_solution':
                    # in the recursive algorithm, just report the coin count and time taken to run the algorithm
                    with open(f'{algorithm.__name__}_{file_name}', 'a') as writer_1:
                        writer_1.write(f"{len(coin_system)}, {execution_time}\n")
                else:
                    # for other algorithms, report the coins used and time taken to run the algorithm
                    with open(f'{algorithm.__name__}_{file_name}', 'a') as writer_1:
                        writer_1.write(f"{' '.join([str(num) for num in coin_system])}, {execution_time}\n")
            else:
                print('Wrong data format. Read the README.md file that accompanies the project')


def convert_input_data(file_to_use):
    with open(file_to_use, 'r') as reader:
        _data = reader.read().split('\n')
        run_all_algorithms(_data, file_name='output.txt')


if __name__ == '__main__':
    if len(sys.argv) > 3:
        post_fix = time.time()
        file = 'input_data_{0:.0f}.txt'.format(post_fix)
        with open(file, 'w') as writer:
            writer.write(f'{" ".join(sys.argv[1:])}\n')
        convert_input_data(file)
    else:
        convert_input_data('input_data.txt')
