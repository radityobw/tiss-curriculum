---
type: quiz
week: 8
day: 2
title: "Quiz: File Permissions (rwx)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Jika sebuah direktori diatur hak aksesnya menggunakan parameter oktal `777`, apa bahayanya dari segi keamanan?
- [ ] A. File di dalam direktori akan otomatis disembunyikan selama 7 hari kalender.
- [ ] B. Terminal akan memblokir semua perintah dan sistem akan terkunci (*brick*).
- [x] C. Ia memberikan hak penuh (Baca, Tulis, dan Eksekusi) kepada semua pengguna sistem (*Others* / *Everyone*), memungkinkan siapa saja untuk memodifikasi, mengeksekusi, atau menghapus file tanpa ada pembatasan keamanan.
- [ ] D. Hal ini menjamin tingkat enkripsi keamanan tertinggi pada direktori.

### Q2
**Type:** True/False
**Question:** Saat menggunakan perintah `chmod`, sistem operasi Linux hanya dapat memahami format alfabet (seperti `chmod +rwx`) dan tidak dapat memproses perintah yang menggunakan parameter nilai angka oktal (seperti `chmod 644`).
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Dalam konversi sistem nilai oktal, berapakah representasi angka matematika masing-masing untuk atribut *Read* (r), *Write* (w), dan *Execute* (x)?
**Answer:** Read (r) = 4, Write (w) = 2, Execute (x) = 1.

### Q4
**Type:** Short Answer
**Question:** Dalam representasi *string* perizinan seperti `-rwxr-xr--`, sistem membaginya menjadi 3 kategori pengguna (*entities*). Sebutkan ketiga kategori tersebut secara berurutan dari kiri ke kanan!
**Answer:** User (Pemilik file), Group (Anggota grup), dan Others (Pengguna lain di sistem).

### Q5
**Type:** Short Answer
**Question:** Apa arti dari karakter "d" ketika muncul di posisi paling kiri pada *output* detail file seperti `drwxr-xr-x`?
**Answer:** Menandakan bahwa item tersebut adalah sebuah direktori (folder), bukan file biasa.
