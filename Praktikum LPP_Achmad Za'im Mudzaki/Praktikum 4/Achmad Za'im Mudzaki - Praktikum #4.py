import random

#Daftar ini memberikan gambaran tentang waktu acara.
Kalimat_starter = random.randint(1, 3)
if Kalimat_starter == 1 :
    kalimat_1 = ("Pada pagi hari yang cerah")
if Kalimat_starter == 2 :
    kalimat_1 = ("Pada siang hari yang terik ")
if Kalimat_starter == 3 :
    kalimat_1 = ("Pada malam hari yang sendu ")

#Daftar ini menceritakan tentang karakter utama dari cerita ini.
karakter = random.randint(1, 3)
if karakter == 1 :
    kalimat_2 = ("Zaim sedang ngopi ")
if karakter == 2 :
    kalimat_2 = ("Zaim sedang makan ")
if karakter == 3 :
    kalimat_2 = ("Zaim sedang menonton acara olahraga ")

#Daftar ini menentukan hari yang tepat di mana beberapa insiden telah terjadi.
waktu = random.randint(1, 3)
if waktu == 1 :
    kalimat_3 = ("dan pada hari ini di hari sabtu, ia akan bersantai")
if waktu == 2 :
    kalimat_3 = ("dan pada hari ini di hari senin hari ia akan menyapu ")
if waktu == 3 :
    kalimat_3 = ("dan pada hari ini hari rabu ia akan mengerjakan tugas ")

#Daftar ini mendefinisikan plot cerita.
story_plot = random.randint(1, 3)
if story_plot == 1 :
    kalimat_4 = ("karena hari libur, ")
if story_plot == 2 :
    kalimat_4 = ("karena ia sedang tidak sibuk, ")
if story_plot == 3 :
    kalimat_4 = ("karena tidak ada hal yang dialakukan, ")

#Daftar ini mendefinisikan tempat di mana insiden itu terjadi.
tempat = random.randint(1, 3)
if tempat == 1 :
    kalimat_5 = ("ia mengerjakanya di teras, ")
if tempat == 2 :
    kalimat_5 = ("ia mengerjakan di dapur, ")
if tempat == 3 :
    kalimat_5 = ("ia mengerjakan di kamar, ")

#Daftar ini mendefinisikan karakter kedua dari cerita.
second_character = random.randint(1, 3)
if second_character == 1 :
    kalimat_6 = ("sedangkan ayah membaca koran ")
if second_character == 2 :
    kalimat_6 = ("sedangkan ibu sedang memasak ")
if second_character == 3 :
    kalimat_6 = ("sedangkan paman sedang olahraga ")

#Daftar ini mendefinisikan usia karakter kedua.
usia = random.randint(1, 3)
if usia == 1 :
    kalimat_7 = ("karena usianya sudah 60 tahun ")
if usia == 2 :
    kalimat_7 = ("karena usianya sudah 61 tahun ")
if usia == 3 :
    kalimat_7 = ("karena usianya sudah 62 tahun ")

#Daftar ini menceritakan tentang pekerjaan yang dilakukan karakter kedua.
pekerjaan = random.randint(1, 3)
if pekerjaan == 1 :
    kalimat_8 = ("karena ia sudah tidak bekerja lagi.")
if pekerjaan == 2 :
    kalimat_8 = ("karenanya ia hanya membuka toko didepan rumah ")
if pekerjaan == 3 :
    kalimat_8 = ("karenanya ia hanya tidak lagi melanjutkan pekerjaan kantornya ")

print (kalimat_1, kalimat_2, kalimat_3, kalimat_4, kalimat_5, kalimat_6, kalimat_7, kalimat_8)