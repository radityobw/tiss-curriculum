---
type: quiz
week: 14
day: 5
title: "Quiz: Lab Securing the API"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dari daftar perlindungan *backend* berikut ini, kombinasi manakah yang paling akurat sesuai dengan kerentanan yang dicegahnya?
- [x] A. Kueri Berparameter (`?`) mencegah serangan SQL Injection; `Helmet.js` mengamankan header HTTP (mencegah *Misconfiguration*); `Rate Limit` mencegah serangan *Brute-Force* dan DDoS.
- [ ] B. `Helmet.js` mencegah kerentanan IDOR, sedangkan kueri `?` digunakan untuk menangkis serangan XSS.
- [ ] C. `Rate Limit` mencegah *Stored XSS* di dalam *database* SQLite3.
- [ ] D. `Bcrypt` digunakan untuk menyembunyikan log *Stack Trace* saat terjadi *error* 500.

### Q2
**Type:** True/False
**Question:** Saat menyusun *middleware* di Express, `express.json()` (pembaca *body request*) boleh diletakkan di akhir kode, setelah semua rute (seperti `app.post(...)`) dideklarasikan.
**Answer:** False

*(Penjelasan: Middleware seperti `express.json()` harus diletakkan SEBELUM rute agar body dari request dapat diproses sebelum masuk ke rute yang dituju).*

### Q3
**Type:** Short Answer
**Question:** Modul NPM apa yang bertugas membaca file `.env` dan menyematkan variabel di dalamnya ke dalam *environment* Node.js (sehingga bisa diakses via `process.env`)?
**Answer:** dotenv

### Q4
**Type:** Short Answer
**Question:** Ketika serangan (seperti *request* dari Postman) melampaui batas maksimal yang ditetapkan oleh `express-rate-limit`, server akan memblokir permintaan tersebut dan mengembalikan status kode HTTP tertentu. Berapakah kode status HTTP untuk pesan "Too Many Requests"?
**Answer:** 429

### Q5
**Type:** Short Answer
**Question:** Untuk mencegah celah IDOR (Insecure Direct Object Reference) pada rute API yang memerlukan otorisasi, dua parameter apa yang umumnya harus dicocokkan/diuji kesetaraannya di dalam logika *backend* (menggunakan objek `req`)?
**Answer:** req.params.id dan req.user.id
