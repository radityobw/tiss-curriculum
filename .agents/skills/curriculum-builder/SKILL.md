---
name: "TISS Null Teaming Curriculum Builder"
description: "Skill untuk membuat kurikulum Null Teaming Division TISS secara bertahap. Menghasilkan 1 file markdown interaktif per hari (5 hari/minggu) selama 24 minggu (6 bulan) untuk di-upload ke academy.tiss.or.id. Trigger: ketika user meminta pembuatan materi mingguan, kurikulum TISS, atau menyebut Null Teaming / rank (Void, Cipher, Packet, Forge, Breach, Sentinel)."
---

# TISS Null Teaming Curriculum Builder

## Tujuan

Kamu adalah **Curriculum Builder Agent** untuk TISS (Tirtayasa Information Security Society). Tugasmu adalah menghasilkan **1 file markdown materi interaktif per hari** (5 hari/minggu, Senin–Jumat) selama 24 minggu untuk Null Teaming Division — pipeline pengembangan kader cyber security dari nol.

- **Total output**: 24 minggu × 5 hari = **120 file markdown**
- **Durasi per file**: 30–60 menit belajar
- **Platform target**: **academy.tiss.or.id** (web-based markdown renderer)

---

## Konteks Organisasi

TISS memiliki 3 layer:
- **L0 (Foundational)**: Null Teaming Division — tempat kader baru belajar dari nol
- **L1 (Operational)**: Red/Blue/Yellow Teaming — spesialisasi teknis + Guild
- **L2 (Executive)**: White Teaming — governance & leadership

Null Teaming Division menggunakan **sistem ranking** dari bawah ke atas:

| Rank | Nama | Fokus | Minggu | Durasi | Hari Total | Platform Rujukan Utama |
|------|------|-------|--------|--------|------------|----------------------|
| Unranked | **Void** | Orientasi UKM & Dunia Cyber Security | 1 | 1 minggu | 5 hari | — |
| Rank 5 | **Cipher** | Technical English Foundation | 2–4 | 3 minggu | 15 hari | BBC Learning English, British Council, EF SET |
| Rank 4 | **Packet** | Networking & Linux Fundamentals | 5–9 | 5 minggu | 25 hari | Cisco NetAcad, Linux Journey, OverTheWire |
| Rank 3 | **Forge** | Web Development (Zero-to-Hero) | 10–14 | 5 minggu | 25 hari | The Odin Project, Full Stack Open, freeCodeCamp |
| Rank 2 | **Breach** | Web Pentesting & Laporan Pentesting | 15–19 | 5 minggu | 25 hari | PortSwigger Academy, TryHackMe, HTB Academy |
| Rank 1 | **Sentinel** | Web Log & Monitoring (Blue Team) | 20–24 | 5 minggu | 25 hari | LetsDefend, Blue Team Labs Online, CyberDefenders |

---

## Cara Menggunakan Skill Ini

### Input dari User
User bisa meminta pembuatan materi dengan format:
- **Per hari**: "Buatkan materi week 1 day 1" / "Buat W1D3"
- **Per minggu (batch)**: "Buatkan semua materi minggu ke-5" → generate 5 file sekaligus
- **Per rank**: "Buatkan materi CIPHER lengkap" → generate semua file untuk rank itu

### Output yang Dihasilkan
Untuk setiap permintaan, hasilkan file markdown dengan:
- **Struktur folder**: `output/week-XX-[rank]/day-X-[topik-singkat].md`
- **Bahasa**: Bahasa Indonesia dengan istilah teknis dalam Bahasa Inggris
- **Format**: Mengikuti template di `references/day-template.md`

### Struktur Output
```
output/
├── week-01-void/
│   ├── day-1-pengenalan-tiss-dan-cybersecurity.md
│   ├── day-2-tiga-pilar-cybersecurity.md
│   ├── day-3-cia-triad-dan-etika-hacking.md
│   ├── day-4-sistem-ranking-dan-roadmap.md
│   └── day-5-setup-tools-dan-weekly-mission.md
├── week-02-cipher/
│   ├── day-1-mengapa-bahasa-inggris-krusial.md
│   ├── day-2-...
│   ...
```

---

## Peta Materi 24 Minggu (120 Hari)

### 🌀 VOID — Orientasi (Minggu 1 · 5 Hari)

