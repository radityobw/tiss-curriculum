# 🔤 Week 2 · Day 4: Teknik Scanning & Skimming

> **Rank**: CIPHER | **Minggu ke-2**, Hari 4/5 | **Durasi**: ~35 menit

📊 **Progress**: Week 2 · Day 4/5 | CIPHER Rank (Minggu 1 dari 3) | Overall: 9/120 hari (8%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara teknik membaca *Scanning* dan *Skimming*
2. **Menerapkan** kedua teknik tersebut untuk membaca dokumentasi teknis atau write-up dengan cepat
3. **Menghemat waktu** dalam proses *information gathering* berbahasa Inggris

---

## 📖 Materi Inti

### Tantangan Membaca di Dunia IT

Dunia Cybersecurity dipenuhi dengan lautan teks: laporan *pentest*, manual book dari *tools* (seperti dokumentasi Nmap yang ratusan halaman), *write-up* (artikel cara seseorang melakukan hack), dan artikel ancaman keamanan.

Jika kamu membaca setiap dokumen tersebut kata-per-kata (*word-by-word*), otakmu akan cepat lelah (*cognitive overload*) apalagi membacanya dalam bahasa Inggris.

Solusinya? **Skimming** dan **Scanning**.

### 1. Skimming (Mendapatkan Gambaran Besar)

**Skimming** adalah teknik membaca dengan cepat (menyapu) untuk mendapatkan ide utama (*main idea*) dari keseluruhan teks tanpa mempedulikan detail spesifik.

**Kapan digunakan?**
Saat kamu menemukan artikel *write-up* CTF yang panjang dan kamu ingin tahu: *"Artikel ini bahas kerentanan jenis apa sih? Apakah relevan buat saya baca lebih lanjut?"*

**Cara Skimming:**
1. Baca **Judul** dan **Subjudul** (Headers).
2. Baca **kalimat pertama** dan **kalimat terakhir** pada setiap paragraf utama.
3. Perhatikan kata-kata yang di-**bold**, di-*italic*, atau be poin-poin (bullet points).
4. Lewati bagian basa-basi, deskripsi panjang, atau kode log.

### 2. Scanning (Mencari Detail Spesifik)

**Scanning** adalah teknik mencari informasi atau kata kunci spesifik di dalam teks. Kamu tidak membaca kalimatnya, melainkan matamu "memindai" mencari satu benda khusus.

**Kapan digunakan?**
Saat kamu butuh jawaban spesifik. Contoh: *"Command apa yang dipakai untuk menginstall tool ini?"* atau *"Berapa CVSS Score dari kerentanan ini?"*

**Cara Scanning:**
1. Tentukan **kata kunci (keyword)** yang dicari sebelum mulai (misal: mencari angka IP, mencari kata `CVSS`, mencari format file `.txt`).
2. Jangan membaca kalimat; biarkan matamu bergerak zigzag atau membentuk huruf 'Z' dari atas ke bawah halaman.
3. Gunakan bantuan visual: cari huruf kapital, angka, simbol (seperti tanda kutip atau kode `$`).
4. Kalau di browser, tentu saja gunakan sakti mandraguna: `Ctrl + F` / `Cmd + F`.

> 💡 **Analogi**: 
> **Skimming** = Kamu melihat peta keseluruhan kota untuk tahu di mana letak pusat perbelanjaan, taman, dan perumahan.
> **Scanning** = Kamu melihat peta untuk mencari persimpangan Jalan Sudirman dan Jalan Thamrin secepat mungkin.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari praktikkan **Scanning**. Di bawah ini adalah kutipan log jaringan palsu. Matamu harus menemukan data spesifik secepat mungkin! Jangan dibaca, pindai (scan) saja!

```text
[10:45:01] Connection established from IP 192.168.1.100 to server.
[10:45:03] User 'admin' failed login attempt.
[10:45:04] User 'admin' failed login attempt.
[10:45:05] User 'admin' failed login attempt.
[10:45:05] ALERT: Brute force detected on port 22.
[10:45:10] Connection established from IP 10.0.5.55 to server.
[10:45:11] User 'sysadmin' logged in successfully.
[10:45:12] Executed command: whoami
[10:45:15] Executed command: cat /etc/shadow
[10:45:20] Data exfiltration detected targeting host maliciousexample.com
```

**Tugas Scanning (Cari dalam waktu <30 detik!):**
1. Port berapa yang terkena serangan Brute Force?
2. Siapa nama user yang berhasil login?
3. File apa yang berusaha dibaca (`cat`) oleh user tersebut?

<details>
<summary>🔑 Klik untuk cek jawaban</summary>

1. Port **22** (Baris: ALERT: Brute force detected on port 22)
2. User **'sysadmin'** (Baris: User 'sysadmin' logged in successfully)
3. File **/etc/shadow** (Baris: Executed command: cat /etc/shadow)

Apakah kamu menemukannya dalam hitungan detik? Itulah *scanning*!

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Kamu sedang membaca dokumentasi sebuah tool hacking di GitHub, dan kamu hanya ingin tahu apakah tool tersebut jalan di Windows atau tidak. Teknik mana yang harus dipakai: Skimming atau Scanning?</summary>

**Jawaban:** **Scanning**. Kamu tidak butuh ide utamanya, kamu hanya perlu mencari kata kunci spesifik seperti "Windows", "OS supported", atau "Requirements".

</details>

<details>
<summary>❓ Kamu menemukan artikel berjudul "How we hacked a smart car". Kamu ingin tahu teknik umum yang mereka gunakan sebelum memutuskan membaca full. Teknik apa yang kamu pakai?</summary>

**Jawaban:** **Skimming**. Kamu menyapu artikel dengan melihat Subjudul dan kalimat pertama setiap paragraf untuk memahami alur penyerangan secara garis besar (*main idea*).

</details>

<details>
<summary>❓ Mengapa tombol `Ctrl+F` atau `Cmd+F` diibaratkan sebagai alat Scanning digital terbaik?</summary>

**Jawaban:** Karena *Scanning* pada intinya adalah proses pencarian kata kunci. Dengan `Ctrl+F`, komputer melakukan pencarian visual instan untukmu, menghemat banyak energi mental. Biasakan mencari *keyword* dengan ini saat menavigasi dokumentasi tebal.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami bedanya Skimming dan Scanning
- [ ] Saya tahu kapan harus menggunakan masing-masing teknik
- [ ] Saya sudah menyelesaikan Mini Lab ekstraksi log dengan Scanning
- [ ] Saya sudah menjawab semua quiz kilat
- [ ] Saya siap untuk hari terakhir minggu ini!

---

## 🔗 Resources

- [How to Skim and Scan (Video Singkat)](https://www.youtube.com/watch?v=F1wzM5Xy3oE) — Video penjelasan visual cara kerja skimming dan scanning.

---

## ➡️ Besok

**Day 5: Lab & Mission: Rangkum CVE Advisory** — Waktunya mempraktikkan semua pelajaran minggu ini! Kamu akan membaca satu CVE asli, melakukan scanning & skimming, lalu membuat kamus mini-mu sendiri!

---

*📅 TISS Null Teaming · Week 2 · Day 4 · CIPHER Rank*
