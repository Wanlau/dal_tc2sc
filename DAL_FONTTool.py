import os
import sys
import csv
import struct

def font_encode(file_path):
    file_path_out = file_path[:-4] + '.code'
    with open(file_path, 'r', encoding='utf-8', newline='') as file: 
        reader = csv.reader(file, delimiter='\t')
        rows = []
        for row in reader:
            rows.append(row)

    head = []
    characters = []

    head.append(int(rows[0][0]))
    head.append(int(rows[0][1]))
    head.append(float(rows[0][2]))
    head.append(float(rows[0][3]))

    for i in range(1, len(rows)):
        character = []
        character.append(rows[i][0])
        character.append(float(rows[i][1]))
        character.append(float(rows[i][2]))
        character.append(int(rows[i][3]))
        character.append(int(rows[i][4]))
        characters.append(character)

    with open(file_path_out, 'wb') as file:
        file.write(struct.pack('<i',head[0]))
        file.write(struct.pack('<i',head[1]))
        file.write(struct.pack('<f',head[2]))
        file.write(struct.pack('<f',head[3]))
        for i in range(0, len(characters)):
            character = characters[i]
            dataN = character[0].encode('utf8')
            while len(dataN)<4:
                dataN = b''.join([b'\x00', dataN])
            data = dataN[::-1]
            file.write(data)
            file.write(struct.pack('<f',character[1]))
            file.write(struct.pack('<f',character[2]))
            file.write(struct.pack('<i',character[3]))
            file.write(struct.pack('<i',character[4]))
    return 0

def font_decode(file_path):
    file_path_out = file_path[:-5] + '.tsv'
    with open(file_path, 'rb') as file:
        head = []
        characters = []
        data = file.read(4)
        height = struct.unpack('<i', data)
        head.append(height[0])
        data = file.read(4)
        num = struct.unpack('<i', data)
        head.append(num[0])
        data = file.read(4)
        dx = struct.unpack('<f', data) 
        head.append(dx[0])
        data = file.read(4)
        dy = struct.unpack('<f', data) 
        head.append(dy[0])
        for i in range(0,num[0]):
            character = []
            dataN = []
            for  i in range(0,4):      
                dataN = [file.read(1)] + dataN
            data = b''.join(dataN)
            while data.startswith(b'\x00'):
                data = data.removeprefix(b'\x00')
            char = data.decode('utf-8')
            character.append(char)
            data = file.read(4)
            xpos = struct.unpack('<f', data) 
            character.append(xpos[0])
            data = file.read(4)
            ypos = struct.unpack('<f', data) 
            character.append(ypos[0])
            data = file.read(4)
            kerning = struct.unpack('<i', data)
            character.append(kerning[0])
            data = file.read(4)
            width = struct.unpack('<i', data)
            character.append(width[0])
            characters.append(character)

    with open(file_path_out, 'w', encoding='utf-8', newline='') as file: 
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(head)
        writer.writerows(characters)

    return 0

def font_encode_batch(directory):
    re = 0
    files = find_files(directory,'.tsv')
    for file in files:
        re += font_encode(file)
    if re > 0:
        re = 1
    return re

def font_decode_batch(directory):
    re = 0
    files = find_files(directory,'.code')
    for file in files:
        re += font_decode(file)
    if re > 0:
        re = 1
    return re

def find_files(directory, extension):  
    files = []  
    for root, dirs, file_names in os.walk(directory):  
        for file_name in file_names:  
            if file_name.endswith(extension):  
                files.append(os.path.join(root, file_name))  
    return files

starttext = 'DAL字符修改工具\n请输入一个.code文件或一个.tsv文件'
helptext = '''
-h  帮助
-c  输入一个code文件并将其转换为一个tsv文件
-t  输入一个tsv文件并将其转换为一个code文件
-cb 输入一个目录，将其中的code文件转换为tsv文件
-tb 输入一个目录，将其中的tsv文件转换为code文件
'''

if len(sys.argv)<2:
    print(starttext)
    sys.exit(1)

if sys.argv[1].startswith('-'):
    command = sys.argv[1][1:]
else:
    print('请输入一个指令')
    sys.exit(1)

#不是，我switch呢？
if command == 'h':
    print(starttext+'\n'+helptext)
elif command == 'c':
    if len(sys.argv)<3:
        print('请指定文件路径')
        sys.exit(1)
    path = sys.argv[2]
    re = font_decode(path)
    sys.exit(re)
elif command == 't':
    if len(sys.argv)<3:
        print('请指定文件路径')
        sys.exit(1)
    path = sys.argv[2]
    re = font_encode(path)
    sys.exit(re)
elif command == 'cb':
    if len(sys.argv)<3:
        print('请指定文件路径')
        sys.exit(1)
    path = sys.argv[2]
    re = font_decode_batch(path)
    sys.exit(re)
elif command == 'tb':
    if len(sys.argv)<3:
        print('请指定文件路径')
        sys.exit(1)
    path = sys.argv[2]
    re = font_encode_batch(path)
    sys.exit(re)
else:
    print(f'未知指令：\n{command}')
    sys.exit(1)