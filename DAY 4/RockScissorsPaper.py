# ///Heads Or Tails///

# import random
# all_list = ["Heads", "Tails"]
# player_input = str(
#     input('Pilih diantara kedua pilihan berikut.\n"Heads" atau "Tails"\n'))
# feed = random.randint(0, 1)
# print("Hasilnya adalah\n"+all_list[feed])


# ///Roulette///

# import random
# name = input("Masukkan nama: ")
# names = name.split(", ")
# name_len = len(names)
# hasil = random.randint(0, name_len)
# print("Yang harus membayar adalah "+names[hasil])


# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = row1, row2, row3
# print(f"{row1}\n{row2}\n{row3}")

# position = (input("Masukkan posisi yang kamu inginkan: "))

# vertical = int(position[0])
# horizontal = int(position[1])
# map[vertical-1][horizontal-1] = "x"
# print(f"{row1}\n{row2}\n{row3}")


# ///Batu Gunting Kertas///

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]
player_input = int(input(
    'Masukkan pilihan anda.\nPilih "0" untuk batu.\nPilih "1" untuk kertas.\nPilih "2" untuk gunting\n'))
print(image[player_input])

computer_input = random.randint(0, 2)
print(image[computer_input])
