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

Karena syarat klausa komparasi `'1'='1'` bernilai mutlak BENAR (True), mesin *Database SQL* akan mengabaikan validasi parameter sandi dan otomatis membiarkan akses terbuka, menyerahkan SELURUH DATA dalam tabel tersebut. Penyerang bahkan bisa menyisipkan komando modifikasi berbahaya lainnya (seperti `DROP TABLE`) untuk merusak *database*!

### Penangkal Mutlak: Parameterized Queries

Jangan pernah merangkai kueri manipulasi SQL dengan penggabungan teks konkatensi (`+`). Terapkan teknik pendelegasian argumen melalui *Driver Database* (misalnya `sqlite3`), yaitu metode **Parameterized Queries** (Kueri Berparameter).

```javascript
const username = req.body.username; 

// AMAN: Gunakan tanda tanya (?) sebagai tempat penampung (Placeholder) yang disanitasi
const kueri = "SELECT * FROM users WHERE username = ?";

// Driver (sqlite3) otomatis akan membersihkan input sehingga mesin hanya memandangnya sebagai data teks belaka.
db.get(kueri, [username]);
```
Dengan deklarasi `?`, berapapun karakter aneh (misal kutip tunggal) yang disuntikkan penyerang, *Database Engine* akan menganggapnya secara mutlak sebagai teks data biasa (bukan perintah SQL).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari mensimulasikan mekanisme eksploitasi serangan *SQL Injection*!

1. Biasanya praktikum injeksi dieksekusi di lab keamanan web interaktif. Kali ini kita mensimulasikannya via tinjauan kode (*code review*).
2. Bayangkan terdapat instalasi sistem rentan dengan kueri: `SELECT * FROM arsip WHERE kategori = 'Rahasia' AND sandi = '${input_sandi}'`.
3. Jika penyerang menyuntikkan kode ini pada kolom `input_sandi`:
`' OR 1=1 --`
4. Maka kueri yang dieksekusi oleh server akan terangkai menjadi seperti ini:
`SELECT * FROM arsip WHERE kategori = 'Rahasia' AND sandi = '' OR 1=1 --'`
5. Simbol `--` pada sintaks *SQL* berarti "Deklarasi Komentar / Abaikan semua teks di belakang karakter ini". Oleh karena itu, sisa fungsi validasi sandi di belakang akan dibuang, dan akses data langsung terbuka lebar akibat klausa kebenaran `1=1` (TRUE)!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengacu pada peta kerentanan global, apakah rincian kepanjangan singkatan yayasan nirlaba keamanan siber OWASP?</summary>

**Jawaban:** Open Worldwide Application Security Project.
</details>

<details>
<summary>❓ Saat penyerang menyuntikkan kode `' OR '1'='1`, mengapa sistem Database SQL otomatis mengabaikan validasi dan menyerahkan seluruh datanya?</summary>

**Jawaban:** Karena klausa logika `OR '1'='1'` akan selalu bernilai *TRUE (Benar)*. Hal ini memaksa *Database* untuk mengabaikan pengecekan *username* atau sandi, dan langsung mengambil seluruh baris data di dalam tabel tersebut.
</details>

<details>
<summary>❓ Teknik apa di sisi *Backend* yang wajib diimplementasikan sebagai metode mitigasi mutlak untuk menangkal serangan *SQL Injection* secara permanen?</summary>

**Jawaban:** Penggunaan **Parameterized Queries** atau **Prepared Statements**. Teknik ini menggunakan simbol *placeholder* (seperti `?`) sehingga input pengguna akan langsung ditangani oleh *Driver* database sebagai teks biasa, bukan sebagai bagian dari perintah SQL yang bisa dieksekusi.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya telah memahami peran panduan referensi pemetaan kerentanan OWASP Top 10.
- [ ] Saya paham mengapa injeksi logika matematika `OR 1=1` sangat berbahaya pada eksploitasi *SQL Injection*.
- [ ] Saya mengerti bahayanya merangkai *string* inputan pengguna langsung ke dalam logika kueri *SQL*.
- [ ] Saya menguasai praktik mitigasi keamanan menggunakan sintaks *Parameterized Queries* (`?`) di *SQLite*.
- [ ] Saya telah mereview pertanyaan pada sesi *Quiz Kilat*.

---

## 🔗 Resources

- [OWASP Top 10 Official](https://owasp.org/www-project-top-ten/) — Dokumen resmi yang membeberkan 10 kategori taksonomi ancaman operasi keamanan aplikasi web.
- [PortSwigger: SQL Injection](https://portswigger.net/web-security/sql-injection) — Sarana belajar dan lab pengujian *SQL Injection* dari pembuat *Burp Suite* ternama!

---

## ➡️ Besok

**Day 2: Cross-Site Scripting (XSS)** — Setelah kamu memahami cara mencegah kebocoran data di infrastruktur *Database* akibat SQLi, besok kita akan beralih ke kerentanan yang menyerang *browser* korban secara langsung: **Cross-Site Scripting (XSS)**! Celah keamanan ini memungkinkan penyerang menyisipkan *JavaScript* berbahaya ke dalam *browser* pengguna lain untuk mencuri token sesi atau memanipulasi tampilan.

---

*📅 TISS Null Teaming · Week 14 · Day 1 · FORGE Rank*
