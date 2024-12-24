toplam=0
sayac=0
while True:
    sayi=int(input("Bir sayı giriniz:"))
    if sayi == 1:
        break
    toplam += sayi
    sayac+=1

if sayac > 0:
    print("sayıların ortalaması",toplam / sayac)
