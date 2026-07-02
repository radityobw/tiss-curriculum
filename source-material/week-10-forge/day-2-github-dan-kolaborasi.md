# 🔨 Week 10 · Day 2: GitHub, Remote & Kolaborasi

> **Rank**: FORGE | **Minggu ke-10**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 10 · Day 2/5 | FORGE Rank (Minggu 1 dari 5) | Overall: 47/120 hari (39%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara Git (alat lokal) dan GitHub (layanan cloud)
2. **Menguasai** perintah remote Git (`push`, `pull`, `clone`)
3. **Memahami** alur kolaborasi open-source menggunakan Forking dan Pull Request (PR)

---

## 📖 Materi Inti

### Git vs GitHub

Banyak pemula kebingungan dan menganggap Git dan GitHub itu sama.
- **Git**: Adalah program mesin waktu (Version Control) yang terpasang di dalam laptopmu. Ia bekerja sepenuhnya (offline).
- **GitHub**: Adalah sebuah situs web (Cloud) tempat kamu bisa mengunggah dan membagikan repositori Git-mu agar bisa dilihat dan dikerjakan bersama orang lain di seluruh dunia. (Analoginya: Git adalah rekaman videonya, GitHub adalah YouTube-nya).

### Perintah Git Remote (Jaringan)

Kemarin kita belajar menyimpan kode secara lokal (`commit`). Bagaimana cara mengirimnya ke GitHub? Kita butuh perintah *remote*.

1. **`git clone <URL>`**
 Mengunduh (menyalin) repositori penuh milik orang lain (atau milikmu) dari GitHub ke laptopmu, lengkap dengan seluruh sejarah `git log`-nya.
 
2. **`git remote add origin <URL>`**
 Menyambungkan folder `.git` di laptopmu ke repositori kosong yang baru kamu buat di GitHub. "Origin" adalah nama alias standar untuk URL GitHub-mu.

3. **`git push -u origin main`**
 Mengunggah (mendorong) kode lokalmu dari cabang `main` ke GitHub (`origin`). Ini seperti mem-backup mesin waktumu ke cloud.

4. **`git pull origin main`**
 Mengunduh (menarik) perubahan terbaru dari GitHub ke laptopmu. Wajib dilakukan jika rekan timmu baru saja mengunggah perubahan kode baru, agar kodemu tidak kedaluwarsa.

### Standar Industri Kolaborasi: Branching & Pull Request (PR)

Bagaimana cara tim *developer* dan *hacker* di perusahaan besar bekerja sama membangun aplikasi tanpa saling merusak kode? Rahasianya ada pada kedisiplinan alur kerja (*workflow*) menggunakan Branch dan Pull Request.

1. **Buat Branch Fitur (Feature Branch)**: Di standar industri, kita DILARANG KERAS melakukan `git push` langsung ke cabang utama (`main`). Setiap kali akan menggarap fitur baru atau memperbaiki bug, buatlah cabang (*branch*) baru dengan penamaan yang spesifik. Contoh: `git checkout -b feat/halaman-login` (untuk fitur) atau `bugfix/header-error` (untuk perbaikan).
2. **Push ke Branch Asal (Origin)**: Setelah kodemu selesai dan di-commit secara lokal, dorong (*push*) cabang fitur tersebut ke GitHub: `git push -u origin feat/halaman-login`.
3. **Membuat Pull Request (PR)**: Buka GitHub, lalu buat "Surat Permohonan" penggabungan (Pull Request). Di halaman PR ini, kamu harus memahami apa yang sedang dibandingkan (*compare*):
 - **Base (Tujuan)**: Cabang utama tempat kodemu akan berlabuh (contoh: `main`, `develop`, atau `staging`).
 - **Compare (Sumber)**: Cabang tempat kamu baru saja bekerja (contoh: `feat/halaman-login`).
 GitHub akan menampilkan baris-baris hijau (tambahan) dan merah (hapusan) yang memperlihatkan perbedaan pasti antara cabang sumbermu dan cabang tujuan.
4. **Code Review & Merge**: Rekan tim (atau pemilik repositori pada kasus proyek Open Source/Forking) akan me-review kodemu. Jika lolos uji keamanan dan tiada konflik (Merge Conflict), mereka akan menekan tombol *Merge* untuk menyatukan cabang `feat/halaman-login` milikmu ke dalam `main` secara resmi!

---

## 🧪 Mini Lab

**Durasi**: ~20 menit

Mari hubungkan repositori lokal yang kamu buat kemarin ke GitHub!

1. **Buka GitHub.com**: Login dan klik tombol **New Repository**.
2. **Buat Repositori**: Beri nama `lab-git-pertama`. **PENTING**: Jangan centang opsi *Add a README file*. Biarkan repositori ini benar-benar kosong. Klik *Create repository*.
3. **Hubungkan Remote**: GitHub akan memberikan instruksi. Buka kembali terminal laptopmu (di dalam folder `lab-git-pertama` dari lab kemarin), dan jalankan:
 ```bash
 git remote add origin https://github.com/USERNAME-MU/lab-git-pertama.git
 ```
 *(Ganti USERNAME-MU dengan username GitHub-mu yang asli)*
4. **Unggah (Push)**:
 ```bash
 git branch -M main
 git push -u origin main
 ```
5. **Cek GitHub**: Muat ulang (Refresh) halaman GitHub-mu. Kamu akan melihat file `index.html` kini berhasil mengudara di awan!

*(Catatan: Saat melakukan `git push`, kamu mungkin diminta memasukkan username dan Personal Access Token (PAT) atau menggunakan SSH Key sebagai autentikasi pengamanan pengganti password biasa).*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar antara `git clone` dan sekadar menekan tombol "Download ZIP" di GitHub?</summary>

**Jawaban:** Tombol "Download ZIP" hanya mengunduh file kodenya saja (tanpa folder tersembunyi `.git`), sehingga tidak ada riwayat versi (sejarah mesin waktu) yang ikut terunduh. Sebaliknya, `git clone` mengunduh SELURUH repositori beserta folder `.git`, sehingga kamu bisa melihat sejarah commit dan melanjutkan version control.

</details>

<details>
<summary>❓ Jika rekan timmu baru saja menambahkan fitur baru ke repositori GitHub, perintah apa yang harus kamu jalankan di laptopmu sebelum mulai bekerja agar kodemu selaras dengan miliknya?</summary>

**Jawaban:** `git pull`. Perintah ini akan menarik perubahan terbaru dari repositori remote (GitHub) dan menggabungkannya ke dalam repositori lokalmu. Mengetik kode tanpa mem-pull versi terbaru sering memicu konflik (Merge Conflict) yang memusingkan kelak.

</details>

<details>
<summary>❓ Mengapa kita perlu melakukan Fork alih-alih langsung Push saat ingin berkontribusi pada proyek sumber terbuka orang lain?</summary>

**Jawaban:** Karena kita tidak memiliki hak akses tulis (write permission) secara langsung ke repositori pusat orang lain. Fork membuat salinan repositori tersebut di bawah otoritas akun kita sendiri, sehingga kita bebas memodifikasi dan mem-push kode tanpa merusak repositori asli, lalu menawarkan perubahannya via Pull Request.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan Git () dan GitHub (daring)
- [ ] Saya mengetahui fungsi `git remote`, `push`, `pull`, dan `clone`
- [ ] Saya memahami alur kontribusi Open Source (Fork & Pull Request)
- [ ] Saya berhasil mem-push repositori lokal saya ke GitHub di Mini Lab
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [GitHub Guides: Hello World](https://guides.github.com/activities/hello-world/) — Panduan resmi dan interaktif alur Fork & Pull Request dari GitHub.
- [Oh Shit, Git!?!](https://ohshitgit.com/) — Situs humor praktis untuk menyelamatkan dirimu jika melakukan kesalahan konyol di Git.

---

## ➡️ Besok

**Day 3: Fondasi Web & HTML Dasar** — Mesin waktu kode kita (Git) sudah aman! Mulai besok, kita akan menyelami bahasa yang membentuk tulang punggung miliaran situs web di internet: HTML. Mari mulai merakit kastil (Yellow Team) kita!

---

*📅 TISS Null Teaming · Week 10 · Day 2 · FORGE Rank*
