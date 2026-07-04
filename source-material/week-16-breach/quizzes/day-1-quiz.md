---
type: quiz
week: 16
day: 1
title: "Quiz: SQL Injection UNION-based"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa syarat mutlak yang wajib dipenuhi saat menggunakan teknik *SQL Injection UNION-based* agar tidak menghasilkan *Syntax Error*?
- [ ] A. Tabel sisipan hanya bisa dieksekusi menggunakan *POST Request*.
- [x] B. Jumlah kolom pada kueri `UNION SELECT` yang disisipkan oleh penyerang harus **sama persis** dengan jumlah kolom pada kueri *SELECT* aslinya.
- [ ] C. *Payload* penyerang tidak boleh menggunakan perintah `ORDER BY`.
- [ ] D. Semua kolom yang digabungkan harus bertipe data *Integer* (angka).

### Q2
**Type:** True/False
**Question:** Ketika penyerang mencoba menebak jumlah kolom dengan kueri `ORDER BY 1`, `ORDER BY 2`, lalu pada `ORDER BY 3` mendadak muncul pesan *error* dari *database*, maka bisa disimpulkan secara pasti bahwa tabel aslinya memiliki persis 2 kolom.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Perintah SQL apa yang secara khusus digunakan untuk menggabungkan (*append*) hasil dari dua perintah `SELECT` yang berbeda ke dalam satu hasil tampilan tabel (*Result Set*)?
**Answer:** UNION (atau UNION SELECT)

### Q4
**Type:** Short Answer
**Question:** Saat mencoba menebak jumlah kolom tabel (*Column Enumeration*), selain menggunakan `ORDER BY`, nilai/karakter kosong apa yang sering digunakan penyerang untuk menyeimbangkan jumlah kolom (contoh: `UNION SELECT _,_--`)?
**Answer:** NULL (contoh: `UNION SELECT NULL, NULL--`)

### Q5
**Type:** Short Answer
**Question:** Pada sebuah injeksi seperti `' UNION SELECT username FROM users--`, apa fungsi utama dari karakter sepasang setrip `--` di akhir kueri tersebut?
**Answer:** Sebagai penanda komentar (*Comment Out*) untuk membatalkan eksekusi sisa kueri SQL asli di belakangnya, sehingga mencegah terjadinya *Syntax Error*.
