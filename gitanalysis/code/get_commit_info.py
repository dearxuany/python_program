#! /usr/bin/python3

import os

def get_author_list(timeDict,destCodeDir):
    authorStr=os.popen('cd {} && git log --after=\'{}\' --before=\'{}\'  --format=\'%aN\'|sort -u'.format(destCodeDir,timeDict["startTime"],timeDict["endTime"])).read()
    authorList=authorStr.split()
    return authorList


def get_author_info(timeDict,destCodeDir,authorName):

    author={}
    author["name"]=authorName

    getCommit="cd {} && git log --author={} --after=\'{}\' --before=\'{}\' --no-merges | grep -e \'commit [a-zA-Z0-9]*\'| grep -v \'(*)\' | wc -l".format(destCodeDir,authorName,timeDict["startTime"],timeDict["endTime"])
    commit=os.popen(getCommit).read()[:-1]
    if commit == "":
        commit=0
    else:
        commit=int(commit)
    author["commit"]=commit

    getAdd="cd {} && git log --author={} --pretty=tformat: --numstat --after=\'{}\' --before=\'{}\'".format(destCodeDir,authorName,timeDict["startTime"],timeDict["endTime"])+"| awk '{add += $1};END {print add}'"
    add=os.popen(getAdd).read()
    if add == "":
        add=0
    else:
        add=int(add)
    author["addLine"]=add

    getRemove="cd {} && git log --author={} --pretty=tformat: --numstat --after=\'{}\' --before=\'{}\'".format(destCodeDir,authorName,timeDict["startTime"],timeDict["endTime"])+"| awk '{remove += $2};END {print remove}'"
    remove=os.popen(getRemove).read()
    if remove == "":
       remove=0
    else:
       remove=int(remove)
    author["removeLine"]=remove

    sub=add-remove
    author["subLine"]=sub
    return dict(timeStamp=timeDict["timeStamp"],collectDateTag=timeDict["collectDateTag"],startTime=timeDict["startTime"],endTime=timeDict["endTime"],author=author)
