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

Minggu pemuncak pamungkas di pelataran *Forge* telah berlalu. Dirimu beralih dimensi mendapuk pemahaman Peretas *(OWASP Top 10)* guna mengenali kerentanan dan menyumbatnya paripurna:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | OWASP & SQLi | Bedah bongkar mekanisme *SQL Injection* lantas tameng Kueri Berparameter `?`. |
| Day 2 | XSS & Sanitasi | Perkenalan trinitas varian *Stored, Reflected, DOM XSS* serta larangan penggunaan parameter `innerHTML`. |
| Day 3 | IDOR & BAC | Keculasan eksploitasi akses parameter URL ID yang tidak disinkronkan dengan otorisasi klien (*Token*). |
| Day 4 | Kelalaian Misconfig | Menyembunyikan gembok parameter brankas rahasia `.env`, membungkus bodi *headers HTTP* menggunakan `Helmet`, dan merem badai serangan menggunakan modul batas akses `Rate Limit`. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Node.js terinstal utuh.
- Editor kode beroperasi siap pakai.
- Modul klien API *Postman*.

### Misi Hari Ini: "Operasi Benteng Pertahanan Mutlak (Patching API)"

Minggu lalu kamu telah mendirikan arsitektur *API CRUD & Login* dasar yang mengandalkan fungsionalisasi peladen sandi *Bcrypt*. Sayangnya, API minggu lalu masih menyimpan serpihan lubang kelemahan fatal jika diaudit keamanannya.

Hari ini, dirimu dituntut menyematkan sulingan lapis baja komplit membalut utuh peladen arsitekturmu secara paripurna.

### Step 1: Merakit Sarang Perisai Terakhir

1. Bentuk direktori `mkdir lab-secure-api` lalu masuki navigasinya: `cd lab-secure-api`.
2. Absahkan inisiasi modul: `npm init -y`.
3. Borong instalasi perisai komplit ekosistem Node:
```bash
npm install express sqlite3 bcrypt dotenv helmet express-rate-limit
```

### Step 2: Mengukir Kodingan Arsitektur Kebal (The Unbreakable Vault)

Siapkan 2 dokumen rahasia terpisah!
**Dokumen 1 (`.env`)**
```text
PORT_SERVER=8080
SANG_RAHASIA=kunci_dewa_tiss_2026
```

**Dokumen 2 (`server.js`)**
Salin struktur koding benteng pelindungan mutakhir ini!

```javascript
// 1. Memanggil bala bantuan perlindungan require('dotenv').config(); // Ekstrak variabel lingkungan
const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const sqlite3 = require('sqlite3').verbose();

const app = express();

// ===============================================
// 2. ROMPI TAMENG GLOBAL (Middleware Keamanan)
// ===============================================
app.use(helmet()); // Tutupi ekspos versi peladen pada Header (Misconfig Patch)
app.use(express.json()); 

// Rem pembatas serangan DDOS/Brute-force (Maksimal 5 serangan per tiap 15 menit)
const penahanSerbuan = rateLimit({
 windowMs: 15 * 60 * 1000,
 max: 5,
 message: { pesan: "Peringatan! Indikasi Serangan Terdeteksi. Santai dulu 15 menit." }
});
app.use('/api/login', penahanSerbuan); 

// ===============================================
// 3. DATABASE AMAN (Penanganan SQLite)
// ===============================================
const db = new sqlite3.Database('./brankas.db');
db.serialize(() => {
 db.run("CREATE TABLE IF NOT EXISTS pasukan (id INTEGER PRIMARY KEY, nama TEXT)");
});

// ===============================================
// 4. RUTE TANGGUH (Parameterized Queries)
// ===============================================
app.post('/api/pasukan', (req, res) => {
 const namaAgen = req.body.nama;
 
 // Cek kelalaian hampa atribut (Cegah pelaporan Error 500 nembus ke depan)
 if(!namaAgen) return res.status(400).json({pesan: "Error 400. Nama agen tidak didefinisikan!"});

 // TAMENG PENANGKAL SQL INJECTION: Murni eksploitasi parameter placeholder `?`
 const pelatukAman = "INSERT INTO pasukan (nama) VALUES (?)";
 db.run(pelatukAman, [namaAgen], function(err) {
 if(err) return res.status(500).json({pesan: "Galat Sistem Internal."}); // Jejak Stack trace disembunyikan
 res.status(201).json({pesan: "Data Agen baru sukses ditambahkan!"});
 });
});

// Menyalakan fungsi gerbang melirik variabel.env (Atau port default 3000 jika absen)
const PORT = process.env.PORT_SERVER || 3000;
app.listen(PORT, () => console.log(`[BENTENG PELADEN] Beroperasi utuh di Port ${PORT}`));
```

