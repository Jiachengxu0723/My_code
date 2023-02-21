# -*-coding:utf-8-*-
import os
import shutil


def load_data(path):
    data = []
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if line:
                line = line.split()
                data.append(line)
            else:
                break
    return data

def add_label(file_name, data):
    label_data = data.copy()
    for i, item in enumerate(label_data):
        item[2] = f'{file_name}_{str(i + 1).zfill(3)}'
    return label_data

def text_save(filename, data):
    file = open(filename, 'w')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')
        s = s.replace("', '", "\t").replace("'", "") + '\n'
        file.write(s)
    file.close()
    print("保存文件成功")

def mycopyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))

def get_file_list(directory, types=[], is_sort=True):
    r"""
    Get the list of all file names with certain types in a directory
    Args:
        directory(string): the directory that contains all files
    Returns:
        file_list(List[str]): List of all the required files
    """
    file_list = []
    for path, dirs, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1] in types:
                file_list.append(os.path.join(path, file))
    if is_sort:
        file_list.sort()
    return file_list

def main():
    file_list = get_file_list('/home/synsense/下载/1', types=['.txt'])
    #print(file_list)
    # print(len(file_list))
    for lable_path in file_list:
        # 备份原文件（命名：原标签文件_original）
        file_name = lable_path.split('/')[-1].split('.')[0]
        copyfile_path = lable_path.replace(file_name, f'{file_name}_original')
        shutil.copyfile(lable_path, copyfile_path)
    #
        data = load_data(lable_path)
        print(data)
        label_data = add_label(file_name, data)
        # print(label_data)

        # 生成新标签文件（与原标签文件同名）
        text_save(filename=lable_path, data=label_data)

main()