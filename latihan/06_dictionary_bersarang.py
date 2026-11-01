
# ==========================================
# LATIHAN 06 - DICTIONARY BERSARANG
# Algoritma dan Pemrograman | Pertemuan 11
# ==========================================

data_mahasiswa = {
    "2225250189": {
        "nama": "Umul Hani",
        "kelas": "3F",
        "nilai": 88
    },
    "2225250026": {
        "nama": "Nia Hamidah",
        "kelas": "3F",
        "nilai": 85
    }
}

print("DATA MAHASISWA")

for nim, data in data_mahasiswa.items():
    print("-" * 40)
    print("NIM   :", nim)
    print("Nama  :", data["nama"])
    print("Kelas :", data["kelas"])
    print("Nilai :", data["nilai"])

print("-" * 40)
