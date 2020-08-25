seq = "1113122113"


def process(seq):
    i = 0
    new_seq = ""
    while i < len(seq):
        tmp_char = seq[i]
        tmp_pos = i + 1
        if tmp_pos >= len(seq):
            new_seq += "1" + tmp_char
            return new_seq
        while seq[tmp_pos] == tmp_char:
            tmp_pos += 1
            if tmp_pos >= len(seq):
                new_seq += str(tmp_pos - i) + tmp_char
                return new_seq
        new_seq += str(tmp_pos - i) + tmp_char
        i = tmp_pos
    return new_seq


print(process("1") == "11")
print(process("12") == "1112")
print(process("11332") == "212312")

for i in range(50):
    print("itearation: " + str(i))
    print("tmp_len: " + str(len(seq)))
    print("")
    seq = process(seq)

print("len", len(seq))