### Step 3: Pengujian Penetrasi Keras

1. Nyalakan server `node server.js`.
2. Gunakan klien penembak *Postman*, berondong serangan metode POST tanpa henti ke lajur rute `http://localhost:8080/api/login` sebanyak 6 kali berturut-turut laksana serangan simulasi pelacak *Brute-Force*.
3. Pada transmisi serangan serangan ke-6, server takkan tumbang, ia lantas mengamankan akses dengan membalas kode penolakan *429 Too Many Requests* dan memutus permintaan dari entitas peretas tersebut! Benteng *Rate Limit* berfungsi secara absolut.

---

## 🎯 Weekly Mission

### Misi: "Manifesto Keamanan (Security Audit Report)"

**Deskripsi:** Seorang arsitek pengembang (*Yellow Team / Blue Team*) sejati tidak sekadar handal merakit arsitektur kode peladen, namun juga dituntut mumpuni merilis dokumen pertanggungjawaban audit kerentanan aplikasi.

**Tugas Mandiri:** Buat 1 fail log berekstensi Markdown (berikan penamaan spesifik `AUDIT_REPORT.md`). Di dalamnya, rangkum secara sistematis 3 kategori bahaya kerentanan web masa kini (*Pilih secara leluasa 3 pemetaan kerentanan dari daftar modul materi OWASP yang kau pelajari minggu ini, misal Injeksi, IDOR, XSS, ataupun Data Exposure*). Susun sebuah representasi format Tabel Markdown ringkas nan padat yang mengkomparasikan: 
1) Nama Kerentanan, 2) Bahaya dan Konsekuensinya Jika Tereksekusi, 3) Metodologi Solusi Penangkal Keamanannya (seperti kueri parameter `?`).

**Deliverables:**
1. Satu fail dokumen `AUDIT_REPORT.md` terangkai sempurna laksana penyusun naskah profesional arsitek aplikasi.

**Kriteria Sukses:**
- [ ] Tersedia struktural Tabel *Markdown* audit klasifikasi kerentanan di dalamnya.
- [ ] Mencakup paparan komprehensif atas tiga penjabaran ancaman beserta pembedahan teknik solusinya.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Mengingat sandi perlindungan peladen membutuhkan pengikatan referensi konfigurasi, modul ekstensi NPM apakah yang perlu diinstal demi menghimpun selimut ekstrak parameter `.env`?</summary>

**Jawaban:** Paket peranti modul instalasi `dotenv`.
</details>

<details>
<summary>❓ [SEDANG] Dari bongkahan parameter ancaman *OWASP*, tipe celah kerentanan fatal otorisasi manakah yang dapat dipicu hanya bermodalkan memodifikasi secara paksa serpihan alamat embel argumen parameter angka atribut *ID* pada URL demi meretas masuk data spesifik milik pengunjung lain?</summary>

**Jawaban:** Eksploitasi kerentanan *IDOR* (*Insecure Direct Object Reference*) yang berinduk pada kategori ancaman peretasan *Broken Access Control*.
</details>

<details>
<summary>❓ [SEDANG] serabut pencegat operasi lapisan antarmuka peladen (*Middleware*) tameng fungsi spesifik klasifikasi apa yang niscaya dicekokkan demi meregulasi membatasi menghalau laju badai transmisi eksploitasi serangan massal tipe *DDoS* maupun tebakan instan *Brute-Force Password* secara membabi-buta tanpa rem?</summary>

**Jawaban:** fungsi pembatas jangkauan modul `rateLimit` (berasal dari integrasi ekstensi *middleware* dependensi arsitektur paket `express-rate-limit`).
</details>

<details>
<summary>❓ [SULIT] Jelaskan benang merah argumen tabrakan parameter pencegahan celah infeksi *SQL Injection* di mana antarmuka *Backend Node.js* diwajibkan menyertakan penyusupan sintaks simbol atribut penulisan kueri parameter `?` pada sirkulasi ekstensi pelaksanaan `db.run`!</summary>

**Jawaban:** Atribut parameter pelambangan simbol `?` berperan krusial berlaku laksana deklarasi wadah penyaringan parameter (Kueri Berparameter / *Parameterized Queries*). Logika metode operasi tersebut wewenang penafsiran dan merangkai struktur teks modifikasi input klien secara mutlak ke komponen utusan mesin *Database Driver*. Komponen *Driver* database lantas secara murni mensterilkan penanganan bongkahan masukan string sehingga terlepas meski *Hacker* mengetik barisan skrip utuh peretasan manipulasi kueri fungsi *SQL* modifikasi ganda silang (semisal sintaks kondisi eksploitasi parameter klausa Boolean *OR 1=1*), peramban eksekutor Database bakal tetap memandangnya secara pasif terisolasi layaknya rentetan bodi teks polos belaka serta mutlak menolak mengkompilasinya / mengartikannya / urung mengeksekusinya sebagai bentuk struktur fungsi aktif baris komando!
</details>

