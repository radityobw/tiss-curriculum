# 🔨 Week 14 · Day 1: OWASP Top 10 & SQL Injection

> **Rank**: FORGE | **Minggu ke-14**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 14 · Day 1/5 | FORGE Rank (Minggu 5 dari 5) | Overall: 66/120 hari (55%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** peranan standar dokumen kerentanan OWASP Top 10.
2. **Mensimulasikan** metode eksploitasi serangan *SQL Injection (SQLi)*.
3. **Membentengi** kueri *Database* menggunakan *Parameterized Queries* demi menangkal ancaman injeksi.

---

## 📖 Materi Inti

### Dokumen Referensi Kerentanan: OWASP Top 10

Pada ranah keamanan web, sebagian besar sistem aplikasi diretas melalui pola eksploitasi kerentanan yang berulang. Untuk memberikan panduan pertahanan, sebuah yayasan global keamanan siber, **OWASP (Open Worldwide Application Security Project)**, menerbitkan dokumen referensi: **OWASP Top 10**.

Dokumen ini membeberkan 10 kategori kerentanan aplikasi web paling mematikan sedunia. Kita akan membedah celah-celah tersebut agar kamu mampu membangun benteng pertahanan kode secara kokoh (Blue/Yellow Team).

### A1: Injection (Eksploitasi Injeksi Kueri SQL)

Posisi puncak ancaman web yang sering dijumpai adalah: **Injection (Injeksi)**.
Kerentanan ini terjadi ketika server *Backend API* menangkap teks formulir input pengguna secara langsung tanpa sanitasi dan merangkainya ke dalam logika kueri Database.

**Contoh Kode Backend Rentan (Murni Rangkaian String):**
```javascript
// Server mengambil data username langsung dari input
const username = req.body.username; 

// SANGAT BERBAHAYA! Merangkai operasi string (String Concatenation)
const kueri = "SELECT * FROM users WHERE username = '" + username + "'";
db.get(kueri);
```

**Bagaimana Penyerang Menghancurkannya?**
Seorang penyerang tidak akan mengisi kolom login secara valid. Ia dapat menyuntikkan muatan logika injeksi:
`' OR '1'='1`

Maka susunan kueri SQL di dalam server akan terangkai menjadi:
`SELECT * FROM users WHERE username = '' OR '1'='1'`

Karena syarat klausa komparasi `'1'='1'` bernilai mutlak BENAR (True), mesin *Database SQL* akan mengabaikan validasi parameter sandi dan otomatis membiarkan akses terbuka, menyerahkan SELURUH DATA dalam tabel tersebut. Penyerang bahkan bisa menyisipkan komando modifikasi berbahaya lainnya (seperti `DROP TABLE`) untuk merusak peladen!

### Penangkal Mutlak: Parameterized Queries

Jangan pernah merangkai kueri manipulasi SQL dengan penggabungan teks konkatensi (`+`). Terapkan teknik delegasi penanganan argumen dari *Driver Database* (misalnya `sqlite3`), yaitu metode **Parameterized Queries** (Kueri Berparameter).

```javascript
const username = req.body.username; 

// AMAN: Gunakan tanda tanya (?) sebagai penyedia tempat (Placeholder) yang disanitasi
const kueri = "SELECT * FROM users WHERE username =?";

// Driver (sqlite3) otomatis akan membersihkan input username sehingga mesin hanya memandangnya sebagai data teks belaka.
db.get(kueri, [username]);
```
Dengan deklarasi `?`, berapapun karakter aneh (misal kutip tunggal) yang disuntikkan penyerang, peramban database niscaya akan menanganinya mutlak sebagai teks data (bukan baris perintah komando SQL).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari mensimulasikan mekanisme eksploitasi serangan *SQL Injection*!

1. Biasanya praktikum injeksi dieksekusi nyata memanfaatkan lab keamanan web. Kali ini kita mensimulasikan logika *code review*.
2. Bayangkan terdapat instalasi sistem rentan dengan kueri: `SELECT * FROM arsip WHERE kategori = 'Rahasia' AND sandi = '${input_sandi}'`.
3. Jika admin penyerang menyuntikkan injeksi pada payload variabel `input_sandi`:
`' OR 1=1 --`
4. Maka kueri instruksional peladen akan terangkai dan dieksekusi menjadi wujud ini:
`SELECT * FROM arsip WHERE kategori = 'Rahasia' AND sandi = '' OR 1=1 --'`
5. Simbol `--` pada sintaks *SQL* berarti "Deklarasi Komentar/Abaikan semua baris instruksi sisa di belakang karakter ini". Oleh karena itu, sisa fungsi validasi akan dibuang/diabaikan, dan gerbang data langsung terbuka akibat klausa kebenaran `1=1` (TRUE)!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengacu pada peta kerentanan global, apakah rincian kepanjangan singkatan yayasan nirlaba keamanan siber OWASP?</summary>

**Jawaban:** Open Worldwide Application Security Project.
</details>

<details>
<summary>❓ Ketika klien menyuntikkan muatan injeksi operasional `' OR '1'='1`, mengapa sistem Basis Data SQL otomatis mengabaikan validasi dan menyerahkan seluruh isi data arsipnya?</summary>

**Jawaban:** Sebab deklarasi klausa logika `OR '1'='1'` senantiasa dievaluasi bernilai statis mutlak *TRUE (Benar)*; memaksa eksekutor Basis Data mengamini kueri dan mengabaikan kegagalan evaluasi pengecekan kecocokan atribut nama, yang langsung berujung pada ekstraksi paksa rincian seluruh baris rekaman pada tabel bersangkutan tanpa terkecuali.
</details>

<details>
<summary>❓ Modifikasi arsitektur tameng perlindungan operasional penulisan komponen *Backend* apa yang wajib diimplementasikan selaku metode mitigasi mutlak demi menangkal serangan celah insiden peretasan *SQL Injection* secara permanen?</summary>

**Jawaban:** Penerapan implementasi penulisan metode penanganan tata bahasa fungsi *Parameterized Queries* / *Prepared Statements* (menyediakan simbol posisi *placeholder* `?` agar masukan input klien ditugaskan otomatis ditangani sistem *Driver* murni sebatas ditafsirkan sebagai format elemen teks murni statis belaka ketimbang skrip kueri peretasan perintah aktif penyayat eksekutor SQL).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya telah memahami peran panduan referensi pemetaan kerentanan OWASP Top 10
- [ ] Saya fasih menjabarkan secara rasional fungsi evaluasi logika matematis serangan `OR 1=1` pada metode eksploitasi peretasan *SQLi*
- [ ] Saya mengetahui bahaya operasional merangkai variabel fungsi pengguna langsung ke logika kueri arsitektur memori database *SQL*
- [ ] Saya menguasai praktik implementasi penulisan sintaks *Parameterized Queries* (`?`) di SQL lokal SQLite
- [ ] Saya telah selesai mengevaluasi seluruh rincian laporan Quiz Kilat di akhir modul

---

## 🔗 Resources

- [OWASP Top 10 Official](https://owasp.org/www-project-top-ten/) — Dokumen repositori absah resmi yang membeberkan 10 kategori taksonomi ancaman operasi keamanan aplikasi .
- [PortSwigger: SQL Injection](https://portswigger.net/web-security/sql-injection) — Sarana belajar pengujian lab penetrasi peretasan parameter jaringan antarmuka fungsi web dari perancang peladen piranti pengujian *Burp Suite* ternama!

---

## ➡️ Besok

**Day 2: Cross-Site Scripting (XSS)** — Usai kau melumpuhkan bahaya penyusupan data peladen pada infrastruktur Database, di materi besok kita menugaskan penelusuran arsitektur keamanan fungsi injeksi peramban operasional menargetkan manipulasi sistem eksternal pengunjung antarmuka aplikasi klien secara langsung: eksploitasi serangan **XSS**! Kerentanan fungsi manipulatif antarmuka situs jaringan ini bertujuan memperalat peramban lokal klien untuk mengeksekusi bongkahan logika *JavaScript* serangan tersembunyi!

---

*📅 TISS Null Teaming · Week 14 · Day 1 · FORGE Rank*
