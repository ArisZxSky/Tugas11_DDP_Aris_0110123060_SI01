def persegi(sisi):
    luas = sisi*sisi
    keliling = 4 * sisi
    print("Luas Persegi: ", luas)
    print("Keliling Persegi: ", keliling)

def persegi_panjang(panjang,  lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("luas persegi panjang: ", luas)
    print("keliling persegi panjang: ", keliling)

def segitiga_sama_sisi(alas, tinggi):
    luas = 0.5 * alas * tinggi
    keliling = 3 * alas
    print("Luas Segitiga sama sisi: ", luas)
    print("keliling segitiga sama sisi: ", keliling)

def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling =( 2 * alas) + (2 * sisi_miring)
    print("Luas jajar genjang: ", luas)
    print("Keliling jajar genjang: ", keliling)

def lingkarang(jari):
    phi = 3.14
    luas = phi * jari * jari
    keliling = 2 * phi ** jari
    print("Luas lingkarang: ", luas)
    print("keliling lingkarang: ", keliling)

def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("Luas belah ketupat: ", luas)
    print("keliling belah ketupat: ", keliling)

def layang_layang(diagonal1, diagonal2, sisi_atas, sisi_bawah):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = (2 * sisi_atas) + (2 * sisi_bawah)
    print("Luas layang layang: ", luas)
    print("keliling layang layang: ", keliling)