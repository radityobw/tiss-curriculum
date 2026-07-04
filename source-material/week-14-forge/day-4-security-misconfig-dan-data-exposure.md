# 🔨 Week 14 · Day 4: Security Misconfig & Data Exposure

> **Rank**: FORGE | **Minggu ke-14**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 14 · Day 4/5 | FORGE Rank (Minggu 5 dari 5) | Overall: 69/120 hari (58%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** celah keamanan akibat kesalahan konfigurasi (*Security Misconfiguration*) dan paparan data sensitif (*Sensitive Data Exposure*).
2. **Mengelola** rahasia server (seperti kunci API dan kredensial *database*) dengan aman menggunakan *environment variables* (`.env`).
3. **Menerapkan** perlindungan *header* HTTP menggunakan *Helmet.js* dan mencegah serangan *brute-force* dengan *Rate Limiting*.

---

## 📖 Materi Inti

### Kesalahan Konfigurasi (Security Misconfiguration)

Seringkali, sistem dapat dibobol bukan karena cacat pada logika kode, melainkan karena **konfigurasi yang tidak aman**.

Beberapa contoh kesalahan konfigurasi yang umum:
1. Menjalankan *database* (seperti MongoDB atau Redis) tanpa kata sandi, sehingga dapat diakses publik dengan pengaturan *default*.
2. Membiarkan mode *debug* tetap aktif di *production*. Ketika terjadi kesalahan (*error* 500), server menampilkan *Stack Trace* yang memperlihatkan struktur folder, versi modul, dan detail *backend* kepada pengguna. Informasi ini sangat berguna bagi penyerang untuk merencanakan eksploitasi.

### Paparan Data Sensitif (Sensitive Data Exposure)

Kerentanan lainnya adalah membiarkan informasi sensitif (seperti kata sandi *database*, API key, atau rahasia JWT) ditulis langsung secara *plaintext* di dalam kode program (`server.js`). 
Jika *developer* secara tidak sengaja memublikasikan kode tersebut ke repositori publik seperti GitHub, *bot* milik penyerang akan segera mendeteksinya dan kredensial tersebut bisa disalahgunakan dalam hitungan menit.

**Solusi: Gunakan file `.env` (Environment Variables)**
Semua data rahasia harus dipisahkan dari kode utama dan disimpan dalam file `.env`. File ini **tidak boleh** dimasukkan ke dalam version control system (seperti Git).

```text
# Contoh isi file .env (Harus diabaikan oleh .gitignore)
DATABASE_PASSWORD=rahasia_tiss_2026
JWT_SECRET=super_kunci_sakti_
```
Di Node.js, kamu bisa mengakses nilai ini menggunakan *library* `dotenv`:
```javascript
const dbPassword = process.env.DATABASE_PASSWORD;
```

### Perlindungan Tambahan (Helmet.js & Rate Limiter)

1. **Helmet.js (Pelindung Header HTTP)**
   Secara default, *framework* Express.js mengirimkan *header* `X-Powered-By: Express`. Ini memberi tahu penyerang teknologi apa yang kamu gunakan. *Helmet.js* membantu mengamankan aplikasi dengan mengatur berbagai *header* HTTP terkait keamanan, termasuk menyembunyikan *header* informasi tersebut.
   ```javascript
   const helmet = require('helmet');
   app.use(helmet());
   ```

2. **Rate Limiting (Pencegah Brute-Force & DDoS)**
   Untuk mencegah penyerang mengirim ribuan permintaan per detik (misalnya mencoba menebak kata sandi di rute `/api/login`), gunakan modul *Rate Limiting*.
   ```javascript
   const rateLimit = require('express-rate-limit');
   const limiter = rateLimit({
     windowMs: 15 * 60 * 1000, // 15 menit
     max: 100 // Batasi 100 request per IP selama windowMs
   });
   app.use(limiter);
   ```

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari mempraktikkan penggunaan file `.env`!

1. Buat folder baru `mkdir lab-rahasia` dan masuk ke dalamnya `cd lab-rahasia`.
2. Inisialisasi proyek Node.js: `npm init -y`.
3. Instal modul *dotenv*: `npm install dotenv`.
4. Buat file `.env` dan `.gitignore`.
5. Di dalam file `.env`, ketikkan:
   `API_KEY=KUNCI_RAHASIA_KITA`
6. Di dalam file `.gitignore`, ketikkan:
   `.env`
   *(Ini mencegah Git mengunggah file `.env` ke GitHub).*
7. Buat file `app.js` dan ketikkan kode berikut:
   ```javascript
   require('dotenv').config();
   console.log("API Key saya adalah: ", process.env.API_KEY);
   ```
8. Jalankan file tersebut: `node app.js`. Kunci rahasiamu akan tercetak di terminal, dan aman dari pantauan publik berkat pengaturan di `.gitignore`!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa kita harus menggunakan file <i>.env</i> untuk menyimpan data rahasia seperti API Key dan password database?</summary>

**Jawaban:** Agar kredensial rahasia dipisahkan dari kode sumber (source code) dan tidak ikut ter-upload ke repositori publik seperti GitHub, yang dapat dieksploitasi oleh peretas.
</details>

<details>
<summary>❓ Mengapa menampilkan <i>Stack Trace</i> error ke pengguna akhir di tahap produksi (production) sangat berbahaya?</summary>

**Jawaban:** Karena *Stack Trace* menampilkan detail internal aplikasi (seperti struktur file server, query database, versi modul, dll). Informasi teknis ini dapat membantu peretas merancang strategi serangan yang lebih akurat.
</details>

<details>
<summary>❓ Apa fungsi dari <i>Helmet.js</i> pada aplikasi berbasis Express.js?</summary>

**Jawaban:** Helmet.js berfungsi mengamankan aplikasi Express.js dengan cara mengatur *HTTP headers* yang direkomendasikan untuk mencegah celah keamanan umum dan menyembunyikan informasi server (misal menghapus header `X-Powered-By`).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami risiko *Security Misconfiguration* dan *Sensitive Data Exposure*.
- [ ] Saya tahu cara memisahkan rahasia menggunakan variabel lingkungan (`.env`) dan mencegahnya bocor dengan `.gitignore`.
- [ ] Saya memahami pentingnya menyembunyikan informasi *header* dengan *Helmet.js* dan mencegah serangan *brute-force* dengan *Rate Limiting*.
- [ ] Saya berhasil mempraktikkan ekstraksi nilai dari file `.env` pada *Mini Lab*.
- [ ] Saya telah menyelesaikan dan memahami jawaban dari *Quiz Kilat*.

---

## 🔗 Resources

- [Helmet.js](https://helmetjs.github.io/) — Dokumentasi resmi untuk mengamankan *header* Express HTTP.
- [Dotenv di NPM](https://www.npmjs.com/package/dotenv) — Modul untuk memuat *environment variables*.

---

## ➡️ Besok

**Day 5: Lab & Mission: Securing the API** — Babak akhir untuk materi *Forge Rank* sudah di depan mata! Besok, kita akan menggabungkan semua konsep keamanan yang sudah dipelajari: *Parameterized Queries* (mencegah Injeksi), sanitasi (mencegah XSS), *authorization checks* (mencegah IDOR), serta *Helmet*, *Rate Limiting*, dan `.env` (mencegah Misconfig & Exposure). Kita akan mengamankan API TISS dari berbagai sudut celah serangan sebelum melanjutkan ke materi sabuk berikutnya.

---

*📅 TISS Null Teaming · Week 14 · Day 4 · FORGE Rank*
