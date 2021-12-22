import math


def paint_calc(height, width, cover):
    # Disini saya menggunakan math.ceil untuk membulatkannya ke angka yang lebih besar. contoh (2.3 menjadi 3)
    hasil = math.ceil((test_h * test_w) / coverage)
    print(f"You'll need {hasil} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)