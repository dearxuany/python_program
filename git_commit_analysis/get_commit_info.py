#! /usr/bin/python3

import os
from datetime import datetime, date, timedelta


def get_author_list(destCodeDir):
    startDate=(date.today() - timedelta(days=7)).strftime("%m-%d-%Y")
    endDate=date.today().strftime("%m-%d-%Y")
    authorStr=os.popen('cd {} && git log --after=\'{}\' --format=\'%aN\'|sort -u'.format(destCodeDir,startDate)).read()
    authorList=authorStr.split()
    return authorList


def get_author_info(destCodeDir,authorName):
    startDate=(date.today() - timedelta(days=7)).strftime("%m-%d-%Y")
    endDate=date.today().strftime("%m-%d-%Y")

    author={}
    author["name"]=authorName

    getCommit="cd {} && git log --author={} --after=\'{}\' --no-merges | grep -e \'commit [a-zA-Z0-9]*\' | wc -l".format(destCodeDir,authorName,startDate)
    commit=os.popen(getCommit).read()[:-1]
    if commit == "":
        commit=0
    else:
        commit=int(commit)
    author["commit"]=commit

    getAdd="cd {} && git log --author={} --pretty=tformat: --numstat --after={}".format(destCodeDir,authorName,startDate)+"| awk '{add += $1};END {print add}'"
    add=os.popen(getAdd).read()
    if add == "":
        add=0
    else:
        add=int(add)
    author["addLine"]=add

    getRemove="cd {} && git log --author={} --pretty=tformat: --numstat --after={}".format(destCodeDir,authorName,startDate)+"| awk '{remove += $2};END {print remove}'"
    remove=os.popen(getRemove).read()
    if remove == "":
       remove=0
    else:
       remove=int(remove)
    author["removeLine"]=remove

    sub=add-remove
    author["subLine"]=sub
    return dict(startDate=startDate,endDate=endDate,author=author)


if __name__ == "__main__":
    destCodeDir="/sdata/gitlab-code/git/gitAnalysis/destCode/ansible-server"
    print(get_author_list(destCodeDir))
