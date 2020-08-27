data = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]
test = [20, 15, 10, 5, 5]

def try_containers(litres, containers):
    good_combinations = 0
    for i in range(len(containers)):
        if litres + containers[i] == 150:
            good_combinations += 1
        elif litres + containers[i] < 150:
            good_combinations += try_containers(litres + containers[i], containers[i+1:])
    return good_combinations

gc_list = []
def get_min_num_containers(used_conts, containers):
    good_combinations = 0
    for i in range(len(containers)):
        if sum(used_conts) + containers[i] == 150:
            if len(used_conts) == 3:
                good_combinations += 1
            gc_list.append(used_conts + [containers[i]])
        elif sum(used_conts) + containers[i] < 150:
            good_combinations += get_min_num_containers(used_conts + [containers[i]], containers[i+1:])
    return good_combinations

print(get_min_num_containers([],data))
print(min([len(l) for l in gc_list]))
