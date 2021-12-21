print("---Selamat datang di program BILL---")
bill = float(input("Silahkan masukkan jumlah bill: $"))
tip = int(input("Silahkan masukkan tip: %"))
jmlh_orang = int(input("Silahkan masukkan jumlah orang: "))
total_tip = tip/100
ttl_tip = total_tip * bill
jmlh_bill = bill + ttl_tip
hasil = jmlh_bill / jmlh_orang
print("Masing-masing harus membayar: ", round(hasil, 2))
