import fileinput

lens = {}

filePath = 'words.txt'

with fileinput.input(files=(filePath)) as f:
    for line in f:
        #if (len(line)) == 1:
        i = len(line)
        if i in lens.keys():
            lens[i] += 1;
        else:
            lens[i] = 1


for t in lens.items():
    print(t)