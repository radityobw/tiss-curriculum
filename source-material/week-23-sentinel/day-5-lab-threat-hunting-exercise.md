# 🛡️ Week 23 · Day 5: Lab & Weekly Mission Threat Hunting Exercise

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓░░] 80% — SENTINEL Rank (Minggu 4 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░] 95% — Hari 115 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → ✅ BREACH → 🔄 SENTINEL

---

## 📝 Rekap Minggu Ini

Modul pada minggu ini berfokus pada transisi kompetensi dari pemantauan keamanan otomatis ke investigasi manual secara proaktif (*Threat Hunting* & *Forensics*).

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Proactive vs Reactive Security | Memahami konsep perburuan ancaman (*Threat Hunting*) menggunakan pendekatan hipotesis (*Hypothesis-Driven Approach*). |
| Day 2 | MITRE ATT&CK Framework | Memetakan dan mengklasifikasi taktik dan teknik peretas menggunakan taksonomi TTPs (*Tactics, Techniques, Procedures*). |
| Day 3 | Digital Forensics Basics | Memahami prosedur penanganan barang bukti elektronik (*Chain of Custody*) dan proses penyalinan (*Forensic Imaging / Hashing*). |
| Day 4 | Memory & Disk Forensics | Mengetahui prioritas pengamanan data berdasarkan *Order of Volatility* dan analisis memori menggunakan *Volatility Framework*. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Aplikasi teks editor (*Notepad, VS Code, dll.*).
- Koneksi internet untuk membuka referensi taktik di *MITRE ATT&CK Navigator* (opsional).

### Misi Hari Ini: "Membangun Pedoman Berburu (Hunting Playbook Engineering)"

Spesialis SOC tingkat lanjut (*Threat Hunter*) harus mampu mendokumentasikan prosedur pencarian ancaman secara sistematis. Pada sesi kali ini, praktikum difokuskan pada pembuatan *Threat Hunting Playbook*. Dokumen ini digunakan sebagai standar panduan tim *SOC* untuk melacak teknik spesifik dari kelompok peretas (APT).

### Step 1: Memilih Skenario (Teknik MITRE)
1. **Skenario:** Berdasarkan tren keamanan terbaru, diketahui peretas sering menggunakan teknik *Persistence* (Mempertahankan akses) agar *malware* mereka tetap berjalan setiap kali *server* dinyalakan ulang.
2. Anda memilih salah satu teknik dari matriks MITRE ATT&CK: **T1053 - Scheduled Task/Job**. (Teknik ini menyalahgunakan fitur *Task Scheduler* di Windows agar beban muatan (*payload*) peretas dieksekusi secara otomatis dan berulang).

### Step 2: Merumuskan Hipotesis (*The Hunter's Hypothesis*)
1. Buatlah dugaan awal berdasarkan teknik T1053 tersebut.
2. **Contoh Hipotesis:**
   *"Berdasarkan intelijen, kelompok APT mungkin telah menyusup dan berusaha mempertahankan akses (Persistence) di dalam server kita. Hipotesis saya adalah mereka menyalahgunakan fitur Windows Scheduled Tasks (T1053) untuk mengeksekusi skrip backdoor secara otomatis setiap tengah malam di luar jam operasional."*

### Step 3: Menentukan Sumber Log (*Data Sources*) dan Kueri Splunk
1. Tentukan sumber log (dari sistem operasi Windows) yang mencatat aktivitas pembuatan *Scheduled Task* baru.
2. **Sumber Log:** Anda mengidentifikasi bahwa kejadian ini dicatat pada **Windows Security Event ID 4698** (*A scheduled task was created*).
3. **Kueri Splunk (SIEM Hunting Syntax):**
   `index=windows_sec EventCode=4698 | table _time, ComputerName, Task_Name, Task_Content`
   *(Penjelasan: Kueri ini akan menyaring seluruh log pembuatan task baru, lalu menampilkannya dalam tabel yang berisi waktu kejadian, nama komputer, nama task, dan isi perintah task tersebut untuk diperiksa lebih lanjut).*

---

## 🎯 Weekly Mission

### Misi: "Menyusun Buku Pedoman Perburuan (Threat Hunting Playbook)"

**Deskripsi:**
Seorang *Threat Hunter* bertugas memberikan instruksi penelusuran kepada tim SOC agar operasi pencarian ancaman di jaringan dapat berjalan terarah. Pada misi ini, Anda diminta untuk menyusun *Playbook* berdasarkan latihan di atas.

**Tugas Mandiri:**
Mengacu pada alur praktikum di atas (Step 1 hingga 3), ubah hasil analisis tersebut menjadi format pelaporan dokumen *Hunting Playbook*.

**Deliverables:**
1. Buat *file* berekstensi *Markdown* bernama `THREAT_HUNTING_PLAYBOOK.md`.
2. Di dalam dokumen tersebut, susun laporan yang memuat 4 parameter berikut:
   - **Taktik & Teknik MITRE:** Sebutkan ID dan nama teknik dari MITRE ATT&CK (Misal: *T1053 Scheduled Task*).
   - **Hipotesis (Hypothesis):** Tuliskan narasi dugaan ancaman (*Hypothesis*).
   - **Sumber Data (Log Sources):** Sebutkan jenis log yang diperlukan (misal: *Event ID 4698*).
   - **Tindakan Lanjut (Triage/Mitigation):** Jelaskan langkah respons yang harus dilakukan jika peretasan benar-benar ditemukan (Contoh: Isolasi komputer dengan mencabut kabel LAN, lalu instruksikan tim forensik untuk melakukan ekstraksi memori RAM menggunakan *Volatility*).

