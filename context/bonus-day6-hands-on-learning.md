Berikut adalah *Standard Operating Procedure* (SOP) resmi untuk eksekusi **"The Null Protocol"**.

---

# 📜 DOKUMEN SOP: THE NULL PROTOCOL

**Unit:** Tirtayasa Information Security Society (TISS)
**Divisi:** Null Teaming Division (L0)
**Durasi:** 24 Minggu (6 Bulan)
**Objektif:** Sertifikasi Standar Operasional L1 Web Specialization

---

## 🏛️ FASE 0: UNRANKED - VOID

**Fokus:** Standardisasi Lingkungan Kerja & Open Source Intelligence

### Minggu 1: Arsitektur Komputer & Virtualisasi Mesin

* **Requirement:** Laptop/PC, Koneksi Internet, Berkas ISO Linux (Ubuntu/Kali).
* **Prosedur:**
1. Unduh dan instal *hypervisor* (VirtualBox/VMware) atau *Windows Subsystem for Linux* (WSL) pada sistem operasi utama.
2. Buat Mesin Virtual (VM) baru, alokasikan minimal 2GB RAM dan 20GB penyimpanan khusus untuk VM tersebut.
3. Nyalakan sistem operasi Linux di dalam VM dan operasikan terminal murni untuk menavigasi direktori.


* **Target Output:** Tangkapan layar terminal Linux yang menampilkan eksekusi perintah absolut `whoami` dan `pwd` yang valid.

### Minggu 2: Etika Peretasan & Investigasi Publik

* **Requirement:** Peramban Web, Akun Email Anonim (khusus riset).
* **Prosedur:**
1. Baca modul internal TISS mengenai kerangka hukum UU ITE dan prinsip *Hacker Manifesto*.
2. Buka mesin pencari Google.
3. Gunakan sintaks *Google Dorking* spesifik: `filetype:pdf intext:confidential site:go.id` (atau domain publik serupa) untuk melacak dokumen yang tidak sengaja terekspos.


* **Target Output:** Dokumen ringkasan berisi URL dan deskripsi temuan data publik (Dilarang keras mengunduh atau melakukan intrusi ke *server* temuan).

---

## 🇬🇧 FASE 1: RANK 5 - CIPHER

**Fokus:** Kapasitas Baca Teknis & Translasi Dokumen Keamanan

### Minggu 3: Technical Reading Comprehension

* **Requirement:** Akses aktif platform British Council LearnEnglish (Kategori B1-B2).
* **Prosedur:**
1. Akses modul *Reading B1-B2*.
2. Baca artikel dengan terminologi teknis/bisnis yang disediakan oleh *platform*.
3. Selesaikan tes pemahaman bacaan pada akhir setiap modul.


* **Target Output:** Tangkapan layar log skor kelulusan tes *Reading B1-B2* dari *dashboard* British Council.

### Minggu 4: Professional Incident Writing

* **Requirement:** Aplikasi pengolah kata (Notion/Word), Draf Skenario Insiden Fiktif (Disediakan oleh pengurus L1/L2).
* **Prosedur:**
1. Terima teks skenario *dummy* yang berantakan (contoh: "Server DB jebol jam 3 pagi karena admin pakai *password* bawaan pabrik").
2. Analisis akar masalah dari teks tersebut.
3. Terjemahkan dan ubah struktur kalimat tersebut menjadi satu paragraf *Executive Summary* berbahasa Inggris formal, tanpa slang atau singkatan tidak baku.


* **Target Output:** Satu paragraf *Executive Summary* berbahasa Inggris yang memenuhi standar tata bahasa pelaporan industri.

---

## 📡 FASE 2: RANK 4 - PACKET

**Fokus:** Topologi Komunikasi Data & Pengalamatan IP

### Minggu 5: Network Architecture Foundation

* **Requirement:** Akun Cisco Skills for All.
* **Prosedur:**
1. Masuk ke kursus instruksional *Networking Basics* (Durasi 22 Jam).
2. Tonton dan selesaikan seluruh modul terkait *OSI Layer* (Layer 1-7) dan *TCP/IP Model*.
3. Selesaikan kuis evaluasi pemahaman topologi jaringan.


* **Target Output:** Bar progres kursus *Networking Basics* mencapai angka penyelesaian 100%.

### Minggu 6: CLI Network Troubleshooting

