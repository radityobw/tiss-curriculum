---
type: quiz
week: 22
day: 5
title: "Quiz: Lab Setup SIEM & Detection Rules"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa peran *Detection Engineer* di dalam SOC dianggap memiliki tanggung jawab dan kualifikasi yang lebih tinggi?
- [x] A. Karena *Detection Engineer* tidak hanya memantau dasbor peringatan, melainkan proaktif merancang aturan jebakan keamanan (*Rules*). Mereka mampu membuat kueri deteksi di *SIEM Splunk* untuk visibilitas, lalu mengintegrasikannya dengan aturan pencegahan (pemblokiran) di *IPS Suricata* untuk menggagalkan serangan secara otomatis.
- [ ] B. Karena spesialis SIEM dilarang menyentuh pengaturan konfigurasi pemblokiran pada *IPS*.
- [ ] C. Karena lisensi *Splunk* mengharuskan pengguna memililki sertifikat penanganan *Ransomware*.
- [ ] D. Karena mereka mengabaikan sistem SIEM dan memilih membaca log menggunakan perintah manual `awk` di terminal.

### Q2
**Type:** True/False
**Question:** Pada analisis kueri di Splunk, seorang Analis dapat mencari *EventCode 4625* dikombinasikan dengan *Logon_Type 10*, lalu menambahkan perintah `| stats count by src_ip` untuk memvalidasi indikasi serangan *Brute Force* (Tebak Sandi) pada koneksi *Remote Desktop* (RDP).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Saat mengeksekusi bahasa kueri *SPL* Splunk, penambahan perintah `| table _time, src_ip, uri` di akhir kueri berfungsi untuk mengubah tampilan data teks menjadi bentuk apa?
**Answer:** Menjadi bentuk Tabel yang rapi (hanya berisi kolom *Timestamp* Waktu, IP Penyerang, dan rute URL).

### Q4
**Type:** Short Answer
**Question:** Saat merancang aturan pencegahan intrusi pada *IPS Suricata/Snort*, instruksi apa yang wajib ditulis di awal baris aturan (*Rule Action*) jika Analis bermaksud langsung memblokir/menggugurkan paket serangan?
**Answer:** `drop` (Bukan sekadar `alert` yang hanya memicu peringatan pasif).

### Q5
**Type:** Short Answer
**Question:** Pada kueri Splunk, jika ditambahkan perintah kondisi matematika seperti `| where count > 20`, parameter penentuan batas ini (yang sering digunakan untuk memicu peringatan otomatis jika dilampaui) disebut sebagai kondisi apa?
**Answer:** Trigger Condition (atau Threshold / Ambang Batas).
