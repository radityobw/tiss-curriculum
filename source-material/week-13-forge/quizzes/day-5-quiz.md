---
type: quiz
week: 13
day: 5
title: "Quiz: Lab Sistem Login/Register"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Saat merancang sistem *API Login*, mengapa pengiriman data kredensial (seperti kata sandi) dilarang menggunakan metode HTTP `GET` dan diwajibkan menggunakan metode `POST`?
- [x] A. Karena pada metode `GET`, data kredensial akan terlihat secara transparan menempel pada baris antarmuka *URL Address Bar* (dan terekam dalam *history browser*), sehingga memicu kerentanan untuk disadap.
- [ ] B. Karena metode `POST` mampu merusak jaringan basis relasional *API* global yang mengirimkan JSON.
- [ ] C. Karena pengiriman via metode `GET` akan otomatis mengeksekusi penghapusan pada tabel *database* internal.
- [ ] D. Karena data *password* tidak boleh diterima oleh Node.js melainkan harus diarahkan ke skrip lokal Python.

### Q2
**Type:** True/False
**Question:** Atribut `UNIQUE` pada perintah pembuatan kolom `username` bertugas memastikan agar tidak ada dua akun berbeda yang berhasil mendaftar menggunakan nama akun / *username* yang sama persis.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Kode status *HTTP Error* berapakah (seri 4xx) yang secara standar harus dikirimkan oleh server saat upaya login klien gagal ditautkan akibat tebakan kata sandi atau *username* yang tidak sesuai?
**Answer:** 401 (Unauthorized).

### Q4
**Type:** Short Answer
**Question:** Fungsi spesifik dari pustaka `bcrypt` manakah yang bertugas membandingkan kecocokan antara *password* (teks murni) yang diketik pengunjung saat *login* dengan data hasil *hash* yang tersimpan di dalam database?
**Answer:** compare (atau bcrypt.compare / compareSync).

### Q5
**Type:** Short Answer
**Question:** Dalam kerangka kerja *Express.js*, fungsi pembantu *middleware* bawaan apakah yang wajib dipanggil sebelum rute (*routes*) dideklarasikan agar server mampu membaca bodi *request* muatan yang dikirim dalam format JSON?
**Answer:** express.json()
