from itertools import permutations


def get_distance(perm, distances):
    total_dist = 0
    for i in range(len(perm) - 1):
        c1 = perm[i]
        c2 = perm[i + 1]
        total_dist += distances[c1][c2]
    return total_dist


with open("input9.txt") as f:
    lines = f.readlines()

distances = {}
for line in lines:
    first_city, _, second_city, _, distance = line.strip().split(" ")
    if first_city not in distances:
        distances[first_city] = {}
    if second_city not in distances:
        distances[second_city] = {}
    distances[first_city][second_city] = int(distance)
    distances[second_city][first_city] = int(distance)

all_permutations = list(permutations(distances.keys()))

lowest_distance = 0
for perm in all_permutations:
    tmp_dist = get_distance(perm, distances)
    if tmp_dist > lowest_distance:
        lowest_distance = tmp_dist
print(lowest_distance)
