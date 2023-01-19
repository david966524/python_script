import requests
import json
 
# 设置Jenkins URL和job名称
jenkins_url = 'http://admin:admin123789@x.x.x.x:8082'
job_name = 'flutter_bourse'
 
# 获取最新构建的信息，包括commit信息
api_url = jenkins_url + '/job/' + job_name + '/lastBuild/api/json'
response = requests.get(api_url)
data = json.loads(response.text)  # 将JSON字符串转换成Python字典对象 
commit_info = data['changeSet']['items'] # 获取commit信息列表 
for commit in commit_info: # 遍历commit信息列表，获取详细信息 
    print('Author:', commit['author']['fullName']) # 打印作者名称 
    print('Message:', commit['msg']) # 打印commit message  

    for file in commit['paths']: # 遍历文件列表，获取文件名和修改类型  

        print('File:', file['file'])  

        if file['editType'] == 'edit':  

            print('Edit Type: Modified')  

        elif file['editType'] == 'add':  

            print('Edit Type: Added')  

        elif file['editType'] == 'delete':  

            print('Edit Type: Deleted')  

