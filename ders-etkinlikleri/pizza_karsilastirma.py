import math

cap1 = float(input("1.pizzanın çapını giriniz: "))
fiyat1 = float(input("1.pizzanın fiyatını giriniz: "))
cap2 = float(input("2.pizzanın çapını giriniz: "))
fiyat2 = float(input("2.pizzanın fiyatını giriniz: "))

yaricap1, yaricap2 = cap1 / 2, cap2 / 2
alan1, alan2 = math.pi * yaricap1 ** 2, math.pi * yaricap2 ** 2
birim1, birim2 = fiyat1 / alan1, fiyat2 / alan2

print("=" * 55)
print(f"{'Özellik':<25}{'1. Pizza':>15}{'2. Pizza':>15}")
print("-" * 55)
print(f"{'Alan (cm²)':<25}{alan1:>15.1f}{alan2:>15.1f}")
print(f"{'Birim Fiyat (TL/cm²)':<25}{birim1:>15.2f}{birim2:>15.2f}")
print("=" * 55)
