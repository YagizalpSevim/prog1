mesafe = float(input("Mesafe giriniz (km): "))
dakika = float(input("Süre giriniz (dk): "))

tempo = mesafe / dakika
print(f"Ortalama hız: {mesafe / (dakika / 60):.2f} km/sa")
print(f"Tempo: Dakikada", tempo, "km")