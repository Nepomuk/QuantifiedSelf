#!/usr/bin/env bash

PY_WORDCOUNT="wordcountDB.py"

LAUNCHCTL_AGENTS="$HOME/Library/LaunchAgents"
LAUNCHCTL_PLIST="com.nepomuk.wordcount.plist"
LAUNCHCTL_LOGDIR="/tmp/com.nepomuk.quantifiedself"

# create the database
/usr/bin/python $PY_WORDCOUNT init
echo "Create database:      /usr/bin/python $PY_WORDCOUNT init"

# get the perl script
echo ""
echo "Get latexcount.pl:"
wget http://ctan.mackichan.com/support/latexcount/latexcount.pl

# insert the launch file into the proper folder
sed -e "s,\${PROG_PATH},$PWD," -e "s,\${LOG_PATH},$LAUNCHCTL_LOGDIR," $LAUNCHCTL_PLIST > $LAUNCHCTL_AGENTS/$LAUNCHCTL_PLIST
echo "Copy launch script and replace path."

# unfortunately, launchctl creates the logdir with the wrong
# permissions, so we have to take care about that
if [ ! -d $LAUNCHCTL_LOGDIR ]
then
    mkdir -m 700 $LAUNCHCTL_LOGDIR
    echo "Launchctl log path created."
fi

# load launch script during runtime
launchctl load $LAUNCHCTL_AGENTS/$LAUNCHCTL_PLIST
echo "Load launch script:   launchctl load $LAUNCHCTL_AGENTS/$LAUNCHCTL_PLIST"

echo "Installation finished."
