file = open("3/input.txt", "r")
input = file.readlines()
file.close()

cols = len(input[0]) - 1
lines = len(input)


def is_part_num(start_col, end_col, line_num):
    if start_col - 1 >= 0:
        start_col = start_col - 1
        if not (
            input[line_num][start_col].isnumeric() or input[line_num][start_col] == "."
        ):
            return True
    if end_col + 1 < cols:
        end_col = end_col + 1
        if not (
            input[line_num][end_col].isnumeric() or input[line_num][end_col] == "."
        ):
            return True
    if line_num - 1 >= 0:
        for i in range(start_col, end_col + 1):
            if not (
                input[line_num - 1][i].isnumeric() or input[line_num - 1][i] == "."
            ):
                return True
    if line_num + 1 < lines:
        for i in range(start_col, end_col + 1):
            if not (
                input[line_num + 1][i].isnumeric() or input[line_num + 1][i] == "."
            ):
                return True
    return False


sum = 0
for line in range(lines):
    start = end = None
    for col in range(cols):
        if input[line][col].isnumeric():
            if start == None:
                start = col
            end = col
        else:
            if start != None and is_part_num(start, end, line):
                sum += int(input[line][start : end + 1])
            start = end = None
    if start != None and is_part_num(start, end, line):
        sum += int(input[line][start : end + 1])

print(sum)
