---
type: quiz
week: 15
day: 5
title: "Quiz: Lab Full Recon Report"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengingat bahwa fase *Active Reconnaissance* (seperti pemindaian menggunakan *Nmap*) sangat berisiko dan dapat memicu deteksi keamanan target, dokumen legalitas apa yang mutlak harus ditandatangani sebelum pengujian dilakukan agar *Pentester* terlindung dari jerat hukum?
- [x] A. Dokumen persetujuan resmi dan otoritas legal dari pemilik sistem, yang sering disebut *Rules of Engagement (RoE)*.
- [ ] B. Dokumen *JWT (JSON Web Token)*.
- [ ] C. Sertifikasi OSINT dari OWASP.
- [ ] D. Lembar perizinan serangan *SQL Injection*.

### Q2
**Type:** True/False
**Question:** Jika Nmap berhasil mendeteksi bahwa server target menjalankan versi perangkat lunak yang sudah usang (misalnya Apache 2.4.49), *Pentester* diwajibkan untuk selalu menggunakan *ffuf* terlebih dahulu sebelum bisa mencari kerentanan (*CVE*) dari versi tersebut.
**Answer:** False

*(Penjelasan: Jika versi spesifik perangkat lunak sudah diketahui dari hasil pemindaian Nmap, Pentester bisa langsung mencari literatur eksploitasi kerentanan publik (CVE) yang sesuai untuk versi tersebut, tanpa perlu melakukan pencarian direktori menggunakan ffuf terlebih dahulu).*

### Q3
**Type:** Short Answer
**Question:** Dari 5 fase metodologi *Pentesting*, apa nama tahapan terakhir yang berfokus pada penyusunan dokumen hasil temuan dan rekomendasi perbaikan untuk pihak perusahaan?
**Answer:** Post-Exploitation & Reporting (atau Reporting)

### Q4
**Type:** Short Answer
**Question:** Pada penggunaan Nmap, parameter (flag) apa yang ditambahkan untuk mendeteksi *Service Version* (nama aplikasi dan versinya yang berjalan di port tersebut)?
**Answer:** -sV

### Q5
**Type:** Short Answer
**Question:** Dalam teknik *Google Dorking*, operator spesifik apa yang digunakan untuk mencari *file* yang hanya berekstensi PDF?
**Answer:** filetype:pdf
