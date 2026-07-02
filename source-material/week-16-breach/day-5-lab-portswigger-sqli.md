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

Kapasitas teknis eksploitasi peretasan (*Red Team Exploitation*) Anda telah diuji minggu ini dengan membedah kelemahan infrastruktur basis data target:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | SQLi: UNION-based | Menggabungkan tabel menggunakan *UNION SELECT* dan mendeteksi jumlah kolom menggunakan *ORDER BY*. |
| Day 2 | SQLi: Blind (Boolean & Time) | Melakukan injeksi SQL tanpa tampilan error, menggunakan respon lambat peladen untuk mengekstrak data (*Time-based SQLi*). |
| Day 3 | SQLMap: Automated Exploitation | Menggunakan SQLMap untuk mengekstrak data otomatis via konsol (flag `--dbs`, `--tables`, `--dump`). |
| Day 4 | Authentication Bypass | Mendobrak otentikasi login menggunakan *SQLi Bypass*, *Brute Force*, dan *Credential Stuffing*. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Koneksi internet yang stabil.
- Akun laboratorium di **[PortSwigger Web Security Academy](https://portswigger.net/web-security)**.

### Misi Hari Ini: "Membantai Tembok SQL (SQLi Gauntlet)"

Pada sesi ini, penggunaan *SQLMap* dilarang keras. Anda ditugaskan untuk mengeksploitasi kerentanan *SQL Injection* secara *manual* guna melatih intuisi penulisan kueri eksploitasi Anda.

### Step 1: Lab Dasar (Bypass Login)
1. Buka materi pembelajaran *PortSwigger SQL Injection*.
2. Pilih lab bertajuk: **"SQL injection vulnerability in WHERE clause allowing retrieval of hidden data"** atau **"SQL injection vulnerability allowing login bypass"**.
3. Akses halaman *Login*. 
4. Masukkan nama pengguna: `administrator'--` dan kosongkan kata sandi.
5. Klik *Login*. Anda akan berhasil masuk! Tanda `--` memerintahkan server untuk membuang pengecekan kata sandi di backend.

### Step 2: Lab Mahaguru (UNION Column Enumeration)
1. Pilih lab bertajuk: **"SQL injection UNION attack, determining the number of columns returned by the query"**.
2. Klik kategori produk, misal `/filter?category=Gifts`.
3. Injeksi kueri pada parameter URL untuk menebak jumlah kolom tabel sasaran:
 - `?category=Gifts' ORDER BY 1--`
 - `?category=Gifts' ORDER BY 2--`
 - Lanjutkan terus hingga server merespons dengan *Internal Server Error*. Jika error muncul pada `ORDER BY 4--`, artinya tabel tersebut persis memiliki 3 kolom.
4. Lanjutkan ekskavasi dengan mencari tahu tipe data masing-masing kolom menggunakan `'a'`:
 - `?category=Gifts' UNION SELECT NULL, 'a', NULL--`

### Step 3: Puncak Klasemen (Ekstraksi Arsip Sandi!)
1. Buka lab bertajuk: **"SQL injection UNION attack, retrieving data from other tables"**.
2. Lakukan pendeteksian jumlah kolom seperti pada Langkah 2.
3. Setelah jumlah kolom diketahui (misal 2 kolom). 
4. Ekstrak data tabel *users*: 
 `?category=Gifts' UNION SELECT username, password FROM users--`
5. Halaman web akan membeberkan baris `administrator` berserta kata sandinya. Salin kata sandi tersebut, lalu masuk ke halaman *Login* untuk menyelesaikan lab!

---

## 🎯 Weekly Mission

### Misi: "Buku Catatan Penaklukan (SQLi Writeups)"

**Deskripsi:** Pentester profesional selalu mendokumentasikan taktik eksploitasi mereka dalam format *Proof of Concept* (PoC) secara komprehensif.

**Tugas Mandiri:** Selesaikan **Minimal 3 Lab SQL Injection** dari *PortSwigger*. Buat manuskrip dokumentasi (di GitHub atau Notion) yang merangkum metodologi Anda dalam menaklukkan setiap lab tersebut (*Writeup* / *PoC*).

**Deliverables:**
1. Satu dokumen Markdown bernama `SQLI_WRITEUPS_PORTSWIGGER.md`.
2. Dokumen memuat 3 judul lab *PortSwigger* dengan rincian:
 - **Tujuan Lab** (Misal: Melakukan bypass login situs).
 - **Langkah Eksploitasi** (Catat urutan logika injeksi dan *payload* yang diaplikasikan).
 - **Screenshot** (Tangkapan layar konfirmasi keberhasilan lab dengan tulisan *'Solved'*).

**Kriteria Sukses:**
- [ ] 3 Lab SQLi berhasil ditaklukkan (status *solved*).
- [ ] Dokumen memuat rincian *payload* injeksi yang terbukti berhasil.
- [ ] Dokumentasi ditulis secara teknikal analitis, merincikan alur fungsi penggabungan *UNION SELECT*.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Pada taktik UNION SQLi, perintah SQL apakah yang digunakan secara iteratif (1, 2, 3, dst.) untuk menebak jumlah kolom tabel sasaran?</summary>

**Jawaban:** Kueri `ORDER BY` (contoh: `' ORDER BY 1--`).
</details>

<details>
<summary>❓ [MUDAH] Sebutkan alat open-source berbasis Python yang digunakan oleh pentester untuk mengeksploitasi kerentanan SQL Injection secara otomatis!</summary>

**Jawaban:** SQLMap.
</details>

<details>
<summary>❓ [SEDANG] Saat pentester berhadapan dengan target Blind SQLi yang sama sekali tidak menampilkan error atau perubahan tampilan, perintah SQL jenis apa yang disisipkan untuk memaksa peladen menunda respons (delay) sebagai bentuk konfirmasi?</summary>

**Jawaban:** Perintah *Time-based delay injection* seperti `SLEEP(10)` atau `pg_sleep(10)`.
</details>

<details>
<summary>❓ [SEDANG] Serangan apa yang mengeksploitasi formulir otentikasi dengan mencoba ulang kredensial (username/password) asli hasil kebocoran database perusahaan lain yang sudah diretas sebelumnya?</summary>

**Jawaban:** Credential Stuffing.
</details>

<details>
<summary>❓ [SULIT] Mengapa pentester harus menggunakan karakter sepasang setrip `--` pada akhir payload SQLi UNION seperti `' UNION SELECT username, password FROM users--`?</summary>

**Jawaban:** Sepasang karakter `--` (atau `#` pada MySQL) difungsikan sebagai instruksi *Comment Out* dalam SQL. Karakter ini sangat esensial untuk membatalkan (mengomentari) sisa-sisa perintah SQL orisinal dari developer backend yang tertulis setelah titik injeksi, sehingga mencegah terjadinya *Syntax Error*.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya telah membedah eksploitasi *SQLi UNION-based*.
- [ ] Saya fasih menjabarkan perbedaan *Blind SQLi (Boolean & Time-based)*.
- [ ] Saya mampu mendemonstrasikan pengoperasian *SQLMap* (termasuk fungsi `--dump`).
- [ ] Saya memahami teknik serangan *Authentication Bypass*.
- [ ] Saya telah menyelesaikan *Weekly Mission* dengan mengumpulkan naskah `SQLI_WRITEUPS_PORTSWIGGER.md`.

---

## 💬 Diskusi Minggu Ini

1. Sesudah mengeksplorasi serangan *UNION SQL Injection* yang manual, dan membandingkannya dengan alat otomatis *SQLMap*, metode manakah yang terasa lebih menegangkan bagimu? Mengapa seorang pemula sangat diharamkan untuk bergantung murni pada *SQLMap* tanpa memahami teori logika manual di baliknya?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ THE SQL ARCHITECT │
│ Week 16 Complete │
│ "Where there is an input, │
│ there is a way." │
│ │
└─────────────────────────────────────┘
```

Selamat! Operasional pengujian kerentanan *SQLi* telah Anda selesaikan secara sempurna di minggu ini!

---

## ➡️ Preview Minggu Depan

**Minggu 17: Web Exploitation — XSS, CSRF & Beyond**

Kita telah sukses membobol jantung peladen (*Database Backend*)! Di minggu depan, serangan bakal diarahkan ke kerentanan sisi klien (*Frontend Client-Side*). Kita akan menyisipkan kode berbahaya langsung ke dalam situs korban melalui **Cross-Site Scripting (XSS)** untuk mencuri *Cookie* otentikasi, merangkainya dengan **CSRF** untuk memanipulasi profil pengguna, dan diakhiri dengan manuver tingkat tinggi **File Upload Vulnerability** untuk menanam *Webshell Backdoor* di server!

> 🚀 *"The database bleeds. Now, corrupt the client."*

---

*📅 TISS Null Teaming · Week 16 · Day 5 · BREACH Rank*
