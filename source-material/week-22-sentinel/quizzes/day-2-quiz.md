---
type: quiz
week: 22
day: 2
title: "Quiz: Splunk Basics"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Bahasa kueri apa yang secara spesifik harus digunakan oleh Analis SOC untuk melakukan pencarian dan analisis data log di platform SIEM Splunk?
- [ ] A. SQL (Structured Query Language).
- [ ] B. Bash Script.
- [x] C. SPL (Search Processing Language).
- [ ] D. regex.

### Q2
**Type:** True/False
**Question:** Sama seperti pada terminal Linux, dalam penulisan kueri Splunk, simbol *Piping* (`|`) berfungsi untuk meneruskan *output* dari satu perintah agar dapat diolah oleh instruksi selanjutnya (seperti meneruskan hasil pencarian ke perintah `| table` atau `| stats`).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada kueri Splunk, perintah apa yang digunakan untuk merapikan hasil pencarian log mentah (*raw log*) menjadi tampilan berformat tabel rapi yang hanya memuat parameter tertentu?
**Answer:** `table`.

### Q4
**Type:** Short Answer
**Question:** Jika seorang Analis mengeksekusi kueri `| stats count by src_ip` pada Splunk, informasi analisis statistik seperti apa yang akan dihasilkan?
**Answer:** Splunk akan menghitung dan menampilkan total jumlah kejadian log berdasarkan masing-masing alamat IP penyerang (`src_ip`).

### Q5
**Type:** Short Answer
**Question:** Dalam terminologi Splunk, apa sebutan untuk parameter/variabel spesifik (seperti `src_ip`, `status`, atau `user`) yang secara dinamis diekstrak dari teks log mentah agar lebih mudah dicari?
**Answer:** Fields.
