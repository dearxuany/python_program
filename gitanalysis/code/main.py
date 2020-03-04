import os
from json import dumps
import get_new_code
from get_code_list import get_code_list
from get_repository_https import read_git_https
import get_project_name
from get_date_time import get_time
import get_commit_info
import get_results

def main(timeDelta,destCodeDir,gitRepositoryHttps,resultsDir,gitlab_url,gitlab_token,autoGetNewProjects):
    codeList=get_code_list(destCodeDir)
    print("已存在 git 代码仓库\n",codeList)

    if autoGetNewProjects == True:
        groups_dict=get_project_name.get_project_info(gitlab_url,gitlab_token)
        gitProjectHttps=get_project_name.get_project_url(gitlab_url,groups_dict)
    else:
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
        for n in range(0,timeDelta):
            timeDict=get_time(n)
            authorList=get_commit_info.get_author_list(timeDict,value)
            for n in range(len(authorList)):
                commitInfo={}
                commitInfo["project"]=key
                authorCommitInfo=get_commit_info.get_author_info(timeDict,value,authorList[n])
                commitInfo.update(authorCommitInfo)
                get_results.results_output(resultsDir,str(dumps(commitInfo,ensure_ascii=False)))
    
if __name__ == "__main__":
    # 目标分析代码目录
    destCodeDir="/sdata/app/gitAnalysis/destCode"
    # 手动导入代码仓库链接配置
    gitRepositoryHttps="/sdata/app/gitAnalysis/docs/gitRepositoryHttps.txt"
    # 分析结果导出目录
    resultsDir="/sdata/app/gitAnalysis/results"
    # 分析时间跨度
    timeDelta=7

    # 敏感信息请勿丢失及泄露
    gitlab_url = "https://git.domainname.com"
    gitlab_token = "passwd"

    # 是否自动导入 gitlab 中最新代码仓库
    autoGetNewProjects=True
    
    main(timeDelta,destCodeDir,gitRepositoryHttps,resultsDir,gitlab_url,gitlab_token,autoGetNewProjects)
