ürün = int(input("Ürün adetini giriniz: "))
kapasite = int(input("Bir koliye kaç ürün sığdığını giriniz: "))

tam_koli = ürün // kapasite
artan_ürün = ürün % kapasite
toplam_koli = tam_koli + (1 if artan_ürün > 0 else 0)

print(f"Tam dolan koli sayısı: {tam_koli}")
print(f"Artan ürün sayısı: {artan_ürün}")
print(f"Toplam gereken koli sayısı: {toplam_koli}")