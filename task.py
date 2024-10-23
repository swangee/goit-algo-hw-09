import timeit


def find_coins_greedy(nominals, value, result = None):
    if not nominals:
        return result

    if result is None:
        nominals.sort()
        result = {}

    nominal = nominals.pop()

    result[nominal] = value // nominal

    return find_coins_greedy(nominals, value - (result[nominal] * nominal), result)


def find_min_coins(nominals, value):
    dp = [float('inf')] * (value + 1)
    dp[0] = 0  # Нуль монет для суми 0

    coin_used = [-1] * (value + 1)

    # Проходимо по всім сумам від 1 до amount
    for i in range(1, value + 1):
        for coin in nominals:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[value] == float('inf'):
        return {}

    result = {}
    current_amount = value
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result



nominals = [50, 25, 10, 5, 2, 1]

val = 11312

print(timeit.timeit(lambda: find_coins_greedy(nominals, val)))
print(timeit.timeit(lambda: find_min_coins(nominals, val)))