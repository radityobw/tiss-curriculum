# 🔤 Week 3 · Day 5: Lab & Weekly Mission

> **Rank**: CIPHER | **Minggu ke-3**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓░░░] 66% — CIPHER Rank (Minggu 2 dari 3)

### Overall Journey
[▓▓▓░░░░░░░░░░░░░░░░░░░░░] 12% — Hari 15 dari 120

### Rank Map
✅ VOID → 🔄 CIPHER → ⬜ PACKET → ⬜ FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini kamu sudah mempelajari:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Struktur Laporan Teknis | Laporan keamanan punya *Executive Summary* untuk bos dan *Findings* untuk teknisi. |
| Day 2 | Email Profesional & Komunikasi | Gunakan aturan *How to Ask Questions the Smart Way* agar direspons di forum IT. |
| Day 3 | Bug Report Writing | Laporan Bug Bounty butuh Title, Desc, Steps to Reproduce (PoC), Impact, & Remediation. |
| Day 4 | Akronim Cybersecurity | Menghafal *Alphabet Soup* (XSS, RCE, PoC, CVE) adalah kunci membaca dokumen teknis. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Komputer dengan VS Code
- Akses ke repository `cybersec-journey` milikmu

### Step 1: Belajar dari Laporan Asli (Hacktivity)

Platform *Bug Bounty* seperti HackerOne mempublikasikan laporan bug yang sudah ditambal. Kita akan menganalisis satu laporan nyata yang sukses.

