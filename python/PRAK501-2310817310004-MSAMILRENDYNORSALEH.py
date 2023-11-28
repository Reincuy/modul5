def MaxBilangan(a, b, c, d):
    max1 = a if a > b else b
    max2 = c if c > d else d
    return max1 if max1 > max2 else max2

if __name__ == "__main__":
    a,b,c,d = map(int, input().split())
    hasil = MaxBilangan(a,b,c,d)
    print(hasil)
