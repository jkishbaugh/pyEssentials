#!usr/bin/env python3


def main():
    the_word = input("Please enter a word. ")
    print_each_char(the_word)
    print(reverse_word(the_word))
    char_to_count = input("Which character would you like to count? ")
    print(f'{char_to_count} appears {count_char(the_word, char_to_count)} times in the word you chose. ')


def print_each_char(word):
    word_as_list = list(word)
    index = 0
    while index < len(word):
        print(word[index])
        index += 1


def reverse_word(word):
    string = word[::-1]
    return string


def count_char(word, char):
    count = 0
    for c in word:
        if c == char:
            count += 1
    return count


if __name__ == "__main__":main()
