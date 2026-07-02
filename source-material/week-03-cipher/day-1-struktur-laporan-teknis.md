# 🔤 Week 3 · Day 1: Struktur Laporan Teknis

> **Rank**: CIPHER | **Minggu ke-3**, Hari 1/5 | **Durasi**: ~35 menit

📊 **Progress**: Week 3 · Day 1/5 | CIPHER Rank (Minggu 2 dari 3) | Overall: 11/120 hari (9%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** anatomi standar dari sebuah laporan keamanan (Technical Report)
2. **Membedakan** bahasa yang digunakan untuk manajemen (Executive) vs teknisi (Engineer)
3. **Menyusun** kerangka laporan teknis dasar dalam bahasa Inggris

---

## 📖 Materi Inti

### Mengapa Laporan Itu Penting?

Di dunia cybersecurity, **kemampuan menetas (hacking) tidak akan berguna jika kamu tidak bisa menjelaskannya**. 

- Jika kamu seorang **Penetration Tester**, klien membayarmu untuk laporannya, bukan untuk aksimu meretas server mereka. 
- Jika kamu seorang **Bug Bounty Hunter**, perusahaan (seperti Google atau Facebook) hanya akan membayarmu jika mereka bisa mengerti dan meniru langkah-langkah eksploitasimu dari laporanmu.

### Anatomi Laporan Keamanan (*Anatomy of a Security Report*)

Sebuah laporan keamanan profesional yang baik memiliki struktur baku. Ini memastikan pembaca mendapatkan informasi dengan cepat.

| Bagian | Nama Inggris | Fungsi | Target Pembaca |
|--------|--------------|--------|----------------|
| **1. Ringkasan** | **Executive Summary** | Menjelaskan *dampak bisnis* dari celah yang ditemukan. Tanpa jargon rumit. | Bos / Manajemen |
| **2. Ruang Lingkup**| **Scope** | Batasan apa saja yang boleh dan tidak boleh diuji. (Contoh: hanya web A, tidak boleh web B). | Manajer Proyek |
| **3. Metodologi** | **Methodology** | Cara dan alat yang digunakan selama pengujian keamanan. | Sesama Tim Keamanan |
| **4. Temuan** | **Findings / Vulnerabilities** | Daftar celah yang ditemukan, tingkat keparahan (*severity*), dan langkah eksploitasi (*Proof of Concept*). | Teknisi / Developer |
| **5. Rekomendasi** | **Remediation / Recommendations** | Cara memperbaiki celah tersebut. | Teknisi / Developer |

### Executive Summary vs Technical Findings

Ini adalah bagian yang paling sering membuat pemula gagal. Kamu harus tahu **kepada siapa kamu berbicara**.

❌ **Bahasa Teknisi untuk Bos (Buruk)**: 
*"We found a blind SQL Injection in the login parameter using a time-based payload `SLEEP(10)`. You need to use parameterized queries."* (Bos tidak tahu apa itu SQLi atau parameterized queries!).

✅ **Bahasa Eksekutif (Executive Summary)**: 
*"We identified a critical flaw in the login page that allows attackers to extract the entire customer database. This could lead to a massive data breach and reputational damage. We highly recommend fixing this immediately."*

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Baca dua kutipan paragraf (Paragraf A dan Paragraf B) di bawah ini. Tentukan mana yang merupakan **Executive Summary** dan mana yang merupakan **Technical Findings**.

**Paragraf A:**
*"The vulnerability allows an unauthenticated attacker to inject malicious JavaScript payloads via the 'search' parameter, which reflects in the DOM without sanitization, leading to a Stored Cross-Site Scripting (XSS) attack."*

**Paragraf B:**
*"During our assessment, we discovered a flaw that could allow cybercriminals to steal active user sessions. If exploited, attackers could hijack employee accounts and access internal company documents without needing a password."*

<details>
<summary>🔑 Klik untuk melihat jawaban</summary>

- **Paragraf A** adalah **Technical Findings**. (Penuh dengan jargon teknis seperti *unauthenticated, payloads, DOM, sanitization, XSS*).
- **Paragraf B** adalah **Executive Summary**. (Fokus pada dampak bisnis: *steal sessions, hijack accounts, access documents* tanpa menggunakan istilah teknis peretasannya).

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Bagian laporan mana yang berisi langkah-langkah detail agar celah bisa direproduksi oleh developer?</summary>

**Jawaban:** **Findings / Vulnerabilities**. Lebih spesifiknya, bagian ini biasanya memuat sub-bagian bernama *Proof of Concept* (PoC) yang menjabarkan langkah-demi-langkah (step-by-step) eksploitasinya.

</details>

<details>
<summary>❓ Jika klien (perusahaan) hanya ingin tahu "Apakah kita aman? Berapa kerugian kalau kita dibobol?", bagian laporan mana yang akan mereka baca?</summary>

**Jawaban:** **Executive Summary**. Manajemen level atas (C-Level, Direktur) biasanya tidak punya waktu atau pemahaman teknis untuk membaca detail eksploitasi. Mereka hanya membaca *Executive Summary* untuk mengambil keputusan bisnis dan anggaran.

</details>

<details>
<summary>❓ Mengapa kita harus memasukkan bagian "Remediation" atau Rekomendasi?</summary>

**Jawaban:** Karena tugas seorang profesional keamanan bukan sekadar menghancurkan, tapi juga **melindungi**. Developer mungkin tahu cara membuat aplikasi, tapi belum tentu tahu cara menulis kode yang aman (*secure coding*). Kita harus memandu mereka cara menambal celah tersebut.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya mengerti bahwa laporan sama pentingnya dengan kemampuan teknis
- [ ] Saya hafal 5 bagian utama dari laporan keamanan (Executive Summary, Scope, dll.)
- [ ] Saya bisa membedakan gaya bahasa untuk Eksekutif vs Teknisi
- [ ] Saya sudah menyelesaikan Mini Lab identifikasi paragraf
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Offensive Security (OSCP) Penetration Test Report Template](https://www.offensive-security.com/pwk-online/PWKv1-REPORT.doc) — Contoh template laporan standar industri dari sertifikasi OSCP (file.doc).
- [How to Write a Good Penetration Testing Report](https://www.youtube.com/watch?v=Fq2mG_Q0k58) — Panduan video dari praktisi.

---

## ➡️ Besok

**Day 2: Email Profesional & Komunikasi Komunitas** — Sebelum menulis laporan resmi, kamu harus tahu cara berkomunikasi sehari-hari secara profesional. Kita akan belajar etika bertanya di forum (*How to Ask Questions the Smart Way*) dan menulis email dalam bahasa Inggris!

---

*📅 TISS Null Teaming · Week 3 · Day 1 · CIPHER Rank*
