---
type: quiz
week: 18
day: 1
title: "Quiz: Burp Suite Proxy & Intercept"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Apa definisi paling akurat mengenai cara kerja *Burp Suite Proxy* jika dibandingkan dengan koneksi peramban web normal?
- [ ] A. *Burp Proxy* ditugaskan mempercepat arus pengiriman payload dari browser hingga 10x lebih cepat untuk menembus Firewall.
- [x] B. *Burp Proxy* memosisikan dirinya sebagai agen perantara tepat di tengah rute komunikasi antara Browser Klien dan Server Target (*Man-in-the-Middle*). Alat ini mampu mencegat (*Intercept*), menahan lalu-lintas, lalu memberikan wewenang pada pentester untuk merombak dan memanipulasi *Request* sebelum paket tersebut dikirim ke Server.
- [ ] C. *Proxy* menonaktifkan fungsionalitas rendering HTML pada browser klien.
- [ ] D. *Burp Proxy* tidak memanipulasi paket *Request*, melainkan hanya mengekstrak isi *Database SQL*.

### Q2
**Type:** True/False
**Question:** Ketika pentester mencegat (*Intercept*) lalu-lintas komunikasi menggunakan *Burp Suite Proxy*, segala bentuk validasi pengamanan di *Frontend* (seperti batasan `maxlength` di HTML atau validasi *JavaScript*) seketika menjadi lumpuh. Hal ini karena pentester dapat merubah nilai payload paket tersebut tepat setelah paket meninggalkan pengawasan browser.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Di antarmuka *Burp Proxy*, apa nama tombol yang harus ditekan agar paket *Request* yang sedang dicegat/ditahan dapat dilepas untuk meneruskan perjalanannya ke *Server Target*?
**Answer:** Forward.

### Q4
**Type:** Short Answer
**Question:** Ketika seorang pentester menyadari bahwa browsernya terus-menerus *loading* tanpa henti dan macet, status tombol apa di *Burp Proxy* yang dipastikan sedang menyala sehingga menyumbat arus paket komunikasi?
**Answer:** Intercept is on.

### Q5
**Type:** Short Answer
**Question:** Di dalam *Header HTTP* yang ditangkap oleh Burp, baris identitas manakah yang aslinya bertugas memberitahu server tentang identitas/merek browser pengguna (contoh: `Mozilla/5.0...`), namun seringkali diubah oleh peretas untuk menyamarkan jejaknya?
**Answer:** User-Agent.
