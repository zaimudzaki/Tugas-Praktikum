import random
# GAME TEBAK ANGKA
#looping program berjalan
while( True ) :
    start= input("\nKetik [mulai] :")
    while(start!= "mulai" ) :
        start= input ("\nMaaf inputan anda salah. Silahkan coba lagi.\n")
    if start== "mulai" :
        kesempatan = 8
        angka_tebakan = random.randint(1,20)
    print ( "\nKesempatan menebak :", kesempatan, "\nAnda harus memilih angka antara 0 dan 21\n" )
    #looping tebak angka
    while (kesempatan >= 0) :
        if kesempatan == 0 :
            print("Angkanya :", angka_tebakan)
            print("Maaf anda belum beruntung")
            break
        else :
            
            tebak = int(input("Masukkan angka : "))
            if tebak == angka_tebakan :
                print("anda Benar: angka tebakan adalah :", angka_tebakan)
                break
            elif tebak > angka_tebakan :
                 print("\nAngkanya di bawah", tebak)
                 kesempatan -=1
            elif tebak < angka_tebakan :
                 print("\nAngkanya di atas", tebak)
                 kesempatan -=1
        print("\nKesempatan menebak :", kesempatan)

    #konfirmasi ulang
    ulang = input("\nMau main lagi? [y/n]: \n")
    while( ulang != "y" and ulang != "n") :
        ulang = input("Maaf inputan anda salah. \nSilahkan coba lagi.\nMau main lagi? : ")

    if ulang == "y" :
        print("\nSilahkan main lagi.\n")
    elif ulang == "n" :
        print("\nTerimakasih sudah main.\n")
        break
