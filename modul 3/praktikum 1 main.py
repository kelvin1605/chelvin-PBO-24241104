class Kendaraan:
    def __init__(self, nama):
        # Set atribut nama untuk setiap instance kendaraan
        self.nama = nama
        # Tampilkan pesan saat objek dibuat
        print(f"Sebuah Kendaraan '{self.nama}' dibuat.")

    def maju(self):
        # Method untuk menandakan kendaraan bergerak maju
        print(f"{self.nama} bergerak maju.")


class Mobil(Kendaraan):
    def putar_AC(self):
        # Method khusus untuk Mobil: menyalakan AC
        print(f"{self.nama}: AC dinyalakan, sejuk!")


print("--- Membuat Object Mobil ---")
# Membuat instance Mobil; __init__ diwarisi dari Kendaraan
avanza = Mobil("Avanza Putih")
# Panggil method yang diwarisi dari Kendaraan
avanza.maju()
# Panggil method khusus Mobil
avanza.putar_AC()
