def count_words(text):
    return len(text.split())

def count_characters(text):
    result = {}
    for c in text.lower():
        if c in result:
            result[c] = result[c] + 1
        else:
            result[c] = 1
    return result

def get_count(dictionary):
    return dictionary["count"]

def get_char_list(character_dict: dict):
    dict_list = [{"character": c, "count": n} for c, n in character_dict.items()]
    dict_list.sort(reverse=True, key=get_count)
    return dict_list