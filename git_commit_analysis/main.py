import os
from json import dumps
import get_new_code
from get_code_list import get_code_list
from get_repository_https import read_git_https
from get_date_time import get_time
import get_commit_info
import get_results

def main(delta,destCodeDir,gitRepositoryHttps,resultsDir):
    codeList=get_code_list(destCodeDir)
    print("已存在 git 代码仓库\n",codeList)
    gitProjectHttps=read_git_https(gitRepositoryHttps)
    for n in range(len(list(gitProjectHttps.keys()))):
    	if list(gitProjectHttps.keys())[n] not in list(codeList.keys()):
            print("新增代码仓库：",list(gitProjectHttps.keys())[n])
            get_new_code.get_new_repository(destCodeDir,gitProjectHttps[list(gitProjectHttps.keys())[n]])
    codeList=get_code_list(destCodeDir)
    print("git 代码仓库更新结果\n",codeList)

    for key,value in codeList.items():
        commitInfo={}
        get_new_code.get_new_code(value)
        for n in range(0,delta):
            timeDict=get_time(n)
            authorList=get_commit_info.get_author_list(timeDict,value)
            for n in range(len(authorList)):
                commitInfo={}
                commitInfo["project"]=key
                authorCommitInfo=get_commit_info.get_author_info(timeDict,value,authorList[n])
                commitInfo.update(authorCommitInfo)
                get_results.results_output(resultsDir,str(dumps(commitInfo,ensure_ascii=False)))
    
if __name__ == "__main__":
    destCodeDir="/sdata/app/gitAnalysis/destCode"
    gitRepositoryHttps="/sdata/app/gitAnalysis/docs/gitRepositoryHttps.txt"
    resultsDir="/sdata/app/gitAnalysis/results"
    timeDelta=7
    main(timeDelta,destCodeDir,gitRepositoryHttps,resultsDir)
