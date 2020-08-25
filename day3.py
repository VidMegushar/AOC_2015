with open("input3.txt") as f:
    directions = f.readline()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

cur_loc = [500, 500]
grid[cur_loc[0]][cur_loc[1]] = 1
for d in directions:
    if d == "^": cur_loc[1] += 1
    elif d == "<": cur_loc[0] -= 1
    elif d == ">": cur_loc[0] += 1
    elif d == "v": cur_loc[1] -= 1
    grid[cur_loc[0]][cur_loc[1]] = 1

presents = 0
for i in range(1000):
    presents += grid[i].count(1)

print("presents1", presents)


def part2(directions):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    grid[500][500] = 1
    robo = [500, 500]
    santa = [500, 500]
    for i in range(len(directions)):
        if i % 2 == 0:
            if directions[i] == "^": santa[1] += 1
            elif directions[i] == "<": santa[0] -= 1
            elif directions[i] == ">": santa[0] += 1
            elif directions[i] == "v": santa[1] -= 1
            grid[santa[0]][santa[1]] = 1
        else:
            if directions[i] == "^": robo[1] += 1
            elif directions[i] == "<": robo[0] -= 1
            elif directions[i] == ">": robo[0] += 1
            elif directions[i] == "v": robo[1] -= 1
            grid[robo[0]][robo[1]] = 1

    presents = 0
    for i in range(1000):
        presents += grid[i].count(1)

    print("presents2: ", presents)


part2(directions)
