# 🔤 Week 3 · Day 3: Bug Report Writing Basics

> **Rank**: CIPHER | **Minggu ke-3**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 3 · Day 3/5 | CIPHER Rank (Minggu 2 dari 3) | Overall: 13/120 hari (11%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** standar format Bug Report di platform seperti HackerOne atau Bugcrowd
2. **Menulis** *Proof of Concept* (PoC) yang mudah direproduksi oleh triager/developer
3. **Mengklasifikasikan** severity (tingkat keparahan) secara objektif

---

## 📖 Materi Inti

### Apa itu Bug Report?

**Bug Report** adalah laporan teknis spesifik yang diserahkan oleh seorang *Security Researcher* (Bug Hunter) kepada perusahaan ketika mereka menemukan celah keamanan. 

Laporan yang baik akan diproses cepat dan menghasilkan hadiah (*bounty*). Laporan yang buruk akan ditolak (*Closed: Not Applicable* atau *Needs More Info*).

### Komponen Wajib Bug Report yang Sukses

Sebuah Bug Report yang bernilai tinggi biasanya mengandung 5 elemen ini:

1. **Title (Judul)**
 Harus sangat deskriptif. Polanya: `[Jenis Vulnerability] on [Endpoint/Fitur] leading to [Dampak]`.
 - ❌ Buruk: *I hacked your website*
 - ✅ Baik: *Stored XSS on /profile/edit endpoint leading to account takeover*

2. **Description (Deskripsi Singkat)**
 Satu paragraf tentang apa celah ini dan di mana letaknya.

3. **Steps to Reproduce (Langkah Reproduksi / PoC)**
 Ini bagian **PALING KRITIS**. Kamu harus menulis instruksi langkah-demi-langkah persis seperti buku resep masakan agar *developer* (yang disebut *Triager*) bisa melakukan *hack* yang sama persis. Mulailah dari langkah pertama (seperti login).

4. **Impact (Dampak Bisnis)**
 Penjelasan apa yang bisa terjadi jika orang jahat (Black Hat) mengeksploitasi celah ini. (Apakah data bocor? Server mati? Uang dicuri?).

5. **Mitigation (Saran Perbaikan)** *opsional tapi disarankan*
 Cara menutup celahnya (contoh: *Sanitize user input before reflecting it to the DOM*).

### Severity: Penilaian Tingkat Keparahan

Perusahaan membayar *bounty* berdasarkan seberapa parah celahmu. Skala yang digunakan adalah **CVSS (Common Vulnerability Scoring System)**:

- **Low (0.1 - 3.9)**: Tidak terlalu bahaya, butuh banyak syarat. (Contoh: menemukan nama versi server).
- **Medium (4.0 - 6.9)**: Cukup bahaya tapi efeknya terbatas. (Contoh: XSS yang butuh klik dari korban).
- **High (7.0 - 8.9)**: Berbahaya dan bisa mengeksploitasi data sensitif. (Contoh: Bisa mencuri database user).
- **Critical (9.0 - 10.0)**: Kiamat bagi perusahaan. (Contoh: Bisa menjalankan program dari jauh tanpa otentikasi / RCE).

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Bayangkan kamu menemukan celah ini:
Kamu masuk ke website `toko-buku.com`. Kamu membuat akun biasa. Lalu kamu sadar, kalau kamu mengubah URL di browser dari `toko-buku.com/user/12` menjadi `toko-buku.com/user/1` (dimana ID 1 adalah Admin), kamu tiba-tiba bisa melihat profil dan mengganti password Admin tersebut tanpa perlu login ulang! Celah ini disebut IDOR (*Insecure Direct Object Reference*).

**Tugas:** Tulis bagian **Steps to Reproduce (Langkah Reproduksi)** untuk kasus di atas dalam bahasa Inggris.

*Tips: Gunakan numbering (1, 2, 3...).*

<details>
<summary>🔑 Klik untuk melihat contoh penu Steps to Reproduce yang baik</summary>

**Steps to Reproduce:**
1. Navigate to `https://toko-buku.com/login` and log in with a standard user account.
2. Go to your profile page. Notice the URL is `https://toko-buku.com/user/12` (assuming your ID is 12).
3. Intercept the request or simply change the ID in the URL bar from `12` to `1` (Admin's ID).
4. Hit Enter.
5. Notice that you are now viewing the Admin's profile and have full access to change their password or email without any authorization prompt.

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa bagian "Steps to Reproduce" adalah bagian paling penting dalam sebuah Bug Report?</summary>

**Jawaban:** Karena *Triager* (orang dari perusahaan yang memvalidasi laporanmu) **harus bisa membuktikan** celah tersebut benar-benar ada sebelum memberikan hadiah/bounty. Jika langkahmu tidak jelas atau terlewat, mereka akan menganggap celah itu tidak valid (*Not Reproducible*) dan kamu tidak dibayar.

</details>

<details>
<summary>❓ Sebuah celah memungkinkan hacker membaca file rahasia perusahaan, tapi untuk melakukannya hacker harus menipu admin untuk mengklik link palsu terlebih dahulu. Apakah celah ini otomatis bernilai "Critical" (10.0)?</summary>

**Jawaban:** **Tidak**. Karena serangan ini membutuhkan **interaksi pengguna** (*User Interaction Required*), skor keparahannya akan turun (biasanya menjadi Medium atau High), tidak menjadi Critical. Celah Critical biasanya bisa diekploitasi tanpa syarat (*Zero Click*).

</details>

<details>
<summary>❓ Mengapa kita harus menyertakan bagian "Impact" (Dampak)? Bukankah developer sudah tahu dampaknya?</summary>

**Jawaban:** Belum tentu. Terkadang celah teknis terlihat sepele (contoh: merubah nilai parameter ID), tapi bisa berdampak besar secara bisnis (bisa mengakses invoice milik perusahaan lain). Menjelaskan dampak memastikan perusahaan menganggap serius laporanmu dan membayarmu dengan nominal yang sesuai dengan risiko bisnis mereka.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya tahu format 5 komponen penting Bug Report (Title, Desc, Steps, Impact, Mitigation)
- [ ] Saya memahami pola penu judul yang deskriptif
- [ ] Saya tahu cara menulis *Steps to Reproduce* yang detail seperti resep masakan
- [ ] Saya memahami perbedaan keparahan (Low, Medium, High, Critical)
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [HackerOne: How to write a good bug report](https://docs.hackerone.com/hackers/quality-reports.html) — Panduan resmi dari platform Bug Bounty terbesar di dunia.
- [Hactivity (HackerOne)](https://hackerone.com/hacktivity) — Daftar Bug Report **asli** yang sudah diselesaikan (Disclosed). Tempat terbaik untuk belajar melihat laporan orang lain.

---

## ➡️ Besok

**Day 4: Akronim & Abbreviation Cybersecurity** — Di dunia IT, kita sangat suka menyingkat kata (APT, XSS, CVE, SIEM, SOC). Besok kita akan menghafal 50 singkatan yang akan muncul di setiap artikel teknis yang kamu baca seumur hidup!

---

*📅 TISS Null Teaming · Week 3 · Day 3 · CIPHER Rank*
