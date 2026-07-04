---
type: quiz
week: 19
day: 3
title: "Quiz: Writing Good Proof of Concepts (PoCs)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Bagian laporan manakah yang bertugas menyajikan instruksi langkah demi langkah secara berurutan agar tim *Developer* mampu mereproduksi serangan secara manual di perangkat mereka sendiri?
- [ ] A. *CVSS v3.1*.
- [ ] B. *Executive Summary*.
- [x] C. *Proof of Concept* (PoC) atau *Steps to Reproduce*.
- [ ] D. *Methodology*.

### Q2
**Type:** True/False
**Question:** Ketika menyusun instruksi *Proof of Concept* (PoC), pentester sangat disarankan untuk **TIDAK** menyuruh *Developer* mereproduksi eksploitasi menggunakan alat peretasan otomatis (seperti *SQLMap* atau *Burp Intruder*) karena belum tentu semua orang mengerti cara pakainya dan berpotensi membebani server *Production*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Jika seorang pentester menemukan kerentanan yang kompleks dan panjang untuk dibuktikan dengan *screenshot* biasa (misalnya *Account Takeover* atau manipulasi berantai), media visual apa yang paling direkomendasikan untuk membuktikan *Proof of Concept* dengan tak terbantahkan?
**Answer:** Video rekaman layar (Screencast / Video PoC).

### Q4
**Type:** Short Answer
**Question:** Saat menyertakan bukti teknis di dalam *Proof of Concept (PoC)*, pentester sering kali menyalin data lalu lintas dari *Burp Suite* yang membuktikan injeksi *Payload*. Data komunikasi teks tersebut merupakan pasangan antara apa dan apa?
**Answer:** HTTP Request dan HTTP Response.

### Q5
**Type:** Short Answer
**Question:** Saat mereproduksi kerentanan dalam penyusunan laporan, prinsip kehati-hatian apa yang wajib dilakukan pentester dalam memilih jenis serangan (*Payload*) agar tidak merusak data yang ada di server korporasi (khususnya *Production*)?
**Answer:** Menggunakan *Safe Payload* (Memilih *payload* yang tidak merusak data, misal sebatas menampilkan `alert(1)`, memanggil `whoami`, atau memancing respons waktu `sleep()`, dan BUKAN eksekusi perintah destruktif seperti penghapusan *database* / `DROP TABLE`).
