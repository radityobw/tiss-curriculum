---
type: quiz
week: 22
day: 2
title: "Quiz: Splunk Basics"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Menganalisis pencarian di platform SIEM *Splunk*, bahasa kueri apakah yang harus dikuasai oleh Analis SOC untuk membedah data log secara teknis?
- [ ] A. SQL (Structured Query Language).
- [ ] B. Bash Script.
- [x] C. SPL (Search Processing Language).
- [ ] D. regex.

### Q2
**Type:** True/False
**Question:** Pada pengoperasian instruksi Splunk, penggunaan simbol *Piping* (`|`) difungsikan untuk menyambung instruksi dari kueri awal pencarian menuju ke tahap instruksi pengolahan data lanjutan (seperti `| table` atau `| stats`).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat menjalankan kueri pencarian data, perintah apa (berawalan huruf 't') di *Splunk* yang bertugas menyeleksi parameter teks log dan menampilkannya dalam format kolom terstruktur?
**Answer:** `table`.

### Q4
**Type:** Short Answer
**Question:** Ketika penganalisis mengeksekusi kueri agregasi `| stats count by src_ip` pada Splunk, keluaran informasi apa yang akan dihasilkan dari instruksi tersebut?
**Answer:** Splunk akan mencetak total jumlah frekuensi kejadian log (akumulasi kalkulasi) yang dikelompokkan secara spesifik per parameter *IP Asal (src_ip)*.

### Q5
**Type:** Short Answer
**Question:** Di ranah pengujian taksonomi penamaan data Splunk, apa istilah teknis (seperti nilai *src_ip, status, user*) yang diekstrak dan diidentifikasikan oleh Splunk dari barisan teks data mentah?
**Answer:** Fields (Nilai/Atribut Parameter).
