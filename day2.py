presents = []

with open("input2.txt") as f:
    pr = f.readlines()

for line in pr:
    p = [int(i) for i in line.strip().split("x")]
    p.sort()
    presents.append(p)

area = 0
for p in presents:
    area += 2 * (p[0] * p[1] + p[1] * p[2] + p[0] * p[2]) + p[0] * p[1]

print("area:", area)

ribbon = 0
for p in presents:
    ribbon += 2 * (p[0] + p[1]) + p[0] * p[1] * p[2]

print("ribbon: ", ribbon)
