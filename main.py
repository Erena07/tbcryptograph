# ============================================================
# 📍 ServerScript: main.py
# Program utama: Enkripsi & Dekripsi menggunakan GOST 28147-89
# ============================================================

from gost import gost_encrypt, gost_decrypt
from utils import pad_key, read_file, write_file, measure_time

def main():
    print("=== PROGRAM ENKRIPSI GOST 28147-89 ===")
    print("1. Enkripsi File")
    print("2. Dekripsi File")
    print("---------------------------------------")
    choice = input("Pilih (1/2): ").strip()

    input_path = input("Masukkan path file input: ").strip()
    output_path = input("Masukkan path file output: ").strip()
    key_text = input("Masukkan kunci (maks 32 karakter): ")

    key = pad_key(key_text)
    data = read_file(input_path)

    if choice == "1":
        print("\n🔒 Melakukan Enkripsi...")
        result, dur = measure_time(gost_encrypt, data, key)
        write_file(output_path, result)
        print(f"✅ Enkripsi selesai dalam {dur:.4f} detik.")
    elif choice == "2":
        print("\n🔓 Melakukan Dekripsi...")
        result, dur = measure_time(gost_decrypt, data, key)
        write_file(output_path, result)
        print(f"✅ Dekripsi selesai dalam {dur:.4f} detik.")
    else:
        print("❌ Pilihan tidak valid!")

if __name__ == "__main__":
    main()
