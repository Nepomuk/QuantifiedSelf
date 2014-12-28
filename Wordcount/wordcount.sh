#!/bin/bash

# get the files to scan
INPUT_FILE="file.list"
FILES=$(tr '\n' ' ' < $INPUT_FILE)

# count with wordcount
WC_BIN="/usr/bin/wc"
WC_COUNT=-1
if [ -e $WC_BIN ]
then
    WC_COUNT=$($WC_BIN -w $FILES | grep 'total' | awk '{count = $1} END{print count}')
    # echo "WordCount: $WC_COUNT"
fi

# count with perl script
PC_BIN="wordcount.pl"
PC_COUNT=-1
if [ -e $PC_BIN ]
then
    PC_COUNT=$(perl $PC_BIN $FILES | grep 'total' | awk '{count = $1} END{print count}')
    # echo "PerlCount: $PC_COUNT"
fi

# count with texcount
TC_BIN="/usr/texbin/texcount"
TC_COUNT=-1
if [ -e $TC_BIN ]
then
    TC_COUNT=$($TC_BIN -quiet -brief -total -sum $FILES)
    # echo "TexCount:  $TC_COUNT"
fi

# call the python script to insert values into the database
PY_INSERT_SCRIPT="wordcountDB.py"
/usr/bin/python $PY_INSERT_SCRIPT -ac $WC_COUNT $PC_COUNT $TC_COUNT insert
