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

Rangkaian keterampilan komprehensif terkait teknik pengumpulan intelijen (*Red Team Recon*) telah berhasil Anda kuasai dalam silabus materi minggu ini:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Pentest Methodology | Membedah dan merumuskan kerangka standar 5 fase PTES dan *OWASP WSTG*. |
| Day 2 | Passive Reconnaissance | Mengumpulkan profil target berbasis ketersediaan jejak sumber data terbuka (*OSINT, WHOIS, Google Dorking, Shodan*). |
| Day 3 | Active Reconnaissance | Meluncurkan iterasi deteksi gerbang port sasaran menggunakan `Nmap` dan membongkar penempatan direktori tersembunyi via fungsi pelacak `Gobuster/Ffuf`. |
| Day 4 | Fingerprinting | Mengekskavasi arsitektur turunan *Subdomain* (*Amass/Sublist3r*) dan mengidentifikasi adonan tumpukan teknologi perangkat lunak instalasi peladen (*Wappalyzer*). |

---

## 🧪 Hands-On Lab

### Prerequisites
- sistem operasi lingkungan pengujian (distro Kali Linux/Ubuntu WSL/Parrot OS).
- Konfigurasi koneksi stabil arsitektur *VPN* menuju portal lab *TryHackMe*.
- Instalasi perangkat pelacak terminal : `nmap`, `ffuf` (atau `gobuster`), serta pelacak ekstensi *Wappalyzer*.

### Misi Hari Ini: "Operasi Sapu Bersih (Full Recon Cycle)"

Pada sesi praktikum ini, Anda secara mutlak difokuskan untuk mempraktikkan siklus pengintaian utuh (*Reconnaissance*) layaknya operasi penganalisis profesional, mendata pemetaan kerentanan infrastruktur sasaran yang kelak bakal menjadi parameter modal eksekusi krusial bagi tahapan eksploitasi peretasan minggu berikutnya. Dilarang keras meluncurkan eksekusi eksploitasi pembobolan (*belum saatnya*).

### Step 1: Inisiasi Uji (TryHackMe)

