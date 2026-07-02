# 🛡️ Week 21 · Day 1: Apache/Nginx Log Format

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 21 · Day 1/5 | SENTINEL Rank (Minggu 2 dari 5) | Overall: 101/120 hari (84%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedah** anatomi baku (Log Format) dari catatan peladen web Apache dan Nginx.
2. **Membedakan** kegunaan antara *Access Logs* dan *Error Logs*.
3. **Mengekstrak** informasi krusial (IP, Timestamp, Method, URL, Status Code) secara manual.

---

## 📖 Materi Inti

### Dua Wajah Server Web: Access vs Error

Mayoritas situs web dalam infrastruktur modern ditenagai oleh perangkat lunak peladen web *Apache* atau *Nginx*. Sebagai yang beroperasi terus-menerus, perangkat ini mendokumentasikan setiap interaksi jaringan ke dalam dua kategori log utama:

1. **Access Logs (Catatan Akses):** Berfungsi sebagai catatan lalu lintas utama. Log ini mendokumentasikan *semua* permintaan (*Request*) jaringan yang masuk ke peladen, terlepas dari apakah permintaan tersebut berhasil dimuat (Status 200 OK) atau ditolak oleh sistem (Status 403 Forbidden).
2. **Error Logs (Catatan Galat):** Berfungsi sebagai catatan diagnostik. Log ini secara spesifik mendokumentasikan masalah internal pada tingkat peladen, seperti kesalahan fatal pada eksekusi *PHP*, kehabisan memori, atau kegagalan modul skrip *Backend*.

Bagi Analis SOC, **Access Logs** adalah sumber data utama (primer) untuk memantau indikasi anomali dan mendeteksi vektor eksploitasi, seperti upaya injeksi (SQLi) atau ekskusi skrip lintas situs (XSS).

### Anatomi Baku: Combined Log Format

Apache dan Nginx umumnya mengadopsi standar pemformatan log yang seragam, yang dikenal sebagai *Combined Log Format*. Mari kita bedah struktur sebaris log ini:

`192.168.1.50 - - [21/Oct/2026:14:05:32 +0700] "GET /login.php HTTP/1.1" 200 4523 "http://google.com" "Mozilla/5.0 (Windows NT 10.0)"`

Baris log tersebut dapat dipisahkan menjadi 7 komponen log (Log Fields) fundamental:
1. **`192.168.1.50` (IP Address):** Alamat IP klien yang menginisiasi permintaan ke peladen.
2. **`- -` (Identitas & Pengguna):** Kolom ini biasanya kosong (berisi tanda hubung) kecuali peladen mewajibkan metode autentikasi klasik (seperti *HTTP Basic Auth*).
3. **`[21/Oct... +0700]` (Timestamp):** Cap waktu (waktu dan tanggal) kejadian beserta informasi zona waktu peladen.
4. **`"GET /login.php HTTP/1.1"` (Request Line):** Terdiri dari Metode HTTP (`GET`), alamat URL/rute yang diminta (`/login.php`), dan versi protokol yang digunakan. Kolom ini krusial karena muatan bahaya (Payload) serangan sering kali tercatat di sini.
5. **`200` (Status Code):** Kode status respon peladen. (200 = Permintaan Sukses, 302 = Pengalihan URL, 404 = Halaman Tidak Ditemukan, 401/403 = Akses Dilarang/Tidak Sah, 500 = Kesalahan Internal Peladen).
6. **`4523` (Response Size):** Ukuran total paket balasan (dalam satuan Bytes). Lonjakan ukuran respons yang tidak wajar pada titik akhir/halaman rahasia merupakan indikator kuat adanya eksfiltrasi data.
7. **`"http://google.com"` (Referer) & `"Mozilla..."` (User-Agent):** Header *Referer* merekam alamat tautan web asal pengunjung sebelum masuk ke situs. Sedangkan *User-Agent* membeberkan informasi perangkat, versi sistem operasi, dan klien peramban web yang digunakan (Penting: alat eksploitasi otomatis seperti Nmap atau SQLMap memiliki sidik jari *User-Agent* khusus).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melakukan analisis logika pemisahan data (Triage) pada catatan akses peladen web!

1. Periksa ketiga baris *Access Log* berikut secara komprehensif:
 - `Baris 1: 10.0.0.99 - - [01/Nov/2026:01:10:05 +0700] "GET /admin HTTP/1.1" 404 210 "-" "Mozilla/5.0"`
 - `Baris 2: 10.0.0.99 - - [01/Nov/2026:01:10:06 +0700] "GET /administrator HTTP/1.1" 404 210 "-" "Mozilla/5.0"`
 - `Baris 3: 10.0.0.99 - - [01/Nov/2026:01:10:07 +0700] "GET /admin/dashboard HTTP/1.1" 200 15400 "-" "Mozilla/5.0"`
2. **Evaluasi Tahap 1:** Identifikasi pola anomali pada aktivitas baris 1 dan 2. 
 - *Analisis:* Tercatat aktivitas klien eksternal yang mengeksplorasi (menebak) rute dasbor administratif secara berurutan dalam hitungan detik. Keduanya memicu kegagalan (Status 404). Ini mengindikasikan aktivitas pemindaian paksa direktori (*Directory Bruteforce/Enumeration*).
3. **Evaluasi Tahap 2:** Identifikasi signifikansi risiko pada baris 3.
 - *Analisis:* Pada permintaan ke-3, status respon bertransisi menjadi `200 OK` (Tebakan rute berhasil). Selain itu, ukuran balasan data (*Response Size*) mengalami eskalasi drastis menjadi `15400` bytes. Kesimpulan: Peretas telah menemukan direktori dasbor yang valid dan peladen memuat antarmuka administratif tersebut secara utuh (*True Positive*).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Menguraikan anatomi pencatatan peladen web, apa perbedaan mendasar mengenai cakupan antara log <i>Access Logs</i> dan <i>Error Logs</i> pada peladen Apache/Nginx?</summary>

**Jawaban:** *Access Logs* berfungsi mencatat dan mendokumentasikan setiap riwayat koneksi lalu lintas masuk (Requests) secara komprehensif, terlepas dari keberhasilan permintaan tersebut. Sedangkan *Error Logs* difungsikan secara spesifik hanya untuk mencatat dan membeberkan masalah teknis tingkat internal peladen, seperti kesalahan, gangguan modul, atau kegagalan operasional *Backend*.
</details>

<details>
<summary>❓ Saat melakukan investigasi log web yang dikonfigurasi menggunakan standar <i>Combined Log Format</i>, atribut log (Log Field) apakah yang menyediakan informasi rute alamat URL situs eksternal asal di mana pengguna melakukan klik?</summary>

**Jawaban:** Referer (atau HTTP Referer).
</details>

<details>
<summary>❓ Apabila penganalisis menelaah sebaris log dan mengidentifikasi nilai indikator <i>Response Size</i> (Ukuran Balasan Bytes) yang mengalami eskalasi atau pembengkakan besar (dibandingkan permintaan yang memicu respons kegagalan sebelumnya), indikasi insiden apa yang bisa ditarik?</summary>

**Jawaban:** Indikasi keberhasilan penetrasi sistem (*True Positive*). Lonjakan ukuran byte (response size) menjadi bukti teknis bahwa peladen memuat penuh dan mengirimkan struktur data halaman rahasia (seperti antarmuka admin) secara utuh kepada peretas.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami diferensiasi antara *Access Log* dan *Error Log*.
- [ ] Saya mampu menguraikan ketujuh atribut format log baku *Apache/Nginx* (Combined Log Format).
- [ ] Saya mengetahui parameter *Request Line* sebagai titik utama untuk mendeteksi vektor *Payload* serangan.
- [ ] Saya mampu menggunakan parameter *Status Code* (200 vs 404) untuk menarik analisis konklusi insiden.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Apache Log Files Documentation](https://httpd.apache.org/docs/2.4/logs.html) — Dokumentasi teknis primer mengenai arsitektur format pencatatan peladen HTTP Apache.

---

## ➡️ Besok

**Day 2: Windows Event Logs** — Setelah menganalisis pemantauan pada aplikasi web, kita akan mengeksplorasi infrastruktur pemantauan pada lingkungan *Endpoint* dan *Server OS*. Mayoritas operasional internal perusahaan berpusat pada ekosistem Windows. Besok, kita akan mempelajari fungsionalitas dan logika klasifikasi dari **Windows Event Viewer**, serta melakukan identifikasi spesifik pada sandi identifikasi unik (Event IDs) krusial terkait proses otentikasi.

---

*📅 TISS Null Teaming · Week 21 · Day 1 · SENTINEL Rank*
