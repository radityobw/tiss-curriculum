# 🌀 Week 1 · Day 5: Lab & Weekly Mission

> **Rank**: VOID (Unranked) | **Minggu ke-1**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓▓▓] 100% — VOID Rank (Minggu 1 dari 1)

### Overall Journey
[▓░░░░░░░░░░░░░░░░░░░░░░░] 4% — Hari 5 dari 120

### Rank Map
```
🔄 VOID → ⬜ CIPHER → ⬜ PACKET → ⬜ FORGE → ⬜ BREACH → ⬜ SENTINEL
 ↑
 Kamu di sini!
```

---

## 📝 Rekap Minggu Ini

Minggu ini kamu sudah mempelajari:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Pengenalan TISS & Cyber Security | TISS punya 3 layer; Cybersecurity melindungi data/sistem global |
| Day 2 | Tiga Pilar Cyber Security | Red (Offense), Blue (Defense), dan Yellow (Build) saling membutuhkan |
| Day 3 | CIA Triad & Etika Hacking | Confidentiality, Integrity, Availability adalah inti keamanan; harus White Hat |
| Day 4 | Sistem Ranking & Roadmap | Perjalanan 120 hari didesain bertahap; CTF adalah cara kompetitif belajar security |

---

## 🧪 Hands-On Lab

### Prerequisites
- Komputer/laptop dengan minimal 4GB RAM
- Koneksi internet
- Browser modern (Chrome/Firefox)

### Step 1: Buat Akun GitHub

GitHub adalah platform wajib untuk semua orang di dunia IT dan Cybersecurity. Ini akan menjadi tempat kamu menyimpan portfolio (writeup CTF, catatan belajar, script bash/python).

1. Buka [github.com](https://github.com)
2. Klik **Sign Up**
3. Gunakan email kampus atau email pribadi yang profesional
4. Pilih username yang rapi (contoh: `ryo-tiss` atau `ryo-cyber`, hindari username alay)
5. Lakukan verifikasi email

**Expected Output:**
```
Akun GitHub berhasil dibuat dan kamu bisa mengakses dashboard utamamu.
```

### Step 2: Buat Akun TryHackMe

TryHackMe adalah platform belajar cybersecurity interaktif yang akan sangat sering kita gunakan, terutama di rank Packet, Breach, dan Sentinel.

1. Buka [tryhackme.com](https://tryhackme.com)
2. Klik **Join Now** (gratis)
3. Lengkapi dan login
4. Di dashboard utama, cari room **"Welcome"** dan selesaikan tantangan perkenalan singkatnya.

**Expected Output:**
```
Kamu memiliki profil TryHackMe dan mengerti cara menggunakan antarmukanya.
```

### Step 3: Install VS Code

Visual Studio Code (VS Code) adalah text editor yang sangat kuat. Kita akan memakainya untuk menulis catatan markdown, coding HTML/CSS/JS (di rank Forge), dan bash scripting (di rank Packet).

1. Download installer dari [code.visualstudio.com](https://code.visualstudio.com)
2. Install sesuai sistem operasi kamu (Windows/macOS/Linux)
3. Buka VS Code, klik ikon **Extensions** di sidebar kiri (atau tekan `Ctrl+Shift+X`)
4. Cari dan install extension **"Markdown Preview Enhanced"** (untuk melihat hasil Markdown yang kamu tulis)

**Expected Output:**
```
VS Code terbuka dengan sukses dan extension Markdown terinstall.
```

### 🔧 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Email GitHub tidak menerima verifikasi | Cek folder Spam, atau klik tombol "Resend verification email" di settings GitHub. |
| TryHackMe terasa lambat | Coba gunakan VPN (kadang routing ke server Eropa agak lambat dari Indonesia), atau gunakan jaringan berbeda. |
| Instalasi VS Code gagal (permission error) | Di Windows, klik kanan installer dan pilih "Run as Administrator". |

---

## 🎯 Weekly Mission

### Misi: "Identity Card — Deklarasi Perjalanan"

**Deskripsi:** Buat repository (folder project) pertamamu di GitHub! Ini akan menjadi jurnal **identitas digital** kamu selama perjalanan 120 hari ke depan, sekaligus portofolio awal karier cybersecurity-mu.

**Deliverables:**
1. **Repository `cybersec-journey`** di akun GitHub-mu yang bersifat Public.
2. **File README.md** di dalam repository tersebut yang berisi profil singkat, motivasi bergabung dengan TISS, dan target rank-mu.
3. **Esai Singkat** berjudul *"Mengapa Saya Memilih Cyber Security"* (minimal 200 kata), disimpan di folder `week-01` dalam repository tersebut.

**Kriteria Sukses:**
- [ ] Saya punya akun GitHub yang aktif
- [ ] Ada repository public bernama `cybersec-journey`
- [ ] File `README.md` terisi rapi menggunakan sintaks markdown dasar
- [ ] Esai motivasi minimal 200 kata tersedia
- [ ] Link GitHub profile bisa diakses oleh orang lain (teman/mentor)

**Estimasi Waktu:** 1–2 jam

---

## 💡 Knowledge Check

<details>
<summary>❓ Apa tiga prinsip utama dalam CIA Triad?</summary>

**Jawaban:** **Confidentiality** (Kerahasiaan data), **Integrity** (Keutuhan/Keaslian data), dan **Availability** (Ketersediaan sistem).

</details>

<details>
<summary>❓ Pilar apa yang berfokus pada "menemukan celah keamanan dengan cara menyerang sistem"?</summary>

**Jawaban:** **Offensive Security (Red Team)**. Mereka bertugas mendobrak pertahanan untuk menemukan kelemahan sebelum attacker asli melakukannya.

</details>

<details>
<summary>❓ Mengapa kita tidak boleh sembarangan menyerang target di internet, meskipun niatnya "hanya latihan"?</summary>

**Jawaban:** Karena di Indonesia hal tersebut melanggar **UU ITE (Pasal 30)** tentang akses tidak sah. Hacking tanpa **izin tertulis** bisa dikenai pidana penjara. Oleh karena itu, kita selalu berlatih secara legal (contoh: White Hat hacking di platform TryHackMe).

</details>

<details>
<summary>❓ Apa itu CTF dan apa manfaatnya bagi kader Null Teaming?</summary>

**Jawaban:** **Capture The Flag (CTF)** adalah kompetisi di mana peserta mencari string rahasia (flag) tersembunyi. Manfaatnya adalah untuk melatih logika, membiasakan diri memecahkan masalah (*problem solving*), dan belajar *hands-on* secara aman sekaligus menyenangkan.

</details>

<details>
<summary>❓ Apa hubungan antara L0, L1, dan L2 di organisasi TISS?</summary>

**Jawaban:**
**L0 (Null Teaming)** adalah tempat inkubasi di mana kader diajarkan fondasi dari nol. Setelah lulus (rank Sentinel), kader naik ke **L1 (Operational Layer)** dan bergabung dengan Red/Blue/Yellow Team untuk mendalami spesialisasi serta berkontribusi di Guild (Secondary Department). Sementara itu, para senior dan manajemen yang mengatur berjalannya semua layer tersebut ada di **L2 (White Teaming)**.

</details>

---

## 📋 Weekly Checklist

- [ ] Saya bisa menjelaskan peran TISS, cybersecurity, dan 3 pilar utama
- [ ] Saya memahami CIA Triad dan etika dasar (White Hat vs Black Hat)
- [ ] Saya paham roadmap perjalanan 24 minggu (120 hari) ke depan
- [ ] Saya sudah menyelesaikan Hands-On Lab (Setup GitHub, TryHackMe, VS Code)
- [ ] Saya sudah menyelesaikan Weekly Mission (Identity Card)
- [ ] Saya siap untuk masuk ke materi teknis minggu depan!

---

## 💬 Diskusi Minggu Ini

1. Setelah membaca tentang Red, Blue, dan Yellow Team minggu ini, mana yang menurutmu paling cocok dengan kepribadianmu dan mengapa?
2. Apakah menulis menggunakan format Markdown di VS Code dan GitHub terasa sulit? Coba bagikan tips singkat jika kamu sudah terbiasa!

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────────┐
│ │
│ 🎖️ VOID COMPLETE │
│ Week 1 of 24 Complete │
│ "Every expert was once a beginner" │
│ │
│ 🌀 Rank: VOID → CLEARED! │
│ 📊 Progress: 4% │
│ 🔜 Next Rank: CIPHER │
│ │
└─────────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 2: Reading Technical Documentation (CIPHER Rank)**

Selamat! Kamu sudah menyelesaikan rank Void dan resmi naik ke **🔤 CIPHER**! Mulai Senin besok, kita akan membangun fondasi **Bahasa Inggris Teknis** — skill yang akan menentukan seberapa cepat kamu memahami teknologi keamanan siber.

Siap membuka "kode rahasia" dunia dokumentasi teknis?

> 🚀 *"The limits of my language mean the limits of my world."* — Ludwig Wittgenstein

---

*📅 TISS Null Teaming · Week 1 · Day 5 · VOID Rank*
