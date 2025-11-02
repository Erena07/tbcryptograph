# 🧩 TBcryptograph — Implementasi Algoritma Kriptografi Simetri GOST 28147-89

Proyek ini merupakan implementasi **algoritma kriptografi kunci simetri GOST 28147-89** menggunakan bahasa pemrograman Python.  
GOST (ГОСТ 28147-89) adalah algoritma enkripsi blok simetris yang dikembangkan di Rusia, bekerja dengan panjang blok **64-bit** dan kunci **256-bit**, serta terdiri dari **32 putaran Feistel**.  
Proyek ini dibuat sebagai bagian dari tugas mata kuliah *Kriptografi*, dengan tujuan memahami proses enkripsi, dekripsi, serta pengujian performa algoritma kunci simetri.

---

## ⚙️ Fitur Program
- 🔒 **Enkripsi & Dekripsi** teks berbasis algoritma GOST 28147-89
- 📂 **Input/Output File**: membaca dan menulis hasil enkripsi dari file `.txt`
- 🧮 **Proses Modular**: fungsi algoritma, utilitas, dan main program dipisahkan
- 🖥️ **Antarmuka GUI (opsional)** berbasis `tkinter`
- ⏱️ **Pengukuran Waktu Eksekusi** otomatis untuk proses enkripsi dan dekripsi

---

## 📂 Struktur Folder
GOST_Encryption_Project/
├── main.py → Program utama (menu enkripsi/dekripsi)
├── gost.py → Implementasi algoritma GOST 28147-89 (Feistel cipher)
├── utils.py → Fungsi bantu (I/O file, padding, pengukuran waktu)
├── data/
│ ├── input.txt → File teks yang akan dienkripsi
│ └── output.txt → Hasil enkripsi/dekripsi
└── gui/
└── main_gui.py → GUI opsional (tkinter)

---

## 🧠 Cara Menjalankan Program
1. Pastikan **Python 3.11+** sudah terinstal di komputer.
2. Buka terminal di dalam folder proyek ini.
3. Jalankan perintah berikut:
   ```bash
   python main.py
4. Pilih mode operasi:
    - Ketik 1 untuk Enkripsi
    - Ketik 2 untuk Dekripsi
5. Masukkan path file input/output (misalnya data/input.txt dan data/output.txt) dan kunci (maksimal 32 karakter).

