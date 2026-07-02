---
type: quiz
week: 18
day: 5
title: "Quiz: Lab Full Pentest Machine"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengkaji arsitektur eksploitasi peretasan percobaan *Burp Suite* secara utuh merangkai arsitektur rantai *End-to-End*, apa urutan taktik yang paling dianut penganalisis demi membantai membobol rute otentikasi *Login* bermodalkan tebakan arsitektur payload ribuan sandi bocor?
- [x] A. Menyalakan arsitektur tangkapan *Intercept is On* di tab *Proxy*; mencegat hantaran bodi kueri *Login POST*; melemparnya merasuk ke arsitektur wewenang tab *Send to Intruder*; melingkari titik sasaran `§sandi§`; memuat daftar *Payloads* ratusan kata ; lantas menekan operasi serangan tembak *Start Attack*.
- [ ] B. Menyuruh *Repeater* menebak 65ribu *Port Nmap*.
- [ ] C. Mematikan *Proxy* lantas menggunakan *Extender* mengirimkan *SQLMap* orisinal.
- [ ] D. *Autorize* diutus meraba *XSS* di jendela *Wappalyzer*.

### Q2
**Type:** True/False
**Question:** Ketika meluncurkan serangan eksploitasi manual <i>Repeater</i> di rahim <i>Burp Suite</i>, peretas niscaya sanggup arsitektur mencicipi injeksi `' OR 1=1 --` tanpa pernah mengklik ulang tombol laman arsitektur <i>Submit</i> HTML di Browser peramban korbannya.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Di medan manipulasi, fitur sandi apa di *Burp Proxy* yang menampung catatan rekam jejak riwayat seluruh pertukaran lalu-lintas komunikasi *HTTP* (mirip fungsi *Logger++*) yang singgah teraba di peramban ?
**Answer:** HTTP History.

### Q4
**Type:** Short Answer
**Question:** Ketika peretas merajut naskah payload laporan pengujian manual lab *Juice Shop / DVWA*, tangkapan layar visual *Burp Suite* apa yang disertakan laksana barang bukti (Proof of Concept) eksekusi ?
**Answer:** Tangkapan layar tab *Repeater* atau *Intruder* (yang memamerkan *Request injeksi* bersanding dengan *Response* sukses).

### Q5
**Type:** Short Answer
**Question:** Pada pengoperasian siluman manipulasi *Autorize*, kelalaian fatal arsitektur Wewenang Hak Akses apakah (yang dikupas di materi hari ke-3) yang terbukti mujarab dilacak dieksploitasi oleh ekstensi BApp Store Autorize tersebut?
**Answer:** IDOR (Insecure Direct Object Reference / Broken Access Control).
