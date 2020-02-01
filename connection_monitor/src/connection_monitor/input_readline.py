import os

def read_file_lines(inputFileDir):

    file=open(inputFileDir)
    inputList=file.readlines()
    file.close()
  
    lineList=[]
        
    for n in range(len(inputList)):
        if inputList[n].startswith("#") == False:
            lineList.append(inputList[n][0:-1])
    
    lineList=list(set(filter(None,lineList)))
         
    return lineList
