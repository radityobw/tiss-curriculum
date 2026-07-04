---
type: quiz
week: 7
day: 4
title: "Quiz: Membaca dan Mencari File"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa fungsi dari operator *pipe* (simbol `|`) di Terminal Linux?
- [x] A. Operator ini mengambil keluaran (*output*) dari perintah di sebelah kirinya dan langsung menjadikannya sebagai masukan (*input*) untuk perintah di sebelah kanannya secara mulus tanpa membuat file perantara.
- [ ] B. Merupakan logo kunci grafis *captcha* sandi gembok masuk administrator.
- [ ] C. Perintah absolut guna memutus koneksi WiFi seketika untuk mencegah *hacking*.
- [ ] D. Fitur percakapan interaktif khusus admin terminal server.

### Q2
**Type:** True/False
**Question:** Administrator jaringan umumnya memantau *file log server* untuk melihat kejadian terbaru di bagian paling bawah (secara *real-time*) dengan menggunakan perintah `head`.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Perintah apa di Linux yang berfungsi untuk mencari kata atau teks spesifik dari dalam sebuah file teks yang panjang?
**Answer:** grep.

### Q4
**Type:** Short Answer
**Question:** Perintah apa yang digunakan untuk menampilkan secara spesifik hanya 10 baris pertama dari sebuah *file* teks?
**Answer:** head (atau head -n 10).

### Q5
**Type:** Short Answer
**Question:** Mekanisme optimal apa yang digunakan oleh program pembaca teks terminal `less` sehingga tidak mengalami *lag* layar seperti yang sering terjadi pada alat lama seperti `cat` saat membuka file berisi jutaan baris data?
**Answer:** `less` hanya memuat (*load*) porsi teks sebesar rentang layar terminal ke dalam RAM, tidak membaca keseluruhan ukuran isi file secara serentak.
