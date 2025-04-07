import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Please type a word: ").upper()
nato_word = [nato_dictionary[letter] for letter in word]
print(nato_word)
