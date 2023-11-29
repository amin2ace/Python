

# Make a list of numeric from start to end
def get_list(start = 0, end = 9):

    numbers_list = list()
    for i in range(int(start), int(end)+1):
        numbers_list.append(chr(i))
    return numbers_list

def main():
    print(get_list(0, 9))

if __name__ == "__main__": main()