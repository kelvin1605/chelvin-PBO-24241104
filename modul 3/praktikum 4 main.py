class Ayah:
    def __init__(self, nama_ayah):
        # Simpan nama ayah pada objek
        self.nama_ayah = nama_ayah

    def bekerja(self):
        # Method untuk menunjukkan ayah sedang bekerja
        print(f"{self.nama_ayah} sedang bekerja.")


class Ibu:
    def __init__(self, nama_ibu):
        # Simpan nama ibu pada objek
        self.nama_ibu = nama_ibu

    def memasak(self):
        # Method untuk menunjukkan ibu sedang memasak
        print(f"{self.nama_ibu} sedang memasak.")


# Anak mewarisi dari Ayah dan Ibu (multiple inheritance)
class Anak(Ayah, Ibu):
    def __init__(self, nama_anak, nama_ayah, nama_ibu):
        # Inisialisasi bagian Ayah dari objek Anak
        Ayah.__init__(self, nama_ayah)
        # Inisialisasi bagian Ibu dari objek Anak
        Ibu.__init__(self, nama_ibu)
        # Simpan nama anak
        self.nama_anak = nama_anak

    def bermain(self):
        # Method khusus Anak
        print(f"{self.nama_anak} sedang bermain.")


# Membuat instance Anak
budi = Anak("Budi", "Hendra (Ayah)", "Wati (Ibu)")

# Memanggil method-method yang diwarisi/dimiliki object budi
budi.bekerja()   # dari Ayah
budi.memasak()   # dari Ibu
budi.bermain()   # dari Anak
