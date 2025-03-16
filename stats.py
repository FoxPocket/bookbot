def word_count(string):

    my_list = string.split()


    count = len(my_list)

    return count


def character_count(string):

    char_count = {}

    lower_string = string.lower()

    for character in lower_string:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count

def sort_on(dict):
    return dict["count"]

def dictionary_sort (dictionary):

    my_list = []

    for char, count in dictionary.items():
        if char.isalpha():
            char_dict = {"char":char, "count":count}

            my_list.append(char_dict)

    my_list.sort(reverse=True, key=sort_on)

    return my_list