---
type: quiz
week: 16
day: 3
title: "Quiz: SQLMap Automated Exploitation"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Pada penggunaan alat *SQLMap*, *flag* (argumen parameter) manakah yang digunakan untuk mengekstrak dan menampilkan daftar nama seluruh *Database* yang ada di server target?
- [x] A. `--dbs`
- [ ] B. `--dump`
- [ ] C. `-sV`
- [ ] D. `--tables`

### Q2
**Type:** True/False
**Question:** *Flag* `--dump` pada perintah *SQLMap* berfungsi untuk menguras/menyedot keseluruhan isi data (baris dan kolom) dari tabel database target dan menampilkannya ke layar terminal penyerang.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Apa nama alat otomatisasi *open-source* berbasis Python yang dirancang khusus untuk mendeteksi dan mengeksploitasi kerentanan *SQL Injection* secara otomatis?
**Answer:** SQLMap

### Q4
**Type:** Short Answer
**Question:** Setelah berhasil menemukan nama *database* menggunakan flag `--dbs`, *flag* lanjutan apa yang harus ditambahkan pada perintah SQLMap untuk melihat daftar tabel di dalam *database* tersebut?
**Answer:** --tables

### Q5
**Type:** Short Answer
**Question:** Jika kerentanan *SQL Injection* berada pada *POST Request* (misalnya formulir *Login*), kita harus menyimpan HTTP Request tersebut ke dalam sebuah file teks. *Flag* huruf apa (contoh penggunaannya: `sqlmap -? file.txt`) yang digunakan SQLMap untuk membaca file HTTP Request tersebut?
**Answer:** -r (contoh: `sqlmap -r request.txt`)
