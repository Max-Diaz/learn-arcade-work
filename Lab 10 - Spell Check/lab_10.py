import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """
    my_file = open("../Testing/dictionary.txt")
    dictionary_list = []
    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)
    my_file.close()
    for name in dictionary_list:
        print(name)

main()