* **Requirement:** Akun Cisco Skills for All, Terminal CLI (Command Prompt/Bash), Wireshark terinstal.
* **Prosedur:**
1. Masuk ke kursus *Network Addressing and Basic Troubleshooting* (Durasi 14 Jam).
2. Buka terminal perangkat lokal, jalankan perintah diagnostik `ping 8.8.8.8` dan `traceroute 8.8.8.8` (atau `tracert` di Windows).
3. Buka Wireshark, pilih *interface* jaringan aktif (misal: wlan0/eth0), dan amati lalu lintas paket ICMP yang baru saja dikirim.


* **Target Output:** *Digital Badge* kelulusan resmi Cisco dan log tangkapan layar paket ICMP di dalam dasbor Wireshark.

---

## 💻 FASE 3: RANK 3 - FORGE

**Fokus:** Anatomi Aplikasi Web & Pemindaian Kode Statis (SAST)

### Minggu 7: Manajemen Versi Kode & Anatomi Web

* **Requirement:** Instalasi Git lokal, Akun GitHub.
* **Prosedur:**
1. Akses The Odin Project: *Foundations Course* (Bagian *Basics of the Web*).
2. Inisialisasi Git di terminal menggunakan perintah `git init`.
3. Buat repositori untuk kerangka proyek web baru, yang ke depannya dapat di-*deploy* menggunakan infrastruktur VPS (*Virtual Private Server*) atau dialihkan ke domain khusus pengerjaan proyek (seperti arsitektur manajemen `pkm.namadomain.com`).
4. Eksekusi `git add`, `git commit`, dan `git push` ke GitHub.


* **Target Output:** Tautan repositori GitHub pribadi yang memuat fail *README.md* pertama.

### Minggu 8: Web Structure (DOM Manipulation)

* **Requirement:** *Code Editor* (Visual Studio Code), Modul *HTML Foundations* (The Odin Project).
* **Prosedur:**
1. Buat berkas `index.html`.
2. Rancang kerangka *Document Object Model* (DOM) yang berisi struktur *Form Input* lengkap dengan tag `<form>`, `<input>`, dan `<button>`.
3. Buka fail tersebut secara lokal di peramban web.


* **Target Output:** Berkas statis `.html` dengan elemen form input yang tervisualisasi di peramban web.

### Minggu 9: Web Profiling & Network Inspector

* **Requirement:** Peramban Web (Google Chrome/Mozilla Firefox), Modul *CSS Foundations*.
* **Prosedur:**
1. Terapkan tata letak dasar menggunakan CSS *Box Model* pada form yang dibuat di minggu ke-8.
2. Buka fitur *Developer Tools* bawaan peramban (F12) dan arahkan ke bagian *Network Tab*.
3. Klik tombol *submit* pada form HTML tersebut dan amati pembentukan paket *Request* yang terekam secara *live* di *Network Tab*.


* **Target Output:** Tangkapan layar *Network Tab* yang menangkap *Request Header* saat tombol statis ditekan.

### Minggu 10: Client-Side Logic & Hardcoded Secret Scan

* **Requirement:** Modul *JavaScript Fundamentals Part 1-3*, Instalasi CLI Trivy.
* **Prosedur:**
1. Sisipkan fail `script.js` yang memuat fungsi kalkulasi sederhana dan deklarasi variabel statis ke dalam proyek HTML.
2. Sisipkan teks *dummy secret* secara sengaja ke dalam kode (Contoh: `const API_KEY = "AKIAIOSFODNN7EXAMPLE";`).
3. Buka terminal pada direktori proyek tersebut, eksekusi perintah pemindaian keamanan kode: `trivy fs .`.


* **Target Output:** Log tangkapan layar terminal yang menampilkan indikator peringatan Trivy saat berhasil mendeteksi "Hardcoded Secret".

---

## 🔴 FASE 4: RANK 2 - BREACH

**Fokus:** Metodologi Penetrasi Web & Dokumentasi Celah (Bug Ticketing)

### Minggu 11: Proxy Interception & Bind Shell Readiness

