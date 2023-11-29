r"""_summary_:
            This module represent a class named 'Tree' witch generates

            directory tree of all subfolders

            for specific path.

            after instanciating Tree generate with 'walking' method.

            author: 'Amin Vahdani'

            feedback: avmap.py@gmail.com
"""


from os import walk, path, getcwd, remove
from time import sleep


class Tree:
    """Attributes:
        all attribs are optional
        root: takes a path like str to generate directory tree. Defaults is current working directory.
        file_name: file name with extension '.txt'. Defaults is 'Tree.txt'.
        speed: determines sleep time after writing each tree record in int 'for debugging purposes'. Defaults is 0.

    Returns:
        Text file as .txt
    """

    # Class Attributes
    PIPE = "│"
    ELBOW = "└──"
    TEE = "├──"

    def __init__(
        self, root: str = getcwd(), file_name: str = "Tree.txt", speed: int = 0
    ) -> None:
        self.speed: int = speed
        self.root: str = root
        self.path: str = path.join(getcwd(), file_name)
        if path.isfile(self.path):
            remove(self.path)

    def walking(self, indent: int = 0):
        """Generates object's tree with walk through the directories

        Args:
            indent (int, optional): Base indention for root directory. Defaults to 0.
        """
        if indent == 0:
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(Tree.root_format(path.basename(self.root)))

        for root, dirs, files in walk(self.root, topdown=True):
            for file in sorted(
                files, key=lambda f: f[0].lower()
            ):  # Print alpha sortet files in current directory
                with open(self.path, "a", encoding="utf-8") as f:
                    f.write(Tree.root_format(path.basename(self.root)))
                sleep(self.speed)
            if not len(dirs):
                continue  # if there is no diractory in current root

            for dir in dirs:  # Print sub directories
                with open(self.path, "a", encoding="utf-8") as f:
                    f.write(Tree.root_format(path.basename(self.root)))
                self.root = path.join(root, dir)  # Changes root to current directory
                self.walking(indent + 3)
                sleep(self.speed)
                if dir == dirs[-1]:
                    indent = 0
            break

    @staticmethod
    def print_format(name: str, indent: int = 0, symbol: str = TEE) -> str:
        return f"{' '*indent}{symbol}{name}\n"

    @staticmethod
    def root_format(name: str) -> str:
        return f"{name}\n"