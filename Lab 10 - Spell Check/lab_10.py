import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """ Read in lines from a file """
    my_file = open("dictionary.txt")
    dictionary_list = []
    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)
    my_file.close()
    print("--- Linear Search ---")

    alice_file = open("AliceInWonderLand200.txt")
    line_number = 0
    for line in alice_file:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            # Start at the beginning of the list
            current_list_position = 0

            # Loop until you reach the end of the list, or the value at the
            # current position is equal to the key
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
                # Advance to the next item in the list
                current_list_position += 1

            if current_list_position == len(dictionary_list):
                print("This word was not found: " + word)
    alice_file.close()


main()