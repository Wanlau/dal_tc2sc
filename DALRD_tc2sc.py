import os
import csv
from opencc import OpenCC

def tsv_tc2sc(file_old):
    texts_tc = []
    texts_sc = []
    mat0=[]

    with open(file_old, 'r', encoding='utf-8', newline='') as file: 
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            mat0.append(row)
            texts_tc.append(row[2])

    cc = OpenCC('t2s')
    num = len(texts_tc)
    tmpstr = ''
    for i in range(0,num):
        tmpstr = cc.convert(texts_tc[i])
        texts_sc.append(tmpstr)

    for i in range(1, len(mat0)):
        mat0[i][2] = ''
        mat0[i].append('')
        mat0[i][3] = texts_sc[i]

    with open(os.path.join('tmp', file_old), 'w', encoding='utf-8', newline='') as file: 
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(mat0)

def find_files(directory, extension):  
    files = []  
    for root, dirs, file_names in os.walk(directory):  
        for file_name in file_names:  
            if file_name.endswith(extension):  
                files.append(os.path.join(root, file_name))  
    return files

def find_dirs(directory):  
    dirs = []  
    for dirpath, dirnames, filenames in os.walk(directory):  
        for dirname in dirnames: 
            if dirname in dirs:
                pass
            else:
                dirs.append(os.path.join(dirpath, dirname))
    return dirs

dirs = find_dirs('.')
if '.\\tmp' in dirs:
    pass
else:
    os.mkdir('.\\tmp')
    
tsv_files = find_files('.', '.tsv')
for file in tsv_files:
    tsv_tc2sc(file)