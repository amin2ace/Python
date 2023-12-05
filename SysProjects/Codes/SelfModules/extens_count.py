"""
File_Name: extens_count.py

This module walks through a
specific root directory and
check the extensions available 
in the directory and returns 
the count and the sum of size
of everyextesions. -> iterator


ex:
    dir_1 = ExtensionsCounter('D:/VENVS/Sys/.venv/SysProjects', 'KB')\n
    dir_2 = ExtensionsCounter('D:/VENVS/Sys/.venv', 'KB')\n
    dir_1.walking()\n
    dir_2.walking('.py', '.pyd', '.pyc')\n
    dir_3 = dir_1-'.png'

__author__ = 'Amin Vahdani'
__email__ = 'avmap.py@gmail.com'
__check__ = ['black', 'isort', 'mypy']

"""


import glob
import os
from typing import Generator


class ExtensionsCounter:
    """Walks through the dir_path root
        and Gives an iterator as tuple:
         (extension_name, count_sum, size_sum)

    attribs:
        root (str): directory to be walk
        size (str): 'KB' or 'MB'
    methods:
        walking:returns tuple of dicts witch\n
                first dict is extensions_count_sum and\n
                second one is extensions_size_sum in\n
                root directory.\n
                extensions can be excluded by 'excluded_text'\n
                as (**kwargs).
        add (overload): returns iterator as sum of
            two path's values
    """

    def __init__(self, dir_path: str, sizing: str = "KB") -> None:
        self.root = dir_path
        self.__exts_count: dict = dict()
        self.__exts_size: dict = dict()
        self.exculde: str | None = None
        if sizing.upper() in ("KB", "MB"):
            self.size = sizing.upper()
        else:
            raise ValueError('sizing must be "KB" or "MB"')

    def walking(self, *excluded_ext: str) -> tuple | None:
        """Gives a tuple as iterator
        parameter:
        excluded_ext: will exclude these extensions
        tuple(str)"""
        try:
            assert os.path.isdir(self.root), AssertionError("Bad directory path")
        except AssertionError as e:
            print(
                f"Root directory Not found: {e}",
            )
            return None
        else:
            self._globed = glob.glob(
                os.path.join(self.root, "**"), recursive=True, include_hidden=True
            )
            return self.split_files(excluded_ext)

    def split_files(self, exclude: tuple) -> tuple:
        """Does counting and sizing seprated"""
        for file in self._globed:
            # Check if the name is file and not None
            if os.path.isfile(file) and os.path.splitext(file)[1] not in exclude:
                if os.path.splitext(file)[1] == "":
                    continue
                self.counting(file)
                self.sizing(file)
        return self.__exts_count, self.__exts_size

    def counting(self, file_):
        ext = os.path.splitext(file_)[1]

        if ext in self.__exts_count.keys():
            self.__exts_count[ext] += 1
        else:
            self.__exts_count[ext] = 1

    def sizing(self, file_):
        ext = os.path.splitext(file_)[1]
        size = os.path.getsize(file_)
        sizing = 1024 if self.size == "KB" else 1024 * 1024

        if ext in self.__exts_size.keys():
            self.__exts_size[ext] += size / sizing
        else:
            self.__exts_size[ext] = size / sizing

    def __add__(self, other) -> Generator:
        ext_count: dict = {**self.__exts_count, **other.__exts_count}
        ext_size: dict = {**self.__exts_size, **other.__exts_size}
        show_dict = zip(ext_size.keys(), ext_count.values(), ext_size.values())
        for ext in show_dict:
            yield ext

    def __sub__(self, e) -> Generator:
        """Exclude extension in calculations"""
        self.__exts_count.pop(e)
        self.__exts_size.pop(e)
        return self.__iter__()

    def __iter__(self) -> Generator:
        show_dict = zip(
            self.__exts_size.keys(),
            self.__exts_count.values(),
            self.__exts_size.values(),
        )
        for ext in show_dict:
            yield ext


dir_1 = ExtensionsCounter("D:/VENVS/Sys/.venv/SysProjects", "KB")
dir_2 = ExtensionsCounter("D:/VENVS/Sys/.venv", "KB")
dir_1.walking()
dir_2.walking(".py", ".pyd", ".pyc")
dir_3 = dir_1 - ".png"
for a in dir_2:
    print(a)
