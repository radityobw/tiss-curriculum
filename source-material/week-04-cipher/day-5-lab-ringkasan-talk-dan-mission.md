# 🔤 Week 4 · Day 5: Lab & Weekly Mission (CIPHER Finale!)

> **Rank**: CIPHER | **Minggu ke-4**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓▓▓] 100% — CIPHER Rank (Minggu 3 dari 3)

### Overall Journey
[▓▓▓▓░░░░░░░░░░░░░░░░░░░░] 16% — Hari 20 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → 🔄 PACKET → ⬜ FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Rank CIPHER (Week 2 - 4)

Selamat! Ini adalah hari terakhirmu belajar **Bahasa Inggris Teknis**. Kamu sudah melalui:

| Topik Utama | Key Takeaway yang harus diingat selamanya |
|------|-------------|
| **Reading & Vocab** | Menerjemahkan istilah teknis secara harfiah itu menyesatkan. Cari *keyword* (Scanning) untuk hemat waktu (CVE, CVSS). |
| **Writing & Comms** | Tulis laporan (*Bug Report*) yang terstruktur untuk dibaca manusia, dan bertanyalah dengan "Smart Way" (anti RTFM). |
| **Listening & Eval** | Biasakan telinga dengan *podcast* (Passive Learning). Kemampuan riilmu diukur dengan standar CEFR. |

---

## 🧪 Hands-On Lab (CIPHER Finale)

Hari ini kita akan menguji kemampuan *Listening*, *Reading*, dan *Writing*-mu sekaligus melalui presentasi DEF CON.

### Prerequisites
- Koneksi YouTube
- Akun GitHub & Repository `cybersec-journey`

### Step 1: Binge-Watch DEF CON (Listening)

Kamu akan diminta menonton sebuah video singkat dan sangat ikonik dari DEF CON 23.

