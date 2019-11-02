import os
from json import dumps
from get_new_code import get_new_code
from get_code_list import get_code_list
import get_commit_info
import get_results

def main(destCodeDir,resultsDir):
    codeList=get_code_list(destCodeDir)
    for key,value in codeList.items():
        commitInfo={}
        get_new_code(value)
        authorList=get_commit_info.get_author_list(value)
        for n in range(len(authorList)):
            commitInfo={}
            commitInfo["project"]=key
            authorCommitInfo=get_commit_info.get_author_info(value,authorList[n])
            commitInfo.update(authorCommitInfo)
            #print(commitInfo)
            get_results.results_output(resultsDir,str(dumps(commitInfo,ensure_ascii=False)))
    
if __name__ == "__main__":
    destCodeDir="/sdata/gitlab-code/git/gitAnalysis/destCode"
    resultsDir="/sdata/gitlab-code/git/gitAnalysis/gitanalysis/results"
    main(destCodeDir,resultsDir)