**Kriteria Sukses:**
- [ ] Tersedianya dokumen `THREAT_HUNTING_PLAYBOOK.md`.
- [ ] Mencantumkan ID teknik standar *MITRE ATT&CK*.
- [ ] Hipotesis logis dan merujuk pada sumber data log yang tepat (*Event ID*).

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Apa sebutan metodologi di mana analis SOC secara proaktif menyusun dugaan/asumsi serangan (misal: "Saya curiga *hacker* mengeksploitasi *Powershell*") sebelum mulai mencari bukti log di SIEM?</summary>

**Jawaban:** Pendekatan Berbasis Hipotesis (*Hypothesis-Driven Approach*).
</details>

<details>
<summary>❓ [MUDAH] Dalam standar *MITRE ATT&CK*, singkatan dari apakah <i>TTPs</i> yang digunakan untuk memetakan perilaku peretas?</summary>

**Jawaban:** *Tactics, Techniques, and Procedures* (TTPs).
</details>

<details>
<summary>❓ [SEDANG] Dalam prosedur forensik penegakan hukum, mengapa pencatatan dokumen riwayat perpindahan barang bukti (*Chain of Custody*) diwajibkan secara mutlak?</summary>

**Jawaban:** Tanpa dokumen yang mencatat siapa, kapan, dan di mana barang bukti tersebut berpindah tangan (Riwayat kontrol), integritas barang bukti tidak bisa dipertanggungjawabkan dan otomatis akan didiskualifikasi di pengadilan karena rawan dimanipulasi (*Data Tampering*).
</details>

<details>
<summary>❓ [SEDANG] Algoritma kriptografi apa (seperti *SHA-256*) yang selalu digunakan untuk memastikan bahwa *file* salinan forensik (*Forensic Image*) 100% identik dengan media aslinya dan tidak mengalami perubahan?</summary>

**Jawaban:** Hashing.
</details>

<details>
<summary>❓ [SULIT] Jika sebuah komputer terinfeksi <i>Ransomware</i>, mengapa tim <i>Incident Response</i> dilarang keras mematikan atau me-<i>restart</i> komputer tersebut?</summary>

**Jawaban:** Hal ini merujuk pada prinsip *Order of Volatility*. Memori RAM pada komputer bersifat *Volatile* (sementara dan mudah hilang jika tidak dialiri listrik). *Ransomware* yang sedang aktif menyimpan Kunci Dekripsi (*Decryption Key*) di dalam RAM. Jika komputer dimatikan atau di-*restart*, RAM akan terhapus, kunci dekripsi tersebut akan hilang selamanya, dan file yang terkunci mungkin tidak akan pernah bisa dibuka lagi.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya telah memahami metodologi *Threat Hunting* berbasis hipotesis.
- [ ] Saya memahami cara menggunakan matriks TTPs dari *MITRE ATT&CK Framework*.
- [ ] Saya mengetahui pentingnya dokumen kronologis penyitaan bukti (*Chain of Custody*).
- [ ] Saya memahami prosedur forensik seperti *Order of Volatility*, *Forensic Imaging*, dan *Hashing*.
- [ ] Saya telah menyelesaikan penyusunan `THREAT_HUNTING_PLAYBOOK.md`.

---

## 💬 Diskusi Minggu Ini

1. Selamat! Dirimu telah menyelesaikan materi intelijen dan forensik digital (*Threat Hunting & Digital Forensics*). Berdasarkan perbandingan antara sistem deteksi otomatis (SIEM/IPS) dan metode pelacakan proaktif manual (*Threat Hunting*), bagaimana pandanganmu tentang keseimbangan integrasi keduanya di dalam arsitektur SOC? Mengapa korporasi multinasional tidak bisa hanya mengandalkan otomatisasi untuk melawan ancaman *Advanced Persistent Threats (APT)*?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│      🕵️ THE CYBER DETECTIVE       │
│          Week 23 Complete           │
│      "Machines catch noise.         │
│     Humans hunt the silence."       │
│                                     │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 24: Capstone — Full Cycle Defense & Graduation**

Kurikulum TISS Null Teaming telah mencapai kulminasinya. Tidak ada lagi teori baru yang akan diperkenalkan. Minggu depan, kamu akan dihadapkan pada ujian pamungkas: **Capstone Project & Graduation Ceremony**.

Seluruh ilmu yang telah kamu pelajari selama 6 bulan terakhir—dari Kriptografi, Kerentanan Aplikasi Web (XSS/SQLi), Nmap, konfigurasi *Splunk/Suricata*, hingga prosedur Forensik dan *Threat Hunting*—akan diuji secara komprehensif. Kamu diwajibkan untuk menyusun Laporan Triage Respons Insiden lengkap (*Full Incident Response Triage Report*) sebagai syarat kelulusan untuk resmi menyandang gelar rank **SENTINEL**. Persiapkan dirimu!

---

*📅 TISS Null Teaming · Week 23 · Day 5 · SENTINEL Rank*
