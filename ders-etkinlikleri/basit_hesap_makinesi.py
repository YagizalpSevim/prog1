def toplama(sayi1, sayi2):
    return sayi1 + sayi2
def cikarma(sayi1, sayi2):
    return sayi1 - sayi2
def bolme(sayi1, sayi2):
    if sayi2 == 0:
        return("Tanımsız (Sıfıra bölünemez)")
    return sayi1 / sayi2
def carpma(sayi1, sayi2):
    return sayi1 * sayi2

print("İşlemler:\n"
      "1. Toplama\n"
      "2. Çıkartma\n"
      "3. Çarpma\n"
      "4. Bölme\n"
      "5. Çıkış\n")

while True:
    secim = int(input("İşlem seçiniz(1-5): "))

    if secim == 5:
        print("Çıkış yapılıyor...")
        break

    sayi1 = int(input("Sayı 1: "))
    sayi2 = int(input("Sayı2: "))

    if secim == 1:
         print(sayi1, "+",sayi2, "=", toplama(sayi1, sayi2))
    elif secim == 2:
        print(sayi1, "-",sayi2, "=", cikarma(sayi1, sayi2))
    elif secim == 3:
        print(sayi1, "*",sayi2, "=", carpma(sayi1, sayi2))
    elif secim == 4:
        print(sayi1, "/",sayi2, "=", bolme(sayi1, sayi2))
    else:
        print("Geçersiz seçim.")