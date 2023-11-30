import os

IND = 0
write_list = []
def tree_ish(p = 'D:/VENVS/Sys/.venv/SysProjects'):
    global IND, write_list
   
    # print(p)
    for _,directories,files in os.walk(p):

        for file in files :
            # prints last file Terminator '.└──' if its last file in the branch 
            if file is files[-1] and len(directories)==0: 
                write_list.append(f"{' '*IND}.└──{file}")
            else:
                write_list.append(f"{' '*IND} ├──{file}")

        for directory_ in directories:
            # prints last directory Terminator '.└──' if its last dir in the branch
            if directory_ is not directories[-1]:
                write_list.append(f"{' '*IND}+├──{directory_}")
            else:
                write_list.append(f"{' '*IND}.└──{directory_}")
            IND+=5 # indent for subdirs and files
            tree_ish(os.path.join(p, directory_))
        IND-=5 # reset indent for directories in the same parent 
        return write_list
