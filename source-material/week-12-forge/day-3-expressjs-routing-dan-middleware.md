# 🔨 Week 12 · Day 3: Express.js, Routing & Middleware

> **Rank**: FORGE | **Minggu ke-12**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 12 · Day 3/5 | FORGE Rank (Minggu 3 dari 5) | Overall: 58/120 hari (48%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membuat** *Web Server* HTTP secara cepat menggunakan *Framework* Express.js.
2. **Merancang** rute (*Routing*) untuk menangani *Request* dari pengguna.
3. **Memahami** konsep lapisan penengah (*Middleware*).

---

## 📖 Materi Inti

### Express.js: Kerangka Perajut Server 

Membangun *web server* menggunakan kode bawaan Node.js (Native HTTP) membutuhkan penulisan kode yang panjang dan kompleks.

Solusinya adalah menggunakan **Express.js**, sebuah *Framework* yang sangat populer di Node.js. Dengan Express, kamu bisa membuat *server* yang siap menerima *Request* hanya dengan beberapa baris kode!

### Anatomi Rute Lalu Lintas (Routing)

Ketika *browser* mengakses URL seperti `/login` atau `/profil`, *server* harus tahu apa yang harus dibalas untuk setiap URL tersebut. Proses mengarahkan URL ke balasan yang tepat inilah yang disebut **Routing**.

Sintaks dasarnya adalah:
`app.METHOD('URL_PATH', (req, res) => { ... })`

Contoh di kode Node.js:
```javascript
const express = require('express');
const app = express(); // Membuat aplikasi Express

// Menangani HTTP GET request ke halaman utama ('/')
app.get('/', (req, res) => {
 res.send('Selamat datang di Halaman Utama.'); 
});

// Menangani request ke URL '/profil'
app.get('/profil', (req, res) => {
 res.send('Ini adalah halaman Profil pengguna.');
});

// Menjalankan server di port 3000
app.listen(3000, () => console.log('Server berjalan di port 3000'));
```

### Pos Pemeriksaan Gerbang Utama: Middleware

Bagaimana jika aplikasimu punya banyak rute, dan kamu butuh satu fungsi pengecekan (misal: cek apakah *user* sudah *login*) sebelum mereka bisa mengakses rute mana pun?

Dalam Express, fungsi pencegat ini disebut **Middleware**.
Middleware adalah fungsi yang berjalan di tengah-tengah antara saat *Request* datang dan saat *Response* dikirim. Middleware bisa mengecek sesuatu, lalu memutuskan: apakah proses boleh dilanjutkan (dengan memanggil `next()`) atau dihentikan.

```javascript
// Middleware Cek Keamanan
const satpam = (req, res, next) => {
 console.log("Ada pengunjung mencurigakan masuk...");
 
 // Jika aman, persilakan terus jalan ke tujuan akhirnya
 next(); 
};

// Pasang Satpam (Middleware) ini ke SEMUA rute!
app.use(satpam);
```

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari kita *install* Express dan buat *server* pertamamu!

1. Buka Terminal, buat folder baru bernama `lab-express` dan masuk ke dalamnya (`cd lab-express`).
2. Inisialisasi *project* NPM: `npm init -y`
3. *Install framework* Express:
```bash
npm install express
```
4. Buat file `app.js` lalu salin kode contoh dari bagian **Routing** dan **Middleware** di atas ke dalam *file* tersebut.
5. Jalankan *server*:
```bash
node app.js
```
6. Buka *browser* (Chrome/Firefox), dan akses URL berikut: `http://localhost:3000`
7. Coba juga akses URL: `http://localhost:3000/profil`
8. Cek Terminalmu; kamu akan melihat pesan `log` dari Middleware setiap kali ada *request* masuk!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa *developer* Node.js sangat merekomendasikan penggunaan *Framework* Express.js dibandingkan kode HTTP Native bawaan Node.js?</summary>

**Jawaban:** Karena Express.js menyederhanakan proses pembuatan *server* dan *Routing*. Kode yang sebelumnya rumit dan panjang di HTTP Native bisa ditulis secara ringkas dan rapi menggunakan Express.js.
</details>

<details>
<summary>❓ Apa nama fungsi dalam Express.js yang bertugas mencegat (*intercept*) sebuah *Request* di tengah jalan (misalnya untuk mengecek status *login*) sebelum request tersebut tiba di rute tujuan?</summary>

**Jawaban:** **Middleware**.
</details>

<details>
<summary>❓ Fungsi apa yang harus dipanggil di dalam sebuah Middleware agar *Request* diizinkan melanjutkan perjalanannya ke rute atau Middleware selanjutnya?</summary>

**Jawaban:** Fungsi `next()`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami kegunaan *Framework* Express.js.
- [ ] Saya bisa membuat *Routing* dasar menggunakan metode seperti `app.get()`.
- [ ] Saya mengerti konsep dan fungsi dari *Middleware*.
- [ ] Saya berhasil menjalankan *server* di `localhost:3000` pada sesi *Mini Lab*.
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Express.js Basic Routing](https://expressjs.com/en/starter/basic-routing.html) — Dokumentasi resmi Express.js tentang dasar-dasar perutean (*Routing*).

---

## ➡️ Besok

**Day 4: REST API Design** — Kamu sudah belajar membuat rute dasar. Besok, kita akan mempelajari cara menstrukturkan rute (URL) yang baik dengan mengikuti standar internasional **REST API**, termasuk cara menyusun operasi CRUD (Create, Read, Update, Delete) yang rapi!

---

*📅 TISS Null Teaming · Week 12 · Day 3 · FORGE Rank*
