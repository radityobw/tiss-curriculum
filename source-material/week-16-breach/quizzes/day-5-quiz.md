---
type: quiz
week: 16
day: 5
title: "Quiz: Lab PortSwigger SQLi"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam mengeksploitasi celah *UNION-based SQL Injection*, urutan alur metodologi manakah yang paling akurat untuk membongkar basis data peladen web?
- [ ] A. Mengeksekusi SQLMap dengan flag `--dbs`, kemudian langsung menggunakan alat pendeteksi Wappalyzer.
- [x] B. Menentukan jumlah kolom menggunakan *ORDER BY* (dinaikkan secara bertahap 1, 2, 3), lalu mengidentifikasi kolom dengan tipe data teks/string menggunakan injeksi `NULL, 'a'`, dan terakhir mengekstrak isi tabel menggunakan payload `UNION SELECT username, password`.
- [ ] C. Mengeksekusi celah waktu dengan *SLEEP(10)* demi mengekstrak pemetaan kolom *Boolean-based Blind SQLi*.
- [ ] D. Melakukan pemindaian direktori menggunakan *Gobuster* untuk menemukan parameter *UNION*, lalu membuang tabel menggunakan flag `--dump`.

### Q2
**Type:** True/False
**Question:** Saat mengeksekusi injeksi SQL secara manual, penempatan sepasang simbol sakti `--` (atau `#` pada MySQL) di bagian akhir payload mutlak diperlukan. Fungsinya adalah untuk menjadi operator komentar (*Comment Out*) yang akan membatalkan pembacaan sisa kueri orisinal backend, guna mencegah terjadinya *Syntax Error*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada iterasi menebak jumlah kolom tabel database sasaran, perintah SQL apakah yang umumnya dinaikkan angkanya secara perlahan (misal dari 1, 2, hingga 3) di bagian ekor kueri?
**Answer:** ORDER BY.

### Q4
**Type:** Short Answer
**Question:** Jika aplikasi web mengembalikan respon yang sepenuhnya bisu, di mana tidak ada pesan *Error* yang muncul dan tidak ada perubahan tampilan sedikit pun pada layar terlepas dari injeksi yang diberikan, kategori teknik penetrasi apakah yang sejatinya harus dipraktikkan untuk membongkar peladen tersebut (dengan menggunakan teknik *Time-based* delay)?
**Answer:** Blind SQL Injection (atau variannya *Time-based Blind SQLi*).

### Q5
**Type:** Short Answer
**Question:** Manuskrip teknis yang menguraikan rekam jejak penyelesaian masalah (termasuk *payload* yang dipakai) dari mesin eksploitasi seperti PortSwigger langkah-demi-langkah, yang lazim diunggah oleh pentester profesional sebagai dokumentasi pembuktian kerentanan (Proof of Concept / PoC), disebut sebagai?
**Answer:** Writeup.
