#!/bin/bash

# Usage:
# ./findcommon.sh file1 file2
# lowercase --> sort --> print first column
sed -e 's/.*/\L&/g' < $1 | awk -F"\t" 'BEGIN{OFS="\t";} { print $1 }' | sort > $1.out
sed -e 's/.*/\L&/g' < $2 | awk -F"\t" 'BEGIN{OFS="\t";} { print $1 }' | sort > $2.out
comm -12 $1.out $2.out > common
rm $1.out $2.out