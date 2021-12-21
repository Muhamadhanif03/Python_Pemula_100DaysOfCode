import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# word = ["asu", "puki", "djancok"]
# MASUKKAN KATA TANPA ADANYA TANDA KOMA (HANYA MENGGUNAKAN TANDA SPASI)
input_word = input("Masukkan kata: ")
word = input_word.split()
choosen_word = random.choice(word)

lives = 6

print(f"contekan {choosen_word}")

display = []
for each in range(len(choosen_word)):
    display += "_"
# print(display)

# guess = input("Tebak kata: ").lower()

end_of_game = False

while not end_of_game:
    guess = input("Tebak kata: ").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in choosen_word:
        lives -= 1
        print(lives)
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
# for answer in choosen_word:
#     if answer == guess:
#         print("Right")
#     else:
#         print("Wrong")
    print(stages[lives])
