# 🔨 Week 10 · Day 5: Lab & Mission Halaman Profil & Hosting

> **Rank**: FORGE | **Minggu ke-10**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓▓▓] 100% — FORGE Rank (Minggu 1 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░] 41% — Hari 50 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → 🔄 FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Di minggu pertama rank Forge, kita telah meletakkan fondasi absolut pembangunan perangkat lunak web dan kolaborasi modern:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Git Local & Version Control | Memakai mesin waktu (`init`, `add`, `commit`) |
| Day 2 | GitHub, Remote & Kolaborasi | Menyambungkan versi ke awan (`remote`, `push`, `pull`, `clone`) |
| Day 3 | Fondasi Web & HTML Dasar | Memahami HTTP dan membangun kerangka web dengan tag semantik |
| Day 4 | CSS Fundamentals & DevTools | Mendesain wajah antarmuka fleksibel dengan Box Model dan Flexbox |

---

## 🧪 Hands-On Lab

### Prerequisites
- Aplikasi Terminal & Git terinstal di komputermu
- VS Code dengan file HTML & CSS
- Akun GitHub aktif (dibuat di Week 1)

### Misi Hari Ini: "Kastil Pertama Mengudara di Awan"

Di lab ini, kamu akan membangun sebuah halaman profil (Portofolio) pribadi sederhana dan mendeploy (menerbitkannya) ke internet menggunakan **GitHub Pages**. GitHub Pages adalah layanan hosting peramban web statis (HTML/CSS/JS) gratis langsung dari repositori GitHub-mu!

### Step 1: Perakitan Kastil (Lokal)

1. Buka Terminal, buat folder baru dan masuk ke dalamnya:
 ```bash
 mkdir profil-cyber-saya
 cd profil-cyber-saya
 ```
2. Mulai inisialisasi mesin Git:
 ```bash
 git init
 ```
3. Buka folder ini di VS Code, buat file `index.html`.
4. Rancang halaman web profil singkat. (Gunakan `<header>`, `<main>`, serta masukkan 1 tag `<form>` pura-pura agar terlihat kompleks).
5. Buat file `style.css` dan sambungkan ke file HTML-mu. Gunakan Flexbox agar elemen-elemen profil berjejer rapi ke tengah layar (centering).
6. Simpan hasil kerja ke ruang tunggu (Staging Area) lalu jadikan permanen (Commit):
 ```bash
 git add.
 git commit -m "Versi final halaman profil portofolio"
 ```

### Step 2: Meluncur ke Awan (GitHub)

1. Buka [github.com](https://github.com) dan tekan tombol **New Repository**.
2. Beri nama repositori (contoh: `profil-cyber-saya`), setel menjadi **Public**, abaikan README, klik Create.
3. Kembali ke terminalmu, kaitkan repositori awan dengan mesin, lalu dorong ke udara:
 ```bash
 git remote add origin https://github.com/USERNAME/profil-cyber-saya.git
 git branch -M main
 git push -u origin main
 ```

### Step 3: Menyalakan Layanan Hosting (Deploy)

1. Di repositori GitHub yang baru diunggah, klik tab ⚙️ **Settings** (di panel atas).
2. Di baris sebelah kiri (Sidebar), gulir ke bawah dan cari menu **Pages** (GitHub Pages).
3. Di bagian **Build and deployment** -> *Source*, pastikan terpilih "Deploy from a branch".
4. Pada drop-down *Branch*, pilih cabang **main** (atau master), klik tombol **Save**.
5. Tunggu sekitar 1-2 menit. Muat ulang (Refresh) halamannya, maka akan muncul pita notifikasi hijau yang berisi tautan publik website profilmu (contoh: `https://USERNAME.github.io/profil-cyber-saya/`).

**Expected Output:**
```
Siapa pun (teman, rekan, klien di seluruh dunia) sekarang dapat mengunjungi tautan GitHub Pages tersebut dari ponsel mereka dan menatap langsung desain dokumen pertamamu tanpa kendala!
```

---

## 💡 Knowledge Check

<details>
<summary>❓ Perintah apa yang bertugas menjepret foto (snapshot) riwayat dokumen kamu di Ruang Tunggu (Staging Area) untuk dipindahkan secara permanen ke Repositori lokal?</summary>

**Jawaban:** Perintah `git commit -m "Pesan"`.

</details>

<details>
<summary>❓ Apa perbedaan antara metode pengiriman data HTTP GET dan POST?</summary>

**Jawaban:** Metode **GET** menyertakan data langsung di dalam URL, sedangkan metode **POST** menyembunyikan data tersebut di dalam *Body* dari *request* HTTP, sehingga lebih aman.

</details>

<details>
<summary>❓ Di dalam CSS, selektor jenis apa (diwakili dengan simbol #) yang memiliki prioritas tertinggi dan hanya boleh dipasang pada satu elemen spesifik dalam satu halaman?</summary>

**Jawaban:** Selektor **ID** (ID Selector).

</details>

<details>
<summary>❓ Apa nama layanan gratis dari GitHub yang dapat mengubah *file* statis (HTML/CSS/JS) di repositori kita menjadi sebuah *website* publik yang bisa diakses siapa saja?</summary>

**Jawaban:** GitHub Pages.

</details>

<details>
<summary>❓ Mengapa kita sering melakukan 'Forking' saat ingin berkontribusi pada proyek sumber terbuka (Open-Source), daripada membuat *Branch* biasa?</summary>

**Jawaban:** Karena kita biasanya tidak memiliki akses tulis (*write permission*) ke proyek utama orang lain. 'Forking' membuat salinan proyek tersebut ke akun kita sendiri, sehingga kita bisa memodifikasi kodenya secara bebas, dan setelah selesai, menawarkan perubahan tersebut ke proyek asli menggunakan *Pull Request*.

</details>

---

## 📋 Weekly Checklist

- [ ] Saya sanggup menyatukan siklus ritme dasar Git Local ke dalam kegiatan *coding*.
- [ ] Saya dapat mendorong karya terminal menuju wadah daring GitHub.
- [ ] Saya memahami struktur anatomi tag semantik perancah tulang HTML5.
- [ ] Saya mampu menyeimbangkan tata rias laman web berbasis CSS Box Model.
- [ ] Saya sukses mengudara menyajikan tautan publik dari GitHub Pages.

---

## 💬 Diskusi Minggu Ini

1. Sesudah mencicipi rumitnya CSS Flexbox di sesi merakit laman profil, apakah sensasinya memusingkan atau malah memantik gelora kreativitas merias kotak-kotak?
2. Jika ada satu pesan peringatan (Commit Message) paling menggelitik atau konyol yang pernah kamu ketikkan minggu ini, apakah itu? 

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────────┐
│ │
│ 🎖️ WEB FOUNDATION ENGINEER │
│ Week 10 of 24 Complete │
│ "First brick of the fortress" │
│ │
│ 🔨 Rank: FORGE (1/5) │
│ 📊 Progress: 41% │
│ │
└─────────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 11: JavaScript Fundamentals**

Minggu ini kita telah mempelajari fondasi web statis menggunakan HTML dan CSS. Besok, kita akan mulai mempelajari **JavaScript**, bahasa pemrograman yang akan membuat halaman web menjadi dinamis dan interaktif. Bersiaplah untuk masuk lebih dalam ke dunia *coding*!

---

*📅 TISS Null Teaming · Week 10 · Day 5 · FORGE Rank*
