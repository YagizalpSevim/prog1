mesafe = float(input("Mesafe giriniz (km): "))
dakika = float(input("Süre giriniz (dk): "))

tempo = dakika / mesafe
saniye = tempo * 60

print(f"Ortalama hız: {mesafe / (dakika / 60):.2f} km/sa")
print(f"1 km için geçen süre(Tempo): {tempo:.2f} dk/km yani 1 km = {saniye:.2f} saniye")
