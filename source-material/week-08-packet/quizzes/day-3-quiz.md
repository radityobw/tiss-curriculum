---
type: quiz
week: 8
day: 3
title: "Quiz: Ownership & Privilege Escalation"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam *best practice* keamanan Linux, mengapa kita disarankan menggunakan `sudo` daripada *login* langsung sebagai akun Root?
- [x] A. Penggunaan `sudo` mencegah eksekusi perintah berbahaya secara tidak sengaja, menyulitkan serangan *brute-force*, dan mencatat *log* aktivitas siapa saja yang mengeksekusi perintah Superuser.
- [ ] B. Karena akun Root memang tidak pernah ditanamkan dan tak nyata tertulis dari sananya semenjak OS diluncurkan, hanya fiktif.
- [ ] C. Lantaran Microsoft melarang peretasan dengan OS Linux.
- [ ] D. Supaya kecepatan rotasi RAM (*Read-Access Memory*) server lebih stabil.

### Q2
**Type:** True/False
**Question:** Setiap pengguna biasa bisa bebas menggunakan perintah `chown` untuk mengubah kepemilikan file milik orang lain.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Proses mencari celah agar pengguna level bawah (seperti `www-data`) bisa meningkatkan hak aksesnya menjadi Root dinamakan apa?
**Answer:** Privilege Escalation (Eskalasi Hak Istimewa).

### Q4
**Type:** Short Answer
**Question:** Perintah apa yang ditambahkan ke awal baris untuk mengeksekusi suatu program/perintah dengan meminjam hak akses Root sementara waktu (untuk menghindari pesan *Permission Denied*)?
**Answer:** sudo (Superuser Do).

### Q5
**Type:** Short Answer
**Question:** Di Linux, setiap file pasti memiliki dua jenis kepemilikan: Pemilik Perorangan (*User Owner*) dan apa?
**Answer:** Group Owner (Grup atau Kelompok).
