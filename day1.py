with open("input1.txt") as f:
    house = f.readline().strip()


def count_floors(house):
    return house.count("(") - house.count(")")


def enter_basement(house):
    tmp_floor = 0
    cur_step = 0
    for fl in house:
        cur_step += 1
        if fl == "(": tmp_floor += 1
        else: tmp_floor -= 1

        if tmp_floor == -1: return cur_step


print(count_floors(house))
print(enter_basement(house))