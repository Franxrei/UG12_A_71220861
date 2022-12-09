pembatas = int(input("Masukan Pembatas : "))
angka_terlarang = int(input("Masukan Angka yang dilarang : "))
for i in range(pembatas):
    if(i==angka_terlarang):
        continue
    else:
        print(i, end=" ")