# 💀 Week 16 · Day 5: Lab & Weekly Mission PortSwigger SQLi

> **Rank**: BREACH | **Minggu ke-16**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓░░░░░░] 40% — BREACH Rank (Minggu 2 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░] 66% — Hari 80 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → 🔄 BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Kemampuan eksploitasi kamu telah diuji minggu ini dengan membedah berbagai kelemahan pada *database* target:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | SQLi: UNION-based | Menggabungkan tabel menggunakan *UNION SELECT* dan mendeteksi jumlah kolom menggunakan *ORDER BY*. |
| Day 2 | SQLi: Blind (Boolean & Time) | Melakukan injeksi SQL tanpa tampilan error, menggunakan logika *True/False* atau respon lambat peladen untuk mengekstrak data (*Time-based SQLi*). |
| Day 3 | SQLMap: Automated Exploitation | Menggunakan SQLMap untuk mengekstrak data otomatis via terminal (menggunakan argumen `--dbs`, `--tables`, `--dump`). |
| Day 4 | Authentication Bypass | Mendobrak sistem *login* menggunakan trik *SQLi Bypass*, *Brute Force*, *Credential Stuffing*, hingga manipulasi *Session*. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Koneksi internet yang stabil.
- Akun gratis di **[PortSwigger Web Security Academy](https://portswigger.net/web-security)**.

### Misi Hari Ini: "Membantai Tembok SQL (SQLi Gauntlet)"

Pada sesi ini, penggunaan *SQLMap* dilarang keras. Kamu ditugaskan untuk mengeksploitasi kerentanan *SQL Injection* secara *manual* untuk melatih logika penulisan kueri SQL.

### Step 1: Lab Dasar (Bypass Login)
1. Buka materi pembelajaran *PortSwigger SQL Injection*.
2. Pilih lab bertajuk: **"SQL injection vulnerability in WHERE clause allowing retrieval of hidden data"** atau **"SQL injection vulnerability allowing login bypass"**.
3. Akses halaman *Login*. 
4. Masukkan nama pengguna: `administrator'--` dan kosongkan kata sandi.
5. Klik *Login*. Kamu akan berhasil masuk! Tanda `--` memerintahkan *database* untuk mengabaikan pengecekan kata sandi di sistem *backend*.

### Step 2: Lab Menengah (UNION Column Enumeration)
1. Pilih lab bertajuk: **"SQL injection UNION attack, determining the number of columns returned by the query"**.
2. Klik kategori produk, misal `/filter?category=Gifts`.
3. Injeksi kueri pada parameter URL untuk menebak jumlah kolom:
 - `?category=Gifts' ORDER BY 1--`
 - `?category=Gifts' ORDER BY 2--`
 - Lanjutkan terus hingga *server* merespons dengan *Internal Server Error*. Jika *error* muncul pada `ORDER BY 4--`, artinya tabel aslinya memiliki persis 3 kolom.
4. Lanjutkan mencari tahu tipe data (mencari kolom yang bisa menampung teks) menggunakan karakter `'a'`:
 - `?category=Gifts' UNION SELECT NULL, 'a', NULL--`

### Step 3: Puncak Tantangan (Ekstraksi Kata Sandi!)
1. Buka lab bertajuk: **"SQL injection UNION attack, retrieving data from other tables"**.
2. Lakukan pencarian jumlah kolom seperti pada Langkah 2.
3. Setelah jumlah kolom diketahui (misal 2 kolom) dan keduanya bisa memuat *string*, kamu bisa mencuri data.
4. Ekstrak data dari tabel *users*: 
 `?category=Gifts' UNION SELECT username, password FROM users--`
5. Halaman web akan membeberkan baris data pengguna `administrator` berserta kata sandinya. Salin kata sandi tersebut, lalu gunakan untuk *Login* demi menyelesaikan lab!

---

## 🎯 Weekly Mission

### Misi: "Buku Catatan Penaklukan (SQLi Writeups)"

**Deskripsi:** *Pentester* profesional selalu mendokumentasikan langkah eksploitasi mereka ke dalam laporan *Proof of Concept* (PoC) yang komprehensif.

**Tugas Mandiri:** Selesaikan **Minimal 3 Lab SQL Injection** dari *PortSwigger*. Buat catatan (di GitHub atau Notion) yang merangkum caramu menaklukkan setiap lab tersebut (*Writeup* / *PoC*).

**Deliverables:**
1. Buat satu dokumen Markdown bernama `SQLI_WRITEUPS_PORTSWIGGER.md`.
2. Dokumen harus memuat 3 judul lab *PortSwigger* yang berhasil kamu selesaikan, beserta:
 - **Tujuan Lab** (Misal: Melakukan bypass login situs).
 - **Langkah Eksploitasi** (Catat urutan logika injeksi dan *payload* kueri yang kamu gunakan).
 - **Screenshot** (Tangkapan layar konfirmasi keberhasilan lab dengan tulisan *'Solved'*).

**Kriteria Sukses:**
- [ ] 3 Lab SQLi berhasil ditaklukkan (status *solved*).
- [ ] Dokumen memuat rincian *payload* injeksi yang terbukti berhasil.
- [ ] Dokumentasi ditulis secara teknikal dan analitis, merincikan logika dari kueri *SQLi* yang digunakan.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Pada teknik UNION SQLi, perintah SQL apakah yang dikirimkan secara berurutan (1, 2, 3, dst.) untuk menebak jumlah kolom tabel asli?</summary>

**Jawaban:** Perintah `ORDER BY` (contoh: `' ORDER BY 1--`).
</details>

<details>
<summary>❓ [MUDAH] Apa nama *tools* open-source berbasis Python yang populer digunakan oleh *Pentester* untuk mengeksekusi kerentanan SQL Injection secara otomatis?</summary>

**Jawaban:** SQLMap.
</details>

<details>
<summary>❓ [SEDANG] Pada skenario Blind SQLi di mana aplikasi web sama sekali tidak menampilkan error atau perubahan di layar, perintah SQL jenis apa yang bisa digunakan untuk memastikan *database* memproses kueri penyerang?</summary>

**Jawaban:** Perintah *Time-based delay injection* seperti `SLEEP(10)` atau `pg_sleep(10)` untuk memaksa *database* menjeda proses (sehingga waktu *loading* web akan melambat).
</details>

<details>
<summary>❓ [SEDANG] Serangan apa yang menggunakan kombinasi *username* dan *password* dari kebocoran data (*data breach*) lama di perusahaan lain, untuk mencoba *login* secara paksa ke situs web target saat ini?</summary>

**Jawaban:** Credential Stuffing.
</details>

<details>
<summary>❓ [SULIT] Mengapa kita perlu menambahkan karakter sepasang setrip `--` pada akhir payload SQLi seperti `' UNION SELECT username, password FROM users--`?</summary>

**Jawaban:** Sepasang karakter `--` (atau `#` pada MySQL) berfungsi sebagai *Comment Out* (komentar) dalam bahasa SQL. Fungsinya adalah untuk mengabaikan / membatalkan semua sisa perintah SQL asli yang ditulis oleh *developer* di *backend* (setelah titik injeksi), sehingga kueri SQL tidak *error* (Syntax Error).
</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami teknik eksploitasi *UNION-based SQLi*.
- [ ] Saya bisa menjelaskan konsep *Blind SQLi (Boolean & Time-based)*.
- [ ] Saya mampu mendemonstrasikan perintah dasar *SQLMap* (termasuk `--dump`).
- [ ] Saya memahami mekanisme *Authentication Bypass* dan bahaya celah *Session*.
- [ ] Saya telah menyelesaikan *Weekly Mission* dengan menyusun dokumen `SQLI_WRITEUPS_PORTSWIGGER.md`.

---

## 💬 Diskusi Minggu Ini

Setelah merasakan betapa melelahkannya mencari celah *SQL Injection* secara manual dan membandingkannya dengan kemudahan otomatisasi dari *SQLMap*, mengapa menurutmu sangat penting bagi seorang pemula untuk tetap mempelajari dan menguasai *SQLi* secara manual sebelum boleh menggunakan *tools* otomatis?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│        🎖️ THE SQL ARCHITECT          │
│          Week 16 Complete           │
│      "Where there is an input,      │
│          there is a way."           │
│                                     │
└─────────────────────────────────────┘
```

Selamat! Eksploitasi kerentanan *SQL Injection* telah berhasil kamu pelajari minggu ini!

---

## ➡️ Preview Minggu Depan

**Minggu 17: Web Exploitation — XSS, CSRF & Beyond**

Kita telah sukses membobol server *Backend* (*Database*)! Minggu depan, kita akan beralih menyerang sisi korban/pengunjung web (*Client-Side*). Kamu akan belajar cara menyisipkan kode berbahaya ke dalam halaman web untuk mencuri *Cookie* orang lain menggunakan teknik **Cross-Site Scripting (XSS)**. Kamu juga akan belajar cara memaksa pengguna melakukan aksi tanpa disadari melalui **CSRF**, dan diakhiri dengan menanam program peretas (*Webshell Backdoor*) langsung ke server menggunakan **File Upload Vulnerability**!

> 🚀 *"The database bleeds. Now, corrupt the client."*

---

*📅 TISS Null Teaming · Week 16 · Day 5 · BREACH Rank*
