# main.py - UTS Dasar Komputer & Pemrograman
# Kasus: Kelompok E - Embedded/IoT (Monitoring Kelembapan Tanah & Aksi Pompa)

def status_sensor(nilai):
    """
    Menentukan status kelembapan tanah berdasarkan aturan:
    - Kelembapan < 35%          -> KERING
    - 35% <= kelembapan <= 70%  -> NORMAL
    - Kelembapan > 70%          -> BASAH
    """
    if nilai < 35:
        return "KERING"
    elif nilai <= 70:
        return "NORMAL"
    else:
        return "BASAH"

def aksi_pompa(status):
    """
    Menentukan aksi pompa berdasarkan status kelembapan:
    - KERING -> POMPA ON
    - NORMAL atau BASAH -> POMPA OFF
    """
    if status == "KERING":
        return "POMPA ON"
    else:
        return "POMPA OFF"

def rata_rata(data):
    """
    Menghitung nilai rata-rata dari list data kelembapan (%).
    Mengembalikan nilai berupa float.
    """
    if len(data) == 0:
        return 0.0
    return sum(data) / len(data)

def main():
    # 15 data inti dari soal UTS (%)
    data_inti = [22, 28, 34, 41, 55, 63, 72, 78, 31, 47, 66, 81, 19, 58, 69]
    
    # 5 data tambahan realistis (0-100%) untuk menguji batas (35, 70, 71) dan variasi ekstrem (0, 100)
    data_tambahan = [0, 35, 70, 71, 100]
    
    # Menggabungkan menjadi total tepat 20 data
    data_kelembapan = data_inti + data_tambahan
    
    list_status = []
    list_aksi = []
    
    # Perulangan untuk memproses status kelembapan dan aksi pompa setiap data
    for nilai in data_kelembapan:
        st = status_sensor(nilai)
        aksi = aksi_pompa(st)
        list_status.append(st)
        list_aksi.append(aksi)
        
    # Menampilkan hasil monitoring per data
    print("===== MONITORING KELEMBAPAN TANAH & AKSI POMPA =====")
    for i in range(len(data_kelembapan)):
        print(f"{i+1:02d}. Kelembapan: {data_kelembapan[i]:3d}% -> Status: {list_status[i]:6s} | Aksi: {list_aksi[i]}")
        
    # Perhitungan statistik ringkasan
    total_data = len(data_kelembapan)
    jml_kering = list_status.count("KERING")
    jml_normal = list_status.count("NORMAL")
    jml_basah = list_status.count("BASAH")
    
    avg_kelembapan = rata_rata(data_kelembapan)
    max_kelembapan = max(data_kelembapan)
    min_kelembapan = min(data_kelembapan)
    
    # Menampilkan ringkasan akhir
    print("\n===== RINGKASAN =====")
    print(f"Total data      : {total_data}")
    print(f"KERING (ON)     : {jml_kering}")
    print(f"NORMAL (OFF)    : {jml_normal}")
    print(f"BASAH  (OFF)    : {jml_basah}")
    print(f"Rata-rata       : {avg_kelembapan:.2f}%")
    print(f"Maksimum        : {max_kelembapan}%")
    print(f"Minimum         : {min_kelembapan}%")

if __name__ == "__main__":
    main()