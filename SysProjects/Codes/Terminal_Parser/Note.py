
import argparse as a
import os


def add_note(note, file_path):
    with open(file_path, 'a') as f:
        f.write(f"{note}\n")
       

def view_notes(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        if lines == []:
            print("\n### You Dont Have Any Note ###\n")
        else:
            for line, note in enumerate(lines):
                print(f"{line + 1} ---> {note}")
    print(f"Number of entries: {len(lines)}")
    
def del_note(line, file_path):
    with open(file_path, 'r+') as f:
        lines = f.readlines()
        if line > len(lines):
            print("\n!!!Invalid Note Number!!!\n")
        else:
            lines.pop(line - 1)
            f.seek(0)
            f.truncate()
            f.writelines(lines)
def main():
    
    path = a.ArgumentParser(description="hello")
    path.add_argument("--path", default=f"{os.path.join(os.getcwd(), 'Notes.txt')}", help="Where do you want store your notes")
    file_path = path.parse_args().path
    while 1:
        print('\n')
        print("### Choose the option number ###")
        user_input = int(input("\n1.Add Note  2.Delete Not  3.View All Notes  4.Exit\t:\t"))
        if user_input == 1:
            note_input = input("\nEnter Note: ")
            add_note(note_input, file_path)
        elif user_input == 2:
            view_notes(file_path)
            line = int(input("\nChoose Note Number to Delete it: "))
            del_note(line, file_path)
        elif user_input == 3:
            view_notes(file_path)
        else:
            exit()
if __name__=="__main__": main()