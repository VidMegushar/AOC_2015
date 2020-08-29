starting_molecule = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
#starting_molecule = "HOHOHO"

with open("input19.txt") as f:
    data = f.readlines()

transformations = dict()
for line in data:
    transf = line.strip().split(" ")
    org = transf[0]
    transformed = transf[2]
    if org not in transformations:
        transformations[org] = []
    transformations[org].append(transformed)


all_trans_molecules = []

for word in transformations:
    l = len(word)
    for i in range(len(starting_molecule) - l + 1):
        if starting_molecule[i:i+l] == word:
            for new_word in transformations[word]:
                all_trans_molecules.append(starting_molecule[:i] + new_word + starting_molecule[i+l:])

#print(transformations)
#print(all_trans_molecules)
print(len(set(all_trans_molecules)))