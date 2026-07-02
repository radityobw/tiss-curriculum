---
type: quiz
week: 10
day: 1
title: "Quiz: Git Local & Version Control"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Jika seorang programmer mengubah kode pada *text editor*, namun belum menjalankan perintah `git add`, di area manakah perubahan *file* tersebut berada pada ekosistem Git?
- [x] A. *File* tersebut masih berada di *Working Directory* (area kerja lokal) dan belum masuk ke *Staging Area*.
- [ ] B. *File* tersebut langsung terunggah ke repositori GitHub secara otomatis.
- [ ] C. *File* tersebut akan disembunyikan oleh sistem keamanan Git lokal.
- [ ] D. *File* tersebut dihapus dan dimasukkan ke dalam keranjang sampah (*Recycle Bin*).

### Q2
**Type:** True/False
**Question:** Saat membuat pesan menggunakan perintah `git commit -m`, sangat disarankan untuk menulis pesan acak seperti "revisi asdfg koding 123" agar pihak luar tidak dapat mengerti alur pengembangan program jika repositori tersebut diunggah ke publik.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Perintah Git dasar apa yang digunakan untuk menginisialisasi atau mengubah sebuah direktori folder proyek lokal biasa menjadi sebuah repositori Git resmi?
**Answer:** git init.

### Q4
**Type:** Short Answer
**Question:** Fitur Git manakah yang secara khusus didesain agar *developer* dapat mencoba mengembangkan fitur baru di ruang terisolasi yang bercabang, sehingga menjamin kode di jalur utama (*main*) tidak terganggu atau rusak?
**Answer:** Branch (Pencabangan).

### Q5
**Type:** Short Answer
**Question:** Berdasarkan alur kerja tiga tahapan Git (*The Three States*), di area manakah sebuah file akan ditampung sementara setelah perintah `git add` dieksekusi, sebelum file tersebut diresmikan lewat proses *commit*?
**Answer:** Staging Area.
