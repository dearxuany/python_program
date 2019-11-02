#! /usr/bin/pyhton3

import os

def write_output(resultsFile,data):
    file=open(resultsFile,'a')
    file.write(data+"\n")
    file.close()
    return

def results_output(resultsDir,data):
    if not os.path.exists(resultsDir):
        os.mkdir(resultsDir)
        return results_output(resultsDir,data)
    else:
        resultsFile=resultsDir+"/analysisResults.txt"
        if not os.path.isfile(resultsFile):
            os.mknod(resultsFile)
            write_output(resultsFile,data)
        else:
            write_output(resultsFile,data)
    return

if __name__ == "__main__":
    resultsDir="/sdata/gitlab-code/git/gitAnalysis/gitanalysis/results"
    data="hello!/ntesting/n"
    results_output(resultsDir,data)
