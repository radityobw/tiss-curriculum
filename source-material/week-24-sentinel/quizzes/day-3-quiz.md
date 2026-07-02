---
type: quiz
week: 24
day: 3
title: "Quiz: Eradication & Remediation"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam siklus respons insiden PICERL, mengapa server yang terinfeksi sangat dilarang untuk dihubungkan kembali ke jaringan publik (Fase Recovery) jika tim belum melakukan perbaikan pada *Root Cause* (Akar Penyebab) insiden?
- [x] A. Karena jika server dipulihkan ke jaringan publik (*Online*) sementara akar penyebabnya (misal: celah SQL Injection) belum ditambal (*Patching*), peretas dapat mengeksploitasi celah terbuka tersebut untuk menyusup ulang dalam hitungan menit.
- [ ] B. Karena inisiasi *Recovery* berpotensi selalu menyebabkan arsitektur *hardware* server menjadi korup.
- [ ] C. Karena fase *Recovery* mensyaratkan server harus diformat ulang secara keseluruhan.
- [ ] D. Karena prosedur *Developer* melarang modifikasi antarmuka SIEM *Splunk* setelah insiden.

### Q2
**Type:** True/False
**Question:** Dalam fase *Eradication (Pemusnahan)*, spesialis keamanan diwajibkan untuk menghentikan proses *malware* aktif dari RAM (*Kill Process*), menghapus file *malware* dari *Hard Disk*, dan mewajibkan seluruh pengguna sistem (terutama Admin) untuk mereset kata sandi (*Password Reset*).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat meracik konfigurasi pada *Intrusion Prevention System (IPS)* seperti Suricata, parameter awal apa (berawalan huruf D) yang digunakan untuk memerintahkan sistem agar menggugurkan atau memblokir paket data dari penyerang?
**Answer:** drop (atau aksi `drop`).

### Q4
**Type:** Short Answer
**Question:** Ketika analis merakit aturan pada *IPS Suricata* untuk memblokir IP penyerang agar tidak bisa menyusup kembali, aktivitas mitigasi ini diklasifikasikan ke dalam tahap apa dari siklus PICERL?
**Answer:** Eradication (Pemusnahan/Penghapusan).

### Q5
**Type:** Short Answer
**Question:** Apa istilah teknis yang lazim digunakan untuk mendeskripsikan tindakan perbaikan atau penambalan pada kode aplikasi yang rentan (misalnya menambal celah injeksi SQL) agar aman dari eksploitasi?
**Answer:** Patching (atau Remediation).
