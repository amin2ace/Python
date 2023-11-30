r"""_summary_:
            This module represent a class named 'Tree' witch generates
            directory tree of all subfolders for specific path.
            representation description:
                (+) represent directories witch still have sibling directories.
                (.)present the last directory or last file
            to save result in a text file use 'to_file' method after instanciating.
            ex: Tree('C:/Users')

            author: 'Amin Vahdani'
            feedback: avmap.py@gmail.com
"""
__author__ = 'Amin Vahdani'
__email__  = 'avmap.py@gmail.com'
__check__ = ['black', 'isort', 'mypy']


import os


class Tree:
    """Attributes:
        root (str and optional): takes a path like str to generate directory tree. Default is current working directory.

    __repr__:
        tree-ish directory in (str)
    
    to_file() method:
        save presentation of tree_ish in a text file in current directory
        argument:
                file_name (str): file name to save.
        return:
                str
    """

    __IND:int = 0 # indention for sub-directories in tree formatting
    __write_list:list = [] # tree-ish to be presented


    def __init__(self, root: str = os.getcwd()) -> None:
        self.root: str = root.replace('\\','/')


    def to_file(self, file_name: str):
        """save the object to a text file in same current directory with (.txt) extension

        Args:
            file_name (str): file name to be save
        """        
        file_name = f'{file_name}.txt'
        with open (os.path.join(self.root, file_name), 'w', encoding='utf-8') as f:
            for line in self.tree_ish(self.root):# pass the path of directory
                f.write(f'{line}\n')

 
    def tree_ish(self, __dir: str):
        #Generates object's tree with walk through the directories   

        for _,directories,files in os.walk(__dir):
            for file in files :
                # prints last file Terminator '.└──' if its last file in the branch 
                if file is files[-1] and len(directories) is 0: 
                    Tree.__write_list.append(f"{' '*Tree.__IND}.└──{file}")
                else:
                    Tree.__write_list.append(f"{' '*Tree.__IND} ├──{file}")

            for directory_ in directories:
                # prints last directory Terminator '.└──' if its last dir in the branch
                if directory_ is not directories[-1]:
                    Tree.__write_list.append(f"{' '*Tree.__IND}+├──{directory_}")
                else:
                    Tree.__write_list.append(f"{' '*Tree.__IND}.└──{directory_}")
                Tree.__IND += 5 # indent for subdirs and files
                self.tree_ish(os.path.join(__dir, directory_))
            Tree.__IND -= 5 # reset indent for directories in the same parent 
            return Tree.__write_list
        

    def __repr__(self) -> str:
        for line in self.tree_ish(self.root):
            print(line)
        return ''
Tree().to_file('amin')