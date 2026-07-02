---
type: quiz
week: 19
day: 1
title: "Quiz: The Anatomy of a Pentest Report"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di ranah peretasan , mengapa penyusunan dokumen Laporan (*Pentest Report*) dinilai jauh lebih krusial daripada sekadar menemukan celah kerentanan itu sendiri?
- [ ] A. Karena *Bug Bounty* membayar per halaman teks laporan, bukan per temuan kerentanan.
- [x] B. Tanpa laporan (yang membedah risiko bisnis dan langkah perbaikan), temuan kerentanan *SQLi* atau *XSS* yang paling berbahaya sekalipun tak ada nilainya (hanya sebatas vandalisme). Laporanlah yang menjembatani kerentanan teknis menjadi informasi yang bisa ditindaklanjuti korporasi demi merajut perbaikan pertahanan.
- [ ] C. Laporan dibutuhkan buat meraba meretas *WAF*.
- [ ] D. *Pentest Report* diwajibkan sebagai parameter *SQLMap*.

### Q2
**Type:** True/False
**Question:** Ketika menyusun anatomi pertama <i>Executive Summary</i> di halaman pembuka laporan, peretas diharamkan menggunakan terminologi bahasa teknis IT (seperti <i>SQLi, XSS, Payload, Cookie</i>) lantaran bagian tersebut ditujukan spesifik untuk dibaca pemangku kepentingan bisnis (CEO/Direksi).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Di penyusunan laporan , anatomi bagian manakah (berawalan huruf 'M') yang wajib membeberkan urutan taktik serangan dan apa saja yang dipakainya (contoh: <i>Burp Suite</i>) berikut rentang jam durasi pengujian?
**Answer:** Methodology (Metodologi).

### Q4
**Type:** Short Answer
**Question:** Ketika penganalisis menenggak jabaran serangan teknis kerentanan, memuat *CVSS Score*, *Proof of Concept (PoC)* dan *HTTP Request* yang ditujukan bagi Tim Developer, anatomi bagian apakah ini?
**Answer:** Findings (atau Vulnerability Details).

### Q5
**Type:** Short Answer
**Question:** Pada laporan penutup, anatomi apakah yang menuntut penganalisis menyuguhkan resep penawar racun perbaikan (seperti saran koding) bagi *Developer*?
**Answer:** Remediation (atau Remediation Advice / Mitigation).
