file = open("4/input.txt", "r")
input = file.readlines()
file.close()

num_cards = len(input) * [1]
for i, line in enumerate(input):
    cards = line.split(":")[1]
    winning, owned = tuple(cards.split("|"))
    winning = winning.strip().split()
    owned = owned.strip().split()

    point = 0
    for card in owned:
        if card in winning:
            point += 1
            num_cards[point + i] += num_cards[i]

print(sum(num_cards))
