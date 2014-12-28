# Wordcount

This script counts the words in all the files given in the `file.list` and puts it into a SQLite3 database. So far it just inserts entries to a local database. Analysing this data is a todo for sometime later.


## Installation

The easiest way is to run the install script:

    ./install_wordcount.sh

It basically contains two steps:

  1. Create local SQLite3 database.

        ./wordcountDB.py init

  2. Install a launch script to automatically run the wordcount script.

        sed -e "s,\${PROG_PATH},$PWD," com.nepomuk.wordcount.plist > $HOME/Library/LaunchAgents/com.nepomuk.wordcount.plist
        launchctl load $HOME/Library/LaunchAgents/com.nepomuk.wordcount.plist

The second step only works on OS X, so if you are using Linux use an entry in your crontab to call `wordcount.sh` instead.


## Functional Description

### Database

The database holds entries with four values:

    timestamp <int>, wc_count <int>, perl_count <int>, tex_count <int>

Every time the script is executed, all of those values will be filled in. In case a counting script fails, the default value '-1' will be inserted.


### File List

The file `file.list` contains the list of files which should be checked. You may also use the wildcard * for selecting a bunch of files.
