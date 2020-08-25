import string
alpha = string.ascii_lowercase
nums = [i for i in range(len(alpha))]

conversion = dict(zip(alpha, nums))


def check_triples(password):
    for i in range(len(password) - 2):
        if conversion[
                password[i]] == conversion[password[i + 1]] - 1 and conversion[
                    password[i + 1]] == conversion[password[i + 2]] - 1:
            return True
    return False


def check_iol(password):
    if "i" in password or "l" in password or "o" in password:
        return False
    else:
        return True


def has_pairs(password):
    i = 0
    num_pairs = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            num_pairs += 1
            i += 2
        else:
            i += 1
    return num_pairs >= 2


#TEST
print("check triples test: " + str(check_triples("jklaawe")) + " " +
      str(check_triples("kloirt")))
print("check iol test: " + str(check_iol("jkaawe")) + " " +
      str(check_iol("kloirt")))
print("has_pairs_test: " + str(has_pairs("jklaawaa")) + " " +
      str(has_pairs("kloeeert")))


def increment(password):
    pos = len(password) - 1
    while password[pos] == "z":
        password = password[:pos] + "a" + password[pos + 1:]
        pos -= 1
    password = password[:pos] + alpha[conversion[password[pos]] +
                                      1] + password[pos + 1:]
    return password


# Test incrememt
print("Test increment: " + str(increment("xy") == "xz") + " " +
      str(increment("azzz") == "baaa"))

password = "vzbxxzaa"
while not (check_triples(password) and check_iol(password)
           and has_pairs(password)):
    password = increment(password)

print(password)