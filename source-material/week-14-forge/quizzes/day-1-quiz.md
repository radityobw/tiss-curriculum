---
type: quiz
week: 14
day: 1
title: "Quiz: OWASP Top 10 Intro & Injection"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Bagaimana logika di balik serangan SQL Injection menggunakan *payload* `' OR '1'='1`?
- [ ] A. Perintah tersebut mereset *database* ke pengaturan pabrik.
- [ ] B. Perintah ini meretas lapisan HTTP dan mengubahnya menjadi protokol TCP.
- [x] C. Kondisi `'1'='1'` selalu bernilai benar (TRUE). Akibatnya, *database* mengabaikan syarat pengecekan lain dan langsung memberikan akses atau mengembalikan data.
- [ ] D. Skrip tersebut adalah *backdoor* bawaan dari SQLite untuk pengujian.

### Q2
**Type:** True/False
**Question:** Menggabungkan input dari pengguna secara langsung ke dalam *string query SQL* (misalnya menggunakan operator `+`) sangat dilarang karena dapat memicu kerentanan SQL Injection.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Apa kepanjangan dari organisasi standar keamanan siber global yang merilis daftar 10 kerentanan aplikasi web paling mematikan?
**Answer:** OWASP (Open Worldwide Application Security Project)

### Q4
**Type:** Short Answer
**Question:** Teknik perlindungan apa yang menggunakan tanda tanya (`?`) sebagai tempat penampung (*placeholder*) variabel untuk menetralkan serangan SQL Injection?
**Answer:** Parameterized Queries

### Q5
**Type:** Short Answer
**Question:** Saat melakukan injeksi SQL pada MySQL atau SQLite, peretas sering menyisipkan simbol `--` di akhir *payload*. Apa fungsi dari simbol tersebut?
**Answer:** Komentar (sehingga sisa perintah di belakangnya akan diabaikan oleh mesin *database*)
