#! /usr/bin/env python3

import os

def read_git_https(gitRepositoryHttps):

    file=open(gitRepositoryHttps)
    gitHttpsList=file.readlines()
    file.close()

    gitProjectHttps={}
    for n in range(len(gitHttpsList)):
        gitProjectHttps[gitHttpsList[n].split("/")[-1][0:-1]]=gitHttpsList[n][0:-1]
     
    return gitProjectHttps

if __name__ == "__main__":
    gitRepositoryHttps="/sdata/app/gitAnalysis/docs/gitRepositoryHttps.txt"
    read_git_https(gitRepositoryHttps)
