"""
File_Name: extens_count.py

This module walks through a
specific root directory and
check the extensions available 
in the directory and returns 
the count and the sum of size
of everyextesions.

representation description: 
    (+) represent directories witch
        still have sibling directories.

    (.)present the last directory or 
        last file
to save result in a text file use 'to_file'
method after instanciating.

ex: Tree('C:/Users')

__author__ = 'Amin Vahdani'
__email__ = 'avmap.py@gmail.com'
__check__ = ['black', 'isort', 'mypy']

"""


import glob
import os

ROOt = 'D:/VENVS/Sys/.venv/SysProjects'
extensions_count: dict=dict()
extensions_size:dict = dict()
def walking(path_:str):
    globed = glob.glob(os.path.join(path_, '**'), recursive=True, include_hidden=True)
    # print(globed)
    split_files(globed)
    
def split_files(files_):
    # extensions_list:list = [os.path.splitext(e)[0] for e in files_]
    # print(extensions_list)
    for file in files_:
        if os.path.isfile(file):
            sizing(file)
            counting(file)
            show() 
def show():
    extensions_size.update()
    print(extensions_count, extensions_size, sep='\n')


def counting(file_):
    ext = os.path.splitext(file_)[1]
   
    if ext in extensions_count.keys():
        extensions_count[ext]+=1
        return 
    extensions_count[ext] = 1 
    # else:
    #     extensions_count[ext] = 1

def sizing(file_, sizing:str='KB'):
    ext = os.path.splitext(file_)[1]
    size = os.path.getsize(file_)
    sizing = 1024 if sizing is 'KB' else 1024*1024
    if ext in extensions_size.keys():
        extensions_size[ext] += size/sizing
    else:
        extensions_size[ext] = size/sizing

def main():
    walking(ROOt)

main()