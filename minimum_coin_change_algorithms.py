def recursive_solution(amount, coin_values):
    if amount == 0:
        return 0
    minimum_number_of_coins = amount
    if amount in coin_values:
        return 1
    else:
        for i in [coin for coin in coin_values if coin <= amount]:
            number_of_coins = 1 + recursive_solution(amount - i, coin_values)
            if number_of_coins < minimum_number_of_coins:
                minimum_number_of_coins = number_of_coins
    return minimum_number_of_coins


def greedy_solution(amount, coin_values):
    if amount == 0:
        return 0
    coin_values.sort(reverse=True)
    number_of_coins = 0
    for coin in coin_values:
        if amount >= coin:
            number_of_coins += (amount // coin)
            amount = amount % coin

    return number_of_coins


def bottom_up_dynamic_solution(amount, coin_values):
    if amount == 0:
        return 0
    coins_arr = [0] * (amount+1)
    for num in range(amount+1):
        coin_count = num
        for j in [coin for coin in coin_values if coin <= num]:
            if coins_arr[num-j] + 1 < coin_count:
                coin_count = coins_arr[num-j]+1
        coins_arr[num] = coin_count

    return coins_arr[amount]
