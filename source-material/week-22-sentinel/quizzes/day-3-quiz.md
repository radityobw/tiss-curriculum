---
type: quiz
week: 22
day: 3
title: "Quiz: Splunk Dashboards & Alerts"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa Analis SOC harus menerjemahkan hasil pencarian SPL ke dalam bentuk *Dashboard* (seperti *Pie Chart* atau grafik batang)?
- [x] A. Karena pihak manajemen atau eksekutif (seperti CISO) membutuhkan ringkasan laporan keamanan secara visual yang mudah dan cepat dipahami secara *Real-Time*, tanpa perlu membaca baris kueri log yang kompleks secara teknis.
- [ ] B. Agar eksekusi kueri SPL tersebut tidak menghabiskan terlalu banyak memori (RAM) pada *server*.
- [ ] C. Karena *Dashboards* adalah syarat wajib untuk bisa mengaktifkan *IPS Suricata*.
- [ ] D. Karena dasbor grafis mampu memblokir serangan secara otomatis.

### Q2
**Type:** True/False
**Question:** Fitur *Alert* (Peringatan Otomatis) di Splunk bekerja dengan cara menjalankan kueri SPL secara terjadwal, dan hanya membunyikan alarm/notifikasi jika hasil pencarian tersebut melampaui kondisi *Threshold* (*Trigger Condition*) yang telah ditentukan.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Dalam platform SIEM, istilah apa yang digunakan untuk menyebut kumpulan panel grafik visual yang merangkum hasil kueri SPL secara berkelanjutan dan *Real-Time*?
**Answer:** Dashboards (Dasbor GUI).

### Q4
**Type:** Short Answer
**Question:** Saat membuat peringatan keamanan otomatis di SIEM dan Analis menetapkan aturan: "Aktifkan notifikasi HANYA JIKA jumlah gagal login > 50", istilah teknis apa yang merujuk pada standar batas " > 50 " tersebut?
**Answer:** Trigger Condition (atau Threshold / Ambang Batas).

### Q5
**Type:** Short Answer
**Question:** Dalam konfigurasi *Alert* di Splunk, apa fungsi dari komponen pengaturan *Trigger Action*?
**Answer:** Menentukan tindakan otomatis setelah insiden terdeteksi (Misalnya: mengirim email notifikasi ke tim SOC, atau otomatis membuat tiket insiden).
