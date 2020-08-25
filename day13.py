from itertools import permutations

with open("input13.txt") as f:
    data = f.readlines()


happiness_dict = dict()

for row in data:
    row = row.strip().split(" ")
    p1 = row[0]
    p2 = row[-1]
    amount = int(row[3])
    lose = row[2] == "lose"
    if lose:
        amount = -amount
    if p1 not in happiness_dict:
        happiness_dict[p1] = dict()
    happiness_dict[p1][p2[:-1]] = amount

all_guests = happiness_dict.keys()
all_guests_perm = list(permutations(all_guests))

max_happiness = 0
best_p = None

guests = ['Alice', 'Eric', 'Bob', 'Carol', 'David', 'George', 'Mallory', 'Frank']

all_guests_perm = []
for i in range(len(guests)):
    all_guests_perm.append(guests[:i] + ["Vid"] + guests[i:])
all_guests_perm.append(guests + ["Vid"])

print(all_guests_perm)

for p in all_guests_perm:
    tmp_happiness = 0 
    for i in range(len(p)-1,-1,-1):
        p1 = p[i]
        p2 = p[i-1]
        if p1 == "Vid" or p2 == "Vid":
            tmp_happiness += 0
        else:
            tmp_happiness += happiness_dict[p[i]][p[i-1]]
            tmp_happiness += happiness_dict[p[i-1]][p[i]]
    if tmp_happiness > max_happiness:
        max_happiness = tmp_happiness
        best_p = p

print(max_happiness)
print(best_p)

