---
type: quiz
week: 13
day: 4
title: "Quiz: Authentication & Password Security"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa pendekatan otentikasi *JSON Web Token (JWT)* bisa membebaskan *Server* dari beban berat untuk mencatat riwayat login (*session*) pengguna di dalam *database*?
- [x] A. Arsitektur *JWT* bersifat *Stateless*. Token JWT yang valid disimpan secara penuh di sisi klien. Server hanya perlu memvalidasi tanda tangan kriptografis di dalam token tersebut tanpa perlu merawat catatan sesi secara internal.
- [ ] B. Karena *Server* JWT secara otomatis menyisipkan database mini langsung ke dalam *hard disk* perangkat klien pengguna.
- [ ] C. *JWT* tidak memerlukan otentikasi dan memberikan akses bebas pada setiap rute web yang dikunjungi.
- [ ] D. *JWT* diam-diam memindahkan riwayat catatan log pengguna ke dalam penyimpanan sistem operasi server, bukan ke *database*.

### Q2
**Type:** True/False
**Question:** Perbedaan mendasar antara *Enkripsi* dan *Hashing* adalah: *Enkripsi* bersifat dua arah (bisa didekripsi), sedangkan *Hashing* bersifat mutlak satu arah (tidak bisa dikembalikan ke wujud aslinya).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Parameter teks acak pengaman tambahan apakah (pada algoritma *Bcrypt*) yang dicampur pada kata sandi sebelum proses enkripsi, guna memastikan dua *password* yang identik tetap akan menghasilkan cetakan *hash* yang sepenuhnya berbeda?
**Answer:** Salt (atau Kadar Garam / Salt Rounds).

### Q4
**Type:** Short Answer
**Question:** Modul *NPM* populer apakah yang sangat direkomendasikan bagi *developer Node.js* untuk melakukan operasi *hashing* pada kata sandi secara aman?
**Answer:** bcrypt (atau bcryptjs).

### Q5
**Type:** Short Answer
**Question:** Apa nama metode serangan peretasan sandi di mana penyerang membombardir server dengan tebakan permutasi kata sandi secara masif dan tanpa henti (biasanya memakai daftar kata / *wordlist*)?
**Answer:** Brute-Force (atau Brute Force Attack / Serangan Brute-Force).
