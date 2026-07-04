---
type: quiz
week: 11
day: 3
title: "Quiz: DOM Manipulation"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Risiko keamanan fatal apa yang bisa terjadi (terkait celah *Cross-Site Scripting / XSS*) jika kita menggunakan `innerHTML` untuk menampilkan input dari pengguna tanpa divalidasi?
- [x] A. Input pengguna akan dieksekusi oleh *browser* sebagai kode HTML/JavaScript aktif. Jika peretas memasukkan `<script>kodeJahat()</script>`, maka skrip tersebut akan dijalankan dan berpotensi mencuri data sensitif pengunjung.
- [ ] B. Sandi akan mengakibatkan atribut warna dan dimensi gambar pada layar laman tertutup penuh.
- [ ] C. Komando sisipan lewat saluran properti *innerHTML* akan seketika membongkar paksa penulisan skrip pemindahan protokol URL sehingga bermutasi memanggil transmisi rute *GET*.
- [ ] D. Skema tersebut akan langsung mencetus layar mengunci perambannya secara permanen dari jaringan luar web publik publik.

### Q2
**Type:** True/False
**Question:** Fungsi `querySelector` menyeleksi elemen DOM menggunakan sintaks yang sama persis dengan *CSS selector* (misalnya `#` untuk *id* dan `.` untuk *class*).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Apa nama objek global bawaan JavaScript yang digunakan sebagai titik awal untuk menyeleksi dan memanipulasi elemen HTML pada halaman *web*?
**Answer:** document.

### Q4
**Type:** Short Answer
**Question:** Untuk menghindari risiko keamanan XSS dari penggunaan `innerHTML`, properti DOM apa yang lebih aman digunakan karena hanya menampilkan *input* sebagai teks biasa (tidak akan mengeksekusi tag HTML)?
**Answer:** innerText (atau textContent).

### Q5
**Type:** Short Answer
**Question:** Properti DOM apa yang digunakan untuk memodifikasi *styling* (CSS) sebuah elemen secara langsung melalui JavaScript (contoh penggunaannya: `elemen.___.color = "red"`)?
**Answer:** style.
