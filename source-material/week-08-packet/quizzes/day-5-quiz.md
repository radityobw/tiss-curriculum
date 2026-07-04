---
type: quiz
week: 8
day: 5
title: "Quiz: Lab Lanjut Wargame Bandit"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa kita sering menambahkan `2>/dev/null` di akhir perintah pencarian seperti `find /`?
- [ ] A. Demi meningkatkan ukuran resolusi huruf pada layar terminal dua kali lipat.
- [ ] B. Hal itu menjamin *output* dicetak dalam konfigurasi *Hexadecimal*.
- [x] C. Untuk membuang semua pesan *error* (seperti *Permission denied*) ke '/dev/null', sehingga layar terminal hanya menampilkan hasil pencarian yang berhasil ditemukan saja.
- [ ] D. Bertujuan mengelabui pihak berwenang sehingga sistem menduga penyerangnya datang dari 2 alamat IP.

### Q2
**Type:** True/False
**Question:** Root bisa langsung menjalankan (*execute*) file program atau *script* apapun, meskipun atribut eksekusi (`x`) pada file tersebut belum diaktifkan.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Opsi/parameter apa yang digunakan pada perintah `find` untuk mencari file dengan ukuran tepat 1033 bytes?
**Answer:** -size 1033c (atau `size 1033`).

### Q4
**Type:** Short Answer
**Question:** Opsi (*flag*) apa yang ditambahkan pada perintah `chmod` agar perubahan hak akses diterapkan ke seluruh isi direktori dan *file* di dalamnya secara massal (*recursive*)?
**Answer:** -R (Recursive).

### Q5
**Type:** Short Answer
**Question:** Misi mingguan OverTheWire Bandit di Week 8 ini menargetkan pencapaian hingga ke level berapa?
**Answer:** Level 8 (yakni menjebol sandi buat menyambangi Level 9).
