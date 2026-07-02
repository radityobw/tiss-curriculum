# 🎯 Week 9 · Day 6 (Bonus): Hands-On Learning

> **Rank**: PACKET | **Minggu ke-9** | Bonus Day

---

## 🌐 Platform Hari Ini

**[OverTheWire — Bandit Wargame (Level 11–20)](https://overthewire.org/wargames/bandit/)**
Lanjutan wargame Bandit dengan tantangan yang lebih kompleks: encoding, networking, scripting, dan koneksi SSH lanjutan.

💰 **Biaya**: Gratis (sepenuhnya gratis via SSH)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menggunakan encoding/decoding (base64, ROT13) dalam konteks keamanan
2. Menerapkan SSH key-based authentication dan port forwarding dasar
3. Menggabungkan pengetahuan networking + Linux yang dipelajari selama 5 minggu terakhir

---

## 📋 Requirement

* Terminal Linux (VM/WSL)
* Koneksi internet stabil
* Password Level 11 dari progress Week 8 Day 6
* Pemahaman dasar SSH (sudah dipelajari di Day 2 minggu ini)

> ⚠️ **Jika belum menyelesaikan Level 0-10**: Kerjakan terlebih dahulu Level 0-10 dari Week 8 Day 6. Kamu memerlukan password Level 11 untuk memulai.

> ⚠️ **Jika kehilangan password Level 11**: Mulai ulang dari Level 0 — setiap level memakan waktu singkat jika sudah paham caranya.

---

## 📝 Prosedur

### Langkah 1: Koneksi ke Level 11
1. Buka terminal Linux
2. Login ke Bandit Level 11:
 ```bash
 ssh bandit11@bandit.labs.overthewire.org -p 2220
 # Masukkan password Level 11 dari catatan Week 8
 ```

### Langkah 2: Kerjakan Level 11–15

**Petunjuk per level (tanpa spoiler):**

| Level | Konsep yang Diuji | Perintah/Konsep yang Berguna |
|-------|-------------------|------------------------------|
| 11 → 12 | Cipher (ROT13) | `tr 'A-Za-z' 'N-ZA-Mn-za-m'` |
| 12 → 13 | Kompresi bertingkat | `xxd`, `gzip`, `bzip2`, `tar`, `file` |
| 13 → 14 | SSH private key | `ssh -i [keyfile]` |
| 14 → 15 | Koneksi TCP | `nc localhost [port]` |
| 15 → 16 | Koneksi SSL/TLS | `openssl s_client -connect` |

> 💡 **Level 12 (kompresi bertingkat) adalah yang paling sulit.** Tips:
> 1. Buat direktori kerja di `/tmp/namamu`
> 2. Copy file ke sana: `cp data.txt /tmp/namamu/`
> 3. Gunakan perintah `file` untuk mendeteksi tipe kompresi
> 4. Decompress berulang kali sesuai tipe file yang terdeteksi
> 5. Sabar — bisa sampai 5-7 kali dekompresi

### Langkah 3: Kerjakan Level 16–20 (Jika Waktu Tersisa)

| Level | Konsep yang Diuji | Perintah/Konsep yang Berguna |
|-------|-------------------|------------------------------|
| 16 → 17 | Port scanning + SSL | `nmap -p 31000-32000 localhost`, `openssl` |
| 17 → 18 | Diff file | `diff file1 file2` |
| 18 → 19 | SSH command execution | `ssh banditX@... "cat readme"` |
| 19 → 20 | Setuid binary | `./bandit20-do cat /etc/bandit_pass/bandit20` |

> 💡 **Level 16 sangat relevan** karena menggabungkan port scanning (nmap) dengan SSL — persis materi networking + Linux minggu ini.

### Langkah 4: Dokumentasi
1. Update file `bandit-progress.txt` dari Week 8:
 ```
 Level 11→12: Menggunakan tr untuk ROT13 cipher
 Level 12→13: Dekompresi bertingkat dengan xxd, gzip, bzip2, tar
 Level 13→14: SSH login menggunakan private key
...
 ```
2. Catat level tertinggi yang berhasil dicapai

---

## 🏁 Target Output

* ✅ Minimal **Level 11 sampai Level 15** selesai (target ideal: Level 20)
* 📝 File `bandit-progress.txt` yang di-update dengan catatan Level 11+
* 📸 Tangkapan layar terminal saat berhasil login ke level tertinggi yang dicapai

---

## 🔄 Fallback

Jika OverTheWire tidak bisa diakses:
1. Praktikkan **Nmap scanning** di VM lokal:
 ```bash
 nmap -sV localhost
 nmap -p 1-1000 [IP VM lain]
 ```
2. Praktikkan **SSH key-based auth** antar VM:
 ```bash
 ssh-keygen -t ed25519
 ssh-copy-id user@[IP VM]
 ssh user@[IP VM]
 ```
3. Dokumentasikan output dari setiap perintah
