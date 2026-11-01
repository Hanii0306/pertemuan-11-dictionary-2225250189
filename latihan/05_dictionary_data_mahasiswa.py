
# ==========================================
# LATIHAN 05 - DATA MAHASISWA
# Algoritma dan Pemrograman | Pertemuan 11
# ==========================================

mahasiswa = {
    "nama": "Umul Hani",
    "nim": "2225250189",
    "kelas": "3F",
    "program_studi": "Pendidikan Matematika"
}

print("DATA MAHASISWA")

for atribut, informasi in mahasiswa.items():
    print(f"{atribut.replace('_', ' ').title():20}: {informasi}")

print("\nPemeriksaan data:")

if "nim" in mahasiswa:
    print("NIM tersedia dalam dictionary.")
else:
    print("NIM tidak tersedia dalam dictionary.")