* **Requirement:** Burp Suite Community Edition, FoxyProxy, Netcat (nc).
* **Prosedur:**
1. Atur ekstensi FoxyProxy untuk merutekan lalu lintas ke *listener* lokal Burp Suite (`127.0.0.1:8080`).
2. Aktifkan *Intercept* di Burp Suite, kunjungi `http://testphp.vulnweb.com/`, dan tahan paket HTTP yang lewat. Modifikasi parameter *User-Agent* pada *header* menjadi `TISS-Agent` lalu klik *Forward*.
3. Buka terminal baru, ketik `nc -lvnp 4444` lalu tekan *Enter* untuk menyiapkan perangkat menangkap koneksi eksekusi jarak jauh.


* **Target Output:** **Operational Readiness Log:** Tangkapan layar 1 (Bukti modifikasi *header* di Burp Suite), Tangkapan layar 2 (Netcat *listening mode* aktif di terminal).

### Minggu 12: Eksploitasi Database (SQLi)

* **Requirement:** Akun PortSwigger Web Security Academy.
* **Prosedur:**
1. Akses laboratorium *SQL Injection*.
2. Lakukan injeksi parameter menggunakan sintaks SQL spesifik (misal: `' OR 1=1--`) pada kolom pencarian atau otentikasi.
3. Dokumentasikan parameter yang rentan dan berhasil tereksekusi.


* **Target Output:** **Bug Ticket 1:** Format rapi berisi URL Target, Kategori Kerentanan, Level *Severity*, dan deskripsi *Proof of Concept* (PoC) langkah demi langkah.

### Minggu 13: Manipulasi Direktori (Path Traversal)

* **Requirement:** PortSwigger Web Security Academy, Burp Suite.
* **Prosedur:**
1. Akses laboratorium *Path Traversal*.
2. Tangkap paket HTTP pengunduhan gambar di Burp Suite.
3. Modifikasi parameter nama berkas (*filename*) dengan injeksi mundur `../../../etc/passwd`.
4. Analisis respons server di kolom *Response*.


* **Target Output:** **Bug Ticket 2:** Berisi PoC tangkapan layar Burp Suite saat berkas sistem *server* berhasil terekstraksi ke layar klien.

### Minggu 14: Logic Bypass & IDOR

* **Requirement:** PortSwigger Web Security Academy, Burp Suite.
* **Prosedur:**
1. Akses laboratorium *Access Control* dan *Business Logic Vulnerabilities*.
2. Analisis alur logika pembayaran atau pengelolaan sesi akun tanpa melakukan injeksi *syntax*.
3. Lakukan modifikasi parameter secara horizontal (*Insecure Direct Object Reference* / IDOR) untuk mengakses panel konfigurasi pengguna lain.


* **Target Output:** **Bug Ticket 3:** Berisi PoC cara memanipulasi celah logika bisnis atau eskalasi hak akses mendatar.

### Minggu 15: Eksekusi Berbasis Klien (XSS)

* **Requirement:** PortSwigger Web Security Academy.
* **Prosedur:**
1. Akses laboratorium *Cross-Site Scripting (XSS)*.
2. Terapkan pemahaman dasar DOM (Fase Forge) untuk merancang vektor serangan `<script>alert(document.cookie)</script>`.
3. Injeksi *payload* tersebut ke dalam kolom ulasan (*Stored*) atau bilah URL (*Reflected*).


* **Target Output:** **Bug Ticket 4:** Dokumentasi eksekusi *payload* XSS yang berhasil lolos dari filter aplikasi.

### Minggu 16 - 18: Makro-Dokumentasi & Triase CVSS

* **Requirement:** Basis data 4 *Bug Ticket* (Minggu 12-15), Sistem Penilaian CVSS.
* **Prosedur:**
1. Kumpulkan seluruh tiket kerentanan.
2. Lakukan kalkulasi metrik *Common Vulnerability Scoring System* (CVSS) untuk setiap celah.
3. Satukan data tersebut ke dalam satu templat laporan pentest formal.
4. Tulis bab *Executive Summary* yang menyoroti eksklusif celah dengan tingkat *Critical/High* beserta rekomendasi penambalannya (*Patching*).


* **Target Output:** Dokumen final **Full Penetration Testing Report** yang diserahkan untuk asesmen komite White Teaming Guild.

---

## 🔵 FASE 5: RANK 1 - SENTINEL

**Fokus:** Postur Pertahanan, Deteksi Anomali, & Respons Insiden

### Minggu 19: Vulnerability Management & Scanner Eksternal