1. Buka YouTube: **[DEF CON 23 - Jayson E. Street - Steal Everything, Kill Everyone, Cause Total Financial Ruin](https://www.youtube.com/watch?v=FjJmE6vWkKM)** (Jika video dihapus, cari judul yang sama di YouTube).
2. Tonton **10 menit pertama** video tersebut. Nyalakan CC (English) jika kesulitan.
3. Analisis apa yang sedang Jayson bicarakan. Apakah dia membahas *hacking* dengan laptop, atau *hacking* fasilitas fisik (membobol bank dengan jalan kaki)?

**Expected Output:**
```
Kamu mengerti bahwa presentasi ini membahas tentang Physical Penetration Testing (Social Engineering) di mana ia membobol bank di Beirut tanpa menggunakan kode komputer rumit.
```

### Step 2: Siapkan Folder Minggu 4

1. Buka VS Code, buka repository `cybersec-journey`.
2. Buat folder baru bernama `week-04`.
3. Di dalam folder `week-04`, buat file bernama `cipher-final-mission.md`.
4. Pindahkan gambar screenshot hasil EF SET-mu kemarin ke dalam folder `week-04` (beri nama `efset-result.png` atau sejenisnya).

---

## 🎯 Weekly Mission (Capstone CIPHER)

### Misi: "Cyber Intelligence Summarizer"

**Deskripsi:**
Ini adalah ujian akhir rank CIPHER. Kamu harus membuktikan bahwa kamu bisa mengonsumsi media berbahasa Inggris (video) dan merangkum *insight* pentingnya ke dalam format tertulis (*English*). Plus, mendeklarasikan *baseline* kemampuan bahasamu.

**Deliverables:**
Buka file `cipher-final-mission.md` yang baru kamu buat, lalu isi dengan format ini:

```markdown
# CIPHER Rank Finale: Intelligence Summary & Language Baseline

## Part 1: My English Baseline
- **EF SET Score**: [Tulis skor angka / CEFR Level dari tes kemarin, contoh: 62/100 (B2 Upper Intermediate)]
- **Screenshot Bukti**: 
![EF SET Result](./efset-result.png)
- **Refleksi Pribadi**: [Tulis 2 kalimat (Boleh bahasa Indonesia) tentang kelemahanmu: apakah lebih susah listening atau reading?]

## Part 2: DEF CON Talk Summary
**Talk Title**: DEF CON 23 - Jayson E. Street (Steal Everything...)

**Executive Summary (in English):**
[Tulis 1-2 paragraf DALAM BAHASA INGGRIS yang merangkum apa yang dilakukan Jayson di video 10 menit tersebut. Gunakan Grammarly/Spellchecker jika perlu, tapi JANGAN pakai Google Translate full dari Bahasa Indonesia! Cobalah berlatih merangkai kalimat sendiri].

**Key Takeaways (in English):**
1. [Poin penting 1 yang kamu pelajari dari video]
2. [Poin penting 2]
```

**Kriteria Sukses:**
- [ ] Folder `week-04` berisi file `cipher-final-mission.md` dan gambar `efset-result.png`
- [ ] Bukti skor EF SET terlampir dengan format markdown image `![alt](./namafile)` yang benar
- [ ] Bagian *Executive Summary* ditulis dalam Bahasa Inggris (minimal 3 kalimat)
- [ ] Ter-commit dan di-push ke GitHub
- [ ] Kamu tidak panik jika *grammar*-mu berantakan (Ingat! *Broken English* adalah hal biasa).

**Estimasi Waktu:** 1.5 – 2 jam

---

## 💡 Knowledge Check (CIPHER Final Quiz)

<details>
<summary>❓ [MUDAH] Mengapa "Membaca Dokumentasi dalam Bahasa Inggris" ditempatkan di rank CIPHER (paling awal setelah perkenalan)?</summary>

**Jawaban:** Karena di rank berikutnya (Packet, Forge, Breach), 90% materi, *command line*, dan *tools* yang akan digunakan hanya memiliki instruksi dalam bahasa Inggris. Tanpa kemampuan bahasa ini, kader akan kesulitan melakukan riset (RTFM/STFW) secara mandiri.

</details>

<details>
<summary>❓ [SEDANG] Bedakan secara fungsi bagian "Methodology" dan "Remediation" pada sebuah Bug Report.</summary>

**Jawaban:**
- **Methodology (Metodologi)** menjelaskan langkah dan *tools* apa saja yang digunakan selama pentest (Contoh: *"Kami menggunakan Nmap untuk scanning, dan BurpSuite untuk memanipulasi request"*).
- **Remediation (Rekomendasi)** berisi instruksi teknis kepada *developer* tentang cara memperbaiki celah yang ditemukan (Contoh: *"Harap sanitasi parameter input menggunakan fungsi htmlspecialchars()"*).

</details>

<details>
<summary>❓ [SEDANG] Apa kesalahan terbesar saat menonton video presentasi DEF CON yang sangat teknis?</summary>

**Jawaban:** Mencoba memahami setiap baris kode atau detail teknis yang ditampilkan di layar (*getting lost in the weeds*). Pemula harus fokus pada konsep besarnya: *"Apa dampak celah ini?"* dan *"Bagaimana konsep dasar serangannya?"*

</details>

<details>
<summary>❓ [SULIT] Sebuah kelompok peretas bernama APT29 diketahui menggunakan celah Zero-Day berbasis RCE untuk masuk WAF perusahaan. Celah tersebut dinilai memiliki CVSS 9.8. <br><br>Gunakan pengetahuan Alphabet Soup-mu minggu lalu untuk menerjemahkan SEMUA kata yang dicetak tebal!</summary>

**Jawaban:** 
Sebuah kelompok peretas tingkat tinggi yang didanai negara (**APT = Advanced Persistent Threat**) diketahui menggunakan celah kerentanan yang belum pernah diketahui pembuat aplikasi (**Zero-Day**) berbasis eksekusi perintah jarak jauh (**RCE = Remote Code Execution**) untuk masuk sistem keamanan penyaring (*firewall*) aplikasi web (**WAF = Web Application Firewall**) perusahaan. Celah tersebut dinilai memiliki skor keparahan (**CVSS = Common Vulnerability Scoring System**) tingkat kritis 9.8 dari 10.0.

</details>

---

## 📋 CIPHER Rank Final Checklist

- [ ] Saya telah melewati tantangan *Reading*, *Writing*, dan *Listening* bahasa Inggris teknis
- [ ] Saya sudah mengukur *baseline* kemampuan saya dengan EF SET (CEFR)
- [ ] Saya telah merangkum video DEF CON internasional dalam bahasa Inggris (Weekly Mission)
- [ ] Saya siap membongkar komputer dan memahami jaringan!

---

## 💬 Diskusi Penutup Rank CIPHER

1. Bandingkan perasaanmu di Hari ke-1 (Minggu 2) dengan Hari ini (Minggu 4). Apakah berurusan dengan *English documentation* dan video tanpa terjemahan masih semenyeramkan sebelumnya?
2. Ayo pamerkan skor CEFR kalian di forum/Grup TISS! Siapa yang paling jago, dan siapa yang mau janjian belajar bareng biar makin jago? 

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────────┐
│ │
│ 🎖️ CIPHER COMPLETE │
│ Week 4 of 24 Complete │
│ "Language is the first weapon │
│ of a hacker." │
│ │
│ 🔤 Rank: CIPHER → CLEARED! │
│ 📊 Progress: 16% │
│ 🔜 Next Rank: PACKET │
│ │
└─────────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 5: Dasar Jaringan Komputer (PACKET Rank)**

*Welcome to the Matrix!*
Bulan pertama selesai, sekarang saatnya masuk ke urat nadi internet: **Jaringan (Networking)**. Minggu depan kamu akan masuk ke rank **📡 PACKET**. Kita akan membedah bagaimana sebuah pesan WhatsApp bisa terkirim ke benua lain dalam hitungan milidetik, apa itu IP Address, dan mengapa Model OSI sangat dipuja di dunia IT.

Siapkan otak logismu, kita masuk ke inti sistem komputer!

> 🚀 *"There is no cloud, it's just someone else's computer."*

---

*📅 TISS Null Teaming · Week 4 · Day 5 · CIPHER Rank*
