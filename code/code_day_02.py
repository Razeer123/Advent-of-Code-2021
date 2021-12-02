with open('../data/input_day_02.txt', 'r') as file:
    file = file.read()
array = file.split('\n')


def first_task():
    horizontal = 0
    depth = 0

    for command in array:
        if 'forward' in command:
            horizontal += int(command[-1])
        elif 'down' in command:
            depth += int(command[-1])
        elif 'up' in command:
            depth -= int(command[-1])

    return horizontal * depth


def second_task():
    horizontal = 0
    depth = 0
    aim = 0

    for command in array:
        if 'forward' in command:
            horizontal += int(command[-1])
            depth += aim * int(command[-1])
        elif 'down' in command:
            aim += int(command[-1])
        elif 'up' in command:
            aim -= int(command[-1])

    return horizontal * depth


print(first_task())
print(second_task())
