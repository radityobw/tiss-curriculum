---
type: quiz
week: 20
day: 5
title: "Quiz: Lab Analisis Access Logs"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Menakar arsitektur penanganan insiden di skenario <i>SQLi Bypass</i>, apa alasan yang menuntut tim SOC harus menggelar fase <i>Lessons Learned</i> sesudah berhasil menyingkirkan penyerang?
- [x] A. Tahap <i>Eradication</i> memang menyingkirkan penyerang saat ini, namun jika tim tidak menggelar fase <i>Lessons Learned</i>, korporasi takkan menemukan akar penyebab struktural (<i>Root Cause</i>), seperti mengapa prosedur pemrograman di perusahaan masih mentolerir pembuatan kode <i>Backend</i> yang rentan SQLi. Evaluasi ini mematangkan pelatihan edukasi arsitek korporasi.
- [ ] B. *Lessons Learned* diwajibkan demi menggunakan *SQLMap* di fase *Recovery*.
- [ ] C. Karena fase ini membuahkan skor *CVSS 9.8*.
- [ ] D. Untuk memblokir penyerang secara otomatis di *Burp Suite*.

### Q2
**Type:** True/False
**Question:** Pada pengujian analisa <i>Web Server Access Log</i>, bila seorang penganalisis menemukan deretan percobaan serangan <i>Brute Force</i> login (ditandai dengan respons <i>401 Unauthorized</i> berulang kali) yang tiba-tiba berubah menjadi satu respons <i>200 OK</i>, itu adalah pertanda bahwa akun korban sukses dibobol (<i>Security Incident</i>).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Ketika meluncurkan analisis log, apa klasifikasi dari Triase (<i>Triage</i>) ketika sebuah sistem sensor diam membisu tanpa membunyikan <i>Alert</i> sama sekali, padahal server korporasi tengah dibobol penyerang?
**Answer:** False Negative.

### Q4
**Type:** Short Answer
**Question:** Ketika tim keamanan menyusun dokumen pedoman krisis (<i>Incident Report/SOP</i>), arahan "Blokir segera IP penyerang di <i>Firewall</i> agar ia tak masuk lagi ke jaringan ", digolongkan tindakan siklus fase PICERL yang mana?
**Answer:** Containment (Penahanan).

### Q5
**Type:** Short Answer
**Question:** Di pembacaan log <i>Apache/Nginx</i>, baris log merekam `GET /admin/dashboard.php HTTP/1.1`. Bagian `GET` ini menunjuk pada metode komunikasi peramban jenis apa?
**Answer:** HTTP Method (atau Request Method).
