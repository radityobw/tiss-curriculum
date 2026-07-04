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

Puncak evaluasi kemampuan respons insiden Anda akan diuji pada penugasan *Capstone* minggu ini:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Incident Briefing & Triage | Menentukan ruang lingkup (*Scope*) insiden serta memilah peringatan keamanan (*Triage*). |
| Day 2 | Forensics & Root Cause Analysis | Mengumpulkan bukti forensik (*IOCs*), menganalisis celah awal (*Root Cause*), dan memetakannya ke *MITRE ATT&CK*. |
| Day 3 | Eradication & Remediation | Menghapus jejak ancaman (*Eradication*), memblokir IP penyerang, dan memastikan celah telah ditambal (*Patching/Remediation*). |
| Day 4 | Incident Report Writing | Merangkum seluruh tahapan respons insiden menjadi dokumen resmi yang mencakup *Executive Summary* dan *Timeline*. |

---

## 🧪 Hands-On Lab (The Final Trial)

### Prerequisites
- Aplikasi pengolah teks atau Markdown (Notepad/VS Code).

### Misi Hari Ini: "Menyusun Laporan Respons Insiden (Incident Report Capstone)"

Pada tahap evaluasi akhir ini, Anda akan berperan sebagai **Incident Commander**. Tugas Anda adalah menyusun Laporan Insiden formal yang mendokumentasikan skenario peretasan pada *Web Server* dan *Database Server* (kasus SQL Injection dan *malware*).

### Step 1: Penulisan Executive Summary (Ringkasan Eksekutif)
1. Buat ringkasan satu paragraf (tanpa bahasa teknis seperti *Hash* atau nama eksploitasi) yang menjelaskan terjadinya pembobolan pada *Web Server* dan penyebaran ke *Database Server*.
2. Cantumkan bahwa tim keamanan telah berhasil mengisolasi serangan, membersihkan sistem, dan mengembalikan layanan operasional menjadi normal 100%.

### Step 2: Penyusunan Incident Timeline (Kronologi Insiden)
1. Buat urutan kejadian berdasarkan waktu. (Misalnya: `03:00` - SIEM mendeteksi peringatan serangan SQL Injection; `03:15` - Server Database dikarantina (*Containment*); `04:00` - Aturan IPS Suricata diperbarui untuk memblokir IP penyerang).

### Step 3: Inventarisasi TTPs & Pemetaan MITRE ATT&CK
1. Petakan metode penyerangan menggunakan taksonomi intelijen ancaman. (Misalnya: T1190 - *Exploit Public-Facing Application* untuk celah SQLi; dan T1036 - *Masquerading* untuk kamuflase file berbahaya).

### Step 4: Perumusan Lessons Learned (Rekomendasi)
1. Buat rekomendasi perbaikan pencegahan. (Misalnya: Divisi *Web Development* diwajibkan menerapkan standar *Secure Coding* (sanitasi input) dan melakukan audit keamanan (*Penetration Testing*) berkala).

---

## 🎯 Capstone Mission

### Misi: "Cyber Incident Report & Portfolio Emas (Graduation)"

**Deskripsi:** Ini adalah penugasan akhir yang memvalidasi kompetensi Anda dalam menangani insiden keamanan siber korporat.

**Tugas Mandiri:** Mengacu pada langkah (Step 1 hingga 4) di atas, susunlah draf laporan insiden tersebut!

**Deliverables:**
1. Satu file Markdown berjudul `CAPSTONE_INCIDENT_REPORT.md`.
2. Laporan ini wajib memuat empat komponen utama:
   - **Executive Summary (Ringkasan Eksekutif)**
   - **Incident Timeline (Kronologi Insiden)**
   - **Technical TTPs & IOCs (Temuan Teknis & Forensik)**
   - **Lessons Learned (Rekomendasi Perbaikan)**
3. **BONUS PORTFOLIO:** Unggah arsip dokumen Laporan Insiden ini beserta *Threat Hunting Playbook* (dari modul sebelumnya) ke repositori **GitHub** publik sebagai portofolio kualifikasi karier Anda!

