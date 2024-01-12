from glob import glob
import os


def nameJoining(rootPath: str, oldFileName: str, _extension: str):
    oldName: list[str] = oldFileName.split("-")
    oldName.pop()  # only one extra - existes
    # oldName.pop()
    renamedName: str = "-".join(oldName) + _extension
    srcFile: str = os.path.join(rootPath, oldFileName)

    # if New Folder Created must be also add the name here
    newFile: str = os.path.join(rootPath, renamedName)
    try:
        if os.path.isfile(newFile):
            return nameJoining(rootPath, oldFileName, "1" + _extension)
    except Exception as e:
        return f"Error: {e}"
    else:
        """To Create New Folder Uncomment this also add the folder name to newFile path
        newFolder = os.path.join(rootPath, 'Renamed')
        if not os.path.isdir(newFolder):
            os.mkdir(newFolder, 777)"""
        return os.rename(srcFile, newFile)


def renameFile(filePath):
    _path: list[str] = filePath.split("\\")
    oldFileName: str = _path[-1]
    rootPath: str = "\\".join(_path[:-1])
    extension: str = oldFileName.split("-")[-1][-4:]
    print(oldFileName)
    if len(oldFileName.split("-")) > 2:
        return nameJoining(rootPath, oldFileName, extension)


def walking(_root):
    try:
        assert os.path.isdir(_root), "Path is not Valid"
    except Exception as e:
        return f"Directory Not Found:{e}"
    else:
        files_list: list = glob(os.path.join(_root, "**"), recursive=True)
        for _file in files_list:
            if os.path.isfile(_file):
                renameFile(_file)
            continue
        return f"Done."


def main():
    while 1:
        _path: str = input("Enter Path: \n")
        walking(_path)


if __name__ == "__main__":
    main()
