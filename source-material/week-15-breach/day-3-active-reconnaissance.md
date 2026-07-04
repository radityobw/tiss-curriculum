# 💀 Week 15 · Day 3: Active Reconnaissance

> **Rank**: BREACH | **Minggu ke-15**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 15 · Day 3/5 | BREACH Rank (Minggu 1 dari 5) | Overall: 73/120 hari (61%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** transisi dan risiko dari tahapan *Active Reconnaissance* (Pengintaian Aktif).
2. **Memindai** port dan layanan server target menggunakan *tools Nmap*.
3. **Mencari** *file* dan direktori web tersembunyi menggunakan teknik *Directory Bruteforcing/Fuzzing*.

---

## 📖 Materi Inti

### Interaksi Langsung (Active Reconnaissance)

Jika *Passive Recon* ibarat mengumpulkan informasi seseorang dari media sosial secara diam-diam, maka **Active Reconnaissance (Pengintaian Aktif)** adalah proses berinteraksi langsung dengan sistem target (mengirim paket data ke server mereka).

Tindakan ini **sangat bising dan mudah terdeteksi**. Sistem keamanan target (seperti *Firewall* atau *Intrusion Detection System / IDS*) akan mencatat lalu lintas IP kamu di dalam *log* mereka dan dapat memblokir koneksi jika mendeteksi aktivitas mencurigakan. Oleh karena itu, *Active Recon* wajib dilakukan hanya jika kamu sudah memiliki izin tertulis (*Rules of Engagement*).

### Pemindai Jaringan: Nmap

*Nmap (Network Mapper)* adalah *tool* esensial bagi setiap *Red Team* atau *Pentester*.
Nmap bekerja dengan mengirimkan paket khusus ke target untuk mengecek status dari 65.535 *Port* yang ada. Tujuannya adalah mencari tahu port mana yang terbuka (*Open*) dan aplikasi atau layanan apa yang berjalan di baliknya (seperti *web server* Apache di port 80, atau SSH di port 22).

```bash
# Pemindaian standar (Mengecek 1000 port paling umum)
nmap target.com

# Memindai port, sekaligus mendeteksi versi layanan (Service Version) dan OS
nmap -sV -O target.com
```

### Meraba Direktori Tersembunyi: Directory Bruteforcing

Sebuah *website* sering kali memiliki direktori atau halaman yang tidak ditautkan ke halaman utama (misalnya `/admin`, `/backup`, atau `/api/v2`). Karena tidak ada *link* yang menuju ke sana, *Google Dorking* biasanya tidak bisa menemukannya.

Cara menemukan halaman ini adalah dengan menebaknya secara paksa dan cepat (*bruteforcing/fuzzing*) menggunakan sebuah kamus kata (*Wordlist*). *Tools* yang umum digunakan adalah **Gobuster** atau **ffuf**.

```bash
# Mencari direktori tersembunyi menggunakan ffuf
ffuf -w kamus_direktori.txt -u https://target.com/FUZZ
```
*Tool* ini akan mengganti kata `FUZZ` dengan setiap kata yang ada di dalam *wordlist* secara bergantian (misal: `target.com/admin`, `target.com/test`, `target.com/backup`). Jika server merespons dengan status `HTTP 200 OK`, berarti halaman atau direktori tersebut benar-benar ada!

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari mempraktikkan penggunaan *Nmap* secara legal (direkomendasikan menggunakan terminal Linux atau WSL).

1. Buka terminal.
2. Pembuat Nmap telah menyediakan server khusus yang legal untuk diserang dan dipindai: `scanme.nmap.org`. **Jangan pernah memindai domain orang lain tanpa izin!** Kita akan menggunakan server ini.
3. Jalankan pemindaian untuk mendeteksi versi layanan:
```bash
nmap -sV scanme.nmap.org
```
4. Tunggu proses *scanning* selesai.
5. Periksa hasilnya. Kamu akan melihat daftar port yang terbuka (seperti port 80 untuk HTTP atau 22 untuk SSH) beserta versi *software* yang berjalan di sana (misalnya *OpenSSH* atau *Apache*). Data inilah yang dicari oleh *pentester* untuk merencanakan langkah eksploitasi selanjutnya!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa <i>Active Reconnaissance</i> dianggap berisiko tinggi dan mudah terdeteksi dibandingkan <i>Passive Reconnaissance</i>?</summary>

**Jawaban:** Karena *Active Recon* berinteraksi langsung (mengirim paket data) ke server target. Interaksi langsung ini akan dicatat oleh log sistem keamanan target (seperti Firewall/IDS) beserta alamat IP si penguji.
</details>

<details>
<summary>❓ <i>Tool</i> apa yang paling populer digunakan oleh peretas/auditor keamanan untuk memindai status port yang terbuka dan layanan apa yang berjalan di baliknya?</summary>

**Jawaban:** Nmap (Network Mapper).
</details>

<details>
<summary>❓ Teknik apa yang digunakan untuk menemukan direktori atau <i>file</i> rahasia di dalam website (misalnya `/admin-backup`) menggunakan daftar kata/tebakan (<i>wordlist</i>)?</summary>

**Jawaban:** Directory Bruteforcing (atau Fuzzing).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami batasan hukum dan risiko deteksi saat melakukan *Active Recon*.
- [ ] Saya tahu fungsi dari alat pemindai jaringan (seperti *Nmap*).
- [ ] Saya mengerti konsep pencarian direktori tersembunyi menggunakan teknik *Directory Bruteforcing* dengan alat bantu seperti *ffuf*.
- [ ] Saya telah mencoba menjalankan *Nmap* secara legal pada domain `scanme.nmap.org` di *Mini Lab*.
- [ ] Saya telah menyelesaikan dan memahami jawaban dari *Quiz Kilat*.

---

## 🔗 Resources

- [Nmap Official Guide](https://nmap.org/book/man.html) — Panduan resmi untuk mempelajari seluruh perintah Nmap.
- [Ffuf - Fast Web Fuzzer](https://github.com/ffuf/ffuf) — Repositori *tool directory fuzzing* populer yang cepat dan efisien.

---

## ➡️ Besok

**Day 4: Subdomain & Technology Fingerprinting** — Bermodalkan port yang terbuka dari Nmap, kita akan menggali lebih dalam! Besok, kita akan belajar cara mencari *Subdomain* tersembunyi (seperti `dev.target.com` atau `staging.target.com`) menggunakan alat seperti *Amass* atau *Sublist3r*. Setelah menemukan domain-domain ini, kita akan melakukan "identifikasi teknologi" (*Technology Fingerprinting*) menggunakan alat seperti *Wappalyzer* dan *WhatWeb* untuk melihat tumpukan teknologi apa saja (seperti versi PHP, *framework* JS, *web server*) yang menyusun aplikasi tersebut.

---

*📅 TISS Null Teaming · Week 15 · Day 3 · BREACH Rank*