1. Akses portal *platform* kompetisi keamanan [TryHackMe](https://tryhackme.com/). (Pastikan konektivitas terminal transmisi OpenVPN-mu menancap sukses tervalidasi).
2. Carilah simulasi infrastruktur mesin gratisan tipe web, semisal lab peladen bertitel **"RootMe"**, **"Bounty Hacker"**, atau **"Basic Pentesting"**.
3. Klik eksekusi instruksional tombol *Start Machine* lantas dokumentasikan catatan payload Alamat IP mesin sasaran tersebut. (Sebagai contoh, asumsikan payload IP-nya adalah `10.10.x.x`).

### Step 2: Percobaan Pemindaian Aktif (Nmap)

1. Buka antarmuka aplikasi terminal komando di sistem OS pengujian Anda.
2. Luncurkan eksekusi perintah pemindaian aktif interogasi port `Nmap` guna memetakan arsitektur terbuka:
 ```bash
 nmap -sC -sV -oN hasil_scan.txt 10.10.x.x
 ```
 *(definisi parameter komando: `-sC` Nmap untuk menjalankan skrining deteksi bawaan (default scripts), `-sV` ditugaskan spesifik membongkar deteksi terawang nama aplikasi dan versinya, lantas fungsi `-oN` mendikte Nmap agar cetakannya mutlak direkam dan ditumpahkan penyimpanannya ke format fail bernama `hasil_scan.txt` agar dokumentasi laporannya kelak terarsip valid)*.

### Step 3: Inspeksi Sidik Jari Teknologi (Wappalyzer)

1. Bilamana pemindaian arsip payload pelaporan Nmap merestui penemuan port HTTP terbuka semisal layanan port `80`, segeralah lakukan inspeksi antarmuka visual peladen. Buka kueri URL `http://10.10.x.x` pada aplikasi peramban Anda.
2. Klik fungsi ekstensi pelacak `Wappalyzer` di sudut perambanmu! 
3. Catat pembongkaran identitas peladennya. Apakah ini dirakit bersandar web server *Apache*? Bersi *PHP* berapakah ia? Adakah cap platform bawaan *WordPress* atau *Node.js* yang menempel?

### Step 4: Menghajar Folder Rahasia (Directory Fuzzing)

1. Mengingat payload tampilan visual antarmuka beranda situs seringkali tidak mengekspos keberadaan letak berkas konfigurasi peladen vital secara langsung pada referensi kueri wajar, lakukan inisiasi pemindaian tebakan iterasi masif ekskavasi direktori rahasia menggunakan alat paksa parameter *ffuf* atau alternatif serumpun *gobuster*!
 ```bash
 # Contoh sintaks komando eksekusi memori ffuf:
 ffuf -w /usr/share/wordlists/dirb/common.txt -u http://10.10.x.x/FUZZ

 # Alternatif pengujian kueri jika menggunakan gobuster:
 gobuster dir -u http://10.10.x.x -w /usr/share/wordlists/dirb/common.txt
 ```
2. Pantau layar kalkulasi berhamburan. Jika muncul balasan pelaporan parameter log keberhasilan respons penemuan peladen berstatus valid *HTTP 200* atau *301* untuk nomenklatur `/admin`, `/panel`, atau `/uploads`, tandai status keberhasilan deteksi payload lokasi arsip arsip tersebut, lalu bubuhkan dokumentasi catatannya.

---

## 🎯 Weekly Mission

### Misi: "Laporan Pengintaian Siluman (Reconnaissance Report)"

**Deskripsi:** Kompetensi esensial dan fundamental yang divaluasi setinggi-tingginya dalam ruang lingkup pelacakan operasi kerentanan profesional dan industri *Bug Bounty* bukan terletak semata-mata pada kemampuan serampangan penguasaan letupan meriam eksploitasi, melainkan pada objektivitas perumusan pelaporan profesionalisme dokumentasi (*Reporting*)! Seluruh serpihan log temuan penelusuran arsitektur di ekosistem mesin Lab sasaran hari ini tidak diperkenankan lenyap diabaikan. 

**Tugas Mandiri:** Kompilasi seluruh rentetan eksekusi pemindaian pengujian parameter *Nmap*, integrasi laporan pengintaian fungsi serapan ekstensi arsitektur *Wappalyzer*, serta tangkapan hasil validasi direktori tersembunyi iterasi pelacak ekskavasi *Ffuf/Gobuster* yang telah direkam barusan, kemudian susun ke dalam format manuskrip draf pelaporan.

**Deliverables:**
1. Menyusun dokumen berbasis pelaporan *Markdown* bertajuk `RECON_REPORT_THM.md` (atau simpan laporannya terdokumentasi mandiri di repositorimu).
2. isi paparan manuskrip wajib mencakup cakupan poin-poin struktural arsitektur sasaran, meliputi: 
 - **Target IP** (Payload informasi log IP Sasaran TryHackMe)
 - **Open Ports & Services** (Paparan deteksi *Nmap*)
 - **Web Technology Stack** (Paparan identitas tumpukan perangkat *Wappalyzer*)
 - **Hidden Directories Found** (Pembeberan direktori terekspos log *Ffuf/Gobuster*)
 - Kesimpulan singkat penganalisis: "Berdasarkan rangkuman paparan fungsi pelacakan porta layanan rentan dan versi usang aplikasi peladen yang terekspos tersebut, metodologi vektor eksploitasi kerentanan manakah yang paling dianalisis dan direkomendasikan pengujiannya sebagai fokus utama peretasan pembongkaran mesin target di siklus arsitektur tahap berikutnya?"

**Kriteria Sukses:**
- [ ] Sanggup menuntaskan pemindaian *Nmap* utuh serta menelurkan rahim perekaman dokumentasi cetakan file sandi `-oN`.
- [ ] Sukses mempreteli lokasi penempatan sarang fail URL arsip log sasaran yang tersembunyi berbasis serangan *Gobuster/Ffuf*.
- [ ] Lahirnya manuskrip ringkasan draf dokumen komprehensif terstruktur berekstensi pelaporan log *.md* pengintaian.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Mengingat implementasi fase arsitektur operasi transmisi <i>Active Reconnaissance</i> yang berisiko krusial serta memicu rekam radar kebisingan pendeteksian pada perisai pertahanan target, perizinan sandi legalitas prasyarat mutlak apakah yang wajib disepakati validasinya sebelum peluncuran peranti interogasi penganalisis (semacam perintah instruksional Nmap) dikomandokan lantas dieksekusi peluncurannya?</summary>

**Jawaban:** Dokumen pakem landasan otorisasi pengikatan persetujuan mandat legal wewenang otentikasi *Rules of Engagement (RoE)* dan formulir kontrak persetujuan resmi empunya aset sasaran.
</details>

<details>
<summary>❓ [MUDAH] Pada rumusan fungsionalisasi siklus metodologi pengujian arsitektur <i>Pentesting</i>, nomenklatur gelar tahapan tahap absolut nomor berapakah yang secara difokuskan penggunaannya bagi pencetakan perumusan payload penu naskah rekomendasi remediasi laporan komplit penambalan kepada direksi organisasi ketika tahap verifikasi penetrasi pembobolan kerentanan kelak tuntas diselesaikan?</summary>

**Jawaban:** Tahapan kelima (pamungkas), yakni *Post-Exploitation & Reporting*.
</details>

<details>
<summary>❓ [SEDANG] Ketika peretas kueri sasaran eksekusi perintah pelacakan pemindai <i>Nmap</i>, peranan imbuhan payload deklarasi ekstensi operator <i>flag</i> `-sV` dipatrikan guna memenuhi penugasan penelusuran arsitektur pelaporan pembongkaran interogasi parameter apa?</summary>

**Jawaban:** Melakukan interogasi payload instruksional ekstraksi parameter identitas pendeteksian pengenalan *Service Version* (Membaca merek jenis layanan aplikasi perangkat lunak penjaga port aktif sasaran, lengkap disertai ekstrak penelusuran versi rentan semacam laporan balasan 'Apache versi 2.4.29').
</details>

<details>
<summary>❓ [SEDANG] Titah sintaks penelusuran ekstrak parameter sakti operator <i>Google Dorking</i> filterisasi arsitektur manakah yang dieksekusi ketika agen intelijen membatasi ekstraksi penemuannya murni eksklusif diarahkan khusus sebatas mengekskavasi paparan dokumen bungkusan bertipe berkas berekstensi log PDF?</summary>

**Jawaban:** Operator penyaring ekstensi atribut *filetype:pdf*.
</details>

<details>
<summary>❓ [SULIT] Jelaskan formulasi letak persekutuan korelasi arsitektur penyusunan operasi pemusnahan sasaran yang secara konseptual antara keberhasilan efisiensi eksekusi tahap temuan pemetaan iteratif meraba arsitektur tautan direktori web rahasia (*Directory Bruteforcing*) berbasis eksekutor sandi *ffuf/gobuster*, kemudian disilang rantai penyambutannya divalidasi inspeksi fungsi analisis pelaporan deteksi tumpukan parameter eksekutor *Wappalyzer*!</summary>

**Jawaban:** Ketika parameter analisis fungsi tebakan pelacak paksa iterasi *ffuf* menabrak situs sasaran lantas mendeteksi rute payload lokasi tersembunyi fail direktori aplikasi peladen rahasia target (misal rute url sasaran `/admin` atau portal rute log masuk konfigurasi peladen), penemuan eksistensi status *200 OK* pada alamat URL tersebut belum membuahkan landasan senjata eksploitasi peladen parameter kueri serangan komprehensif apa pun. Penganalisis wajib segera mengerahkan payload fungsi pembedahan arsitektur ekstensi peramban deteksi *Wappalyzer* guna mengakses dan mengunjungi peramban gerbang lokasi direktori sasaran temuan `/admin` tersebut guna mengidentifikasi teknologi perangkat lunak peramban apa yang melapisinya. Jika temuan ekstraksi analisis parameter detektor pelaporan *Wappalyzer* menerawang status identitas arsitektur bahwasanya platform portal pengoperasian admin spesifik tersebut dibangun berbasis versi arsitektur *CMS (Content Management System)* peladen usang yang rentan eksploitasi kerentanan publik (misal deteksi arsitektur kerangka *WordPress v4.0.0*), peretas sontak mengantongi rumusan senjata penelusuran kerentanan instan pustaka publik untuk membantai arsitektur laman otentikasi rahasia sasaran itu tanpa wajib membuang rentetan usaha trial and error menebak arsitektur kerentanan serangannya secara manual buta. Rantai paduan integrasi penelusuran intelijen keduanya menghasilkan alur peta analisis eksploitasi peretasan sistem sadap yang presisi mematikan!
</details>

---

## 📋 Weekly Checklist

- [ ] Saya meresapi pedoman PTES fase daur hidup *Pentesting* absolut
- [ ] Saya mengantongi penguasaan eksekusi intaian senyap operator *Google Dorking*
- [ ] Saya mendemonstrasikan pemicu keras pemindaian port peladen arsitektur sasaran *Nmap*
- [ ] Saya fasih menginisiasi iterasi pembongkaran direktori web peramban letak URL tersembunyi *Ffuf/Gobuster*
- [ ] Saya sanggup membidani perakitan penyusunan kompilasi draf laporan *RECON_REPORT_THM.md* yang merangkum keseluruhan saripati parameter operasi intelijen mingguan (*Weekly Mission*).

---

## 💬 Diskusi Minggu Ini

1. Sesudah mengoperasikan analisis ekskavasi sumber data publik sumber arsitektur data *OSINT* dan *WHOIS* pada pengujian tahapan Pengintaian Pasif, seberapa krusial kesadaran yang terbangun dalam batin teknikalmu ihwal bahaya penelusuran penempatan informasi arsitektur privasi aplikasi milik peladen pribadimu sendiri yang barangkali selama ini tanpa disadari dibiarkan terekspos serta terpublikasi rawan menganga berceceran meresap jejaknya tanpa pelindungan otorisasi sandi akses pada konfigurasi peramban infrastruktur awan data *search engine* internet publik dunia?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ THE SILENT OBSERVER │
│ Week 15 Complete │
│ "To conquer a fortress, │
│ first you map every stone." │
│ │
└─────────────────────────────────────┘
```

Selamat! Rekonstruksi parameter arsitektur fase awal tahapan *Reconnaissance* telah Anda rampungkan paripurna!

---

## ➡️ Preview Minggu Depan

**Minggu 16: Web Exploitation — Injection Attacks**

Waktu pengintaian usai! Segala peta intelijen infrastruktur pemindaian laporan *Nmap* serta analisis struktur pengintaian detektor *Wappalyzer* sasaran yang direkonstruksi minggu ini kelak berfungsi menjadi pedoman strategis di ransel payload payload operasimu! Bersiap menanggalkan status observasi statis dan sambutlah pengujian eksekusi parameter pembuktian teknis sebagai spesialis arsitektur peretasan! Minggu depan secara utuh dialokasikan sebagai siklus murni **Minggu Serangan (Web Exploitation)**. Kita bakal terjun membongkar serta menyuntik eksploitasi parameter memanipulasi peladen arsitektur struktur modifikasi Database kueri percobaan simulasi kerentanan mutlak modifikasi serangan *SQL Injection* tingkat lanjut (*UNION-based & Blind SQLi*), menyeludupkan payload mesin penetrasi otomasi andalan pakar industri *SQLMap*, hingga meracik rekayasa meruntuhkan gerbang validasi otentikasi login mutlak sistem tanpa perlu menebak sandi *(Authentication Bypass Attack Method Execution Tool SQL Architecture Vulnerability Method Security Penetration Payload Operation Security Injection Testing)*!

> 🚀 *"The reconnaissance is over. The breach begins."*

---

*📅 TISS Null Teaming · Week 15 · Day 5 · BREACH Rank*
