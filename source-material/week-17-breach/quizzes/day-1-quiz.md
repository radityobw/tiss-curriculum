---
type: quiz
week: 17
day: 1
title: "Quiz: XSS (Payload Crafting & Cookie Stealing)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Mengevaluasi arsitektur peretasan eksekusi arsitektur *Cross-Site Scripting (XSS)*, siasat manipulasi eksploitasi parameter *Payload Crafting* dinobatkan secara empiris lebih mematikan dari sekadar injeksi `alert(1)`. Apakah alasan rasional analitis yang membedah fatalitas bahayanya?
- [ ] A. *Payload Crafting* didesain khusus mengekstrak payload pencatatan isi tabel kueri data *SQL*.
- [x] B. Pada penerapan kasta *Payload Crafting*, penganalisis penyerang sasaran tidak sekadar memancing memunculkan kotak *pop-up* usil di antarmuka peramban pengguna korban, melainkan mengarahkan untuk merakit arsitektur skrip pemrograman *JavaScript* kompleks yang ditugaskan secara spesifik lantas terstruktur demi mengeksekusi misi eksploitatif tingkat mahir seperti merampas *Session Cookie* Admin atau penyadapan ketikan papan ketik peramban korban (*Keylogging*).
- [ ] C. Konfigurasi *Payload* tersebut mengizinkan agen penyerang untuk meledakkan simulasi eksekusi serangan *DDoS* dari peramban.
- [ ] D. Skrip parameter *Payload* secara spesifik ditugaskan meretas sistem deteksi *Wappalyzer* orisinal.

### Q2
**Type:** True/False
**Question:** Ketika spesialis peretas merangkai skrip penyadap sandi tombol *JavaScript* (*XSS Keylogger*), arsitektur manipulasi *JavaScript* macam memanggil *Event Listener* (semisal deklarasi penugasan *Event* `keypress`) mutlak wajib diabsahkan penggunaannya guna arsitektur mendeteksi sekaligus merekam hentakan tuts ketikan korban sasar.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Ketika spesialis penganalisis berniat ekskavasi untuk merampas identitas sandi autentik pengguna sasaran peramban, embel deklarasi objek properti apa pada arsitektur bawaan lingkungan operasi peramban *JavaScript* (dengan struktur nilai sandi berawalan kata `document.`) yang wajib dieksploitasi buat menarik wujud sandi pengikatan tersebut?
**Answer:** document.cookie

### Q4
**Type:** Short Answer
**Question:** Ketika perisai tembok pertahanan instalasi parameter *WAF (Web Application Firewall)* sasaran menolak mutlak lantas mengharamkan pencaplokan mengeksekusi muatan injeksi elemen tag `<script>`, tag elemen HTML pembungkus penyisip payload arsitektur gambar apakah yang kerap diakali penganalisis penyerang laksana inang penyamaran (yang lazimnya dikawinkan dengan parameter sandi `onerror=`)?
**Answer:** <img> (atau deklarasi HTML tag img).

### Q5
**Type:** Short Answer
**Question:** Di penghujung rentetan peretasan simulasi pencurian *Cookie* sasaran peramban, ketika parameter sandi tersebut dikonfirmasi sukses dicekik lantas direnggut oleh rahim ekskavasi instruksional *JavaScript* korban sasaran, ke manakah alamat payload sandi hasil rampokan itu mesti dikirimkan lantas diteruskan (sebagai contoh berbekal penerapan perintah `fetch`) agar kelak bisa dikumpulkan lantas dinikmati oleh penganalisis penyerang ?
**Answer:** Dikirimkan (di-POST/di-GET) ke alamat instalasi peladen penadah eksternal spesifik (seperti Server milik Penganalisis/Hacker atau arsitektur pencatatan Webhook sasaran Hacker).