---

## 📋 Weekly Checklist

- [ ] Saya sukses mengemas serta mengkarantina payload Kunci sakti dalam deklarasi `.env`
- [ ] Saya telah merakit terusan peranti integrasi tameng perlindungan informasi arsitektur HTTP *Helmet.js*
- [ ] Saya berhasil menerjunkan modul peredam rute akses *Rate Limiting* untuk mencekik laju eksploitasi injeksi transmisi *Brute-Force*
- [ ] Saya kelar menuntaskan rekam uji coba pengujian simulasi penetrasi rute pelacak pasca arsitektur perlindungan diaplikasikan (*Hands-On Lab API Security Testing*)
- [ ] Saya sukses menuntaskan kompilasi parameter perumusan tabel pembedahan 3 kerentanan OWASP untuk submisi laporan modul dokumen evaluasi (*AUDIT_REPORT.md*)

---

## 💬 Diskusi Minggu Ini

1. Pasca sebulan penuh dirimu secara kontinu mengukir pengalaman merancang simulasi perakitan arsitektur infrastruktur peladen rahasia terpusat *Backend Server* berhimpit tameng pengamanan di ekosistem hierarki peringkat *Forge Rank* ini, apakah secara personal benak nalurimu mendapati gairah logik yang lebih terpacu dan bergolak girang tertuju pada sirkulasi seni penyerangan parameter bedah eksploitasi pembongkaran retas celah penyerangan arsitektur keamanan fungsi aplikasi (*Taktik Offensive Red Team Pen Tester*), ataukah dirimu lebih menikmati kecenderungan parameter kepuasan menata penulisan ketahanan perakitan fungsi modul sirkulasi perbaikan serta membentengi keamanan perisai rancangan struktural *Backend* (*Metodologi Defensive Yellow/Blue Team*)?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ THE FORGEMASTER │
│ RANK UP! FORGE COMPLETE │
│ "Your code is a fortress. │
│ Your logic is unbreakable." │
│ │
└─────────────────────────────────────┘
```

Selamat! Kau berhasil menamatkan rute kurikulum arsitektur sistem infrastruktur peladen *FORGE Rank*—fase terpanjang nan terpadat yang melatih kapasitas logik komputasimu merancang kerangka benteng aplikasi peranti lunak! Sekarang tiba masanya untuk merancang taktik spesifik membakar arsitektur benteng sistem pertahanan peladen rentan tersebut!

---

## ➡️ Preview Minggu Depan

**Minggu 15: BREACH RANK - Web Penetration Testing (Bagian 1)**

Masa-masa menyusun koding murni perakitan infrastruktur pengembang (*Yellow Team*) pada zona nyaman arsitektur di pelataran lingkungan aman telah tuntas dilewati. Selamat mendarat di teritori kelam **Rank Breach (Sabuk Merah)**! Saatnya mendedikasikan membanting pergeseran parameter fungsi otak secara radikal menyelaraskan nalar insting menjadi profil agresif spesialis Peretas Aplikasi Klien tulen *(Insting Red Team Hacker Pen Tester Web Exploitation Vulnerability App Penetration Testing Component Methodology)*! Kita lantas bakal mengistirahatkan rutinitas penyusunan koding arsitektur penulisan infrastruktur skrip peladen. Bermodalkan penyediaan persenjataan ganda fungsi pisau Swiss-Army bedah peramban mutakhir peretas industri mutlak global bertitel instalasi fungsi *Burp Suite Network Interceptor Proxy Tool Web Exploitation API Test Network Component Test Platform Testing Form System Hacker Data Node Network HTTP Method Hacking Architecture Security*, dirimu siap meluncur serta diterjunkan mencekik memanipulasi merancang fungsi menahan modifikasi transmisi paket hantaran pertukaran payload arsitektur peramban jaringan *HTTP* seraya meraba eksploitasi menginfeksi menjamah letak kerentanan arsitektur situs operasi kustom parameter uji coba kompetisi retas flag simulasi *(Capture The Flag Vulnerability Cyber Simulation Challenge Vulnerable Site Hacking System Test Web Logic Network API Request Manipulation Interface)*!

> 🚀 *"The builder rests. The destroyer awakens."*

---

*📅 TISS Null Teaming · Week 14 · Day 5 · FORGE Rank*
