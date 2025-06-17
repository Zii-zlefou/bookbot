from stats import word_count, char_count, list_of_dicts
import sys




def get_book_text(book_path):

    with open(book_path) as b:
        content = b.read()

    return content


def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_word = word_count(book_text)
    char_count_dict = char_count(book_text)
    sorted_list = list_of_dicts(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")

    for letter in sorted_list:
        char = letter['char']
        count = letter['num']
        if char.isalpha():
            print(f'{char}: {count}')

    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()