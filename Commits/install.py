#!/usr/bin/env python
import sqlite3 as sql
#from subprocess import call
import os
import argparse


# IMPORTANT! Change this value to your setup!
_commitScripts = '/Users/andre/Development/QuantifiedSelf/Commits/'

# configuration values, you probably don't have to change anything here
_gitHooksUserDir = '~/.git-hooks/'
_gitHooksUserPostCommitDir = 'post-commit/'
_updateDatabaseFile = 'updateDatabase'
_userBinDir = '/usr/local/bin/'


def createLocalDB(databaseName):
	dbConnection = sql.connect(databaseName)
	with dbConnection:
		dbCursor = dbConnection.cursor()
		dbCursor.execute("DROP TABLE IF EXISTS commits")
		dbCursor.execute("CREATE TABLE commits (hash TEXT PRIMARY KEY, date INT, message TEXT, additions INT, deletions INT, repo TEXT, pc TEXT)")
		return dbCursor


def importOldCommits():
	return True


#def installGitHooks(gitHooksPath):
	#TODO: change to call and catch error
	#os.system("git clone https://github.com/icefox/git-hooks.git {0}".format(gitHooksPath))
	#os.symlink(gitHooksPath+'git-hooks', _userBinDir)
	#gitHooksUserPath = os.path.expanduser(_gitHooksUserDir + _gitHooksUserPostCommitDir)
	#os.makedirs(gitHooksUserPath)
	#os.symlink(_commitScripts + _updateDatabaseFile, gitHooksUserPath)

	# make git hooks run on every future repository
	#os.system('git hooks --installglobal')

def parse():
	parser = argparse.ArgumentParser(description='Initilize the commit script by creating a database and installing needed requirements.')
	parser.add_argument('-db', '--database', default="gitCommits.db", help='Path to the local SQlite3 database file.')
		# parser.add_argument('--overwrite-db', action='store_true', help='')
	parser.add_argument('--skip-database', action='store_true', help='Skip creating a new database.')
	return parser.parse_args()


def importLocalCommits(localGitRepos):
	dbConnection = sql.connect(databaseName)
	with dbConnection:
		dbCursor = dbConnection.cursor()


if __name__ == "__main__":
	args = parse()
	gitHooksPath = '/usr/local/git-hooks/'

	if not args.skip_database:
		createLocalDB(args.database)
		importOldCommits()

	#installGitHooks(gitHooksPath)
	localGitRepos = getLocalGitRepos()
	importLocalCommits(localGitRepos)
