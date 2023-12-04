file = open("4/input.txt", "r")
input = file.readlines()
file.close()

sum = 0
for line in input:
    cards = line.split(":")[1]
    winning, owned = tuple(cards.split("|"))
    winning = winning.strip().split()
    owned = owned.strip().split()

    point = 0
    for card in owned:
        if card in winning:
            if point:
                point *= 2
            else:
                point = 1

    sum += point
print(sum)