1. Buka browser dan pergi ke: [https://hackerone.com/hacktivity](https://hackerone.com/hacktivity)
2. (Opsional jika link lama susah dicari) Buka langsung laporan legendaris ini: **[Stored XSS on Shopify](https://hackerone.com/reports/405694)** (Atau laporan *Stored XSS* apapun yang statusnya *Resolved* / *Disclosed*).
3. **Analisis Struktur Laporannya**:
 - Lihat bagaimana hacker menulis *Title*?
 - Cek *Steps To Reproduce*-nya. Apakah berurutan dengan rapi menggunakan angka (1, 2, 3...)?
 - Perhatikan seberapa *to-the-point* bahasanya.

**Expected Output:**
```
Kamu menyadari bahwa laporan bug bounty profesional tidak butuh bahasa sastra yang rumit; cukup langkah-langkah yang jelas, lugas, dan bisa direproduksi.
```

### Step 2: Persiapkan Folder Minggu 3

1. Buka VS Code dan buka repository `cybersec-journey`.
2. Buat folder baru bernama `week-03`.
3. Di dalam folder `week-03`, buat file `bug-report.md`.

### 🔧 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Tidak paham isi laporan di Hacktivity karena terlalu teknis | Abaikan teknis hacking-nya! Fokus pada **strukturnya** (Judul, Deskripsi, Langkah-langkah, Dampak). Kita belum belajar teknis hacking-nya, itu normal. |

---

## 🎯 Weekly Mission

### Misi: "Bounty Hunter — Tulis Laporan Pertamamu!"

**Deskripsi:**
Kamu baru saja menemukan celah keamanan di website simulasi Universitas Tirtayasa (`simulasi.untirta.ac.id`). Skenarionya adalah:
- Kamu menemukan bahwa halaman Ganti Password tidak menanyakan "Password Lama".
- Akibatnya, kalau kamu meninggalkan laptop menyala (tidak me-lock layar), siapapun yang lewat bisa mengganti passwordmu hanya dengan mengetik password baru lalu klik Save. Celah ini disebut **CSRF (Cross-Site Request Forgery)** atau *Broken Authentication*.

**Tugasmu:** 
Tulis laporan kerentanan profesional dalam **Bahasa Inggris** seolah-olah kamu melaporkannya ke tim IT kampus, dan simpan dalam file `bug-report.md`.

**Format Laporan:**
Ikuti format ini (Isi dengan idemu sendiri berdasarkan skenario di atas):

```markdown
# Security Report

**Title**: [Tulis judul deskriptif dalam Bahasa Inggris]
**Severity**: Medium (Karena butuh korban login dulu dan meninggalkan layar)

## Description
[1 paragraf menjelaskan celah di halaman ganti password]

## Steps to Reproduce
1. Log in to [website] as a standard student account.
2.... [tulis kelanjutannya]
3....
4....

## Impact
[Jelaskan apa akibatnya jika celah ini dieksploitasi oleh orang jahat]

## Remediation / Recommendation
[Saran perbaikan: contohnya menyuruh developer menambahkan konfirmasi 'Old Password']
```

**Kriteria Sukses:**
- [ ] File `bug-report.md` ada di folder `week-03`
- [ ] Format 5 bagian terpenuhi dalam Bahasa Inggris
- [ ] *Steps to Reproduce* ditulis dengan format berurutan (numbered list) dan mudah dipahami
- [ ] Ter-commit dan di-push ke GitHub

**Estimasi Waktu:** 1–1.5 jam

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Kepanjangan dari PoC adalah...</summary>

**Jawaban:** **Proof of Concept**. Bukti nyata atau demonstrasi langkah-demi-langkah bahwa sebuah celah keamanan benar-benar ada dan bisa dieksploitasi.

</details>

<details>
<summary>❓ [MUDAH] Mengapa bagian "Steps to Reproduce" harus ditulis sangat rinci menggunakan angka berurutan?</summary>

**Jawaban:** Agar tim IT (Triager / Developer) yang menerima laporan bisa meniru atau mereproduksi serangan dengan tepat. Jika mereka gagal mereproduksi celah karena instruksi yang membingungkan, celah akan dianggap tidak valid dan laporan ditutup tanpa hadiah.

</details>

<details>
<summary>❓ [SEDANG] Sebuah laporan berbunyi: "An APT exploited an RCE to install malware." Terjemahkan maksud kalimat ini!</summary>

**Jawaban:** "Sebuah kelompok peretas tingkat tinggi (Advanced Persistent Threat) mengeksploitasi celah eksekusi perintah jarak jauh (Remote Code Execution) untuk menginstal perangkat lunak jahat."

</details>

<details>
<summary>❓ [SEDANG] Apa perbedaan utama antara menulis Executive Summary dan Technical Findings dalam sebuah laporan keamanan?</summary>

**Jawaban:** 
- **Executive Summary** ditujukan untuk manajemen/bisnis, menggunakan bahasa awam dan berfokus pada **dampak kerugian/risiko bisnis**.
- **Technical Findings** ditujukan untuk *developer/engineer*, penuh dengan jargon teknis (XSS, parameter, payload) dan berfokus pada **cara kerja celah dan cara memperbaikinya**.

</details>

<details>
<summary>❓ [SULIT] Jika kamu menemukan kerentanan di platform open-source dan ingin membuat issue di GitHub mereka, bagaimana caramu bertanya atau melapor jika merujuk pada prinsip "How to Ask Questions the Smart Way"?</summary>

**Jawaban:** 
1. Jangan membuat judul "Help" atau "URGENT BUG". Buat judul spesifik: "Vulnerability in XYZ component leading to data leak".
2. Jangan hanya protes "Aplikasi kalian tidak aman". Sertakan **bukti spesifik**, log error, atau **Steps to Reproduce** (PoC) yang jelas.
3. Sebutkan versi OS, versi aplikasi, dan apa saja yang sudah coba kamu lakukan untuk memastikan ini benar-benar *bug* dan bukan sekadar salah konfigurasi.

</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami bedanya bahasa laporan untuk eksekutif vs teknisi
- [ ] Saya tahu cara menulis email resmi dan berkomunikasi di forum
- [ ] Saya memahami kerangka dasar sebuah *Bug Report* (PoC, Impact, Remediation)
- [ ] Saya hafal minimal 10 akronim cybersecurity yang paling populer
- [ ] Saya sudah menyelesaikan Hands-On Lab menganalisis laporan asli di Hacktivity
- [ ] Saya sudah menyelesaikan Weekly Mission: Menulis Bug Report di `bug-report.md`

---

## 💬 Diskusi Minggu Ini

1. Saat menulis misi *Bug Report* dalam bahasa Inggris, bagian mana yang menurutmu paling sulit untuk dirangkai kata-katanya?
2. Jika ada seseorang di forum bertanya "Gimana cara nge-hack IG orang? Ajari dong!", bagaimana jawabanmu sebagai kader Null Teaming yang sudah paham etika *Smart Questions* dan *White Hat*? 

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ SCRIBE OF SECRETS │
│ Week 3 Complete │
│ "A vulnerability not reported, │
│ is a vulnerability not fixed." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 4: Listening & Communication (CIPHER Rank Finale)**

Minggu depan adalah minggu terakhir di rank **CIPHER**. Kita akan menutup sesi "Bahasa Inggris Teknis" ini dengan melatih pendengaran (Listening) melalui seminar internasional legendaris seperti DEF CON, plus kita akan mengukur kemampuan akhirmu secara resmi. Bersiaplah untuk memperluas kemampuan bahasamu!

> 🚀 *"The art of communication is the language of leadership."* — James Humes

---

*📅 TISS Null Teaming · Week 3 · Day 5 · CIPHER Rank*
