
# Make a list of alphabet from start to end
def get_list(start = 'a', end = 'z'):

    alphabet_list = list()

    for i in range(ord(start), ord(end)+1):
        alphabet_list.append(chr(i))

    return alphabet_list


def main():
    alphabet_beginnings = 'a'
    alphabet_endings = 'z'
    print(get_list(alphabet_beginnings, alphabet_endings))


if __name__ == "__main__": main()