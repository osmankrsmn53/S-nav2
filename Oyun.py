while True:
    oyunbaslama=input("oyun başlatılsınmı?:")
    if oyunbaslama=="evet":
       print("oyun başlatıldı")
    elif oyunbaslama == "hayır":
         print ("oyun sona erdi")
         break
    oyunadevametme=input("oyuna devam edecek misin: ")
    if oyunadevametme=="evet":
       print ("oyun devam ediyor")
    elif oyunadevametme == "hayır":
         print("oyun sona erdi")
         break
    else:
         print("Yanlış Cvp evet/hayır yazın")
