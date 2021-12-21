print("Selamat datang di program mencari nilai terbesar")
student_score = input("Masukkan nilai siswa ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

highest = 0
for high in student_score:
    if high > highest:
        highest = high
print(f"Nilai terbesar adalah: {highest}")