#### Minggu 1: Selamat Datang di Dunia Cyber Security

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Pengenalan TISS & Cyber Security | Apa itu TISS, visi misi, apa itu cybersecurity, mengapa penting |
| Day 2 | Tiga Pilar Cyber Security | Red Team (offense), Blue Team (defense), Yellow Team (build) + peran karier |
| Day 3 | CIA Triad & Etika Hacking | Confidentiality, Integrity, Availability + white/grey/black hat + UU ITE |
| Day 4 | Sistem Ranking & Roadmap 24 Minggu | Alur Void→Sentinel, pengenalan CTF, preview perjalanan 6 bulan |
| Day 5 | Setup Tools & Weekly Mission | Setup GitHub, TryHackMe, VS Code + misi: buat profil & esai motivasi |

---

### 🔤 CIPHER — Technical English (Minggu 2–4 · 15 Hari)

#### Minggu 2: Reading Technical Documentation

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Mengapa Bahasa Inggris Krusial | Lanskap cybersecurity global, semua docs dalam English |
| Day 2 | Vocabulary Builder: Istilah Dasar | 30 istilah networking & security wajib dengan konteks |
| Day 3 | Cara Membaca CVE & RFC | Format CVE advisory, cara parsing informasi kritis |
| Day 4 | Teknik Scanning & Skimming | Speed reading untuk dokumentasi teknis |
| Day 5 | Lab & Mission: Rangkum CVE Advisory | Praktik baca CVE + buat glossary Inggris-Indonesia |

#### Minggu 3: Writing Technical Reports

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Struktur Laporan Teknis | Anatomy of a technical report: abstract, methodology, findings |
| Day 2 | Email Profesional & Komunikasi Komunitas | Menulis di mailing list, forum, cara bertanya yang baik |
| Day 3 | Bug Report Writing Basics | Format bug report, severity classification, reproducing steps |
| Day 4 | Akronim & Abbreviation Cybersecurity | Daftar 50 akronim wajib: APT, CVE, CVSS, IoC, TTPs, dll. |
| Day 5 | Lab & Mission: Tulis Bug Report | Praktik menulis bug report + technical summary artikel |

#### Minggu 4: Listening & Communication

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Memahami Conference Talks | Tips menonton DEF CON / Black Hat talks efektif |
| Day 2 | Podcast & Video Cybersecurity | Rekomendasi podcast, cara belajar dari multimedia |
| Day 3 | Berdiskusi di Forum Internasional | Etika StackOverflow, Reddit r/netsec, cara bertanya |
| Day 4 | Evaluasi Kemampuan: EF SET | Ikuti EF SET test, pahami skor & rencana improvement |
| Day 5 | Lab & Mission: Ringkasan Conference Talk | Tonton 1 talk + EF SET test + dokumentasi skor |

---

### 📡 PACKET — Networking & Linux Fundamentals (Minggu 5–9 · 25 Hari)

#### Minggu 5: Dasar Jaringan Komputer

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Model OSI Layer (Bagian 1) | Layer 1–4: Physical, Data Link, Network, Transport |
| Day 2 | Model OSI Layer (Bagian 2) | Layer 5–7: Session, Presentation, Application |
| Day 3 | Model TCP/IP & Perbandingan | 4 layer TCP/IP, mapping ke OSI, kapan pakai yang mana |
| Day 4 | IP Address, Subnet & DNS | IPv4, subnetting dasar, cara DNS bekerja |
| Day 5 | Lab & Mission: Identifikasi Jaringan | `ipconfig`/`ifconfig`, `ping`, `traceroute` + buat diagram OSI |

#### Minggu 6: Protokol Jaringan & Analisis Trafik

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | TCP vs UDP | Three-way handshake, reliability vs speed, use cases |
| Day 2 | HTTP/HTTPS Deep-Dive | Request/response cycle, methods, status codes, TLS/SSL |
| Day 3 | DNS, ARP, DHCP, ICMP | Protokol pendukung jaringan, cara kerja masing-masing |
| Day 4 | Pengenalan Wireshark | Install, interface, capture filter vs display filter |
| Day 5 | Lab & Mission: Analisis Trafik Wireshark | Capture 5 protokol + buat laporan analisis trafik |

#### Minggu 7: Linux — Memulai dari Nol

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Apa itu Linux & Mengapa Penting? | Sejarah, distro, peran Linux di server & cybersecurity |
| Day 2 | Instalasi Linux (VM/WSL) | Step-by-step setup VirtualBox + Ubuntu/Kali |
| Day 3 | Navigasi Filesystem | `ls`, `cd`, `pwd`, `mkdir`, `rm`, `cp`, `mv`, `find` |
| Day 4 | File Permissions & Ownership | `chmod`, `chown`, `rwx`, permission numbers (755, 644) |
| Day 5 | Lab & Mission: Eksplorasi Linux | Setup VM + navigasi + buat folder structure + dokumentasi |

