ad = input("Yolcunun adı: ").strip().title()
km = float(input("Gidilen yol (km): "))
saat = int(input("Biniş saati (0-23): "))

ucret = 45 + km * 32.5
gece = saat >= 23 or saat < 6
if gece:
    ucret = ucret * 1.5
if ucret < 150:
    ucret = 150

tarife = "Gece" if gece else "Gündüz"
print("=" * 28)
print(f"{'Yolcu':<12}{ad:>16}")
print(f"{'Mesafe':<12}{km:>13.1f} km")
print(f"{'Tarife':<12}{tarife:>16}")
print("-" * 28)
print(f"{'ÖDENECEK':<14}{ucret:>13.2f} TL")
print("=" * 28)