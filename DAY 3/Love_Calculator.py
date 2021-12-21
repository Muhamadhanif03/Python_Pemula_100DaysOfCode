print("""
      _____$$$$_________$$$$
___$$$$$$$$_____$$$$$$$$
_$$$$$$$$$$$$_$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$$$$$$$$$$$
__$$$$$$$$$$$$$$$$$$$$$$$
____$$$$$$$$$$$$$$$$$$$
_______$$$$$$$$$$$$$
__________$$$$$$$
____________$$$
_____________$
      """)
print("Selamat datang di program TRUE LOVE")
name1 = str(input("Masukkan nama anda: "))
name2 = str(input("Masukkan nama pasangan anda: "))

nama = name1.lower() + name2.lower()
t = nama.count("t")
r = nama.count("r")
u = nama.count("u")
e = nama.count("e")

l = nama.count("l")
o = nama.count("o")
v = nama.count("v")
e = nama.count("e")

true = t + r + u + e
love = l + o + v + e
hasil = str(true) + str(love)
if int(hasil) <= 10 or int(hasil) >= 90:
    print(f"Score anda adalah {hasil}, hubungan anda seperti cola dan mentos.")
elif int(hasil) >= 40 and int(hasil) <= 50:
    print(f"Score anda adalah {hasil}, hubungan anda baik-baik saja.")
else:
    print(f"Score anda adalah {hasil}.")

#true = nama.count("t", "r", "u", "e")
#love = nama.count("l", "o", "v", "e")

# nama1 = name1.lower().count("t") + name1.lower().count("r") + name1.lower().count("u") + name1.lower().count("e") + name2.lower().count("t") + name2.lower().count("r") + name2.lower().count("u") + name2.lower().count("e")

# nama2 =name1.lower().count("l") + name1.lower().count("o") + name1.lower().count("v") + name1.lower().count("e") + name2.lower().count("l") + name2.lower().count("o") + name2.lower().count("v") + name2.lower().count("e")

# jumlah = str(nama1) + str(nama2)

# if int(jumlah) <= 10 or int(jumlah) >= 90:
#     print(f"Your score is {jumlah}, you go together like coke and mentos.")
# elif int(jumlah) >= 40 and int(jumlah) <= 50:
#     print(f"Your score is {jumlah}, you are alright together.")
# else:
#     print(f"Your score is {jumlah}.")
