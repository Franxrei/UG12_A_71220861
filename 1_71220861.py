deretawal = int(input("Masukan Awal Deret : "))
deretakhir = int(input("Masukan Akhir Deret : "))
for i in range(deretawal, deretakhir):
    if (i%2!=0):
        if (i%6==0 or i%3==0): 
            continue
        else:
            print(i, end=" ")