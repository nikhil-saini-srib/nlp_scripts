'''
python3 removeDuplicates.py file1
if file1 == queries.txt :
    set "upto"  = 1 (in convert function)
else if file1 == mobile.tsv or watch.tsv :
    set "upto" = 1,2,3 based on requirement.
file2 : abc.txt (contains utterances which should be deleted from queries.txt)

Usecase : When some utterances are supported by a new capsule (A) which were earlier supported by capsule (B), then we remove them from (B)
'''

import sys 
infilename = sys.argv[1]
outfilename = sys.argv[1]+'-out'
lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")

def convert(line, upto):
    '''
        line : tab separated line
        upto : the number of columns upto which you want to match
        return type : concatenated string
    '''
    nl = line.split('\t')
    nl_str = ""
    for i in range(0, upto):
        nl_str += nl[i]
    return nl_str 

count = 0
upto = 1 # sys.argv[2] # 1, 2, 3

for line in open(infilename, "r"):
    nl = convert(line, upto)
    #print(nl)
    if nl.lower() not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(nl.lower())
    else:
        count += 1
        # print(lines_seen)
        print(nl)
        # a = raw_input()
outfile.close()        
print("Total Lines with Dups : ", count)
print("Output (without duplicates) in in file : ", outfilename)