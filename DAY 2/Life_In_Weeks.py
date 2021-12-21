age = input("Masukkan umur anda: ")

# max umur hidup 90 thn
int_age = int(age)
final_age = 90 - int_age
days = 365 * int_age
weeks = 52 * int_age
month = 12 * int_age
print(f"Sisa hidupmu adalah {days} hari, {weeks} minggu, {month} bulan.")
