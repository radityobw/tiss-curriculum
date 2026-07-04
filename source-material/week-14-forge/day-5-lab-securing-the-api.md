# 🔨 Week 14 · Day 5: Lab & Weekly Mission Securing the API

> **Rank**: FORGE | **Minggu ke-14**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓▓▓] 100% — FORGE Rank (Minggu 5 dari 5) - COMPLETION!

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░] 58% — Hari 70 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → 🔄 BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu terakhir di Rank *Forge* telah selesai. Kamu telah beralih mempelajari perspektif *Attacker* (berdasarkan OWASP Top 10) untuk memahami kerentanan dan cara mencegahnya:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | OWASP & SQLi | Memahami mekanisme *SQL Injection* dan menggunakan *Parameterized Queries*. |
| Day 2 | XSS & Sanitasi | Perkenalan varian *Stored, Reflected, DOM XSS* serta praktik sanitasi HTML. |
| Day 3 | IDOR & BAC | Bahaya akses *parameter* ID yang tidak divalidasi terhadap otorisasi (*Token*) pengguna. |
| Day 4 | Security Misconfig | Menyembunyikan rahasia dengan `.env`, mengamankan *header HTTP* dengan `Helmet`, dan membatasi *request* dengan `Rate Limit`. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Node.js terinstal.
- Code editor (VS Code, dll) siap pakai.
- Aplikasi API Client seperti *Postman* atau *Insomnia*.

### Misi Hari Ini: "Patching the API"

Minggu lalu kamu telah membangun API *CRUD & Login* dasar. Sayangnya, API tersebut masih memiliki celah keamanan jika diaudit.

Hari ini, kamu akan mempraktikkan cara mengamankan server secara menyeluruh berdasarkan materi minggu ini.

### Step 1: Persiapan Proyek

1. Buat direktori `mkdir lab-secure-api` lalu masuk: `cd lab-secure-api`.
2. Inisialisasi NPM: `npm init -y`.
3. Instal semua dependensi yang diperlukan:
```bash
npm install express sqlite3 dotenv helmet express-rate-limit
```

### Step 2: Implementasi Keamanan Backend

Siapkan dua file berikut.
**Dokumen 1 (`.env`)**
```text
PORT=8080
API_KEY=kunci_rahasia_tiss
```

**Dokumen 2 (`server.js`)**
Salin dan pelajari kode *backend* aman berikut ini:

```javascript
require('dotenv').config(); // Ekstrak variabel dari file .env
const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const sqlite3 = require('sqlite3').verbose();

const app = express();

// ===============================================
// 1. MIDDLEWARE KEAMANAN GLOBAL
// ===============================================
app.use(helmet()); // Mengamankan header HTTP
app.use(express.json()); 

// Membatasi request untuk mencegah Brute-force / DDoS
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 menit
  max: 5, // Batas maksimal 5 request per IP dalam 15 menit
  message: { pesan: "Terlalu banyak request. Silakan coba lagi setelah 15 menit." }
});
// Terapkan rate limit khusus untuk rute sensitif seperti login
app.use('/api/login', limiter); 

// ===============================================
// 2. SETUP DATABASE (SQLite)
// ===============================================
const db = new sqlite3.Database('./secure-db.sqlite');
db.serialize(() => {
  db.run("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, nama TEXT)");
});

// ===============================================
// 3. ROUTE AMAN DENGAN PARAMETERIZED QUERIES
// ===============================================
app.post('/api/users', (req, res) => {
  const { nama } = req.body;
  
  // Validasi input
  if (!nama) {
    return res.status(400).json({ pesan: "Bad Request. Nama tidak boleh kosong!" });
  }

  // Mencegah SQL Injection dengan Parameterized Query (?)
  const safeQuery = "INSERT INTO users (nama) VALUES (?)";
  db.run(safeQuery, [nama], function(err) {
    if (err) {
      // Menyembunyikan pesan error internal (Stack trace) dari klien
      return res.status(500).json({ pesan: "Terjadi kesalahan pada server." }); 
    }
    res.status(201).json({ pesan: "Data user berhasil ditambahkan!" });
  });
});

// ===============================================
// 4. JALANKAN SERVER
// ===============================================
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`[SECURE SERVER] Berjalan di port ${PORT}`));
```

### Step 3: Pengujian

1. Jalankan server: `node server.js`.
2. Gunakan *Postman* untuk mengirim *request POST* ke `http://localhost:8080/api/login`. 
3. Lakukan pengiriman data (meskipun *endpoint* ini belum ada *logic*-nya, *middleware* tetap berjalan) berulang-ulang dengan cepat.
4. Pada request ke-6, server akan menolak permintaan dengan status `429 Too Many Requests`! Ini membuktikan bahwa tameng *Rate Limit* berfungsi dengan baik.