#### Minggu 8: Linux — Sistem, User & Scripting

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | User & Group Management | `adduser`, `usermod`, `passwd`, `su`, `sudo`, `/etc/passwd` |
| Day 2 | Process & Service Management | `ps`, `top`, `htop`, `kill`, `systemctl`, `journalctl` |
| Day 3 | Package Management | `apt update/install/remove`, repository, `dpkg` |
| Day 4 | Bash Scripting Dasar | Variables, conditionals, loops, functions, `#!/bin/bash` |
| Day 5 | Lab & Mission: Script Health Check | Buat bash script automasi + OverTheWire Bandit Level 0–5 |

#### Minggu 9: Networking + Linux — Integrasi

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Network Tools di Linux | `nmap`, `netstat`/`ss`, `curl`, `wget`, `dig` |
| Day 2 | SSH & Remote Access | SSH key-based auth, `ssh-keygen`, config file, SCP |
| Day 3 | Firewall Dasar | `iptables` basics, `ufw` setup, allow/deny rules |
| Day 4 | Port Scanning & Service Enumeration | Nmap scan types, service detection, OS fingerprinting |
| Day 5 | Lab & Mission: Network Recon di Linux | Full network scan + SSH setup + firewall rules + Bandit Level 6–10 |

---

### 🔨 FORGE — Web Development Zero-to-Hero (Minggu 10–14 · 25 Hari)

#### Minggu 10: Git, GitHub & HTML — Fondasi Web

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Git Local & Version Control | Konsep VCS, `git init`, `add`, `commit`, `status`, `log`, `branch`, `merge` |
| Day 2 | GitHub, Remote & Kolaborasi | `push`, `pull`, `clone`, SSH keys untuk GitHub, Forking, Pull Request |
| Day 3 | Fondasi Web & HTML Dasar | Client-server, semantic tags, forms, input types, method GET/POST |
| Day 4 | CSS Fundamentals & DevTools | Selectors, box model, flexbox, Inspect Element, Network Tab |
| Day 5 | Lab & Mission: Halaman Profil & Hosting | Buat halaman profil portofolio + deploy ke GitHub Pages |

#### Minggu 11: JavaScript Fundamentals

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Variables, Data Types & Operators | `let`, `const`, strings, numbers, booleans, operators |
| Day 2 | Functions, Scope & Closures | Function declaration/expression, arrow functions, scope chain |
| Day 3 | DOM Manipulation | `querySelector`, `addEventListener`, `innerHTML`, `createElement` |
| Day 4 | Event Handling & Form Validation | Click, submit, keyup events, client-side validation patterns |
| Day 5 | Lab & Mission: To-Do List App | Buat To-Do List interaktif dengan localStorage |

#### Minggu 12: Backend Basics — Node.js & Express

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Apa itu Backend? | Server vs client, request flow, API concept |
| Day 2 | Node.js Fundamentals | Modules, npm, package.json, CommonJS vs ESM |
| Day 3 | Express.js: Routing & Middleware | Routes, params, query, middleware pattern, `next()` |
| Day 4 | REST API Design | CRUD operations, HTTP methods, status codes, JSON |
| Day 5 | Lab & Mission: CRUD REST API | Buat API manajemen catatan + dokumentasi endpoints |

#### Minggu 13: Database & Authentication

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | SQL Basics (Bagian 1) | CREATE TABLE, INSERT, SELECT, WHERE, ORDER BY |
| Day 2 | SQL Basics (Bagian 2) | UPDATE, DELETE, JOIN, relationships, normalization |
| Day 3 | Database di Node.js | SQLite/PostgreSQL driver, query execution, ORM intro |
| Day 4 | Authentication & Password Security | Session vs JWT, bcrypt hashing, login/register flow |
| Day 5 | Lab & Mission: Sistem Login/Register | Buat auth system dengan DB + hashed passwords |

#### Minggu 14: Secure Coding & OWASP Top 10

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Pengenalan OWASP Top 10 | Overview semua 10 vulnerability categories |
| Day 2 | SQL Injection & Prevention | Cara kerja SQLi, parameterized queries, prepared statements |
| Day 3 | XSS & CSRF | Stored/Reflected/DOM XSS, CSRF tokens, prevention |
| Day 4 | Security Headers & Best Practices | CSP, HSTS, X-Frame-Options, input validation, sanitization |
| Day 5 | Lab & Mission: Audit & Fix Vulnerability | Identifikasi + perbaiki vuln di app sendiri + buat OWASP checklist |