**Kriteria Sukses:**
- [ ] Berhasil membuat dokumen `CAPSTONE_INCIDENT_REPORT.md`.
- [ ] Bagian *Executive Summary* ditulis dengan bahasa bisnis yang profesional dan bebas dari jargon teknis.
- [ ] Bagian *Lessons Learned* memberikan masukan logis yang secara langsung mengatasi akar permasalahan (*Root Cause*).

---

## 💡 Knowledge Check (The Final Exam)

<details>
<summary>❓ [MUDAH] Dalam standar penanganan insiden PICERL, fase manakah yang bertanggung jawab untuk memilah peringatan log (Triage) serta menentukan batasan area penyebaran infeksi (Scope)?</summary>

**Jawaban:** Fase Identification (Identifikasi).
</details>

<details>
<summary>❓ [MUDAH] Dalam forensik digital, dokumen apa yang wajib dijaga agar riwayat kepemilikan dan penanganan barang bukti tetap sah di mata hukum?</summary>

**Jawaban:** Chain of Custody (Rantai Kustodi).
</details>

<details>
<summary>❓ [SEDANG] Pada penyusunan Laporan Insiden, bagian manakah yang ditujukan khusus untuk CEO/Manajemen dan dilarang memuat jargon teknis?</summary>

**Jawaban:** Executive Summary (Ringkasan Eksekutif).
</details>

<details>
<summary>❓ [SEDANG] Saat mengonfigurasi aturan keamanan pada IPS (seperti Suricata), parameter apa yang digunakan untuk menginstruksikan sistem agar langsung memblokir/menggugurkan lalu lintas dari IP penyerang?</summary>

**Jawaban:** Parameter `drop` (Drop Action).
</details>

<details>
<summary>❓ [SULIT] Mengapa fase pemulihan sistem (Recovery) tidak boleh dilakukan jika celah kerentanan awal (Root Cause) belum ditambal (Remediation)?</summary>

**Jawaban:** Karena jika server disambungkan kembali ke internet tanpa menambal *Root Cause*, penyerang dapat mengeksploitasi celah tersebut untuk masuk kembali dan menginfeksi server ulang.
</details>

---

## 📋 Graduation Checklist

- [ ] Saya memahami fundamental operasional siklus *Incident Response (PICERL)*.
- [ ] Saya menguasai mitigasi operasional menggunakan *SIEM* dan *IPS*.
- [ ] Saya memahami pemetaan taksonomi serangan menggunakan *MITRE ATT&CK*.
- [ ] Saya telah menyelesaikan penugasan akhir `CAPSTONE_INCIDENT_REPORT.md`.
- [ ] Saya telah menyelesaikan pelatihan selama 24 minggu.

---

## 💬 Pesan Kelulusan

Selamat! Anda telah menyelesaikan seluruh rangkaian kurikulum 24 Minggu (120 Hari) di TISS Null Teaming.

Dari tahap pemahaman dasar sistem (*VOID*), enkripsi data (*CIPHER*), topologi jaringan (*PACKET*), pemrograman (*FORGE*), hingga simulasi pengujian penetrasi (*BREACH*) dan manajemen respons insiden siber skala enterprise (*SENTINEL*), Anda telah membuktikan dedikasi dan kemampuan Anda di bidang keamanan siber.

Validasi kompetensi Anda dalam menggunakan alat pantau (SIEM), sensor pencegahan jaringan (IPS), prosedur forensik digital, dan intelijen ancaman (*MITRE ATT&CK*) telah teruji.

Terus bangun portofolio karier Anda, gunakan ilmu ini secara etis, dan bersiaplah untuk berkontribusi dalam menjaga keamanan infrastruktur teknologi. 

---

## 🏆 ACHIEVEMENT UNLOCKED!

```
┌───────────────────────────────────────────────┐
│                                               │
│       🛡️ SENTINEL RANK (GRADUATED)            │
│        TISS Null Teaming Bootcamp Complete    │
│                                               │
│    Dedikasi, Disiplin, dan Konsistensi        │
│    telah membawa Anda ke tahap akhir ini.     │
│    Selamat bertugas di dunia profesional!     │
│                                               │
└───────────────────────────────────────────────┘
```

> 🚀 *"Keamanan siber adalah proses berkelanjutan. Selamat berkarya dan teruslah belajar, Sentinel."*

---

*📅 TISS Null Teaming · Week 24 · Day 5 · SENTINEL Rank (CURRICULUM FINISHED)*
