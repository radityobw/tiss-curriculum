---
type: quiz
week: 17
day: 3
title: "Quiz: File Upload & IDOR"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa seorang pentester mencoba untuk mengunggah file berekstensi *PHP* alih-alih mengunggah format gambar (*JPEG/PNG*) pada fitur unggah foto profil (*File Upload*)?
- [x] A. Untuk menginjeksi *Web Shell*! Jika file PHP berhasil diunggah dan dieksekusi oleh server, pentester dapat memanggilnya via URL untuk menjalankan perintah sistem operasi dari jarak jauh (*RCE* / Remote Code Execution).
- [ ] B. Karena bahasa pemrogaman *PHP* otomatis mengekstrak kerentanan *IDOR HTML*.
- [ ] C. Karena skrip *PHP* kebal dari deteksi *Wappalyzer*.
- [ ] D. Skrip *PHP* memblokir injeksi otomatis dari alat *SQLMap*.

### Q2
**Type:** True/False
**Question:** Ketika mencoba menembus pertahanan filter *File Upload*, seorang penyerang dapat memanipulasi ekstensi nama berkas menggunakan trik ekstensi ganda (misal: `shell.php.jpg`) guna mengelabui penyaring yang hanya memvalidasi format akhiran `.jpg`.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Dalam pembuatan *Web Shell* PHP yang sederhana, fungsi PHP apakah yang sering digunakan (contoh: `...($_GET['cmd'])`) untuk menjalankan perintah terminal sistem operasi secara langsung?
**Answer:** system() (atau fungsi system)

### Q4
**Type:** Short Answer
**Question:** Ketika pentester menggunakan *Burp Suite* untuk mengubah nilai *header* HTTP dari `Content-Type: application/x-php` menjadi `Content-Type: image/jpeg` saat mengunggah *Web Shell*, metode penipuan WAF apakah yang tengah ia terapkan?
**Answer:** Manipulasi tipe MIME (MIME Type Spoofing / Content-Type Bypass).

### Q5
**Type:** Short Answer
**Question:** Pada eksploitasi *IDOR*, server melakukan kesalahan karena gagal memvalidasi kecocokan antara parameter permintaan dokumen dengan pemilik asli dari objek tersebut (tanpa memeriksa *Session Cookie*). Apa kepanjangan dari akronim kerentanan IDOR tersebut?
**Answer:** Insecure Direct Object Reference
