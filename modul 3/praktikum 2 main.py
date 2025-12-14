# Parent class
class Kendaraan:
    def __init__(self, nama):
        print("-> (Parent __init__ dipanggil)")   # Menandakan constructor parent dipanggil
        self.nama = nama                           # Simpan nama kendaraan


# Child class (inherit dari Kendaraan)
class Mobil(Kendaraan):
    def __init__(self, nama, jumlah_pintu):
        print("-> (Child __init__ dipanggil)")     # Menandakan constructor child dipanggil

        super().__init__(nama)                     # Memanggil constructor parent
                                                   # Agar self.nama dapat digunakan

        self.jumlah_pintu = jumlah_pintu           # Menambahkan atribut khusus mobil
        print(f"    -> Mobil {self.nama} dengan {self.jumlah_pintu} pintu dibuat.")


# Membuat objek Mobil
xenia = Mobil("Xenia Hitam", 4)

# Mengakses atribut object
print(f"Nama object: {xenia.nama}")
