def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    words = text.split()
    character_count = {}
    while len(words) > 0:
        word = words.pop()
        for char in word:
            if char.lower() not in character_count:
                character_count[f"{char.lower()}"] = 1
            else:
                character_count[f"{char.lower()}"] += 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_dictionary(dict):
    ls = []
    for k, v in dict.items():
        ls.append({"char": k, "num": v})
    ls.sort(reverse=True, key=sort_on)
    return ls