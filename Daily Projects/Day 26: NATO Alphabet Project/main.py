import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

def nato_alphabet():
    while True:
        try:
            word = input("Please type a word: ").upper()
            nato_word = [nato_dictionary[letter] for letter in word]
            return nato_word

        except KeyError:
            print("Sorry, only letters in the alphabet please.")

print(nato_alphabet())