---

### 💀 BREACH — Web Pentesting & Report Writing (Minggu 15–19 · 25 Hari)

#### Minggu 15: Reconnaissance & Information Gathering

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Pentest Methodology | PTES, OWASP Testing Guide, phases of pentesting |
| Day 2 | Passive Reconnaissance | WHOIS, DNS lookup, Google dorking, Shodan, theHarvester |
| Day 3 | Active Reconnaissance | Nmap scanning, directory bruteforcing (gobuster/ffuf) |
| Day 4 | Subdomain & Technology Fingerprinting | Sublist3r, Amass, Wappalyzer, WhatWeb |
| Day 5 | Lab & Mission: Full Recon Report | Recon pada TryHackMe machine + buat recon report terstruktur |

#### Minggu 16: Web Exploitation — Injection Attacks

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | SQL Injection: UNION-based | Extracting data via UNION SELECT, column enumeration |
| Day 2 | SQL Injection: Blind (Boolean & Time) | Boolean-based blind, time-based blind, inference |
| Day 3 | SQLMap: Automated Exploitation | Installation, basic usage, tamper scripts, flags |
| Day 4 | Authentication Bypass | Login bypass, credential stuffing, brute force, session attacks |
| Day 5 | Lab & Mission: PortSwigger SQLi Labs | Selesaikan 5 SQLi labs + tulis writeup per lab |

#### Minggu 17: Web Exploitation — XSS, CSRF & Beyond

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | XSS: Stored, Reflected & DOM | Payload crafting, cookie stealing, keylogging |
| Day 2 | CSRF & SSRF | State-changing attacks, internal service access |
| Day 3 | File Upload & IDOR | Unrestricted upload, bypass filters, insecure direct object ref |
| Day 4 | Chaining Vulnerabilities | Combining vulns for higher impact, real-world scenarios |
| Day 5 | Lab & Mission: PortSwigger XSS/CSRF Labs | Selesaikan 5 labs + buat exploitation cheatsheet |

#### Minggu 18: Burp Suite & Advanced Tooling

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Burp Suite: Proxy & Intercept | Setup, proxy config, intercept & modify requests |
| Day 2 | Burp Suite: Repeater & Intruder | Manual testing, automated fuzzing, payload positions |
| Day 3 | Burp Suite: Scanner & Extensions | Automated scanning, useful extensions, macros |
| Day 4 | Other Tools: ZAP, ffuf, nikto | Alternative tools, when to use what, combining tools |
| Day 5 | Lab & Mission: Full Pentest Machine | Pentest vulnerable machine end-to-end dengan Burp Suite |

#### Minggu 19: Pentest Report Writing

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Struktur Laporan Pentesting | Executive summary, scope, methodology, findings |
| Day 2 | CVSS Scoring & Severity Rating | How to rate severity, CVSS calculator, risk assessment |
| Day 3 | PoC Documentation & Remediation | Proof of concept writing, remediation recommendations |
| Day 4 | Menulis Laporan Lengkap | Hands-on: tulis report berdasarkan machine yang dikerjakan |
| Day 5 | Lab & Mission: Peer Review Report | Finalisasi report + peer review + revisi berdasarkan feedback |

---

### 🛡️ SENTINEL — Web Log & Monitoring (Minggu 20–24 · 25 Hari)

#### Minggu 20: Pengenalan Blue Team & SOC

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Apa itu Blue Team & SOC? | Peran SOC Analyst, SOC tiers, daily workflow |
| Day 2 | Security Events vs Incidents | Definisi, klasifikasi, eskalasi, triage |
| Day 3 | Log Sources & Syslog | Web server logs, app logs, OS logs, syslog protocol |
| Day 4 | Incident Response Lifecycle | PICERL: Preparation, Identification, Containment, Eradication, Recovery, Lessons |
| Day 5 | Lab & Mission: Analisis Access Logs | Analisis web server logs + buat SOP incident response |

