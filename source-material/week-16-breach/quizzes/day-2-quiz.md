---
type: quiz
week: 16
day: 2
title: "Quiz: SQL Injection Blind"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan mendasar antara teknik *Blind SQLi* dibandingkan dengan *UNION-based SQLi*?
- [ ] A. *UNION SQLi* dirancang spesifik meretas bot, sementara *Blind SQLi* digunakan untuk membajak Sesi (Session).
- [ ] B. Pada *Blind SQLi*, kita sama sekali tidak boleh menggunakan perintah AND atau OR.
- [x] C. Pada metode *UNION*, hasil pencurian data (seperti daftar *password*) akan langsung dicetak dan ditampilkan secara visual di layar web. Sebaliknya, pada *Blind SQLi*, server tidak menampilkan *error* atau hasil data apapun di layar. Penyerang harus menebak dan mengekstraksi data dengan cara meraba respons aplikasi (memantau perubahan *Boolean* / True-False, atau memantau jeda waktu perlambatan server).
- [ ] D. *Blind SQLi* membutuhkan bantuan alat *Wappalyzer* agar dapat dieksekusi.

### Q2
**Type:** True/False
**Question:** Teknik *Time-based Blind SQLi* mengekstraksi data dari target dengan mengamati perubahan pada tampilan halaman (misalnya halaman akan hilang/error jika salah, dan normal jika benar), tanpa pernah menggunakan fungsi jeda waktu (delay).
**Answer:** False

*(Penjelasan: Mengamati perubahan tampilan web adalah konsep dari Boolean-based Blind SQLi. Time-based Blind SQLi secara spesifik menggunakan fungsi jeda waktu / delay seperti SLEEP() untuk mengetahui apakah tebakannya benar).*

### Q3
**Type:** Short Answer
**Question:** Taktik meraba data secara perlahan huruf-demi-huruf dengan cara menyisipkan kondisi logika *True/False* (Benar/Salah) untuk melihat apakah halaman web merespons normal atau *error* disebut dengan metode *SQLi* apa?
**Answer:** Boolean-based Blind SQLi (atau Boolean)

### Q4
**Type:** Short Answer
**Question:** Pada serangan *Time-based Blind SQL Injection*, perintah SQL spesifik apa yang sering digunakan penyerang untuk memaksa database menahan proses pemuatan (*loading*) halaman web selama 10 detik sebagai bentuk konfirmasi bahwa tebakan kuerinya benar?
**Answer:** SLEEP() (atau pg_sleep() / WAITFOR DELAY)

### Q5
**Type:** Short Answer
**Question:** Karena mengekstraksi data secara *Blind SQLi* (menebak huruf satu per satu) secara manual sangat memakan waktu, spesialis keamanan menggunakan alat otomatisasi berbasis Python. Apa nama alat otomatisasi populer tersebut?
**Answer:** SQLMap
