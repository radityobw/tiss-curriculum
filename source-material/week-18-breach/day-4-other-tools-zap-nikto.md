# 💀 Week 18 · Day 4: Other Tools (ZAP, ffuf, nikto)

> **Rank**: BREACH | **Minggu ke-18**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 18 · Day 4/5 | BREACH Rank (Minggu 4 dari 5) | Overall: 89/120 hari (74%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan kamu mampu:

1. **Memahami** alat alternatif *Open Source* di luar *Burp Suite*.
2. **Mengoperasikan** mesin pemindai otomatis web *OWASP ZAP*.
3. **Mengeksploitasi** pemindai konfigurasi *Nikto* dan alat *Fuzzing* kecepatan tinggi *ffuf*.

---

## 📖 Materi Inti

### Alternatif Pengujian Open Source

*Burp Suite* memang menjadi andalan utama bagi pentester web. Namun, lisensi *Scanner* profesionalnya yang cukup mahal (belasan juta rupiah) terkadang menjadi rintangan bagi pemula.
Sebagai seorang *Bug Hunter*, kamu dituntut untuk fleksibel. Dunia *Open Source* menyediakan berbagai perkakas alternatif yang tak kalah mumpuni dan sepenuhnya gratis!

### 1. OWASP ZAP (Zed Attack Proxy)

Ini adalah kompetitor utama *Burp Scanner*!
**ZAP** adalah *Scanner & Proxy* sumber terbuka (100% Gratis) yang dikembangkan oleh *OWASP*.
Seluruh fungsionalitas pemindai otomatis (*Automated Vulnerability Scanner*) yang dikunci pada *Burp Community Edition*, tersedia secara gratis di *ZAP*!
Kamu cukup memasukkan *URL* target, menekan tombol *Attack*, dan *ZAP* akan secara otomatis mengirimkan ribuan kueri *SQLi*, *XSS*, dan kerentanan lainnya, lalu menghasilkan laporan lengkap (*Automated Scan*).

*Mengapa tidak semua orang menggunakan ZAP?* Karena meskipun fitur otomatisasinya kuat, tata letak antarmuka (*UI/UX*) dan fitur manual *ZAP* terkesan lebih kaku dan kurang seintuitif *Repeater* milik *Burp*. (*Pro-tip: Kombinasikan ZAP untuk Scan Otomatis, lalu lakukan eksploitasi manual di Burp!*).

### 2. Nikto: Mesin Pemindai Konfigurasi Server

Jika *ZAP* fokus mencari celah aplikasi, **Nikto** adalah pemindai berbasis terminal (menggunakan *Perl*) yang sangat handal mendeteksi kelalaian konfigurasi server (*Security Misconfiguration*).
*Nikto* akan memindai *server* (misalnya *Apache* atau *Nginx*) dan melaporkan keberadaan berkas sensitif (seperti `.git` yang terekspos), ketiadaan *Security Headers*, atau penggunaan versi perangkat lunak (seperti *PHP*) yang sudah usang.
**Perintah:** `nikto -h http://target.com` *(Catatan: Pemindaian Nikto sangat bising dan mudah dideteksi oleh Firewall/WAF/IDS!)*.

### 3. Ffuf: Alat Fuzzing Kecepatan Tinggi

Kamu telah menggunakan *ffuf* di materi *Active Recon* untuk mencari direktori (*Directory Brute-forcing*). Namun, **ffuf (Fuzz Faster U Fool)** tidak hanya sebatas pencari direktori tersembunyi!
Ditenagai oleh bahasa *Golang*, *ffuf* adalah salah satu alat tercepat untuk melakukan *Fuzzing* parameter web. Misalnya, jika kamu menemukan parameter `id=1`, *ffuf* dapat menembakkan jutaan *payload* secara bersamaan (misal injeksi *SQL* atau *XSS*) ke parameter tersebut dalam hitungan detik!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Ayo mencoba menjalankan pemindai konfigurasi *Nikto*!

1. Buka Terminal di Kali Linux atau Parrot OS.
2. Pastikan `nikto` terpasang (Biasanya sudah menjadi bawaan instalasi distro keamanan siber).
3. Kita akan menguji server legal *scanme* milik Nmap:
   `nikto -h http://scanme.nmap.org`
4. Perhatikan proses pemindaian yang berjalan di layar terminalmu.
5. Dalam beberapa menit, *Nikto* akan melaporkan berbagai temuan, seperti ketiadaan header *Anti-clickjacking X-Frame-Options*, mendeteksi *Apache/2.4*, dan memberikan peringatan terkait potensi keusangan sistem. (Inilah alat andalan untuk audit miskonfigurasi!).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Aplikasi Proxy dan Scanner buatan komunitas OWASP manakah yang sering digunakan sebagai alternatif gratis dari Burp Suite Professional?</summary>

**Jawaban:** OWASP ZAP (Zed Attack Proxy).
</details>

<details>
<summary>❓ Alat pemindai berbasis CLI manakah yang khusus digunakan untuk mencari kelalaian konfigurasi server (Security Misconfigurations) seperti software usang dan ketiadaan header keamanan?</summary>

**Jawaban:** Nikto.
</details>

<details>
<summary>❓ Alat fuzzing berbasis Golang manakah yang terkenal dengan kecepatannya dalam melontarkan ribuan payload Brute-Force ke parameter web atau direktori?</summary>

**Jawaban:** Ffuf (Fuzz Faster U Fool).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami fitur utama *OWASP ZAP* sebagai alternatif *Scanner*.
- [ ] Saya mengerti cara mengkombinasikan *ZAP* untuk pindai otomatis dan *Burp* untuk pengujian manual.
- [ ] Saya bisa menjalankan perintah dasar pemindaian menggunakan *Nikto*.
- [ ] Saya mengetahui fungsi dan kecepatan alat *Fuzzing* *ffuf*.
- [ ] Saya telah menjawab seluruh *Quiz Kilat* dengan benar.

---

## 🔗 Resources

- [OWASP ZAP Official](https://www.zaproxy.org/) — Situs resmi untuk mengunduh OWASP ZAP.

---

## ➡️ Besok

**Day 5: Lab & Mission: Full Pentest Machine** — Empat hari mempelajari berbagai perkakas peretasan telah kamu lalui. Besok, tibalah ujian akhir di kasta *BREACH*! Kamu akan menanggalkan teori dan langsung mempraktikkan pengujian penetrasi *End-to-End* pada mesin uji *TryHackMe*. Gunakan kombinasi *Proxy, Repeater*, dan *Intruder* untuk menganalisis dan menembus kerentanan web secara nyata!

---

*📅 TISS Null Teaming · Week 18 · Day 4 · BREACH Rank*
