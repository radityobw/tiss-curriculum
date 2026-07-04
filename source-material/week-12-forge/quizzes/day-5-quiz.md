---
type: quiz
week: 12
day: 5
title: "Quiz: Lab CRUD REST API"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Saat membuka `http://localhost:8080/` di *browser*, mengapa kita sering melihat peringatan *error* `Cannot GET /`?
- [ ] A. Koneksi ditolak karena belum menggunakan koneksi HTTPS.
- [ ] B. V8 Engine pada *browser* mengalami kelumpuhan.
- [x] C. Developer belum membuat *Routing* khusus untuk *root URL* (`/`), misalnya dengan `app.get('/', ...)`.
- [ ] D. Node.js mewajibkan database diinstal sebelum bisa menampilkan antarmuka.

### Q2
**Type:** True/False
**Question:** Untuk menangkap data formulir dari klien saat metode *POST* digunakan, objek Express yang tepat untuk membaca data tersebut adalah `req.params`.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Sebutkan setidaknya dua aplikasi penguji *API* yang biasa digunakan *developer backend* untuk mengetes metode HTTP selain `GET` (*POST*, *PUT*, dan *DELETE*)!
**Answer:** Thunder Client, Postman, Insomnia, atau cURL.

### Q4
**Type:** Short Answer
**Question:** *Middleware* wajib apa (menggunakan `app.use(...)`) yang harus diletakkan di bagian atas skrip Express agar *server* bisa membaca data *Request Body* berformat JSON?
**Answer:** `express.json()`

### Q5
**Type:** Short Answer
**Question:** Properti apa pada objek *Request* di Express.js yang digunakan untuk menangkap nilai dari parameter URL dinamis (seperti `:id`)?
**Answer:** `req.params` (atau `req.params.id`).
