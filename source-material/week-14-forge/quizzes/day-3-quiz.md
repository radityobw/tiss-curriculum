---
type: quiz
week: 14
day: 3
title: "Quiz: Broken Access Control & IDOR"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan utama antara *Authentication* (Otentikasi) dan *Authorization* (Otorisasi) dalam keamanan sistem?
- [x] A. Otentikasi memverifikasi identitas pengguna ("Siapa Anda?"), sedangkan Otorisasi menentukan hak akses atau wewenang yang dimiliki pengguna tersebut setelah berhasil login ("Apa yang boleh Anda lakukan/akses?").
- [ ] B. Otorisasi memverifikasi keberadaan data di *database*, sedangkan Otentikasi mengatur rute kueri SQL di *endpoint*.
- [ ] C. Keduanya adalah istilah yang sama persis dan dapat digunakan secara bergantian untuk menggambarkan perlindungan dari serangan XSS.
- [ ] D. Keduanya hanya sebatas ekstensi pelengkap untuk mencegah *SQL Injection*.

### Q2
**Type:** True/False
**Question:** Kerentanan IDOR terjadi ketika server mempercayai ID yang dikirim oleh pengguna di URL (misal: `/api/pesanan/7`) secara langsung tanpa memvalidasi apakah pengguna yang sedang *login* (berdasarkan otorisasi/Token) adalah pemilik asli dari data pesanan bernomor `7` tersebut.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Apa kepanjangan dari kerentanan IDOR?
**Answer:** Insecure Direct Object Reference

### Q4
**Type:** Short Answer
**Question:** Selain IDOR, istilah modern apa yang saat ini lebih sering digunakan oleh pakar keamanan API (*API Security Experts*) untuk menggambarkan celah di mana penyerang dapat mengakses atau memodifikasi objek milik pengguna lain?
**Answer:** BOLA (Broken Object Level Authorization)

### Q5
**Type:** Short Answer
**Question:** Di dalam daftar kerentanan *OWASP Top 10* versi terbaru, kategori apa yang menduduki peringkat pertama sebagai celah keamanan web paling umum dan mematikan (di mana kerentanan IDOR juga termasuk ke dalam kategori ini)?
**Answer:** Broken Access Control (BAC)
