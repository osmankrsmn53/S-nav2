denemesayisi=0
while True:
    sifre=input("Şifreyi giriniz:")
    denemesayisi+=1
    if sifre=="Python":
        print("Giriş Başarılı")
        print(denemesayisi,"tekrarda girdiniz")
        break
    else:
        print("tekrar deneyiniz")
