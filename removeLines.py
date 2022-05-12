'''
python3 removeLines.py file1 file2
file1 : queries.txt 
file2 : abc.txt (contains utterances which should be deleted from queries.txt)

Usecase : When some utterances are supported by a new capsule (A) which were earlier supported by capsule (B), then we remove them from (B)
'''

import sys
import os 

mainFileName = sys.argv[1]
propFileName = sys.argv[2]

propData = open(propFileName, 'r').readlines()
mainData = open(mainFileName, 'r').readlines()

set_prop = {propData[0]}
for line in propData:
    set_prop.add(line.lower().replace('.', ' ').replace('?', ' '))

with open(mainFileName+'-out', 'w') as f:
    for line in mainData:
        if line.lower().replace('.', ' ').replace('?', ' ') not in set_prop:
            f.write(line)
        else:
            print(line)