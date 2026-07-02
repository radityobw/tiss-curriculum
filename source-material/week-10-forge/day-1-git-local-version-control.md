# 🔨 Week 10 · Day 1: Git Local & Version Control

> **Rank**: FORGE | **Minggu ke-10**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 10 · Day 1/5 | FORGE Rank (Minggu 1 dari 5) | Overall: 46/120 hari (38%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep Version Control System (VCS) dan mengapa Git diciptakan
2. **Menguasai** perintah dasar Git di komputer lokal (`init`, `add`, `commit`)
3. **Menggunakan** percabangan (`branch`) untuk pengembangan fitur paralel

---

## 📖 Materi Inti

### Apa itu Git? Mengapa Kita Butuh Version Control?

Pernahkah kamu membuat dokumen dan menyimpannya dengan nama seperti ini:
- `Tugas_Akhir.docx`
- `Tugas_Akhir_Revisi.docx`
- `Tugas_Akhir_Revisi_Final.docx`
- `Tugas_Akhir_Revisi_Final_BGT.docx`

Ini adalah cara manual melacak versi (Version Control). Dalam dunia pemrograman (di mana satu aplikasi bisa memiliki ribuan file kode dan dikerjakan ratusan orang), cara manual ini akan berujung pada bencana.

**Git** diciptakan (oleh Linus Torvalds, pembuat Linux) untuk memecahkan masalah ini. Git merekam setiap baris perubahan pada kode kita seperti sebuah "Mesin Waktu". Jika ada kode yang rusak, kita bisa memutar waktu kembali ke versi sebelumnya dengan satu perintah.

### Konsep Tiga Ruang Git (The Three States)

Sebelum perintah teknis, pahami dulu alur kerja Git yang membagi direktori menjadi 3 ruang:

1. **Working Directory (Ruang Kerja):** Tempat kamu mengetik dan memodifikasi file secara langsung.
2. **Staging Area (Ruang Tunggu):** Tempat kamu memilih file mana saja yang "siap difoto" untuk versi berikutnya. (Perintah: `git add`)
3. **Repository (.git directory):** Album foto permanen tempat versi-versi kodemu disimpan dengan aman. (Perintah: `git commit`)

### Perintah Dasar Git (Local)

Berikut adalah siklus sehari-hari menggunakan Git di komputermu (tanpa butuh internet):

1. **`git init`**
 Menyulap folder biasa menjadi repositori Git. Perintah ini membuat folder tersembunyi `.git`.
2. **`git status`**
 Melihat status file saat ini (merah = belum di-track/dimodifikasi, hijau = sudah di ruang tunggu).
3. **`git add <nama_file>`** atau **`git add.`**
 Memasukkan file yang diubah dari Ruang Kerja ke Ruang Tunggu (Staging Area). Titik (`.`) berarti memasukkan semua file yang berubah.
4. **`git commit -m "Pesan perubahan"`**
 Mengambil foto/snapshot permanen dari file di Ruang Tunggu dan memindahkannya ke Repositori. Selalu gunakan pesan yang deskriptif!
5. **`git log`**
 Melihat sejarah (album) dari seluruh commit yang pernah dilakukan.

### Percabangan (Branching) & Merging

Fitur paling mematikan dari Git adalah **Branching**. 

Bayangkan kamu sedang membuat website utama (`main` branch) yang sudah stabil. Tiba-tiba kamu ingin mencoba merombak desain (eksperimen). Daripada merusak yang sudah stabil, kamu membuat cabang (branch) baru.

- **`git branch <nama_cabang>`**: Membuat cabang baru.
- **`git checkout <nama_cabang>`**: Berpindah masuk ke cabang tersebut. (Bisa disingkat `git checkout -b <nama_cabang>` untuk buat sekaligus pindah).
- **`git merge <nama_cabang>`**: Menggabungkan hasil kerja dari cabang eksperimen kembali ke cabang `main` setelah kamu yakin kodenya berhasil.

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari buat mesin waktu Git pertamamu di terminal Linux/Mac atau Git Bash (Windows)!

1. Buka terminal, buat folder baru dan masuk ke dalamnya:
 ```bash
 mkdir lab-git-pertama
 cd lab-git-pertama
 ```
2. Inisialisasi Git:
 ```bash
 git init
 ```
3. Buat file baru bernama `index.html`:
 ```bash
 echo "<h1>Halo Dunia!</h1>" > index.html
 ```
4. Cek status (pasti index.html berwarna merah):
 ```bash
 git status
 ```
5. Pindahkan ke Staging Area (Ruang Tunggu):
 ```bash
 git add index.html
 ```
6. Simpan permanen (Commit):
 ```bash
 git commit -m "Membuat file index html pertama"
 ```
7. Lihat sejarah (Mesin Waktu):
 ```bash
 git log
 ```

---

## 💡 Quiz Kilat

<details>
<summary>❓ Jika kita mengubah file tetapi BELUM melakukan `git add`, file tersebut berada di ruang mana?</summary>

**Jawaban:** File tersebut masih berada di **Working Directory (Ruang Kerja)**. Git menyadari file tersebut berubah, namun belum dipersiapkan untuk disimpan permanen.

</details>

<details>
<summary>❓ Mengapa kita sangat dianjurkan menulis pesan commit (-m) yang jelas alih-alih asal ketik seperti "asdfg"?</summary>

**Jawaban:** Karena pesan commit berfungsi seperti label pada album foto sejarah kodemu. Di masa depan (atau saat bekerja dengan tim), pesan yang jelas (contoh: "Memperbaiki bug pada tombol login") akan sangat membantu memahami apa dan mengapa perubahan itu dibuat tanpa harus membaca semua kodenya satu per satu.

</details>

<details>
<summary>❓ Apa kegunaan utama dari fitur Branch di Git?</summary>

**Jawaban:** Untuk mengisolasi pengerjaan fitur baru atau eksperimen agar **tidak merusak cabang utama** (`main` / kode yang stabil). Jika eksperimennya gagal, branch bisa dihapus tanpa memengaruhi `main`. Jika berhasil, bisa digabungkan (`merge`).

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami bedanya Git (Software) dan GitHub (Website)
- [ ] Saya hafal siklus 3 langkah Git (Working Dir -> Staging Area -> Repository)
- [ ] Saya berhasil menjalankan `git init`, `add`, dan `commit` di Mini Lab
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials) — Visualisasi terbaik tentang cara kerja Git.
- [Pro Git Book](https://git-scm.com/book/en/v2) — Buku resmi Git (Gratis dan lengkap).

---

## ➡️ Besok

**Day 2: GitHub, Remote & Kolaborasi** — Hari ini kamu bermain Git sendirian tanpa internet. Besok, kita akan belajar cara menaruh kode tersebut ke awan (GitHub) agar bisa berkolaborasi dengan ribuan *hacker* dan *developer* lain di seluruh dunia!

---

*📅 TISS Null Teaming · Week 10 · Day 1 · FORGE Rank*
