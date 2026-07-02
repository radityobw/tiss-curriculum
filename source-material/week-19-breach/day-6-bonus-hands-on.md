# 🎯 Week 19 · Day 6 (Bonus): Hands-On Learning

> **Rank**: BREACH | **Minggu ke-19** | Bonus Day

---

## 🌐 Platform Hari Ini

**[TCM Security — Sample Pentest Report (GitHub)](https://github.com/hmaverickadams/TCM-Security-Sample-Pentest-Report)**
Template laporan penetration testing profesional dari TCM Security (Heath Adams). Template ini digunakan di industri nyata dan tersedia gratis di GitHub.

💰 **Biaya**: Gratis (open source di GitHub)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Memahami struktur laporan pentesting profesional yang digunakan di industri
2. Menganalisis template report dan mengidentifikasi setiap bagiannya
3. Menulis draft laporan pentesting berdasarkan temuan dari lab Week 16-18

---

## 📋 Requirement

* Akun GitHub (sudah ada)
* Peramban web modern (Chrome/Firefox)
* Editor teks (VS Code/Notion/Google Docs)
* Catatan writeup dari Week 16-18 (lab SQLi, XSS, dan Burp Suite)

> ⚠️ **Jika belum punya writeup dari minggu sebelumnya**: Tidak masalah — kamu bisa menggunakan skenario fiktif untuk latihan.

---

## 📝 Prosedur

### Langkah 1: Unduh Template Report
1. Buka [github.com/hmaverickadams/TCM-Security-Sample-Pentest-Report](https://github.com/hmaverickadams/TCM-Security-Sample-Pentest-Report)
2. Klik **Code** → **Download ZIP** (atau clone via terminal)
 ```bash
 git clone https://github.com/hmaverickadams/TCM-Security-Sample-Pentest-Report.git
 ```
3. Buka file laporan (format DOCX/PDF) yang ada di dalam repositori

### Langkah 2: Analisis Struktur Report
Baca laporan dari awal sampai akhir dan identifikasi setiap section:

| Section | Fungsi |
|---------|--------|
| **Cover Page** | Judul, tanggal, auditor, klien |
| **Executive Summary** | Ringkasan eksekutif untuk manajemen non-teknis |
| **Scope** | Ruang lingkup pengujian (IP, domain, metode) |
| **Methodology** | Metodologi yang digunakan (OWASP, PTES) |
| **Findings** | Daftar kerentanan dengan severity, deskripsi, PoC, remediasi |
| **Remediation Summary** | Ringkasan rekomendasi perbaikan |

Catat:
- Bagaimana *severity* diklasifikasikan? (Critical/High/Medium/Low/Info)
- Bagaimana PoC (Proof of Concept) disajikan?
- Bagaimana rekomendasi remediasi ditulis?

### Langkah 3: Tulis Draft Report Sendiri
Menggunakan writeup dari Week 16-18 (atau skenario fiktif), tulis laporan mini dengan struktur berikut:

```markdown
# Laporan Penetration Testing
## Informasi Umum
- Auditor: [Nama Kamu]
- Target: PortSwigger Web Security Academy Labs
- Tanggal: [Tanggal]
- Metodologi: OWASP Testing Guide v4

## Executive Summary
[2-3 kalimat ringkasan temuan untuk audience non-teknis]

## Temuan Kerentanan

### Finding 1: SQL Injection pada Parameter Pencarian
- Severity: HIGH
- Kategori OWASP: A03:2021 – Injection
- Deskripsi: [jelaskan kerentanan]
- Proof of Concept:
 1. [langkah reproduksi]
 2. [payload yang digunakan]
- Dampak: [apa yang bisa dilakukan penyerang]
- Remediasi: [cara memperbaiki]

### Finding 2: Cross-Site Scripting (XSS)
[format yang sama]

### Finding 3: [temuan lain]
[format yang sama]

## Ringkasan Remediasi
| # | Temuan | Severity | Status |
|---|--------|----------|--------|
| 1 | SQL Injection | HIGH | Open |
| 2 | XSS Reflected | MEDIUM | Open |
```

> 💡 **Tips menulis Executive Summary**: Bayangkan kamu menjelaskan temuan ke CEO yang tidak paham teknis. Hindari jargon, fokus pada **dampak bisnis**.

### Langkah 4: Self-Review
1. Baca ulang laporanmu
2. Periksa apakah:
 - Setiap finding memiliki severity, PoC, dan remediasi?
 - Executive Summary bisa dipahami non-teknis?
 - Langkah reproduksi cukup detail untuk diikuti orang lain?
3. Bandingkan dengan template TCM — apa yang perlu ditingkatkan?

---

## 🏁 Target Output

* ✅ Template TCM Security berhasil diunduh dan dianalisis
* 📝 **Draft laporan pentest** dengan minimal 2 findings (lengkap: severity, PoC, remediasi)
* 📝 Catatan analisis: 5 hal penting yang kamu pelajari dari template profesional
* 📸 Tangkapan layar repositori GitHub TCM Security Report

---

## 🔄 Fallback

Jika repositori GitHub TCM tidak bisa diakses:
1. Gunakan template **PTES Report** dari [pentest-standard.org](http://www.pentest-standard.org/index.php/Reporting)
2. Atau gunakan template dari **Offensive Security** yang tersedia gratis secara publik
3. Struktur report tetap sama — tulis draft laporan dengan format yang sudah dipelajari di Day 1-4 minggu ini
