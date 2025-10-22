def check_palindrome():
    text = input("Enter the text to analyze: ").replace(" ", "").lower()
    if text == text[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


def count_words_in_file():
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            print(f"Total words in file: {len(words)}")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")


def main():
    print("Welcome to the Text Analyzer!")
    print("1. Analyze a word or sentence (Palindrome Check)")
    print("2. Analyze a .txt file (Word Counter)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        check_palindrome()
    elif choice == "2":
        count_words_in_file()
    else:
        print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
