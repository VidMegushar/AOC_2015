with open("input18.txt") as f:
    data = [""]
    for line in f:
        data.append(list("." + line.strip() + "."))
    data[0] = list("."*len(data[1]))
    data.append(list("."*len(data[1])))
    data[1][1] = "#"
    data[1][-2] = "#"
    data[-2][1] = "#"
    data[-2][-2] = "#"
def get_lights_on(lights, row_n, light_n):
    lights_on = 0
    directions = [(1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0)]
    for d in directions:
        if lights[row_n + d[1]][light_n + d[0]] == "#":
            lights_on += 1
    return lights_on

# Test
test1 = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
test2 = [
    ["#", "#", "#"],
    ["#", "#", "#"],
    ["#", "#", "#"]
]
test3 = [
    ["#", "#", "."],
    ["#", "#", "."],
    ["#", "#", "."]
]
print("Test1:")
print(get_lights_on(test1,1,1) == 0)
print(get_lights_on(test2,1,1) == 8)
print(get_lights_on(test3,1,1) == 5)

num_of_iterations = 100

data_new = [d.copy() for d in data]
for _ in range(num_of_iterations):
    for row_n in range(1,len(data)-1):
        for light_n in range(1,len(data[0])-1):
            lights_on = get_lights_on(data, row_n, light_n)
            if data[row_n][light_n] == "#":
                if lights_on not in [2,3]:
                    data_new[row_n][light_n] = "."
            elif data[row_n][light_n] == ".":
                if lights_on == 3:
                    data_new[row_n][light_n] = "#"
    data_new[1][1] = "#"
    data_new[1][-2] = "#"
    data_new[-2][1] = "#"
    data_new[-2][-2] = "#"
    data = [d.copy() for d in data_new]

final_data = sum([light == "#" for row in data for light in row])
print("num of lights = " + str(final_data))

