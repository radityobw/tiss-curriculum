---
type: quiz
week: 14
day: 2
title: "Quiz: Cross-Site Scripting (XSS)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa perbedaan mendasar antara target serangan SQL Injection dan XSS?
- [x] A. SQL Injection menargetkan *database* (server-side) untuk memanipulasi data. Sebaliknya, XSS menargetkan browser pengguna (*client-side*) untuk mengeksekusi *script* berbahaya tanpa disadari pengguna.
- [ ] B. SQL Injection hanya menyerang *database* NoSQL seperti MongoDB, sedangkan XSS menyerang database relasional.
- [ ] C. XSS merusak *harddisk* fisik server, sedangkan SQL Injection hanya merusak memori RAM.
- [ ] D. Tidak ada perbedaan; keduanya meretas server menggunakan *request HTTP DELETE*.

### Q2
**Type:** True/False
**Question:** Di antara tiga jenis XSS, *Reflected XSS* adalah yang paling berbahaya karena *payload* skripnya disimpan secara permanen di *database* server, sehingga akan menyerang siapa saja yang mengunjungi halaman tersebut tanpa perlu mengklik tautan jebakan.
**Answer:** False

*(Penjelasan: Pernyataan di atas mendeskripsikan **Stored XSS**, bukan Reflected XSS. Stored XSS yang paling berbahaya karena payload-nya disimpan di database).*

### Q3
**Type:** Short Answer
**Question:** Dari 3 jenis kerentanan XSS (Stored, Reflected, DOM-based), manakah yang terjadi murni karena kesalahan manipulasi HTML di sisi *frontend* (misalnya penggunaan properti `innerHTML` secara ceroboh menggunakan JavaScript)?
**Answer:** DOM-based XSS

### Q4
**Type:** Short Answer
**Question:** Saat mengeksploitasi XSS, *hacker* sering mencoba menjalankan *script* sederhana seperti `alert('1')` sebagai bukti awal (*Proof of Concept*). Dalam serangan nyata, data krusial apa yang biasanya menjadi target utama pencurian (yang bisa digunakan untuk mengambil alih sesi akun korban)?
**Answer:** Cookie (atau Session Cookie)

### Q5
**Type:** Short Answer
**Question:** Apa nama metode pertahanan yang mengubah karakter-karakter sensitif HTML (seperti `<` dan `>`) menjadi karakter entitas yang aman (seperti `&lt;` dan `&gt;`) agar tidak dieksekusi sebagai *script* oleh browser?
**Answer:** Sanitization (atau Output Encoding / HTML Escaping)
