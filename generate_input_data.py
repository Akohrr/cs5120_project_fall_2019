# python file to generate input data
from random import randint


given_test_cases = [11, 23, 31, 51, 73, 83, 91, 99, 69]

file_name = 'input_data.txt'

with open(file_name, 'w+') as writer:
    for amount in given_test_cases:
        if amount == 69:
            writer.write(f'{amount} 5 1 5 10 23 25\n')
        else:
            writer.write(f'{amount} 4 1 5 10 25\n')


def generate_random_test_cases(number_of_test_cases=5):
    """
    Generate random test cases
    :param number_of_test_cases: The number of test cases to generate. Default is 20
    :return: does not return a value, instead it appends it to a file.
    """
    with open(file_name, 'a+') as writer_1:
        for num in range(number_of_test_cases):
            # generate random amount of minimum 9 and maximum 99
            random_amount = randint(9, 99)
            random_coin_system = ['1']
            # generate coin system of minimum 2 values and maximum 5 values
            number_of_coins = randint(2, 5)
            for _ in range(number_of_coins):
                # convert to string so I can use join function to output contents of the random_coin_system list
                random_coin_system.append(str(randint(1, 25)))

            writer_1.write(f'{random_amount} {number_of_coins+1} {" ".join(random_coin_system)}\n')


generate_random_test_cases()
