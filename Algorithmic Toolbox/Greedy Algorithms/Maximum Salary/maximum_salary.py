# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest



def largest_number(numbers):
    # digitize all numbers in list
    # numbers = sum(list(map(lambda x: [int(i) for i in str(x)], numbers)), [])
    salary = ''
    numbers = list(map(lambda l: round(int(l) * 10 ** (-len(l)+1), len(l)), numbers))
    print(numbers)
    while len(numbers) > 0:
        big_n = max(numbers)
        salary += str(big_n)
        numbers.remove(big_n)
    return int(str(salary).replace('.',''))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
