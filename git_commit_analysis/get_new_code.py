#! /usr/bin/python3

import os

def get_new_code(projectDir):
    os.system("cd {} && git pull origin master".format(projectDir))

if __name__ == "__main__":
    projectDir="/sdata/gitlab-code/git/gitAnalysis/destCode/ansible-server"
    get_new_code(projectDir)
