print("Selamat datang di program hitung berat badan")
height = float(input("Masukkan tinggi badan anda: "))
weight = float(input("Masukkan berat badan anda: "))
r_hasil = round(weight/height ** 2)
if r_hasil < 18.5:
    print(
        f"Berat badan anda adalah {r_hasil}, dan anda seperti orang yang kekurangan gizi.")
elif r_hasil > 18.5 and r_hasil < 25:
    print(
        f"Berat badan anda adalah {r_hasil}, dan anda memiliki berat badan yang normal.")
elif r_hasil > 25 and r_hasil < 30:
    print(
        f"Berat badan anda adalah {r_hasil}, dan anda sedikit kelebihan berat badan.")
elif r_hasil > 30 and r_hasil < 35:
    print(
        f"Berat badan anda adalah {r_hasil}, dan anda kelebihan berat badan.")
else:
    print(f"Berat badan anda adalah {r_hasil}, dan anda terkena obesitas")
