
# ==========================================
# LATIHAN 03 - METHOD DICTIONARY
# Algoritma dan Pemrograman | Pertemuan 11
# ==========================================

mahasiswa = {
    "nama": "Umul Hani",
    "nim": "2225250189",
    "kelas": "3F"
}

print("Daftar key:")
print(list(mahasiswa.keys()))

print("\nDaftar value:")
print(list(mahasiswa.values()))

print("\nPasangan key-value:")
print(list(mahasiswa.items()))

print("\nNilai semester:")
print(mahasiswa.get("semester", "Belum tersedia"))
