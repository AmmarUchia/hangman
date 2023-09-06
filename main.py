# import random
# from words import words
# import string


# def hangman():
#     print("-"*50)
#     print("Welcome to the hangman game ")
#     print("-"*50)
#     word = random.choice(words).upper()
#     word_letter = set(word)
#     used_letter = set()
#     alaphbet = set(string.ascii_uppercase)


#     while len(word_letter) > 0:

#         print("You Have used" + ' '.join(used_letter ))
#         user_letter = input("The Computer Has Chosen a word and you have to guess it choose a letter:  ")
#         if user_letter in alaphbet - used_letter:
#             used_letter.add(user_letter)
#             if user_letter in word_letter:
#                 word_letter.remove(user_letter)
#         elif user_letter in user_letter:
#             print("You have already used this character please chose another choice")        

#         else:
#             print("Invalid Choice   ")    


import string

# Create a set containing all uppercase letters of the English alphabet
alphabet = set(string.ascii_uppercase)

# Create a set of letters that have been used
used_letters = set(['A', 'B', 'C'])

# Calculate the set difference to find available letters
available_letters = alphabet - used_letters

print("Available letters:", available_letters)
