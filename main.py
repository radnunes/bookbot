def main():
    book_path = "books/frankenstein.txt"
    text = get_file_contents(book_path)
    
    report(text)

def count_words(text):
        words = text.split()
        return len(words)

def count_letters(text):
    letter_count = {}

    for letter in text:
        lowered = letter.lower()
        if lowered in letter_count:
            letter_count[lowered] += 1
        else:
            letter_count[lowered] = 1
    return letter_count

def get_file_contents(file_path):
    with open(file_path) as f:
        return f.read()

def pretty_print(dictionary):
    for key, value in dictionary.items():
        print("The " + key + " character was found: " + str(value) + " times.")

def report(text):
    print("=== Report ===")
    print("Number of words: ", count_words(text))
    pretty_print(count_letters(text))
    print("=== End Report ===")

main()