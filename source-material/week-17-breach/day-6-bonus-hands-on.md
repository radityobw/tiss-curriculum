# 🎯 Week 17 · Day 6 (Bonus): Hands-On Learning

> **Rank**: BREACH | **Minggu ke-17** | Bonus Day

---

## 🌐 Platform Hari Ini

**[PortSwigger Web Security Academy — Cross-Site Scripting (XSS) Labs](https://portswigger.net/web-security/cross-site-scripting)**
Laboratorium XSS gratis dari PortSwigger dengan berbagai skenario: Reflected, Stored, dan DOM-based XSS. Selaras dengan materi XSS, CSRF, dan chaining minggu ini.

💰 **Biaya**: Gratis (semua lab gratis)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Mengeksploitasi kerentanan XSS di berbagai konteks (HTML, JavaScript, atribut)
2. Memahami perbedaan Reflected, Stored, dan DOM-based XSS secara praktis
3. Menulis payload XSS yang efektif dan mendokumentasikannya

---

## 📋 Requirement

* Akun PortSwigger (sudah dibuat di Week 16 Day 6)
* Peramban web modern (Chrome/Firefox)

---

## 📝 Prosedur

### Langkah 1: Akses Lab XSS
1. Login ke [PortSwigger Web Security Academy](https://portswigger.net/web-security)
2. ke **Cross-site scripting** → klik **View all labs**
3. Mulai dari lab berlabel **APPRENTICE**

### Langkah 2: Lab 1 — Reflected XSS (Termudah)
1. Pilih lab **"Reflected XSS into HTML context with nothing encoded"**
2. Klik **Access the lab**
3. Cari fitur pencarian (*search*) di halaman web
4. Di kolom pencarian, masukkan payload:
 ```html
 <script>alert(1)</script>
 ```
5. Klik search — jika muncul popup alert, lab solved! ✅

> 💡 **Mengapa ini bekerja**: Input dari kolom pencarian langsung di-render ke dalam HTML tanpa sanitasi. Browser mengeksekusi tag `<script>` sebagai kode JavaScript.

### Langkah 3: Lab 2 — Stored XSS
1. Pilih lab **"Stored XSS into HTML context with nothing encoded"**
2. Klik **Access the lab**
3. Buka salah satu blog post
4. Di bagian komentar, isi:
 - Nama: `tester`
 - Email: `test@test.com`
 - Website: `http://test.com`
 - Komentar: `<script>alert(1)</script>`
5. Submit komentar
6. Kembali ke halaman blog post — jika alert muncul, lab solved! ✅

### Langkah 4: Lab 3 — DOM-based XSS
1. Pilih lab **"DOM XSS in document.write sink using source location.search"**
2. Klik **Access the lab**
3. Gunakan fitur pencarian dengan payload:
 ```html
 "><script>alert(1)</script>
 ```
4. Perhatikan: payload perlu *break out* dari konteks HTML terlebih dahulu (`">`) sebelum menyisipkan script

> 💡 **Perbedaan dengan Reflected XSS**: DOM-based XSS terjadi sepenuhnya di sisi klien (JavaScript memanipulasi DOM), bukan di server response.

### Langkah 5: Lab Tambahan — XSS ke Cookie Stealing (Jika Waktu Tersisa)
1. Pilih lab XSS Apprentice lainnya
2. Coba variasi payload:
 ```html
 <img src=x onerror=alert(1)>
 <svg onload=alert(1)>
 <body onload=alert(1)>
 ```
3. Dokumentasikan payload mana yang berhasil di konteks mana

### Langkah 6: Dokumentasi Writeup
Untuk setiap lab, tulis:
```
Lab: [nama lab]
Tipe XSS: [Reflected/Stored/DOM-based]
Payload: [payload yang digunakan]
Konteks injeksi: [HTML body/atribut/JavaScript]
Mengapa berhasil: [penjelasan singkat]
```

---

## 🏁 Target Output

* ✅ Minimal **3 lab XSS** berhasil diselesaikan
* 📝 **Writeup** untuk setiap lab dengan payload dan penjelasan
* 📝 **XSS Cheatsheet**: Daftar 5 payload XSS yang sudah dicoba + konteks penggunaannya
* 📸 Tangkapan layar PortSwigger menunjukkan lab "Solved"

---

## 🔄 Fallback

Jika PortSwigger tidak bisa diakses:
1. Gunakan **DVWA** (jika sudah diinstal dari Week 16):
 ```bash
 docker run -d -p 8080:80 vulnerables/web-dvwa
 ```
2. Login, set security ke **Low**
3. Kerjakan modul **XSS (Reflected)** dan **XSS (Stored)**
4. Dokumentasikan payload dan hasil eksploitasi
