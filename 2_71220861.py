n = str(input("Masukan Nama : "))
x = len(n)
for i in range(x):
    for y in range(i+1):
        print (n[y],end='')
    print()
for i in range(x,0,-1):
    for y in range(0,i-1):
        print (n[y],end='')
    print()