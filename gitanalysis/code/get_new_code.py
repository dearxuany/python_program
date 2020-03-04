#! /usr/bin/python3

import os

def get_new_code(projectDir):
    os.system("cd {} && git pull origin master".format(projectDir))

def get_new_repository(projectDir,gitHttps):
    gitSSH="git@git.woniubaoxian.com:"+"/".join(gitHttps.split("/")[3:])+".git"
    os.system("cd {} && git clone {}".format(projectDir,gitSSH))

if __name__ == "__main__":
    projectDir="/sdata/gitlab-code/git/gitAnalysis/destCode/ansible-server"
    get_new_code(projectDir)
