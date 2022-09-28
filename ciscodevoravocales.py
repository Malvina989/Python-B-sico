word_without_vowels = ""
user_word = input("Ingrese una palabra")

for letter in user_word.upper():
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)