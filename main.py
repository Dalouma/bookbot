from stats import count_words, count_characters, get_char_list
import sys

FILE_PATH = None

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    return None



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    FILE_PATH = sys.argv[1]

    content = get_book_text(FILE_PATH)
    num_words = count_words(content)
    # print(f"{num_words} words found in the document")
    characters_dict = count_characters(content)
    # print(characters_dict)
    character_list = get_char_list(characters_dict)

    # print(character_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {FILE_PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in character_list:
        character = dictionary["character"]
        count = dictionary["count"]
        if not character.isalpha():
            continue
        print(f"{character}: {count}")
    print("============= END ===============")
    


if __name__ == "__main__":
    main()