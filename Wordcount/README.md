# Wordcount

This script counts the words in all the files given in the `file.list` and puts it into a SQLite3 database. So far it just inserts entries to a local database. Analysing this data is a todo for sometime later.


## Installation

The easiest way is to run the install script:

    ./install_wordcount.sh

It basically contains three steps:

  1. Create local SQLite3 database.

        ./wordcountDB.py init

  2. Get the perl script from [this site](http://ctan.mackichan.com/support/latexcount/latexcount.pl):

        wget http://ctan.mackichan.com/support/latexcount/latexcount.pl

  3. Install a launch script to automatically run the wordcount script.

        sed -e "s,\${PROG_PATH},$PWD," com.nepomuk.wordcount.plist > $HOME/Library/LaunchAgents/com.nepomuk.wordcount.plist
        launchctl load $HOME/Library/LaunchAgents/com.nepomuk.wordcount.plist

The last step only works on OS X, so if you are using Linux use an entry in your crontab to call `wordcount.sh` instead.


### File List

Copy the sample file list:

    cp file.list.sample file.list

The file contains the list of files which should be checked (one per line) and needs to be adapted to your local setup. You may also use the wildcard * for selecting a bunch of files.


## Functional Description

### Database

The database holds entries with four values:

    timestamp <int>, wc_count <int>, perl_count <int>, tex_count <int>

Every time the script is executed, all of those values will be filled in. In case a counting script fails, the default value '-1' will be inserted.


## Known Issues

  * The used document class might cause problems with texcount (sometimes it cannot find the used class).

    Workaround: exclude the file which contains the document class command.

