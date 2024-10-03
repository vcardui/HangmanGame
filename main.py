import random
import hangman_art
import hangman_words

print(f'{hangman_art.logo}')

chosen_word = random.choice(hangman_words.word_list)

chosen_word_num = len(chosen_word)
#print(chosen_word)

game_progress = []

for letters in chosen_word:
    game_progress.append("_")

print(''.join(game_progress))

user_lives = 7

gameOver = False

while gameOver == False:
  user_guess = input("\nGuess a letter: ").lower()

  right_letter_guess = False

  i = 0
  while i < chosen_word_num:
    if chosen_word[i] == user_guess:
      game_progress[i] = user_guess
      right_letter_guess = True
      i += 1
    else:
      i += 1

  if right_letter_guess == True:
    missing_blanks = 0
    a = 0
    while a <= (len(game_progress) - 1):
      if game_progress[a] == "_":
        missing_blanks += 1
        a += 1
      else:
        a += 1
  

    if missing_blanks == 0:
      print(''.join(game_progress))
      print("\nCongratualions. You have won!")
      gameOver = True
    else:
      print(''.join(game_progress))
    
  else:
    user_lives -= 1
    print(f"Letter {user_guess} isn't in the word. You have {user_lives} lives left.")
    print(f'{hangman_art.stages[user_lives]}')

    if user_lives == 0:
      print("Too sad. You have lost :( \n GAME OVER")
      print(f"The word was: {chosen_word}")
      gameOver = True
