def Biodata(tahun_lahir, namaku, asal):
    tahun_sekarang = 2020
    usia = tahun_sekarang - tahun_lahir

    print(f"Perkenalkan Nama Saya: {namaku}")
    print(f"Umur Saya: {usia}")
    print(f"Saya Adalah Angkatan: {tahun_sekarang}")
    print(f"Asal Saya dari: {asal}")

def main():
    tahun_lahir = int(input())
    namaku = input()
    asal = input()

    Biodata(tahun_lahir, namaku, asal)

if __name__ == "__main__":
    main()
