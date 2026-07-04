---
type: quiz
week: 6
day: 2
title: "Quiz: HTTP/HTTPS Deep-Dive"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa pembuat situs sangat diwajibkan menggunakan metode pengiriman POST ketimbang GET untuk formulir *login* berisikan kata sandi?
- [x] A. Karena metode GET mengekspos semua parameter formulir langsung pada alamat URL peramban secara transparan yang menjadikannya tersimpan di riwayat (*history*) secara telanjang.
- [ ] B. Karena metode POST secara otomatis mengeksekusi sistem *CAPTCHA*.
- [ ] C. Karena metode GET tidak dapat membawa paket di atas 10 *byte* berlawanan dengan metode POST.
- [ ] D. Karena metode POST berjalan di UDP, bukan TCP.

### Q2
**Type:** True/False
**Question:** *HTTP Status Code* yang berawalan "4" (seperti 404 atau 403) mengindikasikan bahwa *server* dari situs terkait mengalami kerusakan sistem internal.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Pada gerbang pintu (Port) standar nomor berapakah secara *default* operasi pertukaran situs web terenkripsi HTTPS beroperasi?
**Answer:** Port 443.

### Q4
**Type:** Short Answer
**Question:** Apa makna *HTTP Status Code* "200 OK"?
**Answer:** Respons berhasil atau permintaan berhasil diproses peladen tanpa ada masalah.

### Q5
**Type:** Short Answer
**Question:** Standar kriptografi apa yang ditambahkan pada HTTP untuk mengenkripsi komunikasi sehingga menjadi HTTPS?
**Answer:** TLS/SSL.
