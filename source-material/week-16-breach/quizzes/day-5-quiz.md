---
type: quiz
week: 16
day: 5
title: "Quiz: Lab PortSwigger SQLi"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam mengeksploitasi celah *UNION-based SQL Injection*, urutan alur mana yang paling tepat untuk mengekstrak data dari *database* target?
- [ ] A. Mengeksekusi SQLMap dengan flag `--dbs`, kemudian langsung menggunakan alat pendeteksi Wappalyzer.
- [x] B. Menentukan jumlah kolom menggunakan *ORDER BY* (dinaikkan secara bertahap 1, 2, 3), lalu mengidentifikasi kolom dengan tipe data teks/string menggunakan injeksi `NULL, 'a'`, dan terakhir mengekstrak isi tabel menggunakan payload `UNION SELECT username, password`.
- [ ] C. Menggunakan *SLEEP(10)* untuk mengekstrak pemetaan kolom *Boolean-based Blind SQLi*.
- [ ] D. Melakukan pemindaian direktori menggunakan *Gobuster* untuk menemukan parameter *UNION*, lalu membuang tabel menggunakan flag `--dump`.

### Q2
**Type:** True/False
**Question:** Saat mengeksekusi injeksi SQL secara manual, penempatan sepasang karakter `--` (atau `#` pada MySQL) di bagian akhir *payload* berfungsi sebagai komentar (*Comment Out*). Fungsinya adalah untuk membatalkan sisa kueri SQL asli di *backend* guna mencegah terjadinya *Syntax Error*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada iterasi menebak jumlah kolom tabel sasaran, perintah SQL apakah yang umumnya dinaikkan angkanya secara perlahan (misal dari 1, 2, hingga 3) di bagian ekor kueri?
**Answer:** ORDER BY

### Q4
**Type:** Short Answer
**Question:** Jika aplikasi web tidak menampilkan pesan *error* dan tidak ada perubahan tampilan sedikit pun pada layar terlepas dari injeksi yang diberikan, teknik SQLi apa yang harus digunakan untuk mengekstrak data (misalnya dengan menggunakan *delay* waktu respons)?
**Answer:** Blind SQL Injection (atau Time-based Blind SQLi)

### Q5
**Type:** Short Answer
**Question:** Dokumen laporan yang berisi langkah demi langkah penyelesaian lab atau peretasan target (termasuk *payload* yang dipakai), yang sering diunggah oleh *Pentester* sebagai *Proof of Concept* (PoC), biasa disebut apa di industri keamanan?
**Answer:** Writeup
