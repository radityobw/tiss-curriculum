---
type: quiz
week: 21
day: 3
title: "Quiz: Linux Logs & Journalctl"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di sistem operasi Linux, di direktori absolut manakah sebagian besar *file* log (seperti log web, log SSH, dan log kernel) disimpan secara terpusat?
- [ ] A. `/etc/logs/`.
- [ ] B. `/home/user/log/`.
- [x] C. `/var/log/`.
- [ ] D. `/tmp/var/`.

### Q2
**Type:** True/False
**Question:** Saat menyelidiki insiden otentikasi di peladen Linux (distro Ubuntu/Debian), berkas yang pertama kali diperiksa oleh Analis SOC untuk mencari jejak *login* SSH atau eksekusi *sudo* adalah *auth.log*.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada distribusi Linux modern berbasis *systemd*, perintah terminal apa yang digunakan untuk memfilter dan membaca basis data log sistem terpusat?
**Answer:** journalctl.

### Q4
**Type:** Short Answer
**Question:** Saat Analis menjalankan perintah `journalctl -u ssh.service`, flag argumen `-u` tersebut digunakan untuk memfilter log berdasarkan apa?
**Answer:** Unit (atau Service, untuk menampilkan log spesifik dari layanan SSH saja).

### Q5
**Type:** Short Answer
**Question:** Perintah terminal Linux dasar apa yang paling sering digunakan oleh Analis SOC untuk menyaring dan mencari kata kunci tertentu (seperti "Failed password") dari ribuan baris *file* teks log?
**Answer:** grep (atau `grep "Failed password"`).
