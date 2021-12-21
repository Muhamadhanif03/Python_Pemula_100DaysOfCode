import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Selamat datang di password generator")
let = int(input("Mau berapa huruf yang ada di passwordmu? "))
num = int(input("Mau berapa angka yang ada di passwordmu? "))
sym = int(input("Mau berapa simbol yang ada di passwordmu? "))

password = []
for i in range(1, let + 1):
    password.append(random.choice(letters))

# print(huruf)

for n in range(1, num + 1):
    password += random.choice(numbers)

# print(nomor)

for s in range(1, sym + 1):
    password += random.choice(symbols)

# print(simbol)

password_a = ""
random.shuffle(password)
for each in password:
    password_a += each
print(password_a)
