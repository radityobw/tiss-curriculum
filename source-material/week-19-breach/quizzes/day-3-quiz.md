---
type: quiz
week: 19
day: 3
title: "Quiz: Writing Good Proof of Concepts (PoCs)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di penu , anatomi laporan apakah yang dituntut menyajikan instruksi langkah demi langkah (1,2,3) resep yang memampukan tim *Developer* menduplikasi meledakkan ulang serangan secara manual?
- [ ] A. *CVSS v3.1*.
- [ ] B. *Executive Summary*.
- [x] C. *Proof of Concept* (PoC) atau *Steps to Reproduce*.
- [ ] D. *Methodology*.

### Q2
**Type:** True/False
**Question:** Ketika penganalisis menulis resep bukti (<i>PoC</i>), sangatlah diharamkan menyuruh tim *Developer* meretas menggunakan buas otomatis (seperti *SQLMap* atau *Burp Intruder*) lantaran belum tentu terampil memakainya lantas hal itu berpotensi meruntuhkan server *Production*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Ketika penganalisis meratapi kerentanan yang mustahil dibuktikan secara visual lewat tangkapan layar (misal manipulasi *Blind SQLi Time-Based*), rekam apa (be gambar bergerak) yang didapuk pembuktian tak terbantahkan?
**Answer:** Video rekaman layar (Screencast / Video PoC).

### Q4
**Type:** Short Answer
**Question:** Di ranah penu pembuktian (PoC), peretas menyisipkan salinan teks HTTP yang memuat Payload mautnya. Teks ini merangkum lalu-lintas HTTP apa saja?
**Answer:** HTTP Request dan HTTP Response.

### Q5
**Type:** Short Answer
**Question:** Ketika menyusun *Steps to Reproduce*, apa pantangan bagi peretas saat memilih Payload di peladen *Production* korporasi (agar tak merusak data)?
**Answer:** Menggunakan *Safe Payload* (Payload yang tidak merusak, seperti cuma `sleep()` atau mencetak `alert(1)`, bukan `DROP TABLE`).
