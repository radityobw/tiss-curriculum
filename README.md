<div align="center">

# 🛡️ TISS Null Teaming Curriculum

### *Zero-to-Hero Cybersecurity Training Program*

**Tirtayasa Information Security Society**  
Universitas Sultan Ageng Tirtayasa

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
![Weeks](https://img.shields.io/badge/Duration-24%20Weeks-blue)
![Days](https://img.shields.io/badge/Total-120%20Days-green)
![Files](https://img.shields.io/badge/Modules-264%20Files-orange)
![Cost](https://img.shields.io/badge/Cost-100%25%20Free-brightgreen)

</div>

---

## 📌 Tentang Proyek Ini

**TISS Null Teaming Curriculum** adalah kurikulum keamanan siber terstruktur selama **24 minggu (6 bulan / 120 hari pertemuan)** yang dirancang untuk membawa anggota baru dari **nol pengetahuan** hingga siap berkontribusi di divisi operasional TISS.

Kurikulum ini digunakan oleh **Null Teaming Division** — divisi pengembangan sumber daya mahasiswa di bawah Foundational Layer (L0) TISS — sebagai jalur standarisasi kompetensi dasar sebelum anggota masuk ke spesialisasi Red Team, Blue Team, atau Yellow Team.

### Prinsip Desain

| Prinsip | Implementasi |
|---|---|
| 🆓 **100% Gratis** | Seluruh materi, platform, dan tools yang dirujuk bersifat gratis dan open source |
| 📈 **Progresif** | Materi dibangun bertahap dari fondasi (Bahasa Inggris) hingga puncak (Incident Response) |
| 🧪 **Hands-On** | Setiap minggu memiliki lab praktik dan misi mingguan dengan deliverables nyata |
| 🎮 **Gamifikasi** | Sistem ranking (Void → Sentinel) memotivasi progres dan pencapaian |
| 🌐 **Inklusif** | Dirancang agar mahasiswa dari jurusan apapun (bukan hanya Informatika) dapat mengikuti |

---

## 🏗️ Arsitektur Ranking

Kurikulum menggunakan sistem 6 rank yang mencerminkan perjalanan kompetensi anggota:

```
                    ┌──────────────────────────────────────────┐
                    │         🛡️ RANK 1 — SENTINEL            │
                    │      Blue Teaming (SOC & IR)             │
                    │         Minggu 20–24                     │
                    ├──────────────────────────────────────────┤
                    │         💀 RANK 2 — BREACH               │
                    │      Red Teaming (Web Pentesting)        │
                    │         Minggu 15–19                     │
                    ├──────────────────────────────────────────┤
                    │         🔨 RANK 3 — FORGE                │
                    │      Yellow Teaming (Web Dev & Git)      │
                    │         Minggu 10–14                     │
                    ├──────────────────────────────────────────┤
                    │         📡 RANK 4 — PACKET               │
                    │      Networking & Linux                  │
                    │         Minggu 05–09                     │
                    ├──────────────────────────────────────────┤
                    │         🔐 RANK 5 — CIPHER               │
                    │      English Foundation                  │
                    │         Minggu 02–04                     │
                    ├──────────────────────────────────────────┤
                    │         🌀 UNRANKED — VOID               │
                    │      Orientasi & Pengenalan              │
                    │         Minggu 01                        │
                    └──────────────────────────────────────────┘
```

---

## 📅 Peta Kurikulum

### 🌀 Fase VOID — Orientasi (Minggu 1)

| Minggu | Topik Utama |
|--------|-------------|
| 01 | Pengenalan TISS, CIA Triad, Etika Hacking, Setup Tools |

### 🔐 Fase CIPHER — English Foundation (Minggu 2–4)

| Minggu | Topik Utama |
|--------|-------------|
| 02 | Reading & Listening for Cybersecurity |
| 03 | Technical Writing & Bug Report English |
| 04 | Vocabulary Mastery & CEFR Assessment |

### 📡 Fase PACKET — Networking & Linux (Minggu 5–9)

| Minggu | Topik Utama |
|--------|-------------|
| 05 | OSI Model & TCP/IP Fundamentals |
| 06 | Subnetting, DNS, DHCP |
| 07 | Linux CLI & Filesystem Fundamentals |
| 08 | Linux Administration & Permissions |
| 09 | Wireshark & Network Troubleshooting |

### 🔨 Fase FORGE — Web Development & Git (Minggu 10–14)

| Minggu | Topik Utama |
|--------|-------------|
| 10 | HTML & CSS Fundamentals |
| 11 | JavaScript & DOM Manipulation |
| 12 | Backend (Node.js/PHP), Database (SQL) |
| 13 | Git, GitHub, Version Control |
| 14 | Secure Coding & OWASP Top 10 |

### 💀 Fase BREACH — Red Teaming / Web Pentesting (Minggu 15–19)

| Minggu | Topik Utama |
|--------|-------------|
| 15 | Reconnaissance & Information Gathering |
| 16 | SQL Injection (UNION-based, Blind, SQLMap) |
| 17 | XSS, CSRF, SSRF, File Upload, IDOR |
| 18 | Burp Suite (Proxy, Repeater, Intruder) |
| 19 | Bug Bounty Methodology & Reporting |

### 🛡️ Fase SENTINEL — Blue Teaming / SOC (Minggu 20–24)

| Minggu | Topik Utama |
|--------|-------------|
| 20 | SOC Fundamentals & PICERL Framework |
| 21 | Log Analysis (Windows Event Log, Linux Logs) |
| 22 | SIEM (Splunk), IDS/IPS (Suricata & Snort) |
| 23 | Threat Intelligence, MITRE ATT&CK, Digital Forensics |
| 24 | **Capstone Project: Full Incident Response Simulation** |

---

## 📁 Struktur Direktori

```
tiss-curriculum/
├── README.md                       # Dokumentasi proyek (file ini)
├── source-material/                # 📚 Materi kurikulum utama (264 file)
│   ├── week-01-void/               #     Minggu 1: Orientasi
│   │   ├── day-1-*.md              #       Materi hari ke-1
│   │   ├── day-2-*.md              #       Materi hari ke-2
│   │   ├── day-3-*.md              #       Materi hari ke-3
│   │   ├── day-4-*.md              #       Materi hari ke-4
│   │   ├── day-5-*.md              #       Lab & Weekly Mission
│   │   ├── day-6-bonus-hands-on.md #       Bonus: Hands-On Learning
│   │   └── quizzes/                #       Kuis harian (day-1 s/d day-5)
│   │       ├── day-1-quiz.md
│   │       ├── day-2-quiz.md
│   │       └── ...
│   ├── week-02-cipher/
│   ├── ...
│   └── week-24-sentinel/
├── context/                        # 📋 Dokumen referensi & konteks
│   ├── tiss-context.md             #     Organigram & alur kaderisasi TISS
│   ├── tiss-curriculum-source.md   #     Sumber rekomendasi platform belajar
│   └── bonus-day6-hands-on-learning.md # Panduan format bonus Day 6
└── tools/                          # 🔧 Skrip utilitas
    ├── sanitize.py                 #     Pembersihan konten otomatis
    └── fix.pl                      #     Regex fix untuk formatting
```

---

## 📐 Format Materi Per Hari

Setiap file materi harian memiliki struktur konsisten:

### Hari Materi (Day 1–4)

| Komponen | Deskripsi |
|---|---|
| 📊 Progress Tracker | Posisi hari ini dalam rank & keseluruhan journey |
| 🎯 Tujuan Hari Ini | 2–3 learning objectives yang terukur |
| 📖 Materi Inti | Penjelasan topik dengan analogi dan visualisasi |
| 🧪 Mini Lab | Praktik singkat 10–15 menit |
| 💡 Quiz Kilat | 3 pertanyaan dengan jawaban tersembunyi (collapsible) |
| 📋 Checklist | Self-assessment checklist 3–5 item |
| 🔗 Resources | Link ke platform rujukan (semua gratis) |
| ➡️ Preview Besok | Teaser singkat materi esok hari |

### Hari Lab & Mission (Day 5)

| Komponen | Deskripsi |
|---|---|
| 📝 Rekap Minggu | Ringkasan 4 hari sebelumnya |
| 🧪 Hands-On Lab | Lab lengkap step-by-step |
| 🎯 Weekly Mission | Tugas besar dengan deliverables |
| 💡 Knowledge Check | 5 pertanyaan (2 mudah, 2 sedang, 1 sulit) |
| 🏆 Achievement Badge | Badge visual pencapaian minggu ini |

### Bonus Hands-On (Day 6)

| Komponen | Deskripsi |
|---|---|
| 🌐 Platform Eksternal | Instruksi langsung ke platform gratis (TryHackMe, PortSwigger, dll.) |
| 📋 Prasyarat | Daftar kebutuhan teknis sebelum memulai |
| 🔄 Langkah-langkah | SOP step-by-step yang bebas logical flaws |
| ✅ Kriteria Keberhasilan | Indikator objektif bahwa tugas berhasil diselesaikan |

---

## 🌐 Platform & Sumber Belajar

Seluruh platform yang dirujuk dalam kurikulum ini bersifat **gratis** dan dapat diakses tanpa biaya:

| Domain | Platform Utama | Alternatif |
|--------|---------------|------------|
| English | BBC Learning English | British Council, EF SET |
| Networking | Cisco Networking Academy | Jeremy's IT Lab |
| Linux | Linux Journey | OverTheWire (Bandit) |
| Web Dev | The Odin Project | freeCodeCamp, MDN Web Docs |
| Git & GitHub | GitHub Skills | Atlassian Git Tutorials |
| Red Team | PortSwigger Academy | TryHackMe (Free Rooms) |
| Blue Team | LetsDefend | CyberDefenders |
| SIEM | Splunk Free | — |
| Forensics | Autopsy, Volatility 3 | — |

---

## 🚀 Cara Menggunakan Kurikulum Ini

### Untuk Anggota Baru TISS
1. Mulai dari `source-material/week-01-void/day-1-*.md`
2. Selesaikan **1 file per hari** (5 hari/minggu + 1 bonus opsional)
3. Kerjakan kuis harian di folder `quizzes/`
4. Selesaikan *Weekly Mission* setiap hari ke-5
5. Lanjut ke minggu berikutnya setelah checklist mingguan terpenuhi
6. Kerjakan bonus Day 6 jika ingin latihan hands-on tambahan

### Untuk Mentor / Purple Guild
1. Gunakan file kuis (`quizzes/`) sebagai bahan evaluasi mingguan
2. Pantau penyelesaian *Weekly Mission* sebagai indikator progres
3. Gunakan `context/tiss-curriculum-source.md` sebagai referensi rekomendasi platform
4. Sesuaikan kecepatan per individu — kurikulum ini fleksibel

### Untuk Kontributor
1. Fork repository ini
2. Buat branch baru: `git checkout -b fitur/nama-fitur`
3. Commit perubahan: `git commit -m "Deskripsi perubahan"`
4. Push dan buat Pull Request

---

## 📊 Statistik Kurikulum

| Metrik | Nilai |
|--------|-------|
| Total Minggu | 24 minggu |
| Total Hari Pertemuan | 120 hari |
| Total File Materi | 264 file Markdown |
| Fase/Rank | 6 (Void → Cipher → Packet → Forge → Breach → Sentinel) |
| Format | Markdown (.md) |
| Bahasa | Indonesia (dengan terminologi teknis Inggris) |
| Biaya | **Rp 0 (Sepenuhnya Gratis)** |

---

## 🤝 Kontributor

| Peran | Nama |
|-------|------|
| Founder TISS & Curriculum Architect | **Radityo Budi Waskito** |

---

## 📜 Lisensi

Kurikulum ini dilisensikan di bawah [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Anda bebas untuk:
- **Berbagi** — menyalin dan mendistribusikan materi dalam format apapun
- **Mengadaptasi** — mengubah, menerjemahkan, dan mengembangkan materi

Dengan ketentuan:
- **Atribusi** — Mencantumkan kredit kepada TISS
- **NonKomersial** — Tidak digunakan untuk tujuan komersial
- **ShareAlike** — Distribusi turunan menggunakan lisensi yang sama

---

<div align="center">

**Tirtayasa Information Security Society**  
Universitas Sultan Ageng Tirtayasa

*"Belajar → Berkarya → Memimpin"*

</div>
