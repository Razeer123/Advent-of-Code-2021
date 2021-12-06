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


def second_task():
    oxygen_numbers = array
    co2_numbers = array

    for index in range(0, len(array[0])):
        if len(oxygen_numbers) == 1:
            break
        oxygen_numbers = find_common_index_in_row(oxygen_numbers, index)

    for index in range(0, len(array[0])):
        if len(co2_numbers) == 1:
            break
        co2_numbers = find_common_index_in_row(co2_numbers, index, True)

    return int(oxygen_numbers[0], 2) * int(co2_numbers[0], 2)


def find_common_index_in_row(values, row_index, is_min=False):
    ones = sum([1 for word in values if int(word[row_index]) == 1])
    zeroes = sum([1 for word in values if int(word[row_index]) == 0])
    new_values = []

    if is_min:
        if ones < zeroes:
            for value in values:
                if value[row_index] == '1':
                    new_values.append(value)
        elif zeroes < ones:
            for value in values:
                if value[row_index] == '0':
                    new_values.append(value)
        else:
            for value in values:
                if value[row_index] == '0':
                    new_values.append(value)
    else:
        if ones > zeroes:
            for value in values:
                if value[row_index] == '1':
                    new_values.append(value)
        elif zeroes > ones:
            for value in values:
                if value[row_index] == '0':
                    new_values.append(value)
        else:
            for value in values:
                if value[row_index] == '1':
                    new_values.append(value)

    return new_values


print(first_task())
print(second_task())
