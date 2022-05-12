import random 
import sys
# seed and probability of sampling
seed = 13
p = 0.3

random.seed(13)

try:
    infile = sys.argv[1]
except:
    print("Usage: python downsample.py filename.txt")
    print("Program exited without executing")
    exit()

outfile = infile+'-'+str(seed)+'-'+str(p)+'-out'

indata = open(infile, 'r').readlines()

outCount = p * float(len(indata))
outdata = random.sample(indata, int(outCount))


print("Number of input samples : ", len(indata))
print("Number of output samples : ", len(outdata))
print("Output file : ", outfile)

with open(outfile, 'w') as f:
    for line in outdata:
        f.write(line)

