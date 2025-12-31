# Comparative Analysis: Brute Force vs Greedy Algorithm for TSP 📊

Proyek ini adalah implementasi dan analisis perbandingan antara algoritma **Brute Force** dan **Greedy** untuk menyelesaikan masalah *Traveling Salesperson Problem (TSP)* dengan 6 kota.

## 📝 Deskripsi Masalah
Mencari rute terpendek yang mengunjungi setiap kota tepat satu kali dan kembali ke kota asal.

## 🚀 Implementasi Algoritma

### 1. Brute Force
* **Pendekatan:** Mencoba semua kemungkinan permutasi rute.
* **Kompleksitas Waktu:** $O(n!)$ - Eksponensial (Sangat lambat untuk data besar).
* **Hasil:** Selalu **Optimal** (Jarak terpendek pasti ditemukan).

### 2. Greedy Algorithm
* **Pendekatan:** Selalu memilih kota terdekat yang belum dikunjungi (lokal optimal).
* **Kompleksitas Waktu:** $O(n^2)$ - Kuadratik (Jauh lebih cepat).
* **Hasil:** **Suboptimal** (Belum tentu jarak terpendek, tapi cukup baik).

## 🧪 Hasil Eksperimen (6 Kota)

| Algoritma | Rute yang Dihasilkan | Jarak Total | Waktu Eksekusi |
| :--- | :--- | :--- | :--- |
| **Brute Force** | `[0, 1, 5, 3, 4, 2, 0]` | **90** (Optimal) | Lambat |
| **Greedy** | `[0, 1, 5, 3, 4, 2, 0]` | **90** (Kebetulan sama) | Cepat |

## 💡 Kesimpulan
* **Brute Force** ideal untuk jumlah kota sedikit (n < 12) dimana akurasi 100% sangat dibutuhkan.
* **Greedy** lebih cocok untuk dataset besar dimana kecepatan lebih diprioritaskan daripada solusi yang sempurna.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Library:** `itertools` (untuk permutasi)
