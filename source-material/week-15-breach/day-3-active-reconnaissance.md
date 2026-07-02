# 💀 Week 15 · Day 3: Active Reconnaissance

> **Rank**: BREACH | **Minggu ke-15**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 15 · Day 3/5 | BREACH Rank (Minggu 1 dari 5) | Overall: 73/120 hari (61%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** transisi dan risiko operasional dari tahapan Pengintaian Aktif (*Active Recon*).
2. **Memindai** gerbang komunikasi port peladen sasaran menggunakan perkakas *Nmap*.
3. **Membongkar** jalur penempatan direktori web tersembunyi melalui pendekatan *Directory Bruteforcing/Fuzzing*.

---

## 📖 Materi Inti

### Interaksi Langsung (Pengintaian Aktif)

Bila Pengintaian Pasif ibarat mengumpulkan profil seseorang dari arsip publik, maka **Pengintaian Aktif (Active Reconnaissance)** menginisiasi interaksi atau paket koneksi langsung secara terukur ke infrastruktur peladen target.

Tindakan ini **sangat memicu sistem rekam log aktivitas**. Sistem pemantauan keamanan peladen (*Firewall/IDS*) akan mencatat lalu lintas IP Anda dan mengkategorikannya sebagai anomali jaringan. Oleh karena itu, operasional Pengintaian Aktif mutlak dilarang keras untuk dieksekusi tanpa adanya perizinan legalitas kontrak pengujian (*Rules of Engagement / RoE*).

### Perkakas Pemindai Jaringan: Nmap

*Nmap (Network Mapper)* merupakan fundamental dalam analisis keamanan *Red Team*.
*Nmap* memetakan topologi jaringan dengan mengirimkan paket pemindaian ke parameter 65.535 pintu koneksi (*Port*) sasaran demi mendeteksi port yang terbuka (*Open*), serta mengidentifikasi spesifikasi identitas aplikasi layanan (*Service Version*) yang beroperasi di baliknya (misal Apache, MySQL, SSH).

```bash
# Menembak peladen untuk pemindaian umum (Memindai 1000 port prioritas utama)
nmap target.com

# Menginterogasi spesifikasi! (Deteksi versi layanan dan OS sistem target) - Kueri bising!
nmap -sV -O target.com
```

### Merobek Peta Tersembunyi: Directory Bruteforcing

Arsitektur aplikasi web lazimnya menyembunyikan letak direktori sensitif tanpa tautan kasat mata (seperti `/admin-backup` atau `/api/v2`). Karena sifatnya yang murni terputus dari publik situs, maka teknik pelacakan *Google Dorking* niscaya tidak akan mampu menelusurinya.

Spesialis keamanan menyelesaikannya dengan melakukan iterasi pemindaian tebakan (*fuzzing/bruteforcing*) secara masif bermodalkan senarai dokumen kamus tebakan (*Wordlists*) menggunakan seperti **Gobuster** atau **ffuf**.

```bash
# Mengeksekusi tebakan paksa letak direktori peladen memakai ffuf dan wordlist
ffuf -w kamus_direktori.txt -u https://target.com/FUZZ
```
*ffuf* kelak otomatis mengganti parameter kueri kata `FUZZ` berantai secara terus-menerus meniru entri *wordlist*: `target.com/admin`, `target.com/test`, `target.com/backup`. Bilamana peladen memberikan respons kode sandi *HTTP 200 OK*, hal tersebut merepresentasikan direktori valid telah terbongkar.

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari mempraktikkan pemindaian *Nmap* secara legal (pastikan Anda mengoperasikannya di lingkungan terminal OS semisal Kali Linux/Ubuntu WSL).

1. Buka *Terminal* operasional Anda. 
2. Komunitas pengembang Nmap telah menyediakan simulasi peretasan publik berstatus legal bernomenklatur `scanme.nmap.org`. Jangan pernah memindai alamat domain institusi pendidikan atau instansi Anda tanpa mandat tertulis! Kita akan memindai *scanme*!
3. Luncurkan serangan interogasi parameter versi peladen:
```bash
nmap -sV scanme.nmap.org
```
4. Tunggu beberapa detik/menit selagi sistem menelusuri topologi parameter target.
5. Perhatikan laporan yang dihasilkan Nmap. Evaluasi penemuan status keterbukaan port 80 (HTTP) dan port 22 (SSH) yang terpajang terbuka (*Open*) sembari membeberkan merek aplikasi pengawalnya (misal *OpenSSH* atau *Apache* versi spesifik). Laporan inilah peta maut analisis peretas!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah alur operasional pengumpulan intelijen, alasan teknis apakah yang menempatkan eksekusi Pengintaian Aktif (*Active Recon*) sebagai operasi yang bising dan niscaya memicu deteksi pencegat?</summary>

**Jawaban:** Lantaran operasi Pengintaian Aktif (*Active Recon*) mentransmisikan payload pemindaian paket secara langsung menabrak parameter mesin infrastruktur peladen (*Firewall*) sasaran; akibatnya sistem sasaran otomatis mencatat aktivitas interaksi paket IP penyerang pada modul buku log rekam keamanannya.
</details>

<details>
<summary>❓ Perkakas fundamental apakah yang diandalkan selaku pemindaian spesifikasi ribuan gerbang port komunikasi guna mendeteksi status layanan port yang *Open*?</summary>

**Jawaban:** Nmap (Network Mapper).
</details>

<details>
<summary>❓ Metode pendekatan ekskavasi pelacakan apakah yang diadopsi oleh perkakas analisis semacam <i>Gobuster/ffuf</i> guna meraba dan mendeteksi payload letak jalur folder tersembunyi yang absen memiliki referensi publik di antarmuka situs web?</summary>

**Jawaban:** Metode penggempuran tebakan pelacakan iterasi paksa (*Directory Bruteforcing/Fuzzing*) bermodalkan daftar referensi kosa kata tebakan direktori massal (*Wordlists*).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap pengetahuan ihwal batasan legalitas operasional dan risiko bisingnya *Active Recon*
- [ ] Saya fasih meletuskan komando eksekusi *Nmap* (dengan *flag* parameter `-sV`) guna meraba versi aplikasi peladen
- [ ] Saya menguasai mekanisme iterasi pemindaian tebakan pelacak payload direktori *Directory Bruteforcing*
- [ ] Saya sukses menginterogasi server legal *scanme.nmap.org* menggunakan Nmap pada sesi operasional *Mini Lab*
- [ ] Saya telah menyimak tuntas ulasan pelaporan evaluasi *Quiz Kilat*

---

## 🔗 Resources

- [Nmap Official Reference Guide](https://nmap.org/book/man.html) — Dokumen suci referensi teknikal penjabaran seluruh parameter komando *Nmap*.
- [Ffuf - Fast Web Fuzzer](https://github.com/ffuf/ffuf) — Repositori peranti *fuzzer* direktori mutakhir.

---

## ➡️ Besok

**Day 4: Subdomain & Technology Fingerprinting** — Berbekal fungsionalitas Nmap, peta arsitektur peladen mulai direkonstruksi! Esok hari, Anda akan memperluas perburuan parameter permukaan serangan (*Attack Surface*). Kita membongkar hierarki ekstensi *Subdomain* sasaran (seperti *dev.target.com* atau *staging.target.com*) menggunakan keunggulan pelacak ekskavasi *Amass*, lantas membedah rincian adonan arsitektur tumpukan teknologi peladen (*Technology Fingerprinting*) menggunakan *Wappalyzer* dan *WhatWeb*!

---

*📅 TISS Null Teaming · Week 15 · Day 3 · BREACH Rank*