#### Minggu 21: Log Analysis & Threat Detection

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Apache/Nginx Log Format | Log parsing, common fields, access vs error logs |
| Day 2 | Windows Event Logs | Key Event IDs (4624, 4625, 4688, 7045), Event Viewer |
| Day 3 | Linux Logs & Journalctl | `/var/log/`, `journalctl`, `auth.log`, `syslog` |
| Day 4 | Pattern Recognition | Brute force patterns, scanning indicators, data exfiltration |
| Day 5 | Lab & Mission: Identifikasi Serangan | Analisis log file besar dengan grep/awk + identifikasi 3 serangan |

#### Minggu 22: SIEM & Monitoring Tools

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | SIEM Concepts & Architecture | Collect, normalize, correlate, alert, store |
| Day 2 | Splunk Basics | SPL queries, search commands, fields, tables |
| Day 3 | Splunk Dashboards & Alerts | Visualization, dashboard creation, alert configuration |
| Day 4 | IDS/IPS: Suricata & Snort | Rule syntax, signature-based detection, custom rules |
| Day 5 | Lab & Mission: Setup SIEM & Detection Rules | Setup Splunk/ELK + ingest logs + buat 3 detection rules |

#### Minggu 23: Threat Hunting & Digital Forensics Intro

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Proactive vs Reactive Security | Threat hunting philosophy, hypothesis-driven approach |
| Day 2 | MITRE ATT&CK Framework | Tactics, techniques, procedures (TTPs), Navigator tool |
| Day 3 | Digital Forensics Basics | Evidence collection, chain of custody, forensic imaging |
| Day 4 | Memory & Disk Forensics | Volatility introduction, disk analysis, artifact extraction |
| Day 5 | Lab & Mission: Threat Hunting Exercise | MITRE ATT&CK exercise + buat threat hunting playbook |

#### Minggu 24: Capstone — Full Cycle Defense & Graduation

| Hari | Topik | Fokus Utama |
|------|-------|-------------|
| Day 1 | Simulasi Incident (Bagian 1) | Alert triage → initial analysis → scoping |
| Day 2 | Simulasi Incident (Bagian 2) | Containment → eradication → recovery |
| Day 3 | Incident Report Writing | Professional incident report, executive summary, timeline |
| Day 4 | Career Path & Sertifikasi | CEH, eJPT, CompTIA Security+, BTL1, personal branding |
| Day 5 | Final Mission: Portfolio & Graduation | Buat portfolio 24 minggu + review perjalanan + achievement final |

---

## Instruksi Generate Markdown

Ketika user meminta materi, ikuti langkah berikut:

### 1. Identifikasi Hari & Minggu
Tentukan hari dan minggu yang diminta. Cek peta materi di atas untuk menentukan rank dan topik.

### 2. Tentukan Tipe Hari
Ada 2 tipe hari dengan format yang berbeda:

**📖 Hari Materi (Day 1–4):**
- Fokus pada 1 topik spesifik
- Durasi baca: 30–45 menit
- Elemen: materi + mini-lab + quiz kilat
- Gunakan template `references/day-template.md`

**🧪 Hari Lab & Mission (Day 5):**
- Fokus pada praktik dan weekly mission
- Durasi: 60–90 menit
- Elemen: lab lengkap + weekly mission + achievement badge + weekly recap
- Gunakan template `references/day-template.md` dengan section tambahan (lihat template)

### 3. Isi Konten Berdasarkan Peta Materi
Kembangkan setiap topik menjadi penjelasan yang:
- **Intuitif**: gunakan analogi kehidupan sehari-hari untuk konsep abstrak
- **Visual**: sertakan diagram ASCII/Unicode, tabel, dan flowchart di dalam markdown
- **Bertahap**: mulai dari yang paling mudah, bangun ke yang lebih kompleks
- **Kontekstual**: hubungkan dengan materi hari/minggu sebelumnya

### 4. Elemen Interaktif per Tipe Hari

#### Hari Materi (Day 1–4) — Elemen Wajib:

| Elemen | Deskripsi | Jumlah |
|--------|-----------|--------|
| 📊 Progress Tracker | Posisi hari ini dalam rank & journey | 1 |
| 🎯 Tujuan Hari Ini | Learning objectives spesifik | 2–3 |
| 📖 Materi Inti | Penjelasan topik dengan visual & analogi | 1–2 subtopik |
| 🧪 Mini Lab / Latihan | Praktik singkat 10–15 menit | 1 |
| 💡 Quiz Kilat | Collapsible Q&A | 3 pertanyaan |
| 📋 Checklist Hari Ini | Self-assessment checklist | 3–5 item |
| 🔗 Resources | Link ke platform rujukan | 2–3 link |
| ➡️ Preview Besok | Teaser materi besok | 1–2 kalimat |

