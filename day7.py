with open("input7.txt") as f:
    lines = [l.strip() for l in f.readlines()]


def part1(lines):
    variables = {}
    maxi = 2**16 - 1
    while len(variables) < 338:
        for line in lines:
            line = line.split(" ")
            if line[-1] not in variables:
                try:
                    if len(line) == 3:  # Initializing
                        variables[line[2]] = int(line[0])
                    elif len(line) == 4:  # Not operator
                        if line[1].isdigit():
                            variables[line[3]] = maxi - int(line[1])
                        else:
                            variables[line[3]] = maxi - variables[line[1]]
                    else:
                        var1 = int(line[0]) if line[0].isdigit(
                        ) else variables[line[0]]
                        var2 = int(line[2]) if line[2].isdigit(
                        ) else variables[line[2]]
                        if line[1] == "AND":
                            variables[line[-1]] = var1 & var2
                        elif line[1] == "OR":
                            variables[line[-1]] = var1 | var2
                        elif line[1] == "LSHIFT":
                            variables[line[-1]] = var1 << var2
                        elif line[1] == "RSHIFT":
                            variables[line[-1]] = var1 >> var2
                except:
                    continue
        print(len(variables))
    return variables


par1 = part1(lines)
print(par1["lx"])
