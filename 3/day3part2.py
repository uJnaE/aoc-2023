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


part_num_list = list()
for line in range(lines):
    start = end = None
    part_num_list_line = list()
    for col in range(cols):
        if input[line][col].isnumeric():
            if start == None:
                start = col
            end = col
        else:
            if start != None and is_part_num(start, end, line):
                part_num_list_line.append((start, end))
            start = end = None
    if start != None and is_part_num(start, end, line):
        part_num_list_line.append((start, end))
    part_num_list.append(part_num_list_line)


def is_gear(line, col):
    # print(part_num_list)
    near_part_nums = list()
    start_col = col
    end_col = col
    if col - 1 >= 0:
        start_col = col - 1
        for part_nums in part_num_list[line]:
            # print(part_nums, start_col)
            if start_col == part_nums[1]:
                near_part_nums.append(int(input[line][part_nums[0] : part_nums[1] + 1]))

    if col + 1 <= cols:
        end_col = col + 1
        for part_nums in part_num_list[line]:
            if end_col == part_nums[0]:
                near_part_nums.append(int(input[line][part_nums[0] : part_nums[1] + 1]))

    if line - 1 >= 0:
        for part_nums in part_num_list[line - 1]:
            # print(part_nums, start_col, end_col)
            if start_col <= part_nums[1] and end_col >= part_nums[0]:
                near_part_nums.append(
                    int(input[line - 1][part_nums[0] : part_nums[1] + 1])
                )

    if line + 1 >= 0:
        for part_nums in part_num_list[line + 1]:
            # print(part_nums, start_col, end_col)
            if start_col <= part_nums[1] and end_col >= part_nums[0]:
                near_part_nums.append(
                    int(input[line + 1][part_nums[0] : part_nums[1] + 1])
                )
    # print(near_part_nums)
    if len(near_part_nums) == 2:
        return near_part_nums
    return False


total_gr = 0
for line in range(lines):
    for col in range(cols):
        if input[line][col] == "*":
            part_nums = is_gear(line, col)
            if part_nums:
                total_gr += part_nums[0] * part_nums[1]

print(total_gr)
