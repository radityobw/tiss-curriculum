# 🌀 Week 1 · Day 4: Sistem Ranking & Roadmap 24 Minggu

> **Rank**: VOID (Unranked) | **Minggu ke-1**, Hari 4/5 | **Durasi**: ~30 menit

📊 **Progress**: Week 1 · Day 4/5 | VOID Rank (Minggu 1 dari 1) | Overall: 4/120 hari (3%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menavigasi** sistem ranking Null Teaming dari Void sampai Sentinel
2. **Memahami** mengapa urutan ranking dirancang seperti itu
3. **Menjelaskan** apa itu CTF (Capture The Flag) dan bagaimana kompetisinya

---

## 📖 Materi Inti

### Sistem Ranking Null Teaming

Selama 24 minggu (120 hari) ke depan, kamu akan naik rank dari **Void** hingga **Sentinel**. Setiap rank membangun di atas rank sebelumnya:

```
  SENTINEL ─── 🛡️ Week 20-24  │ Web Log & Monitoring
     ↑         (25 hari)      │ "Defend the kingdom"
     │                        │
  BREACH ───── 💀 Week 15-19  │ Web Pentesting
     ↑         (25 hari)      │ "Break the walls"
     │                        │
  FORGE ────── 🔨 Week 10-14  │ Web Development
     ↑         (25 hari)      │ "Build the castle"
     │                        │
  PACKET ───── 📡 Week 5-9    │ Networking & Linux
     ↑         (25 hari)      │ "Understand the roads"
     │                        │
  CIPHER ───── 🔤 Week 2-4    │ Technical English
     ↑         (15 hari)      │ "Learn the language"
     │                        │
  VOID ─────── 🌀 Week 1      │ Orientasi
               (5 hari)       │ "Begin the journey"  ← Kamu di sini!
```

### Mengapa Urutan Ini?

Urutannya mengikuti logika dunia nyata:

| # | Dari | Ke | Alasan |
|---|------|-----|--------|
| 1 | — | **Cipher** (English) | Semua dokumentasi security dalam bahasa Inggris |
| 2 | Cipher | **Packet** (Network + Linux) | Perlu tahu cara komputer berkomunikasi |
| 3 | Packet | **Forge** (Web Dev) | Perlu tahu cara membangun sebelum merusak |
| 4 | Forge | **Breach** (Pentesting) | Sekarang bisa mencari kelemahan di web |
| 5 | Breach | **Sentinel** (Blue Team) | Terakhir, belajar mendeteksi dan bertahan |

> 💡 **Analogi**: Seperti belajar memasak — kamu perlu **membaca resep** (Cipher) → **mengenal bahan dan alat** (Packet) → **memasak sendiri** (Forge) → **tahu kenapa masakan bisa gagal** (Breach) → **menjadi food safety inspector** (Sentinel).

### Apa itu CTF (Capture The Flag)?

**CTF** adalah kompetisi keamanan siber di mana peserta menyelesaikan tantangan (*challenges*) untuk menemukan **flag** — sebuah string rahasia (contoh: `flag{th1s_1s_a_flag}`).

```
┌─────────────────────────────────────────────┐
│  JENIS CTF                                  │
├─────────────────────────────────────────────┤
│                                             │
│  🏁 Jeopardy-style                          │
│  → Soal individual per kategori             │
│  → Web, Crypto, Forensics, Pwn, Misc       │
│  → Paling umum untuk pemula                 │
│                                             │
│  🏰 Attack-Defense                           │
│  → Tim menyerang server tim lain            │
│  → Sekaligus bertahan dari serangan          │
│  → Lebih advanced                           │
│                                             │
│  🔑 Boot2Root / Machine                      │
│  → Hack sebuah machine dari awal            │
│  → Dapatkan user flag & root flag           │
│  → Contoh: HackTheBox, TryHackMe           │
│                                             │
└─────────────────────────────────────────────┘
```

CTF adalah cara terbaik untuk **belajar cybersecurity sambil bersenang-senang**. Di TISS, tiap divisi di L1 punya spesialisasi CTF masing-masing!

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Coba CTF pertamamu! Kunjungi [picoCTF](https://picoctf.org):

1. Buka [picoctf.org](https://picoctf.org) → klik **Practice**
2. Pilih challenge kategori **General Skills** yang paling mudah
3. Coba selesaikan 1 challenge — temukan flag-nya!

```
✅ Expected: Kamu menemukan flag dengan format flag{...} atau picoCTF{...}
   Rasakan sensasi menemukan flag pertamamu! 🎉
```

> 💡 Jika bingung, tidak apa-apa! Tujuannya adalah **merasakan** pengalaman CTF, bukan menyelesaikan semuanya. Kamu akan semakin jago seiring waktu.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa rank Cipher (English) ada di urutan pertama setelah Void?</summary>

**Jawaban:** Karena **hampir semua** dokumentasi keamanan siber, tools, CVE advisory, dan komunitas internasional menggunakan **Bahasa Inggris**. Tanpa kemampuan bahasa Inggris teknis, kader akan kesulitan mengikuti materi di rank-rank selanjutnya. Ini fondasi yang wajib dimiliki sebelum belajar teknis.

</details>

<details>
<summary>❓ Apa itu CTF dan apa format yang paling cocok untuk pemula?</summary>

**Jawaban:** **CTF (Capture The Flag)** adalah kompetisi cybersecurity di mana peserta menyelesaikan tantangan untuk menemukan string rahasia (*flag*). Format paling cocok untuk pemula adalah **Jeopardy-style** karena soalnya individual per kategori, sehingga bisa memilih tantangan sesuai kemampuan.

</details>

<details>
<summary>❓ Seorang anggota TISS yang sudah menyelesaikan semua rank Null Teaming (Rank 1 - Sentinel), apa langkah selanjutnya?</summary>

**Jawaban:** Mereka naik ke **L1: Operational Layer** dan memilih spesialisasi:

**Primary Department** (fokus teknis + CTF):
- 🔴 Red Teaming — Web Pentesting + CTF Offensive
- 🔵 Blue Teaming — Web Log & Monitoring + CTF Defensive
- 🟡 Yellow Teaming — Web Development + CTF Builder

Sekaligus bergabung di **Secondary Department** (Guild organisasi):
- 🟣 Purple Guild — Kaderisasi & kurikulum
- 🟠 Orange Guild — Humas & event
- 🟢 Green Guild — IT Operations

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami urutan ranking dan alasan di baliknya
- [ ] Saya bisa menjelaskan apa itu CTF dan jenis-jenisnya
- [ ] Saya sudah mencoba 1 challenge di picoCTF
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [picoCTF](https://picoctf.org) — Platform CTF terbaik untuk pemula, dibuat oleh Carnegie Mellon University
- [TryHackMe](https://tryhackme.com) — Platform belajar cybersecurity interaktif dengan room bertingkat
- [CTFtime](https://ctftime.org) — Kalender kompetisi CTF internasional

---

## ➡️ Besok

**Day 5: Setup Tools & Weekly Mission** — Hari terakhir minggu ini! Kita akan setup semua tools yang dibutuhkan (GitHub, TryHackMe, VS Code) dan menyelesaikan misi mingguan pertamamu. Siap untuk "resmi" memulai perjalanan? 🚀

---

*📅 TISS Null Teaming · Week 1 · Day 4 · VOID Rank*