---

## 🎯 Weekly Mission

### Misi: "Security Audit Report"

**Deskripsi:** Seorang *developer* atau *security engineer* yang baik harus mampu mendokumentasikan temuan audit keamanan.

**Tugas Mandiri:** Buat 1 file Markdown dengan nama `AUDIT_REPORT.md`. Rangkum 3 kategori kerentanan web yang telah dipelajari minggu ini (misal: SQL Injection, XSS, dan IDOR). Susun rangkuman tersebut dalam format **Tabel Markdown** yang mencakup:
1. Nama Kerentanan.
2. Dampak dan Bahayanya.
3. Solusi Pencegahannya (misal: *Parameterized Queries* untuk SQLi).

**Deliverables:**
1. Satu file `AUDIT_REPORT.md` yang ditulis dengan rapi dan profesional.

**Kriteria Sukses:**
- [ ] Terdapat tabel Markdown yang berisi klasifikasi 3 kerentanan.
- [ ] Tabel mencakup penjelasan kerentanan, dampaknya, dan solusi pencegahannya dengan tepat.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Modul NPM apa yang digunakan untuk membaca variabel dari file <i>.env</i>?</summary>

**Jawaban:** `dotenv`.
</details>

<details>
<summary>❓ [SEDANG] Serangan apa yang bisa dicegah dengan memastikan parameter ID pada URL divalidasi dan dicocokkan dengan data otorisasi (Token) pengguna yang sedang login?</summary>

**Jawaban:** *IDOR (Insecure Direct Object Reference)* / *Broken Access Control*.
</details>

<details>
<summary>❓ [SEDANG] Middleware apa yang digunakan untuk mencegah serangan <i>Brute-Force</i> pada endpoint <i>/api/login</i> dengan membatasi jumlah *request*?</summary>

**Jawaban:** `express-rate-limit`.
</details>

<details>
<summary>❓ [SULIT] Bagaimana Parameterized Queries (penggunaan tanda <code>?</code> pada SQLite) dapat mencegah SQL Injection?</summary>

**Jawaban:** Parameter `?` memastikan bahwa *driver database* memperlakukan input pengguna semata-mata sebagai "data", bukan sebagai "perintah SQL". Sehingga meskipun pengguna memasukkan *payload* seperti `' OR 1=1 --`, *database* tidak akan mengeksekusinya, melainkan hanya menyimpannya sebagai teks biasa.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya telah berhasil menggunakan `.env` untuk menyimpan konfigurasi port.
- [ ] Saya memahami implementasi *Helmet.js* untuk mengamankan *header HTTP*.
- [ ] Saya telah menerapkan *Rate Limiting* untuk mencegah *Brute-Force*.
- [ ] Saya telah menguji *rate limit* menggunakan Postman pada *Hands-On Lab*.
- [ ] Saya telah menyelesaikan tugas `AUDIT_REPORT.md`.

---

## 💬 Diskusi Minggu Ini

1. Setelah sebulan penuh fokus mempelajari pengembangan dan pengamanan *Backend* di *Forge Rank*, apakah kamu lebih tertarik pada perancangan pertahanan sistem (*Defensive/Blue Team/Developer*) atau kamu justru semakin penasaran tentang bagaimana cara membongkar dan menyerang sistem (*Offensive/Red Team*)?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│ 🎖️ THE FORGEMASTER                  │
│ RANK UP! FORGE COMPLETE             │
│ "Your code is a fortress.           │
│ Your logic is unbreakable."         │
│                                     │
└─────────────────────────────────────┘
```

Selamat! Kamu telah menyelesaikan *FORGE Rank*, fase yang berfokus pada pembangunan *backend* dan keamanan aplikasi. Mulai minggu depan, kita akan beralih ke pola pikir penyerang!

---

## ➡️ Preview Minggu Depan

**Minggu 15: BREACH RANK - Web Penetration Testing (Bagian 1)**

Fase membangun (*Yellow Team*) telah selesai. Selamat datang di **Rank Breach (Sabuk Merah)**! 
Mulai minggu depan, kita akan berganti peran menjadi *Red Team* (*Hacker/Penetration Tester*). Kita tidak lagi menyusun kode server, melainkan akan menggunakan *tools* standar industri seperti **Burp Suite** untuk melakukan intersep (mencegat), memanipulasi *request* HTTP, dan mencari celah keamanan nyata melalui simulasi *Capture The Flag* (CTF). 

> 🚀 *"The builder rests. The destroyer awakens."*

---

*📅 TISS Null Teaming · Week 14 · Day 5 · FORGE Rank*
