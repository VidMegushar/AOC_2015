import json

with open("input12.json") as f:
    data = json.load(f)


def check_for_numbers(son):
    tmp_score = 0
    if type(son) == dict:
        for key in son:
            if son[key] == "red":
                return 0
            elif type(son[key]) == dict:
                tmp_score += check_for_numbers(son[key])
            elif type(son[key]) == int:
                tmp_score += son[key]
            elif type(son[key]) == list:
                tmp_score += check_for_numbers(son[key])
    elif type(son) == list:
        for elt in son:
            if type(elt) == int:
                tmp_score += elt
            elif type(elt) == list:
                tmp_score += check_for_numbers(elt)
            elif type(elt) == dict:
                tmp_score += check_for_numbers(elt)
    return tmp_score

print(check_for_numbers(data))


"""
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
"""