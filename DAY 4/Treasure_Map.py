row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input(
    "Masukkan posisi yang ingin kamu dapatkan untuk mengubur harta karun? ")

# if position == "11":
#     row1[0] = "x"
# if position == "12":
#     row2[0] = "x"
# if position == "13":
#     row3[0] = "x"

# if position == "21":
#     row1[1] = "x"
# if position == "22":
#     row2[1] = "x"
# if position == "23":
#     row3[1] = "x"

# if position == "31":
#     row1[2] = "x"
# if position == "32":
#     row2[2] = "x"
# if position == "33":
#     row3[2] = "x"

vertical = int(position[0])
horizontal = int(position[1])
map[vertical-1][horizontal-1] = "x"

print(f"{row1}\n{row2}\n{row3}")
