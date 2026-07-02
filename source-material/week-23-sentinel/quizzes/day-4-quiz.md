---
type: quiz
week: 23
day: 4
title: "Quiz: Memory & Disk Forensics"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Saat mengeksekusi arsitektur penanganan perolehan data dalam insiden forensik korporat, bagaimana penetapan prioritas akuisisi antara *Disk Forensics* dan *Memory Forensics*?
- [x] A. Penanganan *Memory Forensics* memegang prioritas utama untuk diakuisisi (diekstrak), sebab sifat ketersediaan data di alokasi sistem RAM bersifat *Volatile* (mudah hilang). Jika operasi perangkat tak terduga mati daya, ter-restart, ataupun diputus alur pasokan tenaga listriknya, *Volatile* lenyap seketika. Berbanding terbalik dengan itu, klasifikasi *Disk Forensics* diproyeksikan pada penyimpanan tetap berjenis fisik (SSD/Hard Disk) sehingga eksistensi data aman sekalipun siklus daya perangkat dinonaktifkan.
- [ ] B. *Disk Forensics* dioperasikan khusus instalasi platform *Linux*, sementara *Memory Forensics* dipusatkan pada lingkungan sistem *Windows*.
- [ ] C. *Disk Forensics* menganalisis parameter log melalui antarmuka fungsi sistem perangkat lunak *Splunk*, sementara *Memory Forensics* menelusuri penugasan lalu lintas jaringan menggunakan *Wireshark*.
- [ ] D. Tidak ada parameter rasional perbedaan tingkatan eksekusi mitigasi data antara keduanya, dikarenakan dua sistem tersebut mengadopsi struktur integrasi standar perlindungan algoritma kriptografi yang sama.

### Q2
**Type:** True/False
**Question:** Dalam kerangka kerja arsitektur sistem pengontrolan tanggap krisis (*Incident Response*), seandainya sistem peladen utama korporasi sedang ditaklukkan proses *Ransomware*, prosedur instruksi pemutusan aliran suplai listrik *(Shutdown)* tidak disarankan. Alasan instruksional tersebut berlandaskan hipotesis perihal kemungkinan kunci sandi kriptografi pembuka ancaman (*Decryption Key*) sedang dimuat atau ditampung di arsitektur komponen sistem *RAM* tersebut.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Mengingat parameter kepatuhan akuisisi perolehan alat bukti sistem peladen membedakan retensi jangka panjang (*Non-Volatile*), parameter kata apa yang digunakan pada struktur kepatuhan perolehan komponen (Seperti RAM) untuk mengklasifikasikan karakter spesifik dari arsip penyimpanan sistem yang terhapus musnah seketika bila interupsi daya terjadi?
**Answer:** Volatile (Atau Volatility).

### Q4
**Type:** Short Answer
**Question:** Saat penganalisis forensik membedah arsitektur duplikasi *RAM (Memory Dump)*, piranti antarmuka penganalisis *Command-line Interface (CLI)* berbasis bahasa Python manakah yang sering dimanfaatkan untuk memproses rutinitas tersebut?
**Answer:** Volatility Framework (Atau cukup Volatility).

### Q5
**Type:** Short Answer
**Question:** Di wilayah operasi pengkajian arsitektur infrastruktur *Disk Forensics* sistem, andaikata pelaku intervensi serangan secara manual eksekusi sistem OS untuk memusnahkan (*Shift+Delete*) suatu daftar data rahasia, apakah wujud operasi direktori parameter bit data tersebut lenyap absolut dari *Hard Disk* sistem OS tersebut? (Jawab dengan Ya atau Tidak).
**Answer:** Tidak. (Sistem penyimpanan sebatas menghilangkan log tautan file sistem operasi dari tabel indeks OS. Struktur arsitektur blok data asli masih mampu diambil ulang *(Recovery)* selama alokasi memori klaster *Disk* tersebut belum di-overwrite aktivitas tulis file lain).
