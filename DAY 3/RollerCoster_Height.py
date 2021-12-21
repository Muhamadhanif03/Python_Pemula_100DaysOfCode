print("--Selamat datang di program ukur tinggi badan roller coster--")
height = int(input("Masukkan tinggi badan anda dalam cm: "))
bill = 0
if height > 120:
    print("Selamat, anda dapat menaiki wahana ini.")
    usia = int(input("Masukkan usia anda: "))
    if usia < 12:
        bill = 5
        print("Tiket untuk dibawah 12 tahun adalah $5")
    elif usia < 18:
        bill = 8
        print("Tiket untuk dibawah 18 tahun adalah $8")
    else:
        bill = 12
        print("Tiket untuk diatas 18 tahun adalah $12")
    want_photo = input(
        'Apakah anda ingin tambahan foto?\nTambahan foto dikenakan biaya tambahan $3\nMasukkan "y" atau "n"')
    if want_photo == "y":
        bill += 3
    print(f"Biaya total anda adalah {bill}")
else:
    print("Anda tidak diperbolehkan untuk menaiki wahana ini")
