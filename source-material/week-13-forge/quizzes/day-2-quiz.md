---
type: quiz
week: 13
day: 2
title: "Quiz: SQL Basics (Bagian 2)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Konsekuensi kerusakan fatalitas apakah yang niscaya membentur operasi struktur penahanan basis data bilamana arsitek pengelola basis data meluncurkan operasional eksekusi kueri instruksi modifikasi *SQL* pembaruan payload `UPDATE pengguna SET umur = 26;` tanpa mengikutsertakan penyisipan klausa pembatas jaring saringan kondisi sintaksis `WHERE`?
- [x] A. Terjadi kerusakan integritas data fatal secara masif; sistem akan menimpa modifikasi nilai parameter kolom payload usia di SELURUH rekaman entitas baris tabel pada tabel `pengguna` sehingga usianya termodifikasi berganti wujud serentak dipaksakan seragam berubah menjadi angka `26` secara merata dan tanpa terkecuali.
- [ ] B. Pesan peringatan pemblokiran eksekusi logik bernomor indeks 404 bakal dihidangkan menahan paksa instruksi interupsi parameter penempatan kueri administrator peladen *system*.
- [ ] C. Komputer peladen otomatis menetralisir fungsionalitas pengiriman energi catu daya ke lingkungan instalasi kelistrikan sistem disk basis data peramban secara statis mengunci memorinya selama interval tenggang operasional 26 menit penangguhan sistem basis operasional log.
- [ ] D. Tidak membahayakan payload struktural tabel secara dominan, dikarenakan arsitektur pembaruan instruksi tersebut tanpa argumen tambahan lantas mutlak sekadar merevisi fungsionalitas rentang data pengurutan baris referensi paling hulu spesifikasi rekaman (urutan tunggal posisi parameter *record array* 0) belaka.

### Q2
**Type:** True/False
**Question:** Praktik penataan tabel referensi pada basis data bertipe struktur rasional relasional (*Relational Database*) idealnya dituntut mengamalkan kerangka fusi peleburan komponen tabel arsitektur *Denormalisasi* di mana penggabungan pemampatan parameter relasi rincian seluruh payload rekaman disatukan memfosil menumpuk menempati kerangka tabel induk hulu tunggal saja demi kecepatan referensi pencariannya di RAM.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Terminologi nomenklatur teknikal arsitektur RDBMS apakah yang lazim diwacanakan mewakili peran relasional sebuah lajur payload referensial sandi identitas tamu (kolom penunjuk identitas referensi) ketika fungsinya disematkan menjabat bertugas selaku penaut (pengait parameter id pelengkap silang) pada atribut entitas operasional tabel penempatan tabel pengingat berbeda?
**Answer:** Foreign Key (Kunci Tamu / Kunci Asing).

### Q4
**Type:** Short Answer
**Question:** Sintaks operasional penggabungan kerangka logik pengingat *SQL* apakah yang dikerahkan untuk menggabungkan irisan rentetan serpihan komponen rekaman rincian referensi log tabel-tabel eksternal berbeda persimpangan (terpisah dari lebih 1), disatukan menyelaraskan pemetaan kunci penghubungnya (*keys*) ke format tabel satu hasil kueri rangkuman utuh?
**Answer:** JOIN (atau INNER JOIN / LEFT JOIN).

### Q5
**Type:** Short Answer
**Question:** Komando eksekusi instruksional operasional modifikasi parameter perombakan sandi apa pada baris perintah basis struktur log SQL yang dilibatkan bertugas spesifik mencabut penempatan unit entitas sebaris maupun sekelompok rincian rekaman payload modul fungsi referensi direktori rekaman memori dari kumpulan parameter tabel Database secara mutlak eksistensinya?
**Answer:** DELETE.
