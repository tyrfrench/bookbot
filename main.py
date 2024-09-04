
def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book(book_path)

    num_words = word_count(book_content)
    num_chars = char_count(book_content)
    chars_list = chars_to_list(num_chars)
    sorted_chars = sort_chars(chars_list)

    report = get_report(book_path, num_words, sorted_chars)

    print(report)


def get_report(book_path, num_words, sorted_chars):

    num_words = str(num_words)

    report = "--- Content Report on " + book_path + " ---\n \n"
    report = report + "Number of words found in content: " + num_words + "\n \n"
    report = report + "Number of individual letters, ranked highest count to lowest: \n"

    for letter in sorted_chars:
        str_letter = str(letter["letter"])
        str_count = str(letter["count"])
        report = report + "Letter: " + str_letter + "    Number of times found: " + str_count + "\n"

    report = report + "\n--- Report Complete ---"
    
    return report


def sort_on(chars_list):
    return chars_list["count"]


def sort_chars(chars_list):
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list


def chars_to_list(chars_dict):
    letters = []
    for char in chars_dict:
        letters.append({"letter": char, "count": chars_dict[char]})

    return letters


def char_count(book):
    characters = {}
    for char in book:
        lowered_char = char.lower()
        if lowered_char.isalpha():
            if lowered_char not in characters:
                characters.update({lowered_char: 1})
            else:
                dict_count = characters[lowered_char] + 1
                characters.update({lowered_char: dict_count})

    return characters


def word_count(book):
    words = book.split()
    
    return len(words)


def get_book(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents


main()
