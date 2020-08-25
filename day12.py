with open("input12.txt") as f:
    json = f.readline().strip()

final_sum = 0
neg = False
tmp_num = ""
for i in range(len(json) - 1):
    if json[i] == "-" and json[i + 1].isdigit():
        neg = True
    elif json[i].isdigit():
        tmp_num += json[i]
        if not (json[i + 1].isdigit()):
            if neg: final_sum -= int(tmp_num)
            else: final_sum += int(tmp_num)
            tmp_num = ""
            neg = False

print(final_sum)
