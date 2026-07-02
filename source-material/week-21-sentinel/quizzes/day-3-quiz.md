---
type: quiz
week: 21
day: 3
title: "Quiz: Linux Logs & Journalctl"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Membuka anatomi pencatatan aktivitas di Linux, di rute absolut direktori manakah bersarangnya nyaris seluruh rekam jejak file log (seperti log web, log SSH, dan log kernel)?
- [ ] A. `/etc/logs/`.
- [ ] B. `/home/user/log/`.
- [x] C. `/var/log/`.
- [ ] D. `/tmp/var/`.

### Q2
**Type:** True/False
**Question:** Di investigasi otentikasi peladen Linux (distro Ubuntu/Debian), berkas log yang paling pertama diperiksa oleh Analis SOC saat memburu jejak keberhasilan eksploitasi SSH dan eksekusi komando *root (Sudo)* adalah berkas yang bernama <i>auth.log</i>.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat meluncurkan perburuan jejak pada distribusi Linux *systemd* modern, komando terminal (berawalan huruf 'j') apakah yang digunakan untuk memfilter lantas membaca basis data binari log?
**Answer:** journalctl.

### Q4
**Type:** Short Answer
**Question:** Saat penganalisis mengeksekusi kueri terminal, lalu menggunakan perintah `journalctl -u ssh.service`, flag argumen `-u` tersebut didapuk guna memfilter log berdasarkan apa?
**Answer:** Unit (atau Service, guna meraba log spesifik untuk layanan ssh/ daemon saja).

### Q5
**Type:** Short Answer
**Question:** Di komando terminal Linux, apa perintah paling lumrah (satu kata) yang dikerahkan Analis SOC saat ingin menyaring dan memunculkan sebaris barisan log "Failed password" dari ribuan baris teks?
**Answer:** grep (atau `grep "Failed password"`).
