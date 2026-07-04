---
type: quiz
week: 21
day: 1
title: "Quiz: Apache/Nginx Log Format"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan teknis mendasar antara *Access Logs* dengan *Error Logs* pada sebuah *web server* Apache?
- [x] A. *Access Logs* mencatat semua permintaan (*Request*) yang masuk, baik berhasil (200 OK) maupun gagal/ditolak (404/403). Sedangkan *Error Logs* hanya mencatat masalah internal server, seperti eksekusi *script* yang gagal atau kehabisan memori.
- [ ] B. *Error Logs* diperuntukkan bagi *Blue Team*, sementara *Access Logs* wajib untuk *Red Team*.
- [ ] C. *Access Logs* selalu mencatat *password* pengguna, sedangkan *Error Logs* mencatat nama pengguna.
- [ ] D. Tidak ada perbedaan, keduanya menggunakan format CVSS.

### Q2
**Type:** True/False
**Question:** Pada format *Combined Log Format*, atribut *User-Agent* berfungsi mencatat informasi terkait perangkat, sistem operasi, atau aplikasi klien (seperti *Mozilla/5.0* atau *SQLMap/1.4*) yang digunakan untuk mengakses *server*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat melakukan investigasi log web, atribut apa yang mencatat URL situs asal (misal: "http://google.com") dari mana pengguna tersebut mengeklik tautan menuju situs kita?
**Answer:** Referer (atau HTTP Referer).

### Q4
**Type:** Short Answer
**Question:** Ketika seorang analis membaca catatan log dan menemukan kode respons *HTTP Status Code 404*, apa makna dari kode tersebut?
**Answer:** Not Found (Halaman/Direktori tidak ditemukan).

### Q5
**Type:** Short Answer
**Question:** Jika Analis mendapati ratusan baris log web berstatus *404 Not Found* secara berurutan, lalu tiba-tiba ada satu baris dengan status *200 OK* disertai lonjakan drastis pada *Response Size* (ukuran balasan data), indikasi apa ini?
**Answer:** True Positive (Indikasi penyerang sukses menemukan halaman tersembunyi dan *server* berhasil memuat halaman tersebut beserta seluruh isinya).
