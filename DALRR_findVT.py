import os
import shutil
import subprocess
import re
import csv

#检索文件
def find_files(directory, extension):  
    files = []  
    for root, dirs, file_names in os.walk(directory):  
        for file_name in file_names:  
            if file_name.endswith(extension):  
                files.append(os.path.join(root, file_name))  
    return files
#提取语音-文字信息
def findVC(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  
        text = file.read()
    pattern = rf"{re.escape('PlayVoice')}(.*?)([\'\"])(.*?)([\'\"])(.*?){re.escape('Mes(')}(.*?)([\'\"])(.*?)([\'\"])"  
    matches = re.findall(pattern, text, re.DOTALL)  
      
    # 提取并返回引号内的内容  
    results = [[match[2], match[7]] for match in matches if match]  
    return results

#获取当前路径
current_path = os.getcwd()

#DAL工具路径
path_PCKTool = 'DALTools\\PCKTool.exe'
path_STSCTool = 'DALTools\\STSCTool.exe'
#游戏脚本包路径
path_scriptpack = 'Data\\JPN\\Script\\Script.pck'

#使用PCKTool解包
command = [path_PCKTool, path_scriptpack]
subprocess.run(command)

#获取.bin文件列表
bin_files = find_files('Script', '.bin') 

#使用STSCTool把.bin反编译为.txt文件
for i in range(0,len(bin_files)):
    command = [path_STSCTool, bin_files[i]]
    subprocess.run(command)

#获取.txt文件列表
txt_files = find_files('Script', '.txt') 

#提取语音-文字信息
results = []
for txt_file in txt_files:
    results += findVC(txt_file)
with open('results.tsv', 'w', encoding='utf-8', newline='') as file: 
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(results)

#删除临时文件
shutil.rmtree('Script')