import json
class EnglishDictionary:
    def __init__(self):
        self.dictionary = {}

    def add_word(self, word, meanings):
        self.dictionary[word] = meanings

    def remove_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]

    def lookup_word(self, word):
        return self.dictionary.get(word, "Word not found.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.dictionary, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.dictionary = json.load(file)

    def menu(self):
        while True:
            print("\nEnglish Dictionary Menu:")
            print("1. Add a new word")
            print("2. Remove a word")
            print("3. Lookup a word")
            print("4. Save dictionary to file")
            print("5. Load dictionary from file")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                word = input("Enter the word: ")
                meanings = input("Enter the meanings (part of speech, definition, example) separated by semicolons: ")
                meanings_list = [tuple(meaning.split(',')) for meaning in meanings.split(';')]
                self.add_word(word, meanings_list)
            elif choice == '2':
                word = input("Enter the word to remove: ")
                self.remove_word(word)
            elif choice == '3':
                word = input("Enter the word to lookup: ")
                print(self.lookup_word(word))
            elif choice == '4':
                filename = input("Enter the filename to save to: ")
                self.save_to_file(filename)
            elif choice == '5':
                filename = input("Enter the filename to load from: ")
                self.load_from_file(filename)
            elif choice == '6':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage:
dictionary = EnglishDictionary()
dictionary.menu()
