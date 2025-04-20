import sys

recognized_characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","ø","å"]

def find_words(book):
    list_of_words = book.split(" ")
    return len(list_of_words)

def characters(text):
    text = text.lower()
    dictionary = {}
    for char in text:
        if char in dictionary and char in recognized_characters:
            dictionary[char] += 1
        elif char in recognized_characters:
            dictionary[char] = 1
    return dictionary

def sort_on(dict):
    return dict["num"]

def make_list(dictionary):
    list_for_sorting = []
    for char in dictionary:
        list_for_sorting.append({"name": char, "num": dictionary[char]})
    return list_for_sorting

def make_pretty(character_count, dictionary):
    list_for_sorting = []
    for char in dictionary:
        list_for_sorting.append({"name": char, "num": dictionary[char]})
    list_for_sorting.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {character_count} total words")
    print("--------- Character Count -------")
    for dictionary in list_for_sorting:
        print(f"{dictionary["name"]}: {dictionary["num"]}")
    print("============= END ===============")

