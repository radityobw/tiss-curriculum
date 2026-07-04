---
type: quiz
week: 16
day: 4
title: "Quiz: Authentication Bypass"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan utama antara serangan autentikasi *Brute Force* dengan *Credential Stuffing*?
- [ ] A. *Credential Stuffing* selalu membutuhkan SQLMap untuk menebak konfigurasi sandi.
- [x] B. Pada *Brute Force*, penyerang mencoba menebak kombinasi huruf secara acak atau membabi-buta (*password* umum). Sebaliknya, pada *Credential Stuffing*, penyerang menggunakan daftar kombinasi asli (*email* dan *password*) yang bocor dari peretasan situs web lain (di masa lalu), berharap korban menggunakan *password* yang persis sama di situs web target.
- [ ] C. *Brute Force* tidak pernah berhasil mendobrak otorisasi.
- [ ] D. *Credential Stuffing* hanya efektif digunakan pada kerentanan SQL Injection.

### Q2
**Type:** True/False
**Question:** Jika suatu halaman Login rentan terhadap *Authentication Bypass* (misalnya menggunakan *payload* sederhana seperti `' OR 1=1--`), penyerang tidak perlu lagi repot-repot menggunakan *SQL Injection* tingkat lanjut (seperti UNION atau Blind) atau *Brute Force* untuk masuk sebagai *admin*, karena gerbang otentikasinya sudah bisa langsung ditembus.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Serangan apa yang memancing korban untuk mengklik tautan (berisi *Cookie Session* buatan penyerang), sehingga ketika korban berhasil *login*, penyerang bisa langsung mengambil alih akun korban tanpa perlu *login* lagi?
**Answer:** Session Fixation

### Q4
**Type:** Short Answer
**Question:** Jika penyerang masuk sebagai pengguna biasa, mencegat (*intercept*) *HTTP Request*, lalu mengubah nilai dari `role=user` menjadi `role=admin` agar mendapatkan hak akses Administrator, jenis eksploitasi kerentanan apa yang sedang dia praktikkan?
**Answer:** Parameter Tampering (atau berkaitan dengan Broken Access Control / Privilege Escalation)

### Q5
**Type:** Short Answer
**Question:** Fitur keamanan fundamental apa yang luput ditambahkan oleh pengembang pada halaman *Login*, sehingga membiarkan penyerang dapat meluncurkan serangan *Brute Force* ratusan hingga ribuan kali per detik tanpa diblokir?
**Answer:** Rate Limiting (Pembatasan kecepatan pencobaan *Login*) atau absennya sistem CAPTCHA.
