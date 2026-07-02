# 📡 Week 8 · Day 5: Lab & Weekly Mission

> **Rank**: PACKET | **Minggu ke-8**, Hari 5/5 | **Durasi**: ~90–120 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓░░] 80% — PACKET Rank (Minggu 4 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░] 33% — Hari 40 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → 🔄 PACKET → ⬜ FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini kamu telah mempelajari fondasi Keamanan dan Administrasi Sistem:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | User & Group | Akar filosofi Multi-User. Konsep "Root" UID 0 dan cara pindah wujud `su`. |
| Day 2 | File Permissions | Bedah output `ls -l` (User/Group/Others) dan hitungan `chmod` 4-2-1. |
| Day 3 | Ownership & PrivEsc | Kenapa pakai `sudo` lebih aman daripada langsung jadi Root, & ganti kepemilikan (`chown`). |
| Day 4 | Process Management | Cari maling dengan `top` & `ps aux`, matikan dengan `kill -9 [PID]`. |

---

## 🧪 Hands-On Lab (Pemanasan Izin File)

Sebelum terjun ke Wargame, mari pastikan jari-jarimu sudah luwes mengatur izin file di sistem lokal (WSL/Mac).

### Step 1: Bereksperimen dengan Permissions
1. Buka Terminal lokalmu. Pergi ke folder Home (`cd ~`).
2. Buat file baru: `touch rahasia_ku.txt`
3. Cek izin defaultnya: `ls -l rahasia_ku.txt` (Biasanya `-rw-r--r--`).
4. Ubah izinnya menjadi Full Akses untuk Semua Orang (Angka keramat 777!):
 `chmod 777 rahasia_ku.txt`
5. Cek lagi dengan `ls -l`. Kamu akan melihat izinnya berubah hijau (atau setidaknya tu `-rwxrwxrwx`).
6. Sekarang, cabut semua izin untuk grup dan orang luar (Sangat Rahasia: cuma kamu yang boleh baca/tulis, yaitu kode 600):
 `chmod 600 rahasia_ku.txt`
7. Cek dengan `ls -l`. Hasilnya pasti `-rw-------`. Selesai!

**Expected Output:**
```
Kamu telah membuktikan bahwa hak baca-tulis file di Linux sepenuhnya bisa dimanipulasi dengan menggunakan kombinasi angka ajaib chmod!
```

---

## 🎯 Weekly Mission

### Misi: "OverTheWire Bandit - The Persistence (Level 4 - 8)"

**Deskripsi:**
Minggu lalu kamu berhasil menyelesaikan Bandit Lvl 0 sampai 3. Minggu ini, rintangannya bukan sekadar nama file yang aneh, melainkan file-file tersebut disembunyikan menggunakan atribut khusus, jumlahnya ribuan, atau ukuran byte-nya sangat spesifik. Kamu HARUS menggabungkan perintah `ls -la`, `cat`, `grep`, dan `find`!

