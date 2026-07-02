# 📡 Week 7 · Day 5: Lab & Weekly Mission

> **Rank**: PACKET | **Minggu ke-7**, Hari 5/5 | **Durasi**: ~90–120 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓░░░░] 60% — PACKET Rank (Minggu 3 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░] 29% — Hari 35 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → 🔄 PACKET → ⬜ FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini kamu telah mempelajari fondasi sistem peretasan:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Filosofi Linux | Linux itu Kernel, Ubuntu itu Distro. CLI lebih dominan di server dibanding GUI. |
| Day 2 | Direktori | Sistem berawal dari Root (`/`). Pindah dengan `cd`, lihat isi dengan `ls -la`. |
| Day 3 | Manipulasi File | Membuat (`mkdir`, `touch`), Memindah (`cp`, `mv`), Menghancurkan (`rm`). |
| Day 4 | Baca & Pencarian | Dewa filter: `grep`. Baca: `less/tail`. Sihir gabungan: `|` (Piping). |

---

## 🧪 Hands-On Lab (Setup Environment)

Sebelum melakukan misi mingguan, kamu **WAJIB** punya lingkungan Linux asli di komputermu. Membaca teori tentang perintah `cd` dan `ls` tidak akan berguna jika jari-jarimu tidak mempraktikkannya.

Pilih SALAH SATU skenario di bawah berdasarkan sistem operasi aslimu.

### Opsi A: Pengguna Windows (Disarankan: Gunakan WSL)
Windows Subsystem for Linux (WSL) memungkinkanmu menjalankan inti Ubuntu persis di dalam Windows tanpa butuh aplikasi berat seperti VirtualBox/VMware.
1. Buka *PowerShell* sebagai Administrator (Klik Start -> ketik powershell -> Run as Administrator).
2. Ketik perintah sakti ini: `wsl --install` lalu tekan Enter.
3. Tunggu sampai selesai (ukurannya sekitar 1-2 GB).
4. Restart PC/Laptopmu.
5. Setelah nyala kembali, cari aplikasi **"Ubuntu"** di menu Start.
6. Buat *username* dan *password* UNIX barumu (Note: saat ngetik password di Linux, hurufnya tidak akan muncul/bintang di layar, itu wajar demi keamanan. Ketik saja terus lalu Enter).

### Opsi B: Pengguna Mac 
Kabar baik! Sistem operasi Mac (macOS) diturunkan dari UNIX (saudaranya Linux). 95% perintah Linux bisa berjalan mulus di sini.
1. Cari aplikasi bawaan bernama **Terminal** menggunakan Spotlight (`Cmd + Space`).
2. Selesai! Kamu siap bekerja.

