---
type: quiz
week: 3
day: 3
title: "Quiz: Bug Report Writing Basics"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa bagian *Steps to Reproduce* (Langkah Reproduksi) dianggap sebagai bagian paling kritis dalam sebuah laporan *Bug Bounty*?
- [x] A. Karena tim internal (*Triager*) perusahaan harus mampu memvalidasi celah tersebut secara pasti sebelum menyetujui pemberian hadiah (*bounty*).
- [ ] B. Karena bagian tersebut adalah satu-satunya bagian yang dibaca oleh CEO perusahaan.
- [ ] C. Karena tanpa langkah reproduksi, peretas tidak bisa mengingat cara menyerang di kemudian hari.
- [ ] D. Karena hukum mewajibkannya demikian.

### Q2
**Type:** True/False
**Question:** Jika sebuah kerentanan memungkinkan pembacaan data namun mengharuskan peretas untuk menipu Admin agar mengeklik tautan palsu (*User Interaction Required*), maka kerentanan ini akan selalu dikategorikan sebagai Critical (Skor 10.0).
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Sistem standar apakah yang dipakai untuk menghitung skor tingkat keparahan (*severity*) sebuah kerentanan?
**Answer:** CVSS (Common Vulnerability Scoring System).

### Q4
**Type:** Short Answer
**Question:** Jika kamu bisa membaca atau mengubah data milik pengguna lain sekadar dengan memanipulasi angka ID pada tautan URL situs, jenis kerentanan apa ini?
**Answer:** IDOR (Insecure Direct Object Reference).

### Q5
**Type:** Short Answer
**Question:** Apa sebutan profesi bagi perwakilan tim keamanan dari sebuah perusahaan yang bertugas memvalidasi laporan *bug* yang kamu kirimkan?
**Answer:** Triager.
