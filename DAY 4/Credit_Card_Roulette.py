import random
print("Selamat datang di program credit card roulette")
name = input("Masukkan nama: ")
names = name.split(", ")
sub = len(names)
a = random.randint(0, sub - 1)
b = names[a]
print("Yang akan membayar adalah: ", b)
