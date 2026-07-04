# 🛡️ Week 21 · Day 1: Apache/Nginx Log Format

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 21 · Day 1/5 | SENTINEL Rank (Minggu 2 dari 5) | Overall: 101/120 hari (84%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedah** anatomi format log standar (*Combined Log Format*) dari peladen Apache dan Nginx.
2. **Membedakan** fungsi antara *Access Logs* dan *Error Logs*.
3. **Mengekstrak** informasi penting (IP, Timestamp, Method, URL, Status Code) secara manual dari log.

---

## 📖 Materi Inti

### Dua Jenis Log Utama: Access vs Error

Sebagian besar aplikasi web modern menggunakan Apache atau Nginx sebagai *web server*. Server ini secara otomatis mendokumentasikan setiap kejadian ke dalam dua kategori log utama:

1. **Access Logs:** Mencatat semua permintaan (*HTTP Request*) masuk ke server, baik yang berhasil (Status 200 OK) maupun yang ditolak (misal: Status 403 Forbidden).
2. **Error Logs:** Mencatat masalah internal pada server, seperti kesalahan eksekusi modul (*PHP fatal error*), kehabisan memori, atau masalah konfigurasi.

Bagi Analis SOC, **Access Logs** adalah sumber data primer untuk memantau aktivitas pengguna dan mendeteksi serangan siber, seperti percobaan injeksi (*SQLi*) atau *Cross-Site Scripting* (*XSS*).

### Anatomi Baku: Combined Log Format

Apache dan Nginx menggunakan format log standar industri yang dikenal sebagai *Combined Log Format*. Mari kita bedah struktur log berikut:

`192.168.1.50 - - [21/Oct/2026:14:05:32 +0700] "GET /login.php HTTP/1.1" 200 4523 "http://google.com" "Mozilla/5.0 (Windows NT 10.0)"`

Baris log tersebut terdiri dari 7 kolom (*fields*) utama:
1. **`192.168.1.50` (IP Address):** Alamat IP klien yang melakukan permintaan.
2. **`- -` (Identitas & Pengguna):** Biasanya kosong (ditandai dengan tanda hubung) kecuali server menggunakan metode autentikasi dasar (*HTTP Basic Auth*).
3. **`[21/Oct... +0700]` (Timestamp):** Waktu kejadian (*tanggal dan jam*) beserta informasi zona waktu peladen.
4. **`"GET /login.php HTTP/1.1"` (Request Line):** Terdiri dari Metode HTTP (`GET`), *endpoint* yang diminta (`/login.php`), dan versi HTTP. Kolom ini sangat penting karena muatan serangan (*payload*) sering tercatat di sini.
5. **`200` (Status Code):** Kode respon dari server (200 = Sukses, 302 = Redirect, 404 = Not Found, 401/403 = Forbidden/Unauthorized, 500 = Internal Server Error).
6. **`4523` (Response Size):** Ukuran paket balasan yang dikirim ke klien (dalam satuan *Bytes*). Lonjakan ukuran ini pada permintaan tertentu bisa mengindikasikan bahwa data berhasil diakses atau dieksfiltrasi.
7. **`"http://google.com"` (Referer) & `"Mozilla..."` (User-Agent):** *Referer* mencatat dari halaman web mana pengunjung berasal. *User-Agent* memuat informasi sistem operasi dan browser klien (Alat peretasan otomatis seperti SQLMap sering kali menggunakan *User-Agent* khusus jika tidak disamarkan).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari belajar menganalisis log akses server web!

1. Periksa tiga baris *Access Log* berikut:
   - `Baris 1: 10.0.0.99 - - [01/Nov/2026:01:10:05 +0700] "GET /admin HTTP/1.1" 404 210 "-" "Mozilla/5.0"`
   - `Baris 2: 10.0.0.99 - - [01/Nov/2026:01:10:06 +0700] "GET /administrator HTTP/1.1" 404 210 "-" "Mozilla/5.0"`
   - `Baris 3: 10.0.0.99 - - [01/Nov/2026:01:10:07 +0700] "GET /admin/dashboard HTTP/1.1" 200 15400 "-" "Mozilla/5.0"`
2. **Analisis Baris 1 dan 2:** Terdapat permintaan berurutan (dalam detik) ke halaman admin yang menghasilkan status `404 Not Found`. Ini mengindikasikan adanya aktivitas pemindaian paksa (*Directory Bruteforce*).
3. **Analisis Baris 3:** Pada permintaan ke-3, status berubah menjadi `200 OK` (rute ditemukan) dan ukuran respon (`15400` bytes) melonjak drastis dari sebelumnya (`210` bytes).
   - **Kesimpulan:** Penyerang berhasil menemukan direktori administratif yang sah dan server memuat halaman tersebut secara penuh (*True Positive*).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar antara <i>Access Logs</i> dan <i>Error Logs</i> pada web server?</summary>

**Jawaban:** *Access Logs* mencatat setiap lalu lintas masuk (*Requests*) dari klien terlepas dari sukses atau gagal, sedangkan *Error Logs* hanya mencatat masalah teknis internal pada server (seperti kegagalan eksekusi skrip atau *crash* modul).
</details>

<details>
<summary>❓ Dalam format log <i>Combined Log Format</i>, atribut (*Log Field*) apa yang menunjukkan alamat situs web asal yang membawa pengguna ke halaman kita?</summary>

**Jawaban:** Referer (atau HTTP Referer).
</details>

<details>
<summary>❓ Jika ukuran respons (*Response Size*) melonjak drastis pada log akses web (berubah dari ratusan menjadi belasan ribu bytes) bersamaan dengan perubahan status kode dari 404 ke 200, indikasi insiden apa yang terjadi?</summary>

**Jawaban:** Indikasi keberhasilan akses terhadap halaman tersembunyi. Lonjakan *byte* membuktikan bahwa server mengirimkan data antarmuka secara utuh ke penyerang.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan antara *Access Log* dan *Error Log*.
- [ ] Saya mampu menguraikan tujuh komponen format log *Apache/Nginx* (*Combined Log Format*).
- [ ] Saya memahami bahwa kolom *Request Line* adalah titik utama untuk mendeteksi vektor serangan.
- [ ] Saya mampu memanfaatkan *Status Code* dan *Response Size* untuk mendeteksi anomali.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Apache Log Files Documentation](https://httpd.apache.org/docs/2.4/logs.html) — Dokumentasi resmi mengenai format pencatatan server HTTP Apache.

---

## ➡️ Besok

**Day 2: Windows Event Logs** — Setelah menganalisis pemantauan pada aplikasi web, kita akan mengeksplorasi infrastruktur pemantauan pada lingkungan sistem operasi. Mayoritas organisasi menggunakan ekosistem Windows. Besok, kita akan mempelajari fungsionalitas **Windows Event Viewer** dan memahami kode unik (*Event IDs*) penting yang terkait dengan aktivitas autentikasi.

---

*📅 TISS Null Teaming · Week 21 · Day 1 · SENTINEL Rank*
