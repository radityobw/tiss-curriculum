---
type: quiz
week: 17
day: 2
title: "Quiz: CSRF & SSRF"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di ranah arsitektur rekayasa manipulasi mematikan, tabir diferensiasi apakah yang mencerai batasan arsitektur serangan *Cross-Site Request Forgery (CSRF)* bilamana diadu dan dipersandingkan berhadapan melawan taktik eksploitasi sasaran parameter pelaporan *Server-Side Request Forgery (SSRF)*?
- [ ] A. *CSRF* mengeksekusi ekstraksi `Session Cookie`, sedangkan *SSRF* ditugaskan merekam pelaporan sandi `Keylogger`.
- [x] B. Pada percobaan eksploitasi peramban *CSRF*, korban target dipancing agar peramban (*Browser*)-nya sendirilah yang mengirimkan eksekusi permintaan (*Request*) ke peladen sasaran aplikasi tanpa disadarinya. Sebaliknya, pada taktik eksploitasi parameter operasi *SSRF*, sasaran yang ditipu adalah arsitektur *Server Backend aplikasi target* itu sendiri, dengan memaksa mesin peladen sasaran itu sendiri (bukan browser pengguna korban) guna mengirimkan kueri lantas menyerang masuk server kawanannya yang bersarang secara internal di ranah jaringan infrastruktur lokal.
- [ ] C. *SSRF* didapuk menipu integrasi parameter pelindungan sandi WAF, selagi fungsi *CSRF* cuma menipu ekstensi deteksi *Wappalyzer*.
- [ ] D. Ekskavasi eksploitasi operasi *CSRF* tak bisa menjangkit arsitektur operasi sasaran *SSRF* maupun taktik arsitektur parameter peramban *XSS*.

### Q2
**Type:** True/False
**Question:** Kerentanan penyakit eksploitasi fungsi peramban *CSRF* (Cross-Site Request Forgery) lumrah mewabah di ranah ketika penganalisis arsitek pengembang aplikasi *programmer* lalai membiarkan formulir otentik (semacam form eksekusi modifikasi ganti kata sandi sasar) terbuka polos dirender tanpa dibekali sisipan proteksi validasi sandi acak sekali-pakai (seperti nihil pengerahan perlindungan token spesifik arsitektur *CSRF Token*).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Ketika penganalisis merakit serangan penyusupan formulir eksekusi paksaan parameter sandi arsitektur *CSRF* di situs penadahnya, peretas menyusupkan barisan operasi fungsi *JavaScript* di ekor skrip halaman (semisal pengerahan fungsi `document.forms[0]...`) guna menekan eksekusi tombol pengiriman payload kirim formulirnya secara instan otomatis. Metode pemanggilan fungsi pelaporan arsitektur sandi *JS* spesifik apakah yang ditugaskan tersebut?
**Answer:** submit() (atau deklarasi pengerahan sandi metode fungsi Javascript `submit`).

### Q4
**Type:** Short Answer
**Question:** Di pengujian interogasi arsitektur ekskavasi peramban simulasi eksploitasi pelaporan *SSRF*, rentetan deklarasi sandi serangan kombinasi IP apakah (berawalan fungsi `127.x.x.x`) yang secara kerap dieksploitasi <i>Hacker</i> demi menipu arsitektur peladen sasaran agar melirik mengekskavasi pelaporan arsitektur dasbor internal lokalnya sendiri?
**Answer:** 127.0.0.1 (atau nomenklatur fungsi pelaporan `localhost`).

### Q5
**Type:** Short Answer
**Question:** Bilamana mengarsiteki pelaporan peladen *Cloud* (seperti instalasi layanan *AWS/GCP*) lantas dihantam penetrasi silang simulasi peramban eksploitasi pelaporan *SSRF*, alamat keramat sandi arsitektur fungsi pelaporan sandi IP manakah (berawalan nilai `169`) yang acap dibidik penganalisis *hacker* guna mengekstrak pelaporan fungsi kunci kredensial *Metadata* layanan tersebut?
**Answer:** 169.254.169.254 (sebagai alamat Instance Metadata Service / IMDS standar layanan cloud sasaran).
