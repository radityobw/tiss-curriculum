---
type: quiz
week: 20
day: 5
title: "Quiz: Lab Analisis Access Logs"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengapa tim keamanan (SOC) wajib menyelenggarakan fase *Lessons Learned* setelah insiden berhasil ditangani dan penyerang telah disingkirkan?
- [x] A. Meskipun tahap *Eradication* telah menyingkirkan penyerang, tanpa fase *Lessons Learned* organisasi tidak akan mendiskusikan akar masalah (*Root Cause*), seperti mengapa tim pengembang masih menulis kode *Backend* yang rentan *SQLi*. Evaluasi ini krusial untuk memperbaiki kebijakan dan prosedur di masa depan.
- [ ] B. Karena fase *Lessons Learned* diwajibkan sebagai syarat penggunaan *SQLMap* di fase *Recovery*.
- [ ] C. Karena fase ini secara otomatis menghasilkan skor ancaman *CVSS 9.8*.
- [ ] D. Untuk memblokir penyerang secara otomatis di dalam aplikasi *Burp Suite*.

### Q2
**Type:** True/False
**Question:** Dalam analisis *Web Server Access Log*, jika seorang analis mendapati deretan rekaman percobaan *login* yang gagal (status *HTTP 401 Unauthorized*) dan tiba-tiba diikuti oleh rekaman dengan status *HTTP 200 OK* pada alamat IP dan *endpoint* yang sama, maka ini adalah indikasi kuat bahwa akun telah berhasil dibobol (terjadi *Security Incident*).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Dalam klasifikasi Triase (*Triage*), apa sebutan untuk kegagalan sistem sensor keamanan yang tidak mendeteksi dan tidak memberikan peringatan (*alert*) sama sekali saat jaringan perusahaan benar-benar sedang disusupi oleh penyerang?
**Answer:** False Negative.

### Q4
**Type:** Short Answer
**Question:** Saat menyusun dokumen penanganan insiden (*Incident Report*), arahan untuk "Memblokir segera alamat IP penyerang di *Firewall* untuk memutus aksesnya ke jaringan" diklasifikasikan ke dalam tahapan PICERL yang mana?
**Answer:** Containment (Penahanan / Isolasi).

### Q5
**Type:** Short Answer
**Question:** Pada format penulisan log *Apache/Nginx*, rekaman log sering diawali dengan blok spesifik seperti `GET /admin/dashboard.php HTTP/1.1`. Kata `GET` pada blok tersebut merujuk pada parameter komunikasi web apa?
**Answer:** HTTP Method (atau Request Method).
