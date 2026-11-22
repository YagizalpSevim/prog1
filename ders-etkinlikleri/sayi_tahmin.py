import random

sayi = random.choice(range(1, 101))
deneme = 0

print("1 ile 100 arasında sayıyı tahmin edebilecek misin?")

while True:
    tahmin = int(input("Tahminin: "))
    deneme += 1
    fark = abs(sayi - tahmin)

    if tahmin == sayi:
        print(f"Tebrikler! {deneme}. denemede sayıyı ({sayi}) buldunuz")
        break
    
    ipucu = "Daha büyük bir sayı dene" if tahmin < sayi else "Daha küçük bir sayı dene"

    if fark <= 5:
        print(f"Çok yaklaştın (Yanıyorsun)! {ipucu}")
    elif fark <= 15:
        print(f"Yaklaştın (Sıcak). {ipucu}")
    elif fark <= 30:
        print(f"Fena değil (Ilık). {ipucu}")
    else:
        print(f"Çok uzaksın (Soğuk). {ipucu}")