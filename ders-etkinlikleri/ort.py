not1 = float(input("1.not: "))
not2 = float(input("2.notunuz: "))
not3 = float(input("3. notunuz: "))
not4 = float(input("4.notunuz: "))
ortalama = (not1 + not2 + not3 + not4) / 4

if ortalama >= 50:
    print(f"tebrikler {ortalama:.2f}")
else:
    print(f"kaldınız {ortalama:.2f}", round(ortalama , 2))