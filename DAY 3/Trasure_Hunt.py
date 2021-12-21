print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("---Selamat datang di games berburu harta karun---\n---Tugasmu adalah untuk menemukan harta karun---")
kn_kr = input(
    'Kamu melihat ada 2 jalan di depanmu. Kamu harus memilih jalan "kanan" atau "kiri"\n').lower()
if kn_kr == "kiri":
    asu = input('Kamu bertemu dengan sebuah danau, dan kamu melihat sebuah perahu namun perahu tersebut berjarak jauh dengan kamu.\nApakah kamu ingin "menunggu" atau "tidak"?\n').lower()
    if asu == "menunggu":
        aa = input('Selamat! Kamu telah sampai di sebuah pulau.\nKamu dihadapkan dengan 3 pintu berwarna "merah", "kuning", dan "hijau". Kamu diwajibkan untuk memilih salah satu dari ketiga pintu tersebut!\n').lower()
        if aa == "merah":
            print("Mampus! kamu bertemu dengan Om Burhan.\n---Game Over---")
        elif aa == "hijau":
            print("Kamu masuk kedalam ruangan yang dipenuhi oleh api.\n---Game Over---")
        elif aa == "kuning":
            print("Selamat! Kamu menemukan harta karun.")
        else:
            print("Masukkan pilihan yang benar!")
    else:
        print("Kamu dimakan buaya.\n---Game Over---")
else:
    print("Kamu terjatuh kedalam sebuah jurang, dan perjalananmu berakhir disini.\n ---Game Over---")
