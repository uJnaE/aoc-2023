file = open("2/puzzle.txt", "r")
input = file.readlines()
file.close()

# inv = {"red": 12, "green": 13, "blue": 14}

sum = 0
for i in range(len(input)):
    draws = input[i].split(":")[1].strip()
    power = {"red": 0, "green": 0, "blue": 0}
    for draw in draws.split(";"):
        cubes = draw.strip().split(",")
        for cube in cubes:
            values = cube.split()
            if int(values[0]) > power[values[1]]:
                power[values[1]] = int(values[0])
    sum += power["red"] * power["green"] * power["blue"]

print(sum)
