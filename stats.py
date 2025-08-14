def get_num_words(filepath):

    words = []
    with open(filepath) as file:
        words = file.read()
        return len(words.split())

def get_num_characters(text):

    char_count = {
                "a":0,
                "b":0,
                "c":0,
                "d":0,
                "e":0,
                "f":0,
                "g":0,
                "h":0,
                "i":0,
                "j":0,
                "k":0,
                "l":0,
                "m":0,
                "n":0,
                "o":0,
                "p":0,
                "q":0,
                "r":0,
                "s":0,
                "t":0,
                "u":0,
                "v":0,
                "w":0,
                "x":0,
                "y":0,
                "z":0 }
    for char in char_count:
        for letter in text:
            if char == letter.lower():
                char_count[char] += 1
    
    return char_count

def sort_on(items):
    return items["num"]


def report(dict):
    dict_list = []
    for key in dict:
        entry = {"char":key,
                 "num":dict[key]}
        dict_list.append(entry)
    for key in dict_list:
        dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list
