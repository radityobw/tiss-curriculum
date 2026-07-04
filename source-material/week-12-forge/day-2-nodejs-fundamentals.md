# 🔨 Week 12 · Day 2: Node.js Fundamentals

> **Rank**: FORGE | **Minggu ke-12**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 12 · Day 2/5 | FORGE Rank (Minggu 3 dari 5) | Overall: 57/120 hari (47%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menjelaskan** apa itu Node.js dan bagaimana ia mengubah cara *developer* menggunakan JavaScript.
2. **Menggunakan** *Node Package Manager (NPM)* untuk menginisialisasi proyek dan mengelola *library* atau *dependency*.
3. **Membedakan** cara *import/export* *module* menggunakan format klasik (*CommonJS*) dan format modern (*ES Modules / ESM*).

---

## 📖 Materi Inti

### Evolusi Node.js: Mengeksekusi JavaScript di Luar Browser

Pada awalnya, JavaScript adalah bahasa yang hanya bisa hidup dan dieksekusi di dalam *browser* (seperti Chrome, Safari, atau Firefox). Karena berjalan di *browser*, JavaScript tidak memiliki akses ke sistem operasi komputer; ia tidak bisa membaca atau menulis *file* di *hard disk*, dan tidak bisa digunakan untuk membuat *server*. Tugas JavaScript saat itu hanyalah memanipulasi *DOM* dan membuat halaman web menjadi interaktif.

Namun pada tahun 2009, Ryan Dahl memiliki ide cemerlang. Ia mengambil **V8 Engine** (mesin penerjemah JavaScript yang super cepat milik Google Chrome), mengeluarkannya dari *browser*, dan memodifikasinya agar bisa berjalan langsung di atas sistem operasi (Windows, Mac, atau Linux). Lingkungan eksekusi baru ini kemudian diberi nama **Node.js**.

Berkat Node.js, JavaScript kini memiliki "kekuatan super". JavaScript tidak lagi hanya bahasa *Frontend*, melainkan bisa digunakan untuk membangun *Backend Server*, membaca/menulis *file*, berinteraksi dengan *database*, dan bersaing dengan bahasa *backend* lain seperti Python, Ruby, atau PHP.

### Ekosistem Alat Bantu: Node Package Manager (NPM) & package.json

Dalam pengembangan *backend*, seorang *developer* hampir tidak pernah menulis seluruh kode dari nol. Mereka sering menggunakan *library* atau kode pustaka buatan orang lain untuk fitur-fitur seperti enkripsi keamanan, koneksi ke *database*, atau pemrosesan gambar. Gudang sentral terbesar di dunia yang menyimpan jutaan *library* JavaScript siap pakai disebut **NPM (Node Package Manager)**.

Saat kamu memulai sebuah proyek *Node.js* baru, langkah pertama yang selalu dilakukan adalah menjalankan perintah berikut di terminal:
`npm init -y`

Perintah ini akan secara otomatis membuat sebuah *file* bernama `package.json` di dalam folder proyekmu. *File* ini berfungsi seperti "KTP" proyekmu. Ia akan mencatat semua informasi tentang proyekmu beserta daftar seluruh *library* (*dependencies*) apa saja yang proyekmu gunakan, sehingga orang lain atau *server* bisa dengan mudah menginstal ulang kebutuhan proyek tersebut di masa depan.

### Skema Arsitektur Modularisasi Proyek: Pembagian Modul Skrip JavaScript

Untuk aplikasi *backend* skala menengah dan besar, menulis seluruh logika *server* dalam satu *file* JavaScript (*script*) adalah mimpi buruk. *Developer* memecah-mecah kodenya menjadi beberapa *file* kecil yang disebut **Modules**.

Di ekosistem *Node.js*, ada dua format penulisan tata kelola *module* (*import/export*):

1. **CommonJS (CJS)** — Format bawaan (klasik) dari *Node.js*. Format ini masih menjadi *default* dan sangat banyak digunakan. Ciri khasnya adalah penggunaan fungsi `require()`.
```javascript
// Mengimpor module dari luar
const fs = require('fs');

// Mengekspor module agar bisa digunakan oleh file lain
module.exports = fungsiKu;
```

2. **ES Modules (ESM)** — Standar modern dari spesifikasi standar bahasa JavaScript (*EcmaScript*). Format ini menggunakan `import` dan `export` (mirip seperti yang biasa kamu lihat di *framework frontend* seperti React).
```javascript
// Mengimpor module dari luar
import fs from 'fs';

// Mengekspor module agar bisa digunakan oleh file lain
export const fungsiKu = () => {};
```

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari kita jalankan kode *Node.js* pertamamu tanpa *browser*! (Pastikan Node.js sudah terinstal di komputermu dengan mengeceknya lewat perintah `node -v` di terminal).

1. Buka Terminal, buat *folder* baru untuk percobaan (contoh: `mkdir lab-node`), lalu masuk ke *folder* tersebut (`cd lab-node`).
2. Jalankan perintah inisialisasi proyek NPM dengan mengetik: `npm init -y`. Periksa *folder* kamu, *file* `package.json` akan otomatis terbuat.
3. Buat sebuah *file* baru bernama `server.js`, dan tuliskan kode JavaScript berikut ini:
```javascript
// Mengimpor library bawaan (built-in) Node.js untuk mengakses info Sistem Operasi
const os = require('os');

console.log("===============");
console.log("EKSEKUSI SCRIPT NODE.JS PERTAMA");
console.log("Sistem Operasi : " + os.type());
console.log("Total RAM Komputer : " + (os.totalmem() / 1024 / 1024 / 1024).toFixed(2) + " GB");
console.log("===============");
```
4. Kembali ke Terminal, dan eksekusi *file* tersebut menggunakan Node.js dengan perintah:
```bash
node server.js
```
5. Lihat *output*-nya di terminal! Lewat Node.js, JavaScript kini berhasil membaca spesifikasi *hardware* RAM dan detail sistem operasi komputermu langsung dari level sistem operasi, tanpa membutuhkan perantara aplikasi *browser* sama sekali!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apakah Node.js adalah sebuah bahasa pemrograman baru?</summary>

**Jawaban:** Tidak. *Node.js* bukanlah bahasa pemrograman, melainkan sebuah Lingkungan Eksekusi (*Runtime Environment*). Node.js memungkinkan bahasa pemrograman JavaScript (yang dulunya hanya bisa dijalankan di dalam *browser*) untuk berjalan secara independen langsung di sistem operasi.
</details>

<details>
<summary>❓ *File* penting apa yang otomatis terbuat setelah kita menjalankan perintah `npm init -y` pada terminal di dalam folder proyek kita?</summary>

**Jawaban:** File `package.json`. File ini berisi informasi dasar tentang proyek sekaligus menyimpan daftar pustaka (*library/dependencies*) pihak ketiga apa saja yang diinstal oleh proyek tersebut.
</details>

<details>
<summary>❓ Pada penulisan modul bergaya *CommonJS* (format standar bawaan Node.js), fungsi apa yang digunakan untuk mengimpor atau memanggil sebuah *module* dari file lain?</summary>

**Jawaban:** Fungsi `require()`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami apa itu Node.js dan bagaimana perannya membuat JavaScript keluar dari batasan *browser*.
- [ ] Saya paham apa fungsi dari NPM (*Node Package Manager*).
- [ ] Saya mengerti peran dan fungsi dari file manifes `package.json`.
- [ ] Saya sukses menjalankan *script* Node.js untuk mengekstrak informasi RAM komputer di sesi uji coba *Mini Lab*.
- [ ] Saya sudah menjawab semua pertanyaan di bagian *Quiz Kilat*.

---

## 🔗 Resources

- [Node.js Official Documentation](https://nodejs.org/en/docs) — Dokumentasi resmi API bawaan Node.js (misalnya modul `fs` untuk *file system*, `os` untuk informasi sistem, `path` untuk modifikasi path, dan lain-lain).

---

## ➡️ Besok

**Day 3: Express.js: Routing & Middleware** — Membuat *web server* menggunakan modul bawaan (*native*) dari Node.js itu sulit dan memakan banyak waktu. Oleh karena itu, besok kita akan belajar menggunakan *framework backend* paling legendaris di ekosistem Node.js, yaitu **Express.js**. *Framework* ini akan sangat mempermudah kita dalam mengatur sistem *routing* (jalur URL) API dengan rapi dan efisien!

---

*📅 TISS Null Teaming · Week 12 · Day 2 · FORGE Rank*
