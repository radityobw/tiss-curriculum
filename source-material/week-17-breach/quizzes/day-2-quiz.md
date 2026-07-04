---
type: quiz
week: 17
day: 2
title: "Quiz: CSRF & SSRF"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan utama antara serangan *Cross-Site Request Forgery (CSRF)* dan *Server-Side Request Forgery (SSRF)*?
- [ ] A. *CSRF* mengeksekusi ekstraksi `Session Cookie`, sedangkan *SSRF* ditugaskan merekam ketikan menggunakan `Keylogger`.
- [x] B. Pada *CSRF*, korban dipancing agar *Browser*-nya sendiri yang mengirimkan permintaan (*Request*) berbahaya ke *server* aplikasi tanpa disadarinya. Sebaliknya, pada *SSRF*, yang ditipu adalah *Server Backend* aplikasi target itu sendiri, dengan memaksa server tersebut untuk mengirimkan kueri/menyerang layanan internal di jaringannya sendiri (seperti `localhost`).
- [ ] C. *SSRF* didesain untuk menipu perlindungan WAF, sementara *CSRF* untuk menipu ekstensi *Wappalyzer*.
- [ ] D. Keduanya adalah tipe serangan *SQL Injection*.

### Q2
**Type:** True/False
**Question:** Kerentanan *CSRF* (Cross-Site Request Forgery) terjadi karena pengembang aplikasi web lupa menyisipkan perlindungan token acak (seperti *CSRF Token*) pada formulir yang melakukan perubahan data (misalnya form ganti kata sandi atau transfer uang).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada serangan *CSRF*, penyerang sering kali menggunakan fungsi *JavaScript* tersembunyi (seperti `document.forms[0]...`) agar formulir pemalsuan permintaan otomatis terkirim tanpa korban harus menekan tombol "Submit". Fungsi *JavaScript* apa yang digunakan untuk mengirimkan formulir tersebut secara otomatis?
**Answer:** submit()

### Q4
**Type:** Short Answer
**Question:** Dalam simulasi serangan *SSRF*, alamat IP lokal apa (berawalan `127.`) yang sering dibidik oleh penyerang untuk menipu *server* agar mengakses layanan internal atau dasbor admin-nya sendiri?
**Answer:** 127.0.0.1 (atau localhost)

### Q5
**Type:** Short Answer
**Question:** Jika server target di-hosting di layanan Cloud (seperti AWS atau GCP) dan rentan terhadap *SSRF*, alamat IP khusus apa (berawalan `169.`) yang sering dieksploitasi oleh penyerang untuk mencuri *Instance Metadata* layanan *cloud* tersebut?
**Answer:** 169.254.169.254
