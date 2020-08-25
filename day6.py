with open("input6.txt") as f:
    instructions = f.readlines()


def part1(instructions):
    lights_grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for inst in instructions:
        inst = inst.strip().split(" ")
        if inst[0] == "toggle":
            x1, y1 = [int(i) for i in inst[1].split(",")]
            x2, y2 = [int(i) for i in inst[-1].split(",")]
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    lights_grid[y][x] = 1 - lights_grid[y][x]
        elif inst[1] == "on":
            x1, y1 = [int(i) for i in inst[2].split(",")]
            x2, y2 = [int(i) for i in inst[-1].split(",")]
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    lights_grid[y][x] = 1
        else:
            x1, y1 = [int(i) for i in inst[2].split(",")]
            x2, y2 = [int(i) for i in inst[-1].split(",")]
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    lights_grid[y][x] = 0

    lights = 0
    for i in range(1000):
        lights += lights_grid[i].count(1)
    return lights


def part2(instructions):
    lights_grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for inst in instructions:
        inst = inst.strip().split(" ")
        if inst[0] == "toggle":
            x1, y1 = [int(i) for i in inst[1].split(",")]
            x2, y2 = [int(i) for i in inst[-1].split(",")]
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    lights_grid[y][x] += 2
        elif inst[1] == "on":
            x1, y1 = [int(i) for i in inst[2].split(",")]
            x2, y2 = [int(i) for i in inst[-1].split(",")]
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    lights_grid[y][x] += 1
        else:
            x1, y1 = [int(i) for i in inst[2].split(",")]
            x2, y2 = [int(i) for i in inst[-1].split(",")]
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    if lights_grid[y][x] > 0:
                        lights_grid[y][x] -= 1

    lights = 0
    for i in range(1000):
        lights += sum(lights_grid[i])
    return lights


print(part2(instructions))
