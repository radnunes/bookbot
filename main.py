def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    print(text)
    
main()