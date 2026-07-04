# 💀 Week 15 · Day 5: Lab & Weekly Mission Full Recon Report

> **Rank**: BREACH | **Minggu ke-15**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓░░░░░░░░] 20% — BREACH Rank (Minggu 1 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░] 62% — Hari 75 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → 🔄 BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Rangkaian keterampilan komprehensif terkait pengumpulan intelijen (*Reconnaissance*) telah berhasil kamu pelajari minggu ini:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Pentest Methodology | Memahami 5 fase standar *Pentesting* (PTES) dan panduan OWASP WSTG. |
| Day 2 | Passive Reconnaissance | Mengumpulkan informasi tanpa menyentuh server target (*OSINT, WHOIS, Google Dorking, Shodan*). |
| Day 3 | Active Reconnaissance | Melakukan *port scanning* menggunakan `Nmap` dan mencari direktori tersembunyi menggunakan `ffuf` / `Gobuster`. |
| Day 4 | Fingerprinting | Mencari *Subdomain* tersembunyi dan mengidentifikasi teknologi di balik sebuah *website* menggunakan `Wappalyzer`. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Sistem operasi Linux (Kali Linux, Ubuntu, atau WSL).
- Koneksi VPN yang stabil ke platform *TryHackMe*.
- Instalasi alat: `nmap`, `ffuf` (atau `gobuster`), dan ekstensi `Wappalyzer`.

### Misi Hari Ini: "Siklus Pengintaian Utuh (Full Recon Cycle)"

Pada sesi praktikum ini, kamu akan mempraktikkan seluruh siklus *Reconnaissance* untuk memetakan kerentanan infrastruktur target. Data yang kamu kumpulkan hari ini akan menjadi modal untuk eksploitasi di minggu berikutnya. **Dilarang keras melakukan eksploitasi sistem (belum saatnya!).**

### Step 1: Inisiasi Lab (TryHackMe)

1. Akses platform [TryHackMe](https://tryhackme.com/) dan pastikan koneksi OpenVPN kamu sudah aktif.
2. Cari ruangan (*room*) simulasi gratis yang fokus pada eksplorasi web, misalnya **"RootMe"** atau **"Basic Pentesting"**.
3. Klik tombol *Start Machine* dan catat Alamat IP target yang diberikan (misalnya `10.10.x.x`).

### Step 2: Pemindaian Aktif (Nmap)

1. Buka terminal di sistem Linux kamu.
2. Jalankan pemindaian port menggunakan Nmap untuk melihat layanan apa saja yang terbuka:
 ```bash
 nmap -sC -sV -oN hasil_scan.txt 10.10.x.x
 ```
 *(Penjelasan parameter: `-sC` menjalankan skrip default Nmap untuk mencari info tambahan, `-sV` mendeteksi versi layanan/aplikasi yang berjalan, dan `-oN hasil_scan.txt` akan menyimpan hasil pemindaian ke dalam sebuah file).*

### Step 3: Identifikasi Teknologi (Wappalyzer)

1. Jika hasil Nmap menunjukkan bahwa port HTTP (80) terbuka, segera buka *browser* dan kunjungi alamat `http://10.10.x.x`.
2. Klik ekstensi `Wappalyzer` di *browser* kamu.
3. Catat teknologi apa saja yang digunakan server tersebut. Apakah menggunakan *Apache*? *PHP* versi berapa? Apakah ada CMS seperti *WordPress*?

### Step 4: Mencari Direktori Tersembunyi (Directory Fuzzing)

1. Halaman utama sering kali tidak menampilkan letak halaman sensitif (seperti panel admin). Gunakan `ffuf` atau `gobuster` untuk menebak direktori tersembunyi:
 ```bash
 # Menggunakan ffuf:
 ffuf -w /usr/share/wordlists/dirb/common.txt -u http://10.10.x.x/FUZZ

 # Menggunakan gobuster:
 gobuster dir -u http://10.10.x.x -w /usr/share/wordlists/dirb/common.txt
 ```
2. Perhatikan hasilnya. Jika kamu mendapatkan respons dengan status `HTTP 200` atau `301` untuk halaman seperti `/admin`, `/panel`, atau `/uploads`, catat temuan tersebut.

---

## 🎯 Weekly Mission

### Misi: "Menyusun Reconnaissance Report"

**Deskripsi:** Kemampuan yang sangat dihargai dari seorang *Pentester* profesional atau *Bug Bounty Hunter* bukanlah sekadar bisa meretas, melainkan kemampuannya dalam membuat pelaporan (*Reporting*) yang jelas, objektif, dan terstruktur. Jangan biarkan semua data yang kamu kumpulkan hari ini hilang begitu saja.

**Tugas Mandiri:** Kumpulkan seluruh hasil pemindaian *Nmap*, identifikasi teknologi dari *Wappalyzer*, dan daftar direktori tersembunyi dari *ffuf* ke dalam satu laporan tertulis.

**Deliverables:**
1. Buat dokumen *Markdown* bernama `RECON_REPORT_THM.md`.
2. Dokumen laporan harus mencakup poin-poin berikut:
 - **Target IP** (IP dari mesin TryHackMe).
 - **Open Ports & Services** (Hasil dan versi layanan dari Nmap).
 - **Web Technology Stack** (Hasil deteksi Wappalyzer).
 - **Hidden Directories Found** (Daftar direktori tersembunyi dari ffuf/Gobuster).
 - **Kesimpulan & Rekomendasi:** "Berdasarkan port dan layanan yang terbuka, celah mana yang paling menarik untuk dieksploitasi pada tahap berikutnya?"

**Kriteria Sukses:**
- [ ] Berhasil menjalankan pemindaian *Nmap* secara menyeluruh dan menyimpan hasilnya dalam file.
- [ ] Menemukan direktori tersembunyi menggunakan *Gobuster* atau *ffuf*.
- [ ] Membuat dokumen pelaporan (*Markdown*) yang rapi dan terstruktur.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Mengingat <i>Active Reconnaissance</i> sangat bising dan mudah terdeteksi, dokumen apa yang wajib disetujui dan ditandatangani sebelum <i>Pentester</i> diizinkan melakukan pemindaian (seperti menggunakan Nmap)?</summary>

**Jawaban:** Rules of Engagement (RoE) / Kontrak persetujuan resmi.
</details>

<details>
<summary>❓ [MUDAH] Dari 5 fase <i>Pentesting</i>, fase manakah yang berfokus pada penyusunan dokumen hasil temuan dan rekomendasi perbaikan untuk pihak perusahaan?</summary>

**Jawaban:** Fase kelima, yaitu *Post-Exploitation & Reporting*.
</details>

<details>
<summary>❓ [SEDANG] Apa fungsi dari parameter (<i>flag</i>) `-sV` pada saat menjalankan perintah Nmap?</summary>

**Jawaban:** Untuk mendeteksi *Service Version* (Mencari tahu nama dan versi spesifik dari aplikasi/layanan yang berjalan di port tersebut, misal: Apache 2.4.29).
</details>

<details>
<summary>❓ [SEDANG] Pada <i>Google Dorking</i>, operator apa yang digunakan jika kita hanya ingin mencari file dengan ekstensi PDF?</summary>

**Jawaban:** `filetype:pdf`
</details>

<details>
<summary>❓ [SULIT] Bagaimana penggunaan alat <i>Directory Fuzzing (ffuf/Gobuster)</i> dan <i>Technology Fingerprinting (Wappalyzer)</i> saling melengkapi untuk membantu peretas menemukan celah secara presisi?</summary>

**Jawaban:** Alat *Fuzzing* (seperti ffuf) membantu menemukan halaman rahasia (seperti `/admin`) yang disembunyikan. Namun, hanya menemukan halaman tersebut belum cukup untuk melakukan serangan. Dengan menggunakan *Wappalyzer* pada halaman `/admin` yang baru ditemukan, peretas dapat mengetahui *software* atau CMS versi berapa yang berjalan di sana (misalnya WordPress versi 4.0.0). Berbekal informasi direktori dan versi CMS tersebut, peretas bisa langsung mencari *Exploit* spesifik untuk versi itu, tanpa harus repot menebak-nebak (trial and error) kerentanan apa yang mungkin ada.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami 5 fase metodologi *Pentesting* (PTES).
- [ ] Saya bisa melakukan pengintaian pasif menggunakan *Google Dorking*.
- [ ] Saya bisa menjalankan *port scanning* menggunakan *Nmap*.
- [ ] Saya bisa mencari direktori tersembunyi menggunakan *ffuf/Gobuster*.
- [ ] Saya telah menyusun laporan pengintaian (`RECON_REPORT_THM.md`) di sesi *Weekly Mission*.

---

## 💬 Diskusi Minggu Ini

Setelah mempelajari *Passive Reconnaissance* dan menyadari betapa mudahnya mencari informasi melalui *OSINT* dan *Google Dorking*, apakah kamu khawatir ada data pribadimu (atau data dari aplikasimu) yang secara tidak sengaja terindeks dan terekspos di internet publik?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│     🎖️ THE SILENT OBSERVER          │
│       Week 15 Complete              │
│     "To conquer a fortress,         │
│   first you map every stone."       │
│                                     │
└─────────────────────────────────────┘
```

Selamat! Kamu telah menguasai keseluruhan fase pengumpulan intelijen (*Reconnaissance*)!

---

## ➡️ Preview Minggu Depan

**Minggu 16: Web Exploitation — Injection Attacks**

Waktu untuk mengintai telah usai! Semua data dari Nmap, Wappalyzer, dan Ffuf yang kamu kumpulkan minggu ini akan menjadi "senjata" utamamu. Minggu depan adalah **Minggu Serangan (Web Exploitation)**. Kita akan langsung membongkar aplikasi web melalui serangan injeksi (*SQL Injection*). Kamu akan belajar tentang *UNION-based & Blind SQLi*, menggunakan *tool* otomasi industri bernama **SQLMap**, dan meretas form *login* tanpa perlu menebak kata sandi (*Authentication Bypass*)!

> 🚀 *"The reconnaissance is over. The breach begins."*

---

*📅 TISS Null Teaming · Week 15 · Day 5 · BREACH Rank*
