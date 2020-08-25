import hashlib

trying = True
num = 0
while trying:
    num += 1
    str2hash = "iwrupvqb" + str(num)

    result = hashlib.md5(str2hash.encode())

    if result.hexdigest()[:6] == "000000":
        trying = False

print(num)