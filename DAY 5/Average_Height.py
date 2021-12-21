student_height = input("Masukkan tinggi siswa ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

total_height = 0
for heigh in student_height:
    total_height += heigh
# print(total_height)
total_student = 0
for student in student_height:
    total_student += 1
# print(total_student)
hasil = total_height/total_student
print(round(hasil))
