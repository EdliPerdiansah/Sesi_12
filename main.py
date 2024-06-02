# Nama  : Edli Perdiansah
# NIM   : 20230040033
# Kelas : TI23C

from luas.persegi import luas_persegi
from luas.segitiga import luas_segitiga
from luas.lingkaran import luas_lingkaran
from volume.bola import volume_bola
from volume.kubik import volume_kubik
from volume.trapesium import volume_trapesium

def menu():
    print('======Menu Untuk Menghitung=====')
    print('1. Menghitung luas persegi')
    print('2. Menghitung luas segitiga')
    print('3. Menghitung luas lingkaran')
    print('4. Menghitung volume bola')
    print('5. Menghitung volume kubik')
    print('6. Menghitumg volume trapesium')
    print('0. Exit\n')
    
def main():
    while True:
        menu()
        pilihan = input("Masukan pilihan anda")
        
        if pilihan == "1":
            sisi = float(input("Masukan Panjang sisi persegi: "))
            hasil = luas_persegi(sisi)
            print("Luas persegi dengan sisi", sisi, "adalah :", hasil)
        elif pilihan == "2":
            alas = float(input("Masukan Panjang alas segitiga: "))
            tinggi = float(input("Masukan tinggi segitiga: "))
            hasil = luas_segitiga(alas, tinggi)
            print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah :", hasil)
        elif pilihan == "3":
            jari = float(input("Masukan pangjang jari-jari lingkaran: "))
            hasil = luas_lingkaran(jari)
            print("Luas Lingkaran dengan jari-jari", jari, "adalah : ", hasil)
        elif pilihan == "4":
            jari = float(input("Masukan panjang jari-jari bola :"))
            hasil = volume_bola(jari)
            print("Volume bola dengan jari-jari bola", jari, "adalah :", hasil)
        elif pilihan == "5":
            sisi = float(input("Masukan panjang sisi kubik :"))
            hasil = volume_kubik(sisi)
            print("Volume kubik dengan sisi", sisi, "adalah :", hasil)
        elif pilihan == "6":
            tinggi = float(input("Masukan tinggi trapesium :"))
            alas1 = float(input("Masukan panjang alas atas trapesium :"))
            alas2 = float(input("Masukan panjang alas bawah trapesium :"))
            hasil = volume_trapesium(tinggi, alas1, alas2)
            print("Volume trapesium dengan tinggi", tinggi, "alas atas", alas1, "dan alas bawah", alas2, "adalah :")
        elif pilihan == "0":
            print("terimakasih telah berkunjung")
            break
        else :
            print("Maaf, Pilihan anda tidak ada. Silahkan Coba Kembali.")
            
    if __name__== "__main__":
        main()  