# 🎯 Week 18 · Day 6 (Bonus): Hands-On Learning

> **Rank**: BREACH | **Minggu ke-18** | Bonus Day

---

## 🌐 Platform Hari Ini

**[PortSwigger Web Security Academy — Practitioner Labs (Burp Suite Focus)](https://portswigger.net/web-security/all-labs)**
Lab PortSwigger tingkat Practitioner yang menggabungkan berbagai teknik eksploitasi menggunakan Burp Suite Community Edition. Fokus pada intercept, repeater, dan manipulasi request.

💰 **Biaya**: Gratis (semua lab gratis, Burp Suite Community Edition gratis)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menggunakan Burp Suite Proxy untuk intercept dan memodifikasi HTTP request
2. Menggunakan Burp Suite Repeater untuk menguji payload secara iteratif
3. Menyelesaikan lab PortSwigger menggunakan Burp Suite sebagai tool utama

---

## 📋 Requirement

* Akun PortSwigger (sudah ada)
* Burp Suite Community Edition terinstal (sudah diajarkan di Day 1-3 minggu ini)
* Peramban web dengan FoxyProxy terinstal (sudah dikonfigurasi minggu ini)

> ⚠️ **Jika Burp Suite belum terinstal**: Unduh dari [portswigger.net/burp/communitydownload](https://portswigger.net/burp/communitydownload) — gratis, tersedia untuk Windows/Mac/Linux.

> ⚠️ **Jika FoxyProxy belum diatur**: Instal ekstensi FoxyProxy di browser, buat profil proxy ke `127.0.0.1:8080`. Instruksi detail ada di materi Day 1 minggu ini.

---

## 📝 Prosedur

### Langkah 1: Setup Burp Suite + Browser
1. Buka Burp Suite Community Edition
2. Buat proyek **Temporary Project** → klik **Next** → **Start Burp**
3. Pastikan Proxy listener aktif di `127.0.0.1:8080` (tab Proxy → Options)
4. Aktifkan FoxyProxy di browser → pilih profil Burp Suite
5. Pastikan **Intercept is off** terlebih dahulu (kita akan menyalakannya nanti)

### Langkah 2: Lab — Access Control (Menggunakan Proxy)
1. Buka PortSwigger → All Labs → filter kategori **Access Control**
2. Pilih lab **"Unprotected admin functionality"** (Apprentice)
3. Klik **Access the lab**
4. Di Burp Suite, buka tab **Proxy → HTTP History**
5. ke halaman web — perhatikan semua request tercatat di HTTP History
6. Cari file `robots.txt` di HTTP History, atau akses langsung: `/robots.txt`
7. Temukan path admin panel yang tertulis di dalamnya
8. Akses path tersebut — lab solved! ✅

### Langkah 3: Lab — File Path Traversal (Menggunakan Repeater)
1. Pilih lab **"File path traversal, simple case"** (Apprentice)
2. Klik **Access the lab**
3. Di halaman web, klik salah satu gambar produk
4. Di Burp Suite **HTTP History**, temukan request yang mengambil gambar (cari parameter `filename=`)
5. **Klik kanan** request tersebut → **Send to Repeater**
6. Di tab **Repeater**, modifikasi parameter:
 ```
 filename=../../../etc/passwd
 ```
7. Klik **Send** — periksa response body
8. Jika isi `/etc/passwd` muncul — lab solved! ✅

> 💡 **Repeater** memungkinkan kamu mengirim ulang request dengan modifikasi tanpa harus refresh browser. Ini jauh lebih efisien daripada mengubah URL manual.

### Langkah 4: Lab — Authentication (Menggunakan Intruder)
1. Pilih lab **"Username enumeration via different responses"** (Apprentice)
2. Klik **Access the lab**
3. Buka halaman login, coba login dengan `test` / `test`
4. Di HTTP History, temukan POST request login
5. **Klik kanan** → **Send to Intruder**
6. Di tab Intruder:
 - Tandai parameter `username` sebagai posisi payload
 - Di tab Payloads, masukkan daftar username umum: `admin`, `administrator`, `user`, `root`, `guest`, `test`
 - Klik **Start Attack** (Community Edition lebih lambat — ini normal)
7. Bandingkan response length — username valid biasanya punya response berbeda
8. Setelah menemukan username valid, gunakan Repeater untuk bruteforce password

> 💡 **Burp Community Edition membatasi kecepatan Intruder.** Ini normal — gunakan wordlist kecil (10-20 kata) untuk demonstrasi konsep.

---

## 🏁 Target Output

* ✅ Minimal **2 lab** diselesaikan menggunakan Burp Suite
* 📝 Dokumentasi untuk setiap lab: tool Burp yang digunakan (Proxy/Repeater/Intruder) dan cara kerjanya
* 📸 Tangkapan layar Burp Suite Repeater menunjukkan request yang dimodifikasi dan response-nya
* 📸 Tangkapan layar PortSwigger lab "Solved"

---

## 🔄 Fallback

Jika Burp Suite bermasalah:
1. Gunakan **OWASP ZAP** (gratis dan open source):
 - Unduh dari [zaproxy.org](https://www.zaproxy.org/download/)
 - ZAP memiliki fitur Proxy, Repeater (Manual Request), dan Fuzzer (seperti Intruder)
2. Kerjakan lab PortSwigger yang sama menggunakan ZAP
3. Atau kerjakan lab langsung di browser (beberapa lab Apprentice bisa tanpa proxy tool)