#### Hari Lab & Mission (Day 5) — Elemen Wajib:

| Elemen | Deskripsi | Jumlah |
|--------|-----------|--------|
| 📊 Progress Tracker | Posisi minggu ini dalam rank & journey | 1 |
| 📝 Rekap Minggu Ini | Ringkasan 4 hari sebelumnya | 1 |
| 🧪 Hands-On Lab | Lab lengkap step-by-step dengan troubleshooting | 1 besar |
| 🎯 Weekly Mission | Tugas besar yang menghasilkan deliverable | 1 |
| 💡 Knowledge Check | Quiz komprehensif minggu ini | 5 pertanyaan (2 mudah, 2 sedang, 1 sulit) |
| 📋 Weekly Checklist | Checklist keseluruhan minggu | 5–8 item |
| 💬 Diskusi Minggu Ini | Pertanyaan terbuka untuk forum/grup | 2–3 pertanyaan |
| 🏆 Achievement Badge | Badge visual untuk minggu ini | 1 |
| ➡️ Preview Minggu Depan | Teaser minggu berikutnya | 2–3 kalimat |

### 5. Collapsible Quiz Format
```markdown
<details>
<summary>❓ Pertanyaan: [pertanyaan]</summary>

**Jawaban:**
[jawaban lengkap]

</details>
```

### 6. Progress Tracker Format

**Untuk Hari Materi (Day 1–4):**
```markdown
📊 **Progress**: Week X · Day Y/5 | [RANK_NAME] Rank (Minggu X dari Y) | Overall: Z/120 hari (XX%)
```

**Untuk Hari Lab & Mission (Day 5):**
```markdown
## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓░░] 80% — PACKET Rank (Minggu 4 dari 5)

### Overall Journey
[▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░] 25% — Hari 30 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → 🔄 PACKET → ⬜ FORGE → ⬜ BREACH → ⬜ SENTINEL
```

### 7. Formatting Rules
- Gunakan heading hierarchy yang konsisten: `#` untuk judul, `##` untuk section, `###` untuk subsection
- Gunakan emoji secara konsisten untuk setiap jenis section
- Code blocks dengan language identifier: ` ```bash `, ` ```javascript `, dll.
- Gunakan blockquotes (`>`) untuk tips dan catatan penting
- Gunakan horizontal rules (`---`) untuk separasi antar section besar
- Gunakan **bold** untuk istilah penting dan *italic* untuk penekanan
- Setiap tabel harus memiliki header yang jelas
- Diagram ASCII harus enclosed dalam code blocks
- File harian harus **lebih ringkas** daripada file mingguan — fokus pada 1 topik

### 8. Naming Convention
```
output/
├── week-01-void/
│   ├── day-1-[topik-singkat].md
│   ├── day-2-[topik-singkat].md
│   ├── day-3-[topik-singkat].md
│   ├── day-4-[topik-singkat].md
│   └── day-5-[topik-singkat].md
├── week-02-cipher/
│   ├── day-1-[topik-singkat].md
│   ...
```

### 9. Quality Checklist

**Untuk Hari Materi (Day 1–4):**
- [ ] Progress tracker akurat
- [ ] 2–3 learning objectives jelas
- [ ] Materi fokus pada 1 topik, penjelasan intuitif
- [ ] Minimal 1 mini-lab/latihan
- [ ] 3 quiz kilat dengan collapsible answers
- [ ] Checklist hari ini lengkap
- [ ] Link resources relevan
- [ ] Preview besok ada
- [ ] Bahasa Indonesia natural + istilah teknis English

**Untuk Hari Lab & Mission (Day 5):**
- [ ] Rekap minggu ini ada
- [ ] Lab step-by-step detail dengan troubleshooting
- [ ] Weekly mission spesifik dan measurable
- [ ] 5 quiz komprehensif (2 mudah, 2 sedang, 1 sulit)
- [ ] Weekly checklist lengkap
- [ ] 2–3 discussion prompts
- [ ] Achievement badge
- [ ] Preview minggu depan

---

## Referensi

Untuk daftar lengkap platform dan rekomendasi per domain, lihat:
- `tiss-context.md` — konteks organisasi dan organigram TISS
- `tiss-curriculum-source.md` — ranking ROI platform pembelajaran per domain
- `references/day-template.md` — template standar untuk output markdown harian
- `examples/week-01-void/` — contoh output lengkap untuk 1 minggu (5 file harian)
