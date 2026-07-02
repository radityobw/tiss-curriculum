# 🎯 Week 14 · Day 6 (Bonus): Hands-On Learning

> **Rank**: FORGE | **Minggu ke-14** | Bonus Day

---

## 🌐 Platform Hari Ini

**[OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)**
Aplikasi web sengaja rentan (*intentionally vulnerable*) yang dikembangkan oleh OWASP. Dirancang untuk mempraktikkan kerentanan OWASP Top 10 dalam lingkungan aman dan legal.

💰 **Biaya**: Gratis (open source, self-hosted)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menjalankan aplikasi web rentan secara lokal menggunakan Docker atau Node.js
2. Menemukan minimal 3 kerentanan OWASP Top 10 di Juice Shop
3. Menghubungkan teori OWASP Top 10 (Day 1-4) dengan eksploitasi nyata

---

## 📋 Requirement

* Terminal (Bash/Zsh)
* **Salah satu** dari opsi berikut:
 - **Opsi A (Direkomendasikan)**: Docker terinstal
 - **Opsi B**: Node.js terinstal (sudah ada dari Week 12)
* Peramban web modern (Chrome/Firefox)

> ⚠️ **Jika Docker belum terinstal** — ikuti Opsi B yang menggunakan Node.js (sudah tersedia).

---

## 📝 Prosedur

### Langkah 1: Jalankan Juice Shop

**Opsi A — Menggunakan Docker (Paling Mudah):**
```bash
docker pull bkimminich/juice-shop
docker run -d -p 3000:3000 bkimminich/juice-shop
```
Buka browser: `http://localhost:3000`

**Opsi B — Menggunakan Node.js (Tanpa Docker):**
```bash
git clone https://github.com/juice-shop/juice-shop.git
cd juice-shop
npm install
npm start
```
Buka browser: `http://localhost:3000`

> 💡 **Jika `npm install` gagal**: Pastikan menggunakan Node.js versi LTS (18 atau 20). Cek dengan `node --version`. Jika masih gagal, gunakan Opsi A (Docker).

> 💡 **Jika port 3000 sudah dipakai**: Ubah port — Docker: `-p 8080:3000`, Node.js: edit file konfigurasi atau gunakan `PORT=8080 npm start`.

### Langkah 2: Eksplorasi Antarmuka
1. Buka `http://localhost:3000` di browser
2. Jelajahi toko online fiktif ini — buka setiap halaman, klik setiap menu
3. Buka **DevTools (F12)** → tab **Network** — amati request yang dikirim
4. Perhatikan hal-hal mencurigakan:
 - Apakah ada endpoint API yang terlihat?
 - Apakah ada data sensitif di response?
 - Apakah ada parameter URL yang bisa dimanipulasi?

### Langkah 3: Temukan Kerentanan (Guided)

**Tantangan 1 — Score Board (Difficulty: ⭐)**
1. Juice Shop menyembunyikan halaman *Score Board* yang mencatat semua tantangan
2. Petunjuk: Coba buka DevTools → Sources atau baca file JavaScript utama
3. Cari path/URL tersembunyi yang mengarah ke score board
4. Buka URL tersebut di browser

**Tantangan 2 — Admin Section (Difficulty: ⭐⭐)**
1. Coba temukan panel administrasi yang tersembunyi
2. Petunjuk: Analisis struktur URL dan coba tebak path-nya
3. Ini berhubungan dengan **Broken Access Control** (OWASP #1)

**Tantangan 3 — SQL Injection Login (Difficulty: ⭐⭐)**
1. Buka halaman Login
2. Di kolom email, coba masukkan: `' OR 1=1--`
3. Password boleh diisi sembarang
4. Klik Login — apa yang terjadi?
5. Ini adalah **Injection** (OWASP #3) — persis materi Day 1 minggu ini!

> 💡 **Jika stuck**: Buka Score Board (Tantangan 1) — di sana ada daftar semua tantangan dengan tingkat kesulitan dan kategori OWASP-nya.

### Langkah 4: Dokumentasi Temuan
Untuk setiap kerentanan yang ditemukan, tulis *mini bug report*:
```
Nama Kerentanan: [nama]
Kategori OWASP: [misal: A01 Broken Access Control]
Langkah Reproduksi:
 1. [langkah 1]
 2. [langkah 2]
Dampak: [apa yang bisa dilakukan penyerang]
```

---

## 🏁 Target Output

* ✅ OWASP Juice Shop berhasil berjalan di `localhost:3000`
* ✅ Minimal **3 tantangan** berhasil diselesaikan (Score Board + 2 lainnya)
* 📝 **3 mini bug report** untuk setiap kerentanan yang ditemukan
* 📸 Tangkapan layar Score Board dengan tantangan yang sudah solved (ditandai hijau)

---

## 🔄 Fallback

Jika Juice Shop gagal diinstal (Docker dan Node.js gagal):
1. Buka [PortSwigger Web Security Academy](https://portswigger.net/web-security) (gratis)
2. Kerjakan 3 lab dari kategori:
 - **SQL Injection**: Lab "SQL injection vulnerability in WHERE clause"
 - **XSS**: Lab "Reflected XSS into HTML context"
 - **Access Control**: Lab "Unprotected admin functionality"
3. Tulis mini bug report untuk setiap lab yang diselesaikan
