#!/bin/bash

# Usage: find lines which are present only in file1 and not in file2 == file1 - (file1 intersection file2)
# ./findunique.sh file1 file2
# lowercase --> sort --> print first column
sed -e 's/.*/\L&/g' < $1 | awk -F"\t" 'BEGIN{OFS="\t";} { print $1 }' | sort > $1.out
sed -e 's/.*/\L&/g' < $2 | awk -F"\t" 'BEGIN{OFS="\t";} { print $1 }' | sort > $2.out
comm -23 $1.out $2.out > only1.txt
# remove irrelavant lines from only1.txt
sed -i '/^\/\//d' only1.txt
# remove empty lines from only1.txt
sed -ri '/^\s*$/d' only1.txt
# insert in $2
echo '\n' >>  $2
echo "//migration: adding data from mobile to watch for acc data augmentation" >> $2
cat only1.txt | uniq >> $2
# remove empty lines from $2
sed -ri '/^\s*$/d' $2
# cleanup
rm $1.out $2.out