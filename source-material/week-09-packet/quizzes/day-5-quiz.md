---
type: quiz
week: 9
day: 5
title: "Quiz: Lab Ping Sweeper dan Mission"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam pengerjaan skrip jaringan *Ping Sweeper*, dampak apakah yang akan terjadi apabila pemrogram alfa menyertakan simbol ampersand (`&`) saat memanggil perintah *ping* di dalam kerangka *loop*?
- [ ] A. Perulangan *ping* akan merusak alur perangkat *router* karena kesalahan logika.
- [ ] B. Terminal akan memblokir perintah tersebut dan melabelinya sebagai *DDoS attack*.
- [x] C. Eksekusi program akan berjalan sangat lambat secara sekuensial (skrip menunggu *ping* IP pertama selesai lalu pindah ke IP kedua), tidak berjalan secara sinkron paralel di latar belakang (*background*).
- [ ] D. Daftar target alamat IP dari rentang variabel akan dihapus otomatis dari OS.

### Q2
**Type:** True/False
**Question:** Saat mengetikkan perintah `ping google.com` pada terminal Ubuntu, sistem akan secara otomatis melacak serta mencetak letak fisik geografis atau koordinat pasti lokasi *data center* milik perusahaan Google.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Konsep identifikasi target (taktik pengintaian di jaringan internal) dengan menyebarkan gema ICMP secara merata untuk mendeteksi perangkat aktif (*host discovery*) umumnya disebut dengan istilah operasi serangan dasar apa?
**Answer:** Ping Sweeper (atau Network Sweep).

### Q4
**Type:** Short Answer
**Question:** Berapakah batas angka terjauh rentang inang (*host ID*) normal untuk skala jaringan IPv4 Kelas C (seperti *Subnet* /24) yang umumnya dieksplorasi dalam rotasi target *script For Loop* Misi `1..[Batas Akhir]` pekan ini?
**Answer:** 254.

### Q5
**Type:** Short Answer
**Question:** Parameter opsi khusus (ditulis menggunakan huruf kapital) apa yang umumnya dimasukkan ke dalam perintah `ping` (contoh: `ping -c 1`) agar program membatasi jeda *timeout* saat peladen tidak merespons, sehingga skrip tidak mengalami kemacetan panjang (*hang*)?
**Answer:** `-W 1` (Opsi Wait/Timeout batas toleransi 1 detik).
