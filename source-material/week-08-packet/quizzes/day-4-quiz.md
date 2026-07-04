---
type: quiz
week: 8
day: 4
title: "Quiz: Proses & Services"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Jika kamu menemukan sebuah program dengan PID `1337` yang *hang* dan menolak dimatikan dengan cara biasa, perintah apa yang harus digunakan untuk mematikannya secara paksa?
- [ ] A. `exit 1337`
- [ ] B. `sudo stop 1337`
- [ ] C. `purge 1337`
- [x] D. `kill -9 1337`

### Q2
**Type:** True/False
**Question:** Perintah `ps aux` menampilkan data proses secara *Real-Time* (terus bergerak), sedangkan `top` hanya menampilkan data statis seperti sebuah *screenshot* (tak bergerak).
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Apa kepanjangan dari PID (nomor identitas unik yang diberikan sistem ke setiap program yang berjalan)?
**Answer:** Process ID (Process Identifier).

### Q4
**Type:** Short Answer
**Question:** Perintah/opsi `systemctl` apa yang digunakan agar suatu *service* (misal: *web server*) bisa menyala otomatis saat komputer baru saja di-restart?
**Answer:** systemctl enable (atau `enable`).

### Q5
**Type:** Short Answer
**Question:** Tombol apa yang harus ditekan di *keyboard* untuk keluar dari pantauan perintah `top` dan kembali ke *prompt* terminal biasa?
**Answer:** Huruf q (berarti *Quit*).
