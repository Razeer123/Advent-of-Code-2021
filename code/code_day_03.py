import numpy as np

with open('../data/input_day_03.txt', 'r') as file:
    file = file.read()
array = file.split('\n')


def first_task():
    ones = np.zeros(len(array[0]))
    zeroes = np.zeros(len(array[0]))

    for char_index in range(0, len(array[0])):
        ones[char_index] += sum([1 for word in array if int(word[char_index]) == 1])
        zeroes[char_index] += len(array) - ones[char_index]

    most_common_binary = ''
    least_common_binary = ''

    for common_index in range(0, len(ones)):
        most_common_binary += '1' if max(ones[common_index], zeroes[common_index]) == ones[common_index] else '0'
        least_common_binary += '1' if min(ones[common_index], zeroes[common_index]) == ones[common_index] else '0'
    return int(most_common_binary, 2) * int(least_common_binary, 2)


print(first_task())
