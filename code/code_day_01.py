with open('../data/input_day_01.txt', 'r') as file:
    file = file.read()
array = file.split('\n')


def first_task():
    return sum([1 for i in range(1, len(array)) if int(array[i]) > int(array[i - 1])])


# We are ignoring middle numbers, because they are unneeded in the comparison
def second_task():
    return sum([1 for i in range(3, len(array)) if int(array[i]) > int(array[i - 3])])


print(first_task())
print(second_task())
