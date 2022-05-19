import sys, os, random 
import string 
import pandas as pd
import numpy as np 

locale = 'en-IN'
device = 'mobile'
capsule = ''
context = 'context.any'

tc_dir = '22E'

addAccData = True
downsample = True 
randomDownsample = True 

test_cases = 'tc.tsv'
acc_data_dir = ''
eval_dir = ''

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def set_data_dir():
    global acc_data_dir
    assert capsule != '' and (context == 'context.any' or context == 'context.self' or context == 'context.none') 
    assert (locale == 'en-IN' or locale == 'en-GB')
    assert (device == 'mobile' or device == 'watch')
    acc_data_dir = '../' + locale + '/routers/' + device + '/utterances/' + capsule + "/" + context + '/queries.txt'

def set_eval_dir():
    global eval_dir
    assert (device == 'mobile' or device == 'watch')
    assert (tc_dir != '')
    tc_filename = device + '.tsv'
    eval_dir = '../' + locale + '/evaluations/' + tc_dir + '/' + tc_filename

def removeDuplicates(filename):
    os.system("python3 removeDuplicates.py " + filename + " 1")
    os.system("rm " + filename) 
    os.system("mv " + filename + "-out " + filename)
    print("removed duplicates from the file: ", filename)

def findConflictingTC():
    pass 

def handleConflicts():
    pass

def mergeTC():
    pass 

def appendTC():
    cmd = input("Enter 'y' or 'Y' if you want to add TC to evaluation file, else we will skip it.")
    if (!(cmd == 'y' or cmd == 'Y' or cmd == 'Yes'))
        print("TC addition to evaluation file - SKIPPED")
        return
    set_eval_dir()
    data = pd.read_csv(test_cases, sep = '\t')
    data.to_csv(eval_dir, index=False, encoding='utf-8', sep='\t', header=False, mode='a')
    print("TC addition to evaluation file - COMPLETED")
    print("Warning 1: Kindly check the first appended line, a new line should be inserted before it, feature yet to be completed.")

def solve():
    global capsule
    data = pd.read_csv(test_cases, sep = '\t')
    ds = data.sort_values('Comment')
    print(ds.head)
    labels = pd.unique(ds['Label'])
    for l in labels: 
        capsule = l
        rows = ds[ds['Label'] == l]
        issueIds = pd.unique(rows['Comment'])
        # print("Label: ", l)
        # print("-"*50)
        for issue in issueIds:
            utts = rows[rows['Comment'] == issue]['Utterance']
            set_data_dir()
            with open(acc_data_dir, 'a') as f:
                data_to_write = "\n//" + issue + "\n" + "\n".join(utts.values.tolist())
                f.write(data_to_write)
            # print("Issue Id: ", issue)
            # print("Data:", utts)
            # print("."*20)
        # removeDuplicates(acc_data_dir)
    '''
    capsule 1 : [u1, u2, ...., un]
    capsule 2 : [u1, u2, ...., un]
    .
    .
    capsule n : [u1, u2, ...., un]
    ''' 

def alert():
    print("You are going to change the routers data in: {}".format(locale+"/"+device))
    print("To continue, enter Y or y or yes:")
    access = input()
    if (not (access == 'y' or access == 'yes' or access == 'Y')):
        exit()
                                                                                                                                                                                                           

if __name__ == "__main__" :
    
    alert()

    # id = id_generator()
    # os.mkdir(id)
    
    # remove duplicates from tc.tsv
    # removeDuplicates()
    
    # find conflicting tc in the same set.
    findConflictingTC()
    
    # merge same tc of different comments
    mergeTC()
    # handle conflicts in tc.tsv 
    handleConflicts()
    
    # add TC to TC file. 
    appendTC()

    # readData
    # solve()
  

