with open("input5.txt") as f:
    lines = f.readlines()


def is_nice1(line):
    if num_of_vowels(line) < 3:
        return False
    double = False
    for i in range(len(line) - 1):
        if line[i] + line[i + 1] in ["xy", "ab", "cd", "pq"]:
            return False
        if line[i] == line[i + 1]:
            double = True
    return double


def num_of_vowels(line):
    vowels = set("aeiou")
    num = 0
    for letter in line:
        if letter in vowels:
            num += 1
    return num


def is_nice2(line):
    n1 = False
    n2 = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            n1 = True
        if find_repeat(line[i] + line[i + 1], i + 2, line):
            n2 = True
    return n1 and n2


def find_repeat(s, start, line):
    for i in range(start, len(line) - 1):
        if line[i] + line[i + 1] == s:
            return True
    return False


nice = 0
for l in lines:
    l = l.strip()
    if is_nice2(l):
        nice += 1

print("Number of nice strings: ", nice)