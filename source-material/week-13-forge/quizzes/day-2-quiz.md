---
type: quiz
week: 13
day: 2
title: "Quiz: SQL Basics (Bagian 2)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa yang akan terjadi jika kita mengeksekusi perintah SQL `UPDATE pengguna SET umur = 26;` tanpa menyertakan klausa kondisi `WHERE`?
- [x] A. Seluruh baris di dalam tabel `pengguna` akan termodifikasi sehingga nilai umurnya berubah menjadi `26` secara seragam.
- [ ] B. Pesan galat *error 404* akan ditampilkan dan server secara otomatis menolak operasi tersebut.
- [ ] C. Komputer peladen akan terkunci memorinya selama 26 menit sebagai hukuman eksekusi SQL yang salah.
- [ ] D. Tidak membahayakan data tabel secara dominan, karena perintah tersebut hanya akan memperbarui baris urutan pertama saja.

### Q2
**Type:** True/False
**Question:** Dalam *Relational Database*, sangat disarankan untuk menggabungkan seluruh jenis data (seperti pengguna, pesanan, dan produk) ke dalam satu tabel raksasa (*Denormalisasi*) agar pencarian memori menjadi jauh lebih cepat.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Apa sebutan teknis untuk kolom di sebuah tabel yang berfungsi sebagai penaut atau referensi ke ID utama (*Primary Key*) di tabel lain?
**Answer:** Foreign Key (Kunci Tamu / Kunci Asing).

### Q4
**Type:** Short Answer
**Question:** Perintah operasional SQL apakah yang dikerahkan untuk menggabungkan data dari dua tabel terpisah atau lebih berdasarkan kecocokan kolom penghubungnya?
**Answer:** JOIN (atau INNER JOIN / LEFT JOIN).

### Q5
**Type:** Short Answer
**Question:** Perintah SQL apa yang secara spesifik digunakan untuk menghapus baris data dari dalam sebuah tabel?
**Answer:** DELETE.