**Instruksi Lab Wargame:**
Buka kembali instruksi resmi: [https://overthewire.org/wargames/bandit/](https://overthewire.org/wargames/bandit/)

1. Cari file `bandit-writeup.md` milikmu dari tugas minggu lalu. Kita akan melanjutkannya!
2. Jika lupa cara login, ingat perintahnya (Misal untuk lanjut dari level 3 ke 4):
 `ssh bandit4@bandit.labs.overthewire.org -p 2220` (masukkan password yang kamu dapat minggu lalu).
3. **Misi Level 4**: Password disembunyikan di dalam sebuah direktori, di satu-satunya file yang berjenis "human-readable" (bisa dibaca manusia).
4. **Misi Level 5**: Password disembunyikan di bawah direktori `inhere`, dengan kriteria: tidak bisa dieksekusi (not executable), ukuran *tepat* 1033 bytes! (Hint: gunakan perintah `find` dengan parameter *size*).
5. Lanjutkan mendaki hingga **mendapatkan password untuk Bandit Level 9** (Batas akhir misi adalah memecahkan Level 8 ke 9).

**Deliverables:**
Buka file `bandit-writeup.md` di folder `week-07`, buat judul baru `## Week 8 - Continuation` dan dokumentasikan!

```markdown
## Week 8 - Continuation

### Level 4 to Level 5
- **Password didapat**: [...]
- **Perintah yang saya gunakan**: 
 - `file./*` (untuk mencari tahu tipe file mana yang 'human-readable'/ASCII teks).
 - `cat [nama_file_target]`

### Level 5 to Level 6
- **Password didapat**: [...]
- **Perintah yang saya gunakan**: [Tulis perintah "find" ajaibmu yang memfilter size tepat 1033 bytes]

### Level 6 to Level 7
- **Password didapat**: [...]
- **Perintah yang saya gunakan**: [Hint: gunakan `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`]

### Level 7 to Level 8
- **Password didapat**: [...]
- **Perintah yang saya gunakan**: [Hint: gunakan kombinasi Pipa `|` dan `grep`]

### Level 8 to Level 9
- **Password didapat**: [...]
- **Perintah yang saya gunakan**: [Hint: gunakan perintah `sort` dipadukan dengan `uniq -u`]
```

**Kriteria Sukses:**
- [ ] Kamu berhasil mengekstrak password dari file tersembunyi
- [ ] Kamu sukses menerapkan pencarian dengan filter *size* (Level 5) dan filter kepemilikan *User/Group* (Level 6)
- [ ] Log penyelesaian (Level 4 hingga 8) ditambahkan ke dalam file writeup lamamu
- [ ] Perubahan file sudah di-commit dan di-push ke GitHub

**Estimasi Waktu:** 2 – 3 jam (Bersabarlah, wargame Linux butuh Google/STFW!).

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Kamu ingin menyuruh folder "Laporan" agar bisa dibaca, ditulis, dan dieksekusi oleh siapa saja (Full akses 777), tapi kamu juga ingin agar SEMUA file di DALAM folder tersebut ikut menjadi 777. Opsi apa yang kamu tambahkan pada chmod?</summary>

**Jawaban:** Tambahkan flag **`-R`** (huruf R besar, artinya *Recursive*). Contoh: `chmod -R 777 Laporan/`.

</details>

<details>
<summary>❓ [SEDANG] Pada tantangan Bandit Level 7 (mencari file berdasarkan nama User dan Group), mengapa perintah pencariannya ditambahkan kode aneh `2>/dev/null` di belakangnya?</summary>

**Jawaban:** Saat mencari file di seluruh sistem root (`/`), pasti ada banyak folder rahasia milik Root yang akan menolak akses kita (muncul ribuan baris eror *"Permission denied"* di layar). Trik `2>/dev/null` berguna untuk **membuang semua pesan error (Output Stream ke-2) ke tong sampah hitam (null)**, sehingga yang tampil di layar HANYA hasil pencarian yang bersih dan berhasil.

</details>

<details>
<summary>❓ [SULIT] Apa yang salah dengan logika kalimat ini: "Karena aku login sebagai Root, aku pasti tidak perlu memikirkan chmod rwx lagi karena aku bisa membaca semuanya."</summary>

**Jawaban:** Logika itu 90% benar, tapi kurang tepat. Root memang bisa masuk izin `Read` dan `Write` file siapa pun tanpa peduli rwx-nya. NAMUN, jika atribut Execute (`x`) dari sebuah file teks/script sengaja dimatikan, **Root sekalipun tidak akan bisa menjalankan (mengeksekusi) script tersebut** sampai ia mengubah hak chmod-nya menjadi executable terlebih dahulu.

</details>

---

## 📋 Weekly Checklist

- [ ] Saya hafal sistem hitungan 4 (Read), 2 (Write), 1 (Execute)
- [ ] Saya bisa mengidentifikasi proses yang berjalan liar dengan `top/ps`
- [ ] Saya memahami bedanya `sudo` dan masuk sepenuhnya sebagai Root
- [ ] Saya menyelesaikan pendakian OverTheWire Bandit hingga Level 8 (Otw Lvl 9)
- [ ] Writeup saya sudah di-push ke GitHub repository `cybersec-journey`

---

## 💬 Diskusi Minggu Ini

1. Level mana dari tantangan Bandit (Lvl 4 - 8) yang membuatmu *stuck* paling lama dan mengharuskanmu paling banyak Googling?
2. Setelah merasakan menggunakan CLI (Terminal) di OverTheWire, apakah menurutmu *hacker* di film yang ngetik cepat dengan layar berjalan otomatis itu realistis?

---

## 🏆 Achievement Unlocked!

```
┌──────────────────────────────────────────┐
│ │
│ 🎖️ LINUX PRIVILEGED │
│ Week 8 Complete │
│ "Root is not just an account. │
│ It is a state of mind." │
│ │
└──────────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 9: Shell Scripting & Automation (PACKET Finale)**

Semua dasar sudah kamu kuasai. Tapi *Hacker* yang baik itu malas. Kita benci mengetik perintah yang sama 100 kali. Oleh karena itu, minggu depan kita akan mempelajari cara merangkai semua perintah yang sudah kamu hafal (ls, grep, ping) menjadi sebuah program yang berjalan otomatis. Kita akan menyentuh **Bash Scripting**, senjata rahasia otomatisasi IT!

Siapkan kopimu, kita masuk ke dunia "Coding" terminal!

---

*📅 TISS Null Teaming · Week 8 · Day 5 · PACKET Rank*