* **Requirement:** Instalasi Nessus Essentials lokal, Klien OpenVPN, Akun TryHackMe.
* **Prosedur:**
1. Unduh berkas konfigurasi OpenVPN dari dasbor TryHackMe dan lakukan koneksi.
2. Aktifkan modul *Basic Pentesting* atau ruangan *Metasploitable* di TryHackMe (untuk mendapatkan target IP legal di jaringan VPN).
3. Eksekusi pemindaian *Basic Network Scan* via Nessus Essentials yang diarahkan ke IP target TryHackMe tersebut.
4. Tunggu pemindaian selesai dan baca dasbor klasifikasi risiko.


* **Target Output:** **SOC Shift Handover Log 1:** Menyajikan temuan spesifik Nessus berstatus *Critical* dan rekomendasi tindakan (Misal: Port 21 FTP versi lama, rekomendasikan pembaruan paket sistem).

### Minggu 20: Triage Log Statis & SPL Ninja

* **Requirement:** Instalasi Splunk Free lokal, Unduhan data log `access.log` Apache/Nginx (berasal dari *SecRepo.com* atau repositori internal TISS).
* **Prosedur:**
1. Lakukan *Drag-and-Drop* berkas `access.log` ke fitur *Add Data* di Splunk Free.
2. Buka antarmuka pencarian (Search & Reporting).
3. Gunakan *Splunk Processing Language* (SPL) dasar, misal: `sourcetype=access_combined | search "UNION SELECT" OR "/etc/passwd"` untuk memfilter injeksi berbahaya dari ribuan log normal.


* **Target Output:** **SOC Shift Handover Log 2:** Laporan tangkapan layar *query* SPL dan isolasi *IP Address* penyerang yang terekam di dalam log.

### Minggu 21: Live SIEM Simulation (Cloud)

* **Requirement:** Peramban Web, Akun TryHackMe.
* **Prosedur:**
1. Akses ruangan simulasi **Wazuh** di TryHackMe (Gratis).
2. Lakukan eksplorasi dasbor *Endpoint Detection and Response* (EDR) yang sudah disediakan.
3. Identifikasi peringatan pergerakan lateral agen yang terpicu secara *real-time* di dasbor tersebut.


* **Target Output:** **SOC Shift Handover Log 3:** Identifikasi ID peringatan spesifik dan deskripsi singkat anomali yang terdeteksi Wazuh.

### Minggu 22: Diseksi Phishing & Network PCAP

* **Requirement:** Modul Let's Defend (*Phishing Email Analysis*), Unduhan arsip dari Malware-Traffic-Analysis.net, Wireshark.
* **Prosedur:**
1. Bagian 1: Pelajari cara membedah integritas *Email Header* (SPF, DKIM, DMARC) di modul Let's Defend.
2. Bagian 2: Kunjungi situs Malware-Traffic-Analysis, unduh satu *dataset* PCAP spesifik. Buka ekstrak berkas dengan sandi `infected`.
3. Tarik berkas PCAP ke Wireshark. Analisis transaksi paket HTTP (Filter: `http.request`) untuk menemukan URL pengunduhan muatan (*payload*).


* **Target Output:** **SOC Shift Handover Log 4:** Mencatat parameter SPF email yang gagal (fail) dan domain *Command & Control* (C2) dari hasil filtrasi Wireshark.

### Minggu 23 - 24: Real-World Threat Hunting

* **Requirement:** Dasbor Platform CyberDefenders (Gratis), *Dataset Network Forensics* atau *Endpoint Forensics*.
* **Prosedur:**
1. Masuk ke sesi latihan investigasi di CyberDefenders.
2. Analisis seluruh artefak yang diberikan secara kolektif (memadukan keahlian Splunk, Wireshark, dan intelijen ancaman OSINT).
3. Jawab kueri pelacakan musuh untuk menemukan vektor masuk utama (*Initial Access*).
4. Tulis hasil investigasi secara naratif dan kronologis.


* **Target Output:** Dokumen **Incident Response Report (IRR)**. Memuat abstraksi insiden siber utuh, Tabel *Indicator of Compromise* (IoC), metodologi *Root Cause Analysis* (RCA), serta desain perbaikan arsitektur sistem keamanan yang diusulkan. Rekap akhir diajukan kepada panel TISS (Executive Board/L2).