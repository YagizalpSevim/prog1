tüketim = float(input("Aylık tüketimi girin(kWh): "))
fiyat = float(input("Birim fiyatı girin: "))

fatura = tüketim * fiyat
kdv = fatura * (20 / 100)
toplam = fatura + kdv

print(f"Vergisiz fiyat: {fatura:.2f} TL")
print(f"KDV(%20): {kdv:.2f} TL")
print(f"Toplam tutar: {toplam:.2f} TL")

