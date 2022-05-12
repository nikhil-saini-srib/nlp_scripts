#!/bin/bash

# Usage: find common files in two directories
# ./commonFiles.sh dir1 dir2
# ./commonFiles.sh en-IN_routers_mobile/utterances en-IN/routers/watch/utterances
src=$1
tgt=$2

if [ ! -d $src ]
then 
    echo "$src does not exist"
    exit
fi

if [ ! -d $tgt ]
then 
    echo "$tgt does not exist"
    exit
fi

# Find common capsules in both directories
# comm -12 <(ls en-IN_router_mobile/utterances/) <(ls en-IN/routers/watch/utterances/)
comm -12 <(ls $src) <(ls $tgt) > commonCapsules.txt

# create logs directory if it doesn't exist
[ -d logs ] || mkdir logs
timestamp=logs/$(date +%s).log
# Iterate over both capsules
while read fileName; do
    echo "$src/$fileName/context.any/queries.txt" >> $timestamp
    echo "$tgt/$fileName/context.any/queries.txt" >> $timestamp
    sh ./findunique.sh $src/$fileName/context.any/queries.txt $tgt/$fileName/context.any/queries.txt
done < commonCapsules.txt