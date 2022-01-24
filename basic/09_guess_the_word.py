import random
word_list = ["suryaprakash","shivani","shruti","pranesh","gauri"]

i = random.randint(0, len(word_list)-1)
chosen_word = (word_list[i])
print(chosen_word)
blanks = len(chosen_word)
print(blanks)

guessed = input("Guess the letter : ").lower()
for letter in chosen_word:
  if letter == guessed:
    print("Right")
  else:
    print("Wrong")