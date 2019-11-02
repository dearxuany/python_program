import os

def get_code_list(destCodeDir):
    codeList=os.listdir(destCodeDir)
    codeDirList=[]
    projectDict={}
    for n in range(len(codeList)):
        codeDirList.append(destCodeDir)
        projectDict[codeList[n]]=codeDirList[n]+"/"+codeList[n]        
    return projectDict

if __name__ == "__main__":
    destCodeDir="."
    codeDirList=get_code_list(destCodeDir)
    print(codeDirList)
