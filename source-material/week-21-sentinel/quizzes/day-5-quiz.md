---
type: quiz
week: 21
day: 5
title: "Quiz: Lab Identifikasi Serangan"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam investigasi log menggunakan terminal Linux, mengapa teknik *Piping* (penggunaan simbol `|`) sangat diandalkan?
- [x] A. Karena *Piping* memungkinkan Analis untuk meneruskan *output* data dari satu perintah (misal `awk`) sebagai *input* langsung ke perintah berikutnya (misal `sort | uniq | grep`), sehingga dapat memproses aliran data besar secara efisien tanpa harus menyimpan *file* sementara.
- [ ] B. Karena *Piping* mengonversi teks log Linux menjadi format `.evtx` Windows.
- [ ] C. Fungsi *Piping* bertugas untuk mematikan perlindungan *Firewall* Linux (iptables).
- [ ] D. *Piping* adalah fitur pencarian grafis khusus pada perangkat *Burp Suite*.

### Q2
**Type:** True/False
**Question:** Saat mengekstrak alamat IP penyerang dominan (*Top Talkers*) di terminal Linux, Analis SOC menggabungkan perintah `awk` untuk mengambil kolom IP, lalu meneruskannya ke perintah `uniq -c` untuk menghitung jumlah kemunculan alamat IP tersebut.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Setelah menghitung jumlah log dengan `uniq -c`, perintah Linux apa yang biasanya ditambahkan di akhir teknik *Piping* untuk mengurutkan data dari jumlah frekuensi terbesar ke yang terkecil?
**Answer:** `sort -nr`.

### Q4
**Type:** Short Answer
**Question:** Jika seorang Analis mengeksekusi komando Linux dan menambahkan argumen `head -n 5` di akhir rantai *Piping*, apa fungsi spesifik dari instruksi tersebut?
**Answer:** Hanya menampilkan/mencetak 5 baris pertama (atau 5 hasil teratas) dari output teks tersebut.

### Q5
**Type:** Short Answer
**Question:** Dalam proses analisis insiden, jika Analis telah memisahkan log penyerang ke dalam *file* `hacker_log.txt` lalu menjalankan perintah `grep " 200 " hacker_log.txt`, apa indikasi keamanan yang sedang ia cari?
**Answer:** Indikasi serangan yang *Berhasil* (mencari log dengan *HTTP status code 200 OK*, yang berarti penyerang sukses mengakses halaman atau masuk ke sistem).
