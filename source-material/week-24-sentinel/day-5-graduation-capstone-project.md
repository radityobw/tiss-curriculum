# 🛡️ Week 24 · Day 5: Graduation Capstone Project & Sentinel Trial

> **Rank**: SENTINEL | **Minggu ke-24**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓▓▓] 100% — SENTINEL Rank (Minggu 5 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 100% — Hari 120 dari 120 (GRADUATION DAY)

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → ✅ BREACH → ✅ **SENTINEL (GRADUATED)**

---

## 📝 Rekap Minggu Ini (The Final Week)

Penobatan kapabilitas manajerial respons insiden siber tingkat lanjut akan dievaluasi pada penugasan *Capstone* minggu ini:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Incident Briefing & Triage | Menentukan batasan ruang lingkup (*Scope*) insiden serta memprioritaskan peringatan berdasarkan tingkat bahaya (*Triage*). |
| Day 2 | Forensics & Root Cause Analysis | Mengekstrak barang bukti forensik (*IOCs*), melacak pintu masuk penyerang (*Root Cause*), dan memetakannya ke standar intelijen ancaman *MITRE ATT&CK*. |
| Day 3 | Eradication & Remediation | Meracik aturan pencegahan (IPS Rule), memusnahkan ancaman, dan memastikan celah keamanan telah tertambal (*Patching/Remediation*). |
| Day 4 | Incident Report Writing | Merangkum seluruh proses penanganan insiden menjadi dokumen resmi yang memuat *Executive Summary* dan *Timeline* untuk pelaporan korporat. |

---

## 🧪 Hands-On Lab (The Final Trial)

### Prerequisites
- Aplikasi pengolah teks atau Markdown (Notepad/VS Code).

### Misi Hari Ini: "Merancang Naskah Laporan Respons Insiden (Incident Report Capstone)"

Pada modul puncak evaluasi ini, peran Anda bukan lagi sekadar pelaksana analitik, melainkan seorang **Incident Commander**. Anda ditugaskan untuk merakit laporan penanganan insiden formal yang merangkum keseluruhan skenario simulasi insiden minggu ini (Mulai dari insiden peretasan Web SQLi, hingga penanaman malware `svchost.exe` di Database).

### Step 1: Penulisan Executive Summary (Ringkasan Eksekutif)
1. Tulis sebuah komposisi ringkas (satu paragraf, tanpa menyertakan elemen teknis seperti *Hash* atau kode eksploitasi) yang mendeskripsikan insiden pada *Web Server* (192.168.1.100) dan *Database Server* (10.0.0.55).
2. Tegaskan konfirmasi bahwa tim SOC telah berhasil mengeksekusi pemutusan akses penyerang dan memulihkan layanan sistem operasional organisasi kembali normal 100%.

### Step 2: Penyusunan Incident Timeline (Rekonstruksi Kronologi)
1. Buat pemaparan riwayat kejadian berdasarkan urutan waktu. (Misalnya: `03:00` - Sistem SIEM Splunk memicu peringatan serangan SQL Injection; `03:15` - Server Database dikarantina (Tahap Containment); `04:00` - Pembaruan filter IPS Suricata diterapkan untuk memblokir IP penyerang asal Rusia).

### Step 3: Inventarisasi Teknis TTPs & Pemetaan MITRE ATT&CK
1. Konfigurasikan pemetaan penamaan metode spesifik eksploitasi peretas menggunakan taksonomi intelijen ancaman. (Misal: Klasifikasi T1190 - *Exploit Public-Facing Application* pada kerentanan SQLi; dan klasifikasi T1036 - *Masquerading* atas metode kamuflase file `svchost.exe`).

### Step 4: Perumusan Rekomendasi Lessons Learned (Evaluasi Strategis)
1. Buat rekomendasi perbaikan untuk mencegah insiden terulang. (Misal: Divisi *Web Development* diwajibkan untuk mengimplementasikan pedoman *Secure Coding* dan sanitasi input, serta melakukan *Penetration Testing* berkala agar terhindar dari penetrasi *SQLi*).

---

## 🎯 Capstone Mission

### Misi: "Cyber Incident Report & Portfolio Emas (Graduation)"

**Deskripsi:** Ini adalah dokumen pengesahan kompetensi puncak Anda dalam pengawasan dan respons keamanan sistem siber korporat.

**Tugas Mandiri:** Mengacu kepada kerangka panduan (Step 1 hingga 4) di atas, susunlah draf laporan insiden formal tersebut!

**Deliverables:**
1. Satu file markdown berjudul `CAPSTONE_INCIDENT_REPORT.md`.
2. Dokumen laporan ini wajib merangkum insiden minggu ini ke dalam empat struktur:
 - **Executive Summary (Ringkasan Non-Teknis)**
 - **Incident Timeline (Rentetan Kronologi)**
 - **Technical TTPs & IOCs (Temuan Forensik & Taktik)**
 - **Lessons Learned (Rekomendasi Perbaikan)**
3. **BONUS PORTFOLIO:** Unggah arsip dokumen Laporan Insiden ini beserta *Threat Hunting Playbook* Anda ke repositori **GitHub** publik untuk disematkan sebagai portfolio kualifikasi rekrutmen profesional SOC!

**Kriteria Sukses:**
- [ ] Berhasil membuat dokumen pelaporan `CAPSTONE_INCIDENT_REPORT.md`.
- [ ] Bagian *Executive Summary* ditulis dengan gaya bahasa naratif manajerial yang profesional, singkat, dan bersih dari jargon *Hash* rumit.
- [ ] Bagian *Lessons Learned* memberikan masukan logis yang secara langsung mengatasi akar permasalahan (*Root Cause*).

---

## 💡 Knowledge Check (The Final Exam)

<details>
<summary>❓ [MUDAH] Mengacu pada kerangka insiden PICERL, fase manakah yang menugaskan spesialis untuk menentukan prioritas peringatan log (Triage) serta menarik batasan area penyebaran infeksi (Scope)?</summary>

**Jawaban:** Fase Identification (Identifikasi).
</details>

<details>
<summary>❓ [MUDAH] Di ranah forensik digital, dokumentasi apa yang wajib dijaga agar integritas barang bukti (seperti Hard Disk pelaku) diakui sah di mata hukum dan persidangan?</summary>

**Jawaban:** Chain of Custody (Rantai Kustodi).
</details>

<details>
<summary>❓ [SEDANG] Berkaitan dengan penyusunan Laporan Insiden, bagian manakah yang mutlak diletakkan di halaman pertama, dirancang untuk dibaca oleh CEO/Manajemen, dan dilarang keras berisi jargon teknikal?</summary>

**Jawaban:** Executive Summary (Ringkasan Eksekutif).
</details>

<details>
<summary>❓ [SEDANG] Dalam penyusunan parameter IPS (Intrusion Prevention System) seperti Suricata, jika SOC menugaskan intervensi untuk menghentikan paket ancaman dari IP penyerang, parameter (berawalan huruf D) apa yang harus diletakkan di awal baris *Rule*?</summary>

**Jawaban:** Parameter `drop` (Drop Action).
</details>

<details>
<summary>❓ [SULIT] Dalam alur PICERL, mengapa tim Blue Team sangat melarang pengembalian server ke layanan internet publik (Fase Recovery) jika tahap penambalan akar kerentanan (Fase Remediation) belum dilakukan?</summary>

**Jawaban:** Karena jika infrastruktur server dipulihkan dan di-*Online*-kan ke publik dalam kondisi celah awal (*Root Cause*) seperti *SQL Injection* belum tertambal, maka penyerang manapun akan langsung menggunakan celah terbuka tersebut untuk kembali meretas dan menginfeksi ulang server. Pemulihan tanpa penambalan sama saja mempersilakan peretas masuk kembali.
</details>

---

## 📋 Graduation Checklist

- [ ] Saya memahami fundamental operasional siklus *Incident Response (PICERL)*.
- [ ] Saya menguasai mekanisme mitigasi operasional menggunakan *SIEM Splunk & IPS Suricata*.
- [ ] Saya memahami pemetaan intelijen taksonomi global *MITRE ATT&CK*.
- [ ] Saya telah membuktikan kapabilitas dengan menyetor penugasan laporan `CAPSTONE_INCIDENT_REPORT.md`.
- [ ] SAYA TELAH MENYAMPAIKAN DEDIKASI PENUH SELAMA 24 MINGGU!

---

## 💬 Pesan Kelulusan (TISS Null Teaming)

Kepada Ahli Strategi Keamanan (Sentinel),

Sepanjang perjalanan pelatihan 24 Minggu (120 Hari) ini, Anda telah membuktikan transisi kapabilitas yang luar biasa. Beranjak dari level pemula yang meraba abstraksi sistem keamanan (*VOID*), membedah enkripsi dan kriptografi (*CIPHER*), mengendalikan topologi jaringan dan arsitektur peladen (*PACKET*), membangun pemrograman otomasi peretasan dan *web development* (*FORGE*), mengeksekusi uji penetrasi ofensif tingkat lanjut ke server klien (*BREACH*), hingga mencapai puncak penguasaan operasional otoritas pertahanan, forensik, dan respons krisis skala enterprise (*SENTINEL*).

Validasi kapabilitas telah tercapai. Integrasi pemantauan *SIEM Splunk*, sensor pencegahan perimeter *Suricata*, kaidah pembedahan *Digital Forensics*, dan referensi intelijen *MITRE ATT&CK Framework* kini berada di bawah kendali komando PICERL Anda.

Selamat! Predikat **SENTINEL** telah resmi disematkan pada kredensial nama Anda. Terus sempurnakan repositori portofolio GitHub Anda, songsong dunia karir keamanan siber dengan percaya diri, dan lindungilah infrastruktur teknologi bangsa ini dari ancaman kejahatan siber!

---

## 🏆 THE FINAL ACHIEVEMENT UNLOCKED!

```
┌───────────────────────────────────────────────┐
│                                               │
│       🛡️ SENTINEL OF THE ABYSS (GRADUATED)  │
│        TISS Null Teaming Bootcamp Complete    │
│    "You have walked through the fire          │
│        of the offensive arts,                 │
│    only to forge the ultimate shield.         │
│      The cyber battlefield is yours."         │
│                                               │
└───────────────────────────────────────────────┘
```

> 🚀 *"This is not the end. This is Day Zero of your real war. Welcome to TISS, Sentinel."*

---

*📅 TISS Null Teaming · Week 24 · Day 5 · SENTINEL Rank (CURRICULUM FINISHED)*
