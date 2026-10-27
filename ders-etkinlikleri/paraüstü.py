paraüstü = int(input("Paraüstünü giriniz: "))

yirmitl = paraüstü // 20
yirmitlx = paraüstü % 20
ontl =  yirmitlx // 10
ontlx = yirmitlx % 10
bestl = ontlx // 5
bestlx = ontlx % 5
birtl = bestlx // 1

print(f"20TL: {yirmitl} tane ,10TL {ontl} tane, 5TL {bestl} tane , 1TL: {birtl} tane")