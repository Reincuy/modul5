def maksimal(a, b):
    return a if a > b else b

def minimal(a, b):
    return a if a < b else b

bilangan = int(input("Masukkan jumlah bilangan: "))
maks = -100000
minim = 100000

for _ in range(bilangan):
    nilai = int(input("Masukkan nilai: "))
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)

print(f"Output: {maks} {minim}")