*(Jika gagal menggunakan Opsi A/B, kamu selalu bisa menggunakan website penyedia Linux Terminal gratis di browser seperti [JSLinux](https://bellard.org/jslinux/)*).

---

## 🎯 Weekly Mission

### Misi: "OverTheWire Bandit - Level 0 hingga 3"

**Deskripsi:**
Ini bukan tutorial membaca, ini adalah *Game Hacking* legendaris di dunia nyata. Komunitas keamanan global memiliki sebuah server latih (Wargame) bernama **OverTheWire Bandit**. Kamu harus menggunakan perintah-perintah CLI Linux yang sudah dipelajari minggu ini untuk "mencuri" file password (Flag) di dalam server mereka, lalu naik ke level berikutnya.

**Instruksi Lab Wargame:**
Buka panduannya di web resmi: [https://overthewire.org/wargames/bandit/](https://overthewire.org/wargames/bandit/)

1. **Bandit Level 0**:
 - Buka Terminal Ubuntu/Mac-mu.
 - Ketik perintah (SSH adalah protokol untuk meremote server linux dari jarak jauh):
 `ssh bandit0@bandit.labs.overthewire.org -p 2220`
 - Jika ditanya *(yes/no)* ketik `yes`.
 - Masukkan password: `bandit0`
 - Kamu berhasil login ke server mereka!
2. **Menuju Bandit Level 1**:
 - Di dalam server tadi (bandit0), temukan sebuah file bernama `readme`.
 - Gunakan perintah baca file (seperti `cat`) untuk melihat isinya.
 - Deretan kata/angka acak di dalamnya adalah **Password untuk Level 1**! Copy password itu.
 - Ketik `exit` untuk keluar dari server.
3. Lanjutkan meretas masuk sebagai user `bandit1` menggunakan password yang baru kamu dapatkan tadi. Lanjutkan permainan hingga mencapai **Level 3**.

**Deliverables:**
1. Buka repository `cybersec-journey` di VS Code.
2. Buka folder `week-07`.
3. Buat file `bandit-writeup.md`.
4. Dokumentasikan cara/perintah (*command*) yang kamu gunakan untuk mengalahkan tiap level. (Format bebas, contoh di bawah):

```markdown
# OverTheWire: Bandit Level 0 - 3 Writeup

## Level 0 to Level 1
- **Password didapat**: [Tulis password acaknya di sini]
- **Perintah yang saya gunakan**: 
 - `ls` (untuk melihat ada file apa saja)
 - `cat readme` (untuk membaca isi passwordnya)

## Level 1 to Level 2
- **Password didapat**: [...]
- **Perintah yang saya gunakan**: [Tulis bagaimana caramu membaca nama file yang berawalan dengan simbol minus '-'. (Hint: Google "how to cat a file named dash in linux")]

## Level 2 to Level 3
- **Password didapat**: [...]
- **Perintah yang saya gunakan**: [Tulis bagaimana kamu membaca file yang namanya memakai spasi. (Hint: Gunakan tanda kutip atau backslash)]
```

**Kriteria Sukses:**
- [ ] Linux environment (WSL/Terminal) berhasil terpasang di PC/Laptop
- [ ] Folder `week-07` berisi file `bandit-writeup.md`
- [ ] Kamu berhasil menyentuh Level 3 di game OverTheWire Bandit
- [ ] File Writeup sudah ter-commit dan di-push ke GitHub

**Estimasi Waktu:** 2 – 2.5 jam

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Mengapa password tidak muncul (bahkan tidak ada tanda bintang `***`) saat kita mengetiknya di Terminal Linux?</summary>

**Jawaban:** Itu adalah fitur keamanan warisan UNIX masa lalu (mencegah orang di sebelahmu menghitung berapa panjang karakter passwordmu dari jumlah bintangnya). Terminal memang terlihat diam/macet, tapi *input*-mu tetap masuk. Ketik saja sampai selesai dan tekan Enter.

</details>

<details>
<summary>❓ [SEDANG] Di Bandit Level 2, ada file bernama "spaces in this filename". Mengapa mengetik `cat spaces in this filename` akan menyebabkan Error (No such file or directory)?</summary>

**Jawaban:** Karena Terminal membaca spasi sebagai pemisah antar *command* (parameter). Terminal mengira kamu menyuruh `cat` untuk membuka 4 file berbeda: (1) file bernama `spaces`, (2) file `in`, (3) file `this`, (4) file `filename`. Untuk mengatasi ini, kita harus mengurung/mengapit nama filenya dengan tanda kutip ganda: `cat "spaces in this filename"`.

</details>

<details>
<summary>❓ [SEDANG] Perintah `ssh` singkatan dari Secure Shell. Apa fungsi utama protokol ini di dunia nyata?</summary>

**Jawaban:** SSH digunakan oleh System Administrator atau Hacker untuk masuk (login) secara aman ke Terminal (*Command Line*) dari server/komputer target yang berada jauh di belahan bumi lain. Protokol ini dienkripsi kuat sehingga aman dari sadapan (seperti halnya HTTPS mengamankan web).

</details>

---

## 📋 Weekly Checklist

- [ ] Saya memiliki akses ke Linux Terminal (WSL/Mac/VM)
- [ ] Saya tidak panik jika ngetik password tidak muncul bintang
- [ ] Saya bisa menggunakan `ls` dan `cd` dengan lancar tanpa mikir
- [ ] Saya berhasil login SSH ke OverTheWire Bandit
- [ ] Saya sudah mengerjakan Weekly Mission `bandit-writeup.md`
- [ ] File mission sudah ter-push ke GitHub

---

## 💬 Diskusi Minggu Ini

1. Selamat datang di Command Line! Bagaimana kesan pertamamu mengendalikan komputer tanpa klik *mouse* sama sekali di misi OverTheWire? Apakah pusing atau malah merasa seperti hacker sejati?
2. Jika ada teman yang mentok di Bandit Level 1 (file dengan nama strip `-`), jangan langsung beri tahu jawabannya. Berikan dia petunjuk (Hint) apa yang harus di-Google! 

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ CLI INITIATE │
│ Week 7 Complete │
│ "Your mouse has no power here." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 8: Linux Security & Permissions (PACKET Rank)**

Kamu sudah tahu cara mainnya. Tapi sebuah sistem yang baik memiliki pintu terkunci. Minggu depan kita akan masuk ke fondasi keamanan Linux paling tua: **Permissions (rwx) & Sudo**. Kamu akan belajar siapa itu "Root", mengapa ia layaknya Tuhan di dalam server, dan bagaimana cara membatasi hak akses file agar tidak mudah dicuri hacker lain!

---

*📅 TISS Null Teaming · Week 7 · Day 5 · PACKET Rank*
