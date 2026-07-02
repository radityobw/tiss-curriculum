---
type: quiz
week: 21
day: 1
title: "Quiz: Apache/Nginx Log Format"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengurai anatomi catatan lalu lintas web korporat, apa perbedaan mendasar secara teknis antara <i>Access Logs</i> dengan <i>Error Logs</i> pada sebuah sistem *Apache*?
- [x] A. *Access Logs* (Catatan Akses) merekam dan mencatat semua riwayat permintaan (Request) yang masuk ke server web, tak peduli apakah responsnya berhasil (200 OK) atau gagal/diblokir (404/403). Sedangkan *Error Logs* (Catatan Galat) spesifik hanya menyoroti dan merekam masalah internal server, semisal *script* yang mogok bekerja atau kehabisan memori.
- [ ] B. *Error Logs* diperuntukkan bagi *Blue Team*, sementara *Access Logs* wajib untuk *Red Team*.
- [ ] C. *Access Logs* selalu mencetak riwayat alamat sandi (Password), sedangkan *Error Logs* mencetak nama pengguna.
- [ ] D. Tidak ada perbedaan, keduanya menggunakan arsitektur CVSS.

### Q2
**Type:** True/False
**Question:** Di pembedahan <i>Combined Log Format</i>, atribut <i>User-Agent</i> berfungsi memberikan informasi terkait identitas peramban (seperti *Mozilla/5.0*) atau perangkat eksekusi (seperti *SQLMap/1.4*) yang digunakan oleh klien untuk mengakses peladen.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat melakukan investigasi log web, atribut atau bagian log apakah (berawalan huruf R) yang merekam URL tautan situs eksternal (misal: "http://google.com") asal mula pengguna tersebut mengeklik situs kita?
**Answer:** Referer (atau HTTP Referer).

### Q4
**Type:** Short Answer
**Question:** Ketika penganalisis menganalisis catatan log dan mendapati nilai kode balasan *HTTP Status Code 404*, apa makna insiden atau kondisi yang ditandai oleh angka respons tersebut?
**Answer:** Not Found (Halaman/Direktori tidak ditemukan).

### Q5
**Type:** Short Answer
**Question:** Di ranah pengujian analisa *Web Access Log*, bila penganalisis mendapati ratusan baris log merekam *404 Not Found* berurutan, lantas satu baris log tiba-tiba berubah statusnya menjadi *200 OK* disertai dengan angka <i>Response Size</i> (Ukuran Balasan Bytes) yang melonjak sangat besar, indikasi jenis apakah itu?
**Answer:** True Positive (Indikasi peretas sukses menebak rute halaman rahasia dan berhasil memuat halamannya utuh beserta seluruh isinya).
