---
type: quiz
week: 15
day: 4
title: "Quiz: Subdomain & Technology Fingerprinting"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa para *Bug Bounty Hunter* atau *Pentester* sering memprioritaskan perburuan *Subdomain* tersembunyi dibandingkan hanya menyerang domain utama?
- [x] A. Karena domain utama umumnya diawasi ketat dan rutin di-*update*. Sebaliknya, *subdomain* (seperti server *staging* atau portal khusus developer) sering kali terlupakan oleh administrator, jarang mendapatkan *patch* keamanan, sehingga menjadi permukaan serangan (*attack surface*) yang sangat rapuh.
- [ ] B. Karena domain utama tidak pernah memuat kode HTML.
- [ ] C. Karena ekstensi *Wappalyzer* akan otomatis memblokir pemindaian jika digunakan pada domain utama.
- [ ] D. Karena semua *subdomain* selalu menggunakan protokol HTTP yang sudah usang.

### Q2
**Type:** True/False
**Question:** Ekstensi *Wappalyzer* berfungsi untuk mendeteksi *Technology Fingerprinting*, yaitu mengekstrak informasi mengenai kerangka kerja (*framework*), bahasa pemrograman, *web server*, dan CMS yang digunakan oleh sebuah situs web.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Selain *Sublist3r*, apa nama alat pencari *Subdomain* tangguh buatan OWASP yang mampu mencari subdomain dengan cara membedah sertifikat SSL dan DNS?
**Answer:** Amass (atau OWASP Amass)

### Q4
**Type:** Short Answer
**Question:** Apa istilah teknis untuk aktivitas mengidentifikasi rincian tumpukan teknologi perangkat lunak (*tech stack*) yang digunakan oleh target (seperti mengetahui bahwa target menggunakan Nginx atau PHP versi tertentu)?
**Answer:** Technology Fingerprinting

### Q5
**Type:** Short Answer
**Question:** Selain menggunakan ekstensi *Wappalyzer* di *browser*, apa nama alat bawaan OS *Kali Linux* (berawalan "What") yang juga berfungsi melakukan *Technology Fingerprinting* melalui terminal?
**Answer:** WhatWeb
