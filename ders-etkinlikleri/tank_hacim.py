import math

yaricap = float(input("Tankın yarıçapını giriniz(metre):"))
yükseklik = float(input("Tankın yüksekliğini giriniz(metre):"))

hacim = math.pi * yaricap**2 * yükseklik
litre = hacim * 1000

print(f"Hacim: {hacim:.2f} m³")
print(f"Hacim: {litre:.2f} litre")
