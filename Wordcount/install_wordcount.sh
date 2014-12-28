#!/usr/bin/env bash

PY_WORDCOUNT="wordcountDB.py"

LAUNCHCTL_AGENTS="$HOME/Library/LaunchAgents"
LAUNCHCTL_PLIST="com.nepomuk.wordcount.plist"

# create the database
/usr/bin/python $PY_WORDCOUNT init
echo "Create database:      /usr/bin/python $PY_WORDCOUNT init"

# get the perl script
echo ""
echo "Get latexcount.pl:"
wget http://ctan.mackichan.com/support/latexcount/latexcount.pl

# insert the launch file into the proper folder
sed -e "s,\${PROG_PATH},$PWD," $LAUNCHCTL_PLIST > $LAUNCHCTL_AGENTS/$LAUNCHCTL_PLIST
echo "Copy launch script and replace path."

# load launch script during runtime
launchctl load $LAUNCHCTL_AGENTS/$LAUNCHCTL_PLIST
echo "Load launch script:   launchctl load $LAUNCHCTL_AGENTS/$LAUNCHCTL_PLIST"

echo "Installation finished."
