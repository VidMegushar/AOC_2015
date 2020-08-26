import string

translator = str.maketrans('', '', string.punctuation)

with open("input16.txt") as f:
    data = f.readlines()

real_aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

for aunt in data:
    aunt = aunt.strip().split(" ")
    she_is_the_one = True
    for i in range(2,len(aunt), 2):
        item = aunt[i].translate(translator)
        num = int(aunt[i+1].translate(translator))
        if item in ["cats", "trees"]:
            if real_aunt[item] >= num:
                she_is_the_one = False
        elif item in ["pomeranians", "goldfish"]:
            if real_aunt[item] <= num:
                she_is_the_one = False
        elif real_aunt[item] != num:
            she_is_the_one = False
    if she_is_the_one:
        print(aunt)
        break

