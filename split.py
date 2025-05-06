import os

def split_txt_by_size(filename, size_per_part_mb):
    size_per_part = size_per_part_mb * 1024 * 1024  # Konversi MB ke byte

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            part_number = 1
            current_part_size = 0
            part_lines = []

            for line in f:
                line_size = len(line.encode('utf-8'))  # Ukuran dalam byte
                if current_part_size + line_size > size_per_part:
                    # Simpan bagian saat ini ke file
                    part_filename = f"{filename}_part{part_number}.txt"
                    with open(part_filename, 'w', encoding='utf-8') as part_file:
                        part_file.writelines(part_lines)
                    print(f"[+] File dibuat: {part_filename} ({len(part_lines)} baris)")
                    part_number += 1
                    part_lines = []
                    current_part_size = 0

                part_lines.append(line)
                current_part_size += line_size

            # Simpan sisa bagian terakhir (jika ada)
            if part_lines:
                part_filename = f"{filename}_part{part_number}.txt"
                with open(part_filename, 'w', encoding='utf-8') as part_file:
                    part_file.writelines(part_lines)
                print(f"[+] File dibuat: {part_filename} ({len(part_lines)} baris)")

        print(f"\n[✔] Selesai! File dibagi menjadi {part_number} bagian.")

    except FileNotFoundError:
        print(f"[!] File '{filename}' tidak ditemukan.")
    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")

# Contoh penggunaan:
# Ganti 'namafile.txt' dengan nama file kamu, dan 1 untuk membagi setiap 1MB
split_txt_by_size('logs.txt', 1000)
