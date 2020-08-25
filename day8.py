def get_real_len(line):
    i = 0
    new_len = 0
    while i < len(line) - 1:
        tmp_char = line[i]
        next_char = line[i + 1]
        if tmp_char == "\\":
            if next_char == "x":
                i += 4
            else:
                i += 2
        else:
            i += 1
        new_len += 1
    return new_len - 1


def get_long_len(line):
    length = 0
    for char in line:
        if char in ["\"", "\\"]:
            length += 2
        else:
            length += 1
    return length + 2


with open("input8.txt", "r") as f:
    lines = f.readlines()
    answer = 0
    for line in lines:
        line = line.strip()
        #print(line, get_long_len(line))
        answer += get_long_len(line) - len(line)
    print(answer)
