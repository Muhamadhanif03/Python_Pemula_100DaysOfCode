# year = int(input("Masukkan tahun: "))
# if year % 4 != 0:
#     print("Not leap year.")
# elif year % 100 != 0:
#     print("Leap year.")
# elif year % 400 == 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")

print("Selamat datang di program Leap Year")
year = int(input("Masukkan tahun: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
