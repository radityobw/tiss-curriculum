---
type: quiz
week: 20
day: 3
title: "Quiz: Log Sources & Syslog"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam arsitektur pemantauan keamanan, mengapa arsip log (*Logs*) dianggap sangat krusial bagi operasional *Blue Team*?
- [x] A. Tanpa arsip *Logs*, tim keamanan siber tidak memiliki visibilitas atas apa yang terjadi di dalam jaringan. Log menyajikan bukti historis yang berisi metadata (siapa, apa, kapan, dan di mana sebuah aktivitas terjadi), menjadikannya instrumen utama untuk mendeteksi ancaman dan melakukan investigasi forensik.
- [ ] B. Karena *Logs* secara otomatis berfungsi menghapus ancaman *Ransomware*.
- [ ] C. *Logs* hanya diwajibkan semata-mata untuk mencegah serangan *CVSS 9.8*.
- [ ] D. *Logs* berguna untuk meretas celah keamanan *IDOR* bagi *Red Team*.

### Q2
**Type:** True/False
**Question:** Jika seorang Analis keamanan ingin menelusuri alamat IP penyerang yang terus-menerus mencoba menyuntikkan *payload SQL Injection* pada parameter URL situs web perusahaan, maka jenis sumber log (*Log Source*) yang paling tepat untuk dianalisis adalah *Operating System (OS) Logs*.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Dalam sentralisasi pengumpulan log keamanan, apa nama protokol standar (yang umumnya menggunakan port UDP 514) yang digunakan untuk mengirim pesan catatan log dari berbagai perangkat (*clients*) ke satu server pengumpul pusat (*SIEM/Log Server*)?
**Answer:** Syslog.

### Q4
**Type:** Short Answer
**Question:** Saat melakukan investigasi pada *Access Log* (*Apache/Nginx*) dan menemukan baris log dengan informasi identitas peramban seperti `Mozilla/5.0...` atau indikasi alat otomatis seperti `sqlmap/1.4`, sebutan parameter atribut HTTP apakah yang memuat informasi identitas perangkat tamu ini?
**Answer:** User-Agent.

### Q5
**Type:** Short Answer
**Question:** Saat menganalisis lalu lintas akses log dari *web server*, jika analis menemukan pengunjung mengakses halaman tanpa halangan dan sistem merespons bahwa dokumen berhasil ditemukan serta dilayani, kode status respons HTTP apakah (berawalan angka 2) yang muncul pada log tersebut?
**Answer:** 200 (atau 200 OK).
