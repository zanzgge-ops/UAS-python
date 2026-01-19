satuan = "cm"
#fungsi(def)
def persegi():
    sisi = int(input("masukkan sisi: "))
    luas_persegi = sisi * sisi
    keliling_persegi = sisi * 4
    print("<=================================================>")
    print("luas persegi panjang adalah", luas_persegi,satuan,"dan keliling persegi panjang adalah", keliling_persegi,satuan)

def persegi_panjang():
    panjang = int(input("masukkan panjang: "))
    lebar = int(input("masukkan lebar: "))
    luas_persegi_panjang = panjang * lebar  
    keliling_persegi_panjang = 2 * (panjang + lebar)
    print("<==========================================>")
    print("luas persegi panjang adalah", luas_persegi_panjang,satuan,"dan keliling persegi panjang adalah", keliling_persegi_panjang,satuan)

def segitiga():
    alas = int(input("masukkan alas: "  ))
    sisi2 = int(input("masukkan sisi 2: " ))
    sisi3 = int(input("masukkan sisi 3: "))
    tinggi = int(input("masukkan tinggi: "))
    luas_segitiga = (alas * tinggi) / 2
    keliling_segitiga = alas + sisi2 + sisi3
    print("<==================================>")
    print("luas segitiga adalah",luas_segitiga,satuan,"dan keliling segitiga adalah",keliling_segitiga,satuan)

def lingkaran():
    jari_jari = int(input("masukkan jarijari: "))
    luas_linkaran = (22 / 7) * jari_jari * jari_jari
    keliling_lingkaran = 2 * (22 / 7) * jari_jari
    print("<==================================>")
    print("luas lingkaran adalah",luas_linkaran,satuan,"dan keliling lingkaran adalah",keliling_lingkaran,satuan)

def jajargenjang():
    miring = int(input("masukkan miring: "))
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    luas_jajargenjang = alas *  tinggi
    keliling_jajargenjang = (alas * tinggi) * 2
    print("<======================================>")
    print("luas jajargenjang adalah",luas_jajargenjang,satuan,"dan keliling jajargnejnag adalah", keliling_jajargenjang,satuan)

def trapesium():
    sisi_atas = int(input("masukkan sisi atas: "))
    sisi_bawah = int(input("masukkan sisi bawah: "))
    sisi_kanan = int(input("masukka sisi kanan: "))
    sisi_kiri = int(input("masukkan sisi kiri: "))
    tinggi = int(input("masukkan tinggi: "))
    luas_trapesium = 0.5 * tinggi * (sisi_atas + sisi_bawah)
    keliling_trapesium = sisi_atas + sisi_bawah + sisi_kanan + sisi_kiri
    print("<====================================>")
    print("luas trapesium adalah", luas_trapesium,satuan,"dan keliling trapesium adalah", keliling_trapesium,satuan)

#array
bangun_datar = ["1. persegi", "2. persegi panjang", "3. segitiga", "4. lingkaran", "5. jajargenjang", "6. trapesium"]
print("<===========================================>")
nama = input("Masukkan Nama Anda: ")
print("<===========================================>")
#perulangan while
while True:
    print("silahkan pilih bangun datar: ")
    print("<============================>")
    for item in bangun_datar:
        print(item)
    print("<=======================================>")
    pilih = input("silahkan pilih bangun datar, pilih 1-6: ")
    print("<=======================================>")
    #control flow
    
    if pilih == "1":
        print("Anda memilih bangun datar", bangun_datar[0])
        print("<==================================>")
        persegi()
    elif pilih == "2":
        print("Anda memilih bangun datar", bangun_datar[1])
        print("<==========================================>")
        persegi_panjang()
    elif pilih == "3":
        print("Anda memilih bangun datar", bangun_datar[2])
        print("<===================================>")
        segitiga()
    elif pilih == "4":
        print("Anda memilih bangun datar", bangun_datar[3])
        print("<====================================>")
        lingkaran()
    elif pilih == "5":
        print("Anda memilih bangu datar", bangun_datar[4])
        print("<======================================>")
        jajargenjang()
    elif pilih == "6":
        print("Anda memilih bangun datar", bangun_datar[5])
        print("<=====================================")
        trapesium()
    else:
        print("!!!!!!!!!!!!!!! PERHATIAN !!!!!!!!!!!!!!!")
        print("pilihan tidak tersedia, silahkan pilih 1-6")
        print("!!!!!!!!!!!!!!! PERHATIAN !!!!!!!!!!!!!!!")
        print("<=======================================>")
        continue

    print("<==================================================>")
    lagi = input("apakah anda ingin menghitung yang lain? ketik y/n: ")
    print("<==================================================>")
    if lagi.lower() != "y":
        print("terima kasih", nama)
        break