import gitlab

def get_project_info(gitlab_url,gitlab_token):
    gl = gitlab.Gitlab(gitlab_url, gitlab_token)

    groups = gl.groups.list(all=True)

    groups_dict={}

    for g in groups:
        groups_dict[g.id]={"g.name":g.name}                

    for key in groups_dict:
        group = gl.groups.get(key)
        projects = group.projects.list(all=True, as_list=False)
    
        project_name_list=[]

        for p in projects:
            project_name_list.append(p.name)          
  
        groups_dict[key]["g.projects"]=project_name_list        
   
    print(groups_dict)

    return groups_dict

def get_project_url(gitlab_url,groups_dict):
    gitProjectHttps={}
    for key in groups_dict:
        for n in range(len(groups_dict[key]["g.projects"])):
            gitProjectHttps[groups_dict[key]["g.projects"][n]]=gitlab_url+"/"+groups_dict[key]["g.name"]+"/"+groups_dict[key]["g.projects"][n]
    print(gitProjectHttps)
        
    return gitProjectHttps
            

if __name__ == "__main__":
    gitlab_url = "https://git.domainname.com"
    gitlab_token = "passwd"
    groups_dict=get_project_info(gitlab_url,gitlab_token)
    get_project_url(gitlab_url,groups_dict)

