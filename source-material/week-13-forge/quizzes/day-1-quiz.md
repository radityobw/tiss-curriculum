---
type: quiz
week: 13
day: 1
title: "Quiz: SQL Basics (Bagian 1)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Menakar betapa rentannya penyimpanan data menggunakan struktur *array In-Memory JavaScript* saat menampung payload profil layanan, alasan logis apakah yang mengharuskan adopsi ekosistem basis data seperti *Database Relasional (RDBMS)* untuk kelangsungan sistem peladen *Backend* yang tangguh?
- [x] A. Penyimpanan *In-Memory* bersifat *volatile* (sementara), di mana seluruh data akan sirna seketika saat peladen *Node.js* di-restart atau mengalami *crash*. Sebaliknya, *SQL RDBMS* memastikan rekaman data dikomitmenkan berwujud file secara permanen (*persistent*) menancap ke ranah memori perangkat *disk storage* pada sistem operasi peladen.
- [ ] B. Karena struktur relasi *Database* secara bawaan sanggup mengecilkan lonjakan antrean pengiriman volume laju panggilan payload API klien hingga menyusut sepertiganya.
- [ ] C. RDBMS adalah parameter ekstensi krusial yang mewajibkan fitur kompatibilitas *CSS* berjalan murni di peladen internal Google Chrome.
- [ ] D. Node.js otomatis memblokir eksekutor penugasannya sekiranya sistem referensi *file HTML* urung diformulasikan merajut ke struktur kolom *database* kustom.

### Q2
**Type:** True/False
**Question:** Demi memicu eksekusi perintah kueri modifikasi yang bertugas spesifik merombak, merevisi, atau memperbarui isi baris di lingkungan *Database SQL*, peramban sistem manajemen operasi basis data memfardhukan eksekutor admin peladen untuk senantiasa mendahulukan awalan pemicu sintaks `SELECT`.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Apakah simbol spesifikasi karakter pengikatan tunggal (yang senantiasa disematkan merujuk fungsi parameternya selepas penempatan instruksi pemanggilan referensial `SELECT`) guna menerbitkan eksekutor perintah mencetak ekstraksi menyedot SELURUH alokasi kolom secara komprehensif pada kueri basis data tanpa terkecuali?
**Answer:** Bintang (Karakter Asterisk `*`).

### Q4
**Type:** Short Answer
**Question:** Pada tata pedoman struktur kerangka penulisan gramatika *SQL*, sintaks instruksional kondisional apakah yang dikondisikan berperan selaku sarana penjaring penentu pengecualian atau *filter* (semisal menginstruksikan logik penarikan spesifik : "Hanya seleksi dan kembalikan referensi baris payload di mana nilainya memuat parameter *umur > 20*")?
**Answer:** WHERE.

### Q5
**Type:** Short Answer
**Question:** Ketika pengelola administrator meluncurkan sirkuit inisialisasi perintah penciptaan cetakan kerangka arsitektur spesifikasi tabel baru ke dalam memori *database SQL* (serta memilah susunan penyesuaian panjang rincian tipe data batas kolom abjad maupun numerik), kombinasi sepasang frasa logik dua patah kata pembuka sintaks absolut apakah yang mutlak mengawali operasi konstruksi penciptaannya?
**Answer:** CREATE TABLE.
