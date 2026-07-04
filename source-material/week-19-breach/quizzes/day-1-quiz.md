---
type: quiz
week: 19
day: 1
title: "Quiz: The Anatomy of a Pentest Report"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa penyusunan dokumen Laporan (*Pentest Report*) dinilai jauh lebih krusial bagi sebuah korporasi dibandingkan sekadar menemukan kerentanan teknis itu sendiri?
- [ ] A. Karena *Bug Bounty* membayar berdasarkan jumlah halaman teks laporan, bukan berdasarkan temuan kerentanan.
- [x] B. Tanpa laporan yang membedah risiko bisnis dan langkah perbaikan, temuan kerentanan *SQLi* atau *XSS* yang paling berbahaya sekalipun tidak memiliki nilai bisnis (hanya sebatas vandalisme). Laporanlah yang menerjemahkan kerentanan teknis menjadi informasi yang bisa ditindaklanjuti oleh korporasi untuk memperbaiki pertahanan mereka.
- [ ] C. Laporan dibutuhkan secara teknis untuk bisa melewati sistem *WAF*.
- [ ] D. *Pentest Report* adalah dokumen log yang wajib dilampirkan sebagai parameter eksekusi *SQLMap*.

### Q2
**Type:** True/False
**Question:** Saat menyusun bagian *Executive Summary* di halaman pembuka laporan, pentester sangat disarankan untuk **TIDAK** menggunakan istilah teknis IT (seperti *SQLi, XSS, Payload, Cookie*) karena bagian tersebut ditujukan khusus untuk dibaca oleh pemangku kepentingan bisnis dan eksekutif (CEO/Direksi).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada struktur dokumen laporan, bagian manakah (berawalan huruf 'M') yang berfungsi untuk menjabarkan ruang lingkup (*scope*), alat (*tools*) yang digunakan (contoh: *Burp Suite, Nmap*), serta rentang waktu pelaksanaan pengujian?
**Answer:** Methodology (Metodologi).

### Q4
**Type:** Short Answer
**Question:** Bagian laporan manakah yang memuat rincian teknis serangan seperti *CVSS Score*, jenis kerentanan, *Proof of Concept (PoC)*, dan data *HTTP Request/Response* yang secara khusus ditujukan untuk Tim Developer?
**Answer:** Findings (atau Vulnerability Details).

### Q5
**Type:** Short Answer
**Question:** Pada bagian akhir laporan pengujian keamanan, bagian manakah yang mengharuskan pentester untuk menyuguhkan solusi mitigasi (seperti saran koding yang aman) bagi *Developer*?
**Answer:** Remediation (atau Remediation Advice / Mitigation).
