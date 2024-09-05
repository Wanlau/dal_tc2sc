import os
import shutil
import subprocess
import re
from opencc import OpenCC

#检索文件
def find_files(directory, extension):  
    files = []  
    for root, dirs, file_names in os.walk(directory):  
        for file_name in file_names:  
            if file_name.endswith(extension):  
                files.append(os.path.join(root, file_name))  
    return files

#检索目录并新建临时目录
def find_dirs(directory):  
    dirs = []  
    for dirpath, dirnames, filenames in os.walk(directory):  
        for dirname in dirnames: 
            if dirname in dirs:
                pass
            else:
                dirs.append(os.path.join(dirpath, dirname))

    for dir in dirs:
        os.makedirs(os.path.join('tmp', dir))

    return dirs
             
    

#使用OpenCC进行简繁转换
#检索文本中的关键词并提取其后引号里的内容
def find_content_after_keyword(file_path, keyword):  
    # 读取文本文件内容  
    with open(file_path, 'r', encoding='utf-8') as file:  
        text = file.read()  
      
    # 使用正则表达式查找关键词后紧跟的引号内的内容  
    # 注意：这个正则表达式假设引号内没有转义的引号  
    pattern = rf"{re.escape(keyword)}(.*?)([\'\"])(.*?)([\'\"])"  
    matches = re.findall(pattern, text, re.DOTALL)  
      
    # 提取并返回引号内的内容  
    results = [match[2] for match in matches if match]  
    return results

#根据输入列表检索并替换文本中的关键词  并将新文本写入至临时目录的新文件中
def text_replace(file_old, results_tc, results_sc, num):
    with open(file_old, 'r', encoding='utf-8') as file:
        text_old = file.read()

    file_new = os.path.join('tmp', file_old)
    text_new = text_old

    for i in range(0,num):
        text_new = text_old.replace(results_tc[i], results_sc[i])
        text_old = text_new

    #特殊转换
    #此为OpenCC中未进行转换但因字体缘故需要转换的部分
    str_list_tc = ['妳']
    str_list_sc = ['你']
    for i in range(0,len(str_list_tc)):
        text_new = text_old.replace(str_list_tc[i], str_list_sc[i])
        text_old = text_new

    with open(file_new, 'w', encoding='utf-8') as file:
        file.write(text_new)

    return file_new

#将文本中的繁体内容转换为简体并写入至临时目录的新文件中
def tc2sc(file):
    results_tc = find_content_after_keyword(file, "Mes(")
    results_tc += find_content_after_keyword(file, "SetChoice(")
    cc = OpenCC('t2s')
    results_sc = []
    num = len(results_tc)
    tmpstr = ''
    for i in range(0,num):
        tmpstr = cc.convert(results_tc[i])
        results_sc.append(tmpstr)
    file_new = text_replace(file, results_tc, results_sc, num)
    return file_new

#获取当前路径
current_path = os.getcwd()

#DAL工具路径
path_PCKTool = 'DALTools\\PCKTool.exe'
path_STSCTool = 'DALTools\\STSCTool.exe'
#游戏脚本包路径
path_scriptpack = 'Data\\CHN\\Script\\Script.pck'

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

#获取目录列表并新建临时目录
dirs = find_dirs('Script')

##使用OpenCC对.txt文件进行简繁转换
txt_file_news = []
for txt_file in txt_files:
    txt_file_new = tc2sc(txt_file)
    txt_file_news.append(txt_file_new)

#使用STSCTool把.txt编译为.bin文件
for txt_file_new in txt_file_news:
    command = [path_STSCTool, txt_file_new]
    subprocess.run(command)
    #删除.txt文件
    os.remove(txt_file_new)    

#使用PCKTool打包新文件
command = [path_PCKTool, 'tmp\\Script']
subprocess.run(command)

#用新的pck文件替换原文件并删除临时文件
os.remove(path_scriptpack)
shutil.move('tmp\\Script.pck', path_scriptpack)
shutil.rmtree('Script')
shutil.rmtree('tmp')