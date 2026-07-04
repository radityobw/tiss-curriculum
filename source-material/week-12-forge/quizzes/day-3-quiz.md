---
type: quiz
week: 12
day: 3
title: "Quiz: Express.js, Routing & Middleware"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa *developer backend* lebih memilih *framework* Express.js dibandingkan menggunakan modul HTTP bawaan (*Native*) Node.js?
- [x] A. Modul HTTP bawaan Node.js membutuhkan penulisan kode (*boilerplate*) yang panjang untuk *routing*, sementara Express.js menyediakan struktur sintaksis yang lebih ringkas dan mudah dibaca.
- [ ] B. Kode HTTP bawaan Node.js sering *error* jika tidak menggunakan *proxy* HTTP.
- [ ] C. Express.js melipatgandakan kapasitas memori RAM *server*.
- [ ] D. Modul asli Node.js tidak bisa membaca ekstensi HTML.

### Q2
**Type:** True/False
**Question:** Fungsi `next()` pada *middleware* Express.js bertujuan untuk memutus koneksi dari permintaan (*Request*) klien secara paksa.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Konsep yang mengatur pemetaan tautan URL untuk diarahkan ke fungsi *handler* pemrosesan tertentu di dalam *server* disebut?
**Answer:** Routing (atau Rute).

### Q4
**Type:** Short Answer
**Question:** Komponen kode yang ditancapkan untuk mencegat dan memodifikasi *HTTP Request* sebelum diserahkan ke *handler* utama disebut?
**Answer:** Middleware.

### Q5
**Type:** Short Answer
**Question:** Pada *Express.js*, fungsi apa yang dipanggil di akhir skrip aplikasi untuk mengaktifkan *server* agar mulai mendengarkan lalu lintas permintaan (biasanya membutuhkan nomor *port*)?
**Answer:** `app.listen()` (atau `listen`).
