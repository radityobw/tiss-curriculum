# 🎯 Week 10 · Day 6 (Bonus): Hands-On Learning

> **Rank**: FORGE | **Minggu ke-10** | Bonus Day

---

## 🌐 Platform Hari Ini

**[GitHub Skills — Introduction to GitHub](https://github.com/skills/introduction-to-github)**
Kursus interaktif resmi dari GitHub yang mengajarkan dasar-dasar GitHub langsung di dalam repositori. Kamu belajar dengan mengikuti instruksi otomatis yang muncul di *Issues* dan *Pull Requests*.

💰 **Biaya**: Gratis (dijalankan di repositori GitHub pribadi)
⏱️ **Estimasi Waktu**: ~60 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Membuat branch, commit, dan Pull Request langsung di GitHub
2. Melakukan merge Pull Request dan memahami alur kolaborasi GitHub
3. Mendapatkan pengalaman dengan GitHub Flow — workflow standar industri

---

## 📋 Requirement

* Akun GitHub (sudah dibuat di Week 1 Day 5)
* Peramban web modern (Chrome/Firefox)

> ⚠️ **Jika belum punya akun GitHub**: Buka [github.com](https://github.com), klik **Sign Up**, daftar dengan email aktif. Gratis.

---

## 📝 Prosedur

### Langkah 1: Mulai Kursus
1. Buka [github.com/skills/introduction-to-github](https://github.com/skills/introduction-to-github)
2. Klik tombol hijau **"Use this template"** → **"Create a new repository"**
3. Atur repository:
 - Owner: akun GitHub-mu
 - Repository name: `skills-introduction-to-github`
 - Pilih **Public**
4. Klik **Create repository**
5. Tunggu ~20 detik — GitHub Actions akan otomatis membuat instruksi pertama

### Langkah 2: Ikuti Instruksi Otomatis
1. Buka tab **Issues** di repository baru-mu
2. Akan muncul Issue pertama dengan instruksi langkah demi langkah
3. Ikuti instruksi dengan teliti:
 - **Step 1**: Membuat branch baru
 - **Step 2**: Membuat commit di branch tersebut
 - **Step 3**: Membuat Pull Request
 - **Step 4**: Merge Pull Request
4. Setelah setiap langkah selesai, GitHub Actions akan otomatis membuat instruksi berikutnya

> 💡 **Setiap kali kamu menyelesaikan satu step**, tunggu beberapa detik lalu refresh halaman — instruksi selanjutnya akan muncul secara otomatis via GitHub Actions.

### Langkah 3: Verifikasi dengan Git CLI (Opsional tapi Direkomendasikan)
1. Buka terminal lokal
2. Clone repository yang baru dibuat:
 ```bash
 git clone https://github.com/[username-mu]/skills-introduction-to-github.git
 cd skills-introduction-to-github
 ```
3. Lihat history commit:
 ```bash
 git log --oneline --graph
 ```
4. Cocokkan dengan apa yang terlihat di GitHub web — ini menghubungkan konsep Day 1-2 (Git CLI) dengan Day 6 (GitHub web)

### Langkah 4: Eksplorasi Kursus Lanjutan (Jika Waktu Tersisa)
1. Kembali ke [github.com/skills](https://github.com/skills)
2. Coba kursus **"Communicate using Markdown"** — sangat berguna untuk menulis README dan dokumentasi
3. Proses sama: Use template → ikuti instruksi

---

## 🏁 Target Output

* ✅ Kursus **"Introduction to GitHub"** selesai (semua steps completed)
* 📸 Tangkapan layar: Pull Request yang sudah di-merge di repository-mu
* 📸 Tangkapan layar: Output `git log --oneline --graph` dari terminal (jika mengerjakan Langkah 3)
* 🔗 Link repository: `https://github.com/[username]/skills-introduction-to-github`

---

## 🔄 Fallback

Jika GitHub Skills tidak berfungsi (GitHub Actions error):
1. Unduh dan instal [Git-it (NodeSchool)](https://github.com/jlord/git-it-electron/releases) — aplikasi desktop offline untuk belajar Git dan GitHub
2. Kerjakan semua tantangan di dalam aplikasi
3. Setiap tantangan mengajarkan satu konsep Git/GitHub secara interaktif
