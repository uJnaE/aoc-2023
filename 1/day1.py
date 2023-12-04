import re


def get_val(input: str):
    left = None
    right = None
    pattern = re.compile(
        "(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))"
    )
    match = re.findall(pattern, input)
    num = [match[0], match[-1]]

    for i in range(2):
        if not num[i].isnumeric():
            match num[i]:
                case "one":
                    num[i] = "1"
                case "two":
                    num[i] = "2"
                case "three":
                    num[i] = "3"
                case "four":
                    num[i] = "4"
                case "five":
                    num[i] = "5"
                case "six":
                    num[i] = "6"
                case "seven":
                    num[i] = "7"
                case "eight":
                    num[i] = "8"
                case "nine":
                    num[i] = "9"
    # print(num)
    return "".join(num)


file = open("day1_input.txt", "r")
input = file.read()
file.close()

input = input.splitlines()
sum = 0
for string in input:
    sum += int(get_val(string))

print(sum)
