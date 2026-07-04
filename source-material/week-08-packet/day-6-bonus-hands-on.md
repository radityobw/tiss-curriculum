# 🎯 Week 8 · Day 6 (Bonus): Hands-On Learning

> **Rank**: PACKET | **Minggu ke-8** | Bonus Day

---

## 🌐 Platform Hari Ini

**[OverTheWire — Bandit Wargame (Level 0–10)](https://overthewire.org/wargames/bandit/)**
Wargame berbasis SSH yang mengajarkan konsep Linux dan keamanan melalui tantangan bertingkat. Setiap level memerlukan kamu untuk menemukan *password* ke level berikutnya menggunakan perintah Linux.

💰 **Biaya**: Gratis (sepenuhnya gratis via SSH, tanpa registrasi)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menggunakan SSH untuk koneksi ke server remote
2. Menyelesaikan minimal 5 level Bandit menggunakan perintah Linux yang dipelajari minggu ini
3. Menerapkan konsep file permissions, dan pencarian file dalam skenario nyata

---

## 📋 Requirement

* Terminal Linux (VM/WSL yang sudah disetup)
* Koneksi internet stabil
* Kemampuan dasar perintah Linux (sudah dipelajari Day 1-4 minggu ini)

> ⚠️ **Tidak perlu registrasi.** OverTheWire diakses langsung via SSH dari terminal.

---

## 📝 Prosedur

### Langkah 1: Koneksi ke Level 0
1. Buka terminal Linux
2. Koneksikan ke server Bandit dengan SSH:
 ```bash
 ssh bandit0@bandit.labs.overthewire.org -p 2220
 ```
3. Ketika ditanya password, masukkan: `bandit0`
4. Kamu sekarang sudah masuk ke Level 0!

> 💡 **Jika SSH gagal**: Pastikan port 2220 tidak diblokir oleh jaringan kampus/ISP. Coba gunakan koneksi data seluler (tethering) sebagai alternatif.

### Langkah 2: Selesaikan Level 0 → Level 1
1. Baca petunjuk level di [halaman Bandit Level 0](https://overthewire.org/wargames/bandit/bandit0.html)
2. Tujuan: Temukan password untuk Level 1 yang tersimpan di file `readme`
3. Gunakan perintah:
 ```bash
 ls
 cat readme
 ```
4. Catat password yang muncul — ini digunakan untuk login ke Level 1

### Langkah 3: Lanjutkan Level demi Level
1. Keluar dari sesi saat ini: `exit`
2. Login ke level berikutnya:
 ```bash
 ssh bandit1@bandit.labs.overthewire.org -p 2220
 # Masukkan password dari level sebelumnya
 ```
3. Untuk setiap level, baca petunjuk di halaman web OverTheWire
4. Catat password setiap level di catatan lokal

**Petunjuk per level (tanpa spoiler):**

| Level | Konsep yang Diuji | Perintah yang Berguna |
|-------|-------------------|----------------------|
| 0 → 1 | Membaca file | `cat` |
| 1 → 2 | File dengan nama khusus | `cat./-` |
| 2 → 3 | File dengan spasi di nama | `cat "nama file"` |
| 3 → 4 | File tersembunyi | `ls -la`, `cat` |
| 4 → 5 | Tipe file | `file`, `cat` |
| 5 → 6 | Properti file (ukuran, dll) | `find` dengan opsi |
| 6 → 7 | Owner dan group file | `find / -user -group -size` |
| 7 → 8 | Mencari kata dalam file | `grep` |
| 8 → 9 | Baris unik dalam file | `sort`, `uniq` |
| 9 → 10 | String dalam file biner | `strings`, `grep` |

> 💡 **Jika stuck di suatu level lebih dari 15 menit**: Baca halaman petunjuk OverTheWire untuk level tersebut — mereka mencantumkan perintah yang berguna. Jangan malu membaca `man [perintah]` untuk memahami opsi-opsinya.

### Langkah 4: Dokumentasi
1. Buat file catatan `bandit-progress.txt`:
 ```bash
 # Di terminal lokal (bukan di server Bandit)
 nano bandit-progress.txt
 ```
2. Untuk setiap level yang berhasil, catat:
 - Nomor level
 - Perintah yang digunakan
 - Penjelasan singkat apa yang kamu pelajari

---

## 🏁 Target Output

* ✅ Minimal **Level 0 sampai Level 5** selesai (target ideal: Level 10)
* 📝 File `bandit-progress.txt` berisi catatan perintah dan pembelajaran per level
* 📸 Tangkapan layar terminal saat berhasil login ke level tertinggi yang dicapai

---

## 🔄 Fallback

Jika OverTheWire tidak bisa diakses (server down/port blocked):
1. Buka [Linux Journey — Journeyman Modules](https://linuxjourney.com/)
2. Kerjakan modul **"Filesystem"** dan **"Permissions"** di level Journeyman
3. Praktikkan perintah `find`, `grep`, `sort`, `uniq` di terminal lokal dengan file-file di sistem kamu
