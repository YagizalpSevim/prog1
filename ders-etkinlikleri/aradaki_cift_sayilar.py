baslangic = int(input("başlangıç gir: "))
bitis = int(input("bitis gir: "))

if baslangic > bitis:
    baslangic, bitis = bitis, baslangic

if baslangic % 2 != 0:
    baslangic += 1

while baslangic <= bitis:
    print(baslangic)
    baslangic += 2