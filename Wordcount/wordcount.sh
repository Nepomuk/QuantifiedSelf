#!/bin/bash

# get the files to scan
INPUT_FILE="file.list"
FILES=$(tr '\n' ' ' < $INPUT_FILE)

# count with wordcount
WC_BIN="/usr/bin/wc"
if [ -e $WC_BIN ]
then
    WC_COUNT=$($WC_BIN -w $FILES | grep 'total' | awk '{count = $1} END{print count}')
    echo "WordCount: $WC_COUNT"
fi

# count with perl script
PC_BIN="wordcount.pl"
if [ -e $PC_BIN ]
then
    PC_COUNT=$(perl $PC_BIN $FILES | grep 'total' | awk '{count = $1} END{print count}')
    echo "PerlCount: $PC_COUNT"
fi

# count with texcount
TC_BIN="/usr/texbin/texcount"
if [ -e $TC_BIN ]
then
    TC_COUNT=$($TC_BIN -quiet -brief -total -sum $FILES)
    echo "TexCount:  $TC_COUNT"
fi
