# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    #print('\n\n\t\t---New Test---')

    ## Sort loot
    pairs = list(zip(prices, weights))
    value = [prices[i] / weights[i] for i in range(len(prices))]
    pair_value = list(zip(value, pairs))
    pairs = [x for y, x in sorted(pair_value, reverse=True)]

    ## Fill bag
    loot = 0
    for i in range(len(pairs)):
        #print(capacity, pairs, loot)
        if capacity == 0: continue
        elif i <= len(pairs):
            a = min(capacity, pairs[i][1])
            loot += a * (pairs[i][0] / pairs[i][1])
            pairs[i] = (pairs[i][0], pairs[i][1] - a)
            capacity -= a
    #print('Max Loot: ', loot)
    return loot


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
