# 🎯 Week 20 · Day 6 (Bonus): Hands-On Learning

> **Rank**: SENTINEL | **Minggu ke-20** | Bonus Day

---

## 🌐 Platform Hari Ini

**[LetsDefend — SOC Fundamentals (Free Tier)](https://app.letsdefend.io/training/lessons/soc-fundamentals)**
Platform simulasi SOC (Security Operations Center) yang menyediakan modul pembelajaran gratis tentang dasar-dasar operasi pertahanan , termasuk alert triage dan incident handling.

💰 **Biaya**: Gratis (modul SOC Fundamentals tersedia di free tier)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Memahami workflow SOC Analyst melalui simulasi di platform LetsDefend
2. Melakukan alert triage dan klasifikasi severity pada peristiwa keamanan
3. Mengenal antarmuka SIEM dashboard dalam konteks SOC nyata

---

## 📋 Requirement

* Akun LetsDefend (free tier)
* Peramban web modern (Chrome/Firefox)
* Koneksi internet stabil

> ⚠️ **Jika belum punya akun LetsDefend**: Buka [letsdefend.io](https://letsdefend.io), klik **Register**, daftar dengan email aktif. Free tier memberikan akses ke modul dasar dan beberapa challenges.

---

## 📝 Prosedur

### Langkah 1: Akses Modul SOC Fundamentals
1. Login ke [app.letsdefend.io](https://app.letsdefend.io)
2. ke **Training** → cari modul **"SOC Fundamentals"**
3. Klik modul untuk memulai pembelajaran

### Langkah 2: Pelajari Materi SOC
1. Baca penjelasan tentang:
 - Apa itu SOC dan perannya
 - SOC Analyst Tier 1, Tier 2, Tier 3
 - Workflow harian SOC Analyst
2. Kerjakan kuis di setiap akhir sub-topik
3. Catat terminologi baru yang kamu temukan:
 - **SIEM** (Security Information and Event Management)
 - **Alert Triage** (proses memprioritaskan peringatan)
 - **False Positive** vs **True Positive**
 - **Escalation** (meneruskan insiden ke tier lebih tinggi)

> 💡 **Hubungkan dengan materi minggu ini**: Modul LetsDefend memperkuat konsep yang dipelajari di Day 1 (Blue Team & SOC) dan Day 4 (Incident Response Lifecycle).

### Langkah 3: Eksplorasi Dashboard Monitoring
1. ke bagian **Monitoring** di LetsDefend (jika tersedia di free tier)
2. Amati alert-alert yang muncul di dashboard
3. Untuk setiap alert, perhatikan:
 - Source IP dan Destination IP
 - Tipe alert (Malware, Phishing, Brute Force, dll)
 - Severity level
4. Coba klik satu alert dan baca detail-nya

### Langkah 4: Kerjakan Challenge Gratis
1. ke **Challenges** → filter yang berlabel **Free**
2. Pilih challenge yang berhubungan dengan **Phishing Email Analysis** (jika tersedia gratis)
3. Ikuti instruksi challenge:
 - Analisis header email
 - Identifikasi indikator phishing
 - Tentukan apakah alert True Positive atau False Positive
4. Submit jawaban

### Langkah 5: Dokumentasi SOC Shift Log
Tulis SOC Shift Handover Log pertamamu:
```markdown
# SOC Shift Handover Log
- Tanggal: [tanggal]
- Analyst: [nama kamu]
- Shift: Day 6 Bonus

## Alert yang Ditangani
| # | Alert Type | Source IP | Severity | Verdict |
|---|-----------|----------|----------|---------|
| 1 | [tipe] | [IP] | [High/Med/Low] | [TP/FP] |

## Catatan
- [observasi penting]
- [rekomendasi tindak lanjut]
```

---

## 🏁 Target Output

* ✅ Modul **SOC Fundamentals** selesai (atau progress signifikan)
* 📝 **SOC Shift Handover Log** pertama (format di atas)
* 📝 Daftar 5 terminologi SOC baru yang dipelajari beserta definisinya
* 📸 Tangkapan layar dashboard LetsDefend

---

## 🔄 Fallback

Jika LetsDefend tidak bisa diakses atau free tier terlalu terbatas:
1. Buka **TryHackMe** — cari room **"Intro to Cyber Threat Intel"** atau **"Junior Security Analyst Intro"** (pastikan room Free)
2. Kerjakan room tersebut
3. Tetap tulis SOC Shift Handover Log berdasarkan informasi dari room TryHackMe
