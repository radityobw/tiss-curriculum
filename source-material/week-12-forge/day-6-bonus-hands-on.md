# 🎯 Week 12 · Day 6 (Bonus): Hands-On Learning

> **Rank**: FORGE | **Minggu ke-12** | Bonus Day

---

## 🌐 Platform Hari Ini

**[freeCodeCamp — Back End Development and APIs](https://www.freecodecamp.org/learn/back-end-development-and-apis/)**
Kursus sertifikasi backend gratis dari freeCodeCamp yang mencakup Node.js, Express, MongoDB, dan pembuatan API — selaras dengan materi Week 12.

💰 **Biaya**: Gratis (kursus + sertifikasi gratis)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menyelesaikan tantangan Node.js dan Express di lingkungan freeCodeCamp
2. Memahami pola *middleware* dan *routing* melalui latihan interaktif
3. Membandingkan pendekatan freeCodeCamp dengan materi The Odin Project

---

## 📋 Requirement

* Akun freeCodeCamp (gratis)
* Peramban web modern (Chrome/Firefox)
* Node.js terinstal di komputer lokal (sudah diajarkan di Day 2 minggu ini)

> ⚠️ **Jika belum punya akun freeCodeCamp**: Buka [freecodecamp.org](https://www.freecodecamp.org), klik **Sign In**, daftar dengan email atau akun GitHub. Gratis.

> ⚠️ **Jika Node.js belum terinstal**: Ikuti langkah di Day 2 minggu ini, atau unduh dari [nodejs.org](https://nodejs.org) — pilih versi LTS.

---

## 📝 Prosedur

### Langkah 1: Akses Kursus
1. Login ke [freecodecamp.org](https://www.freecodecamp.org)
2. ke **Back End Development and APIs** certification
3. Buka bagian pertama: **Managing Packages with NPM**

### Langkah 2: Kerjakan Modul NPM
1. Ikuti instruksi untuk setiap tantangan di bagian *Managing Packages with NPM*
2. Tantangan ini mengajarkan:
 - Cara kerja `package.json`
 - Menambahkan dependencies
 - Semantic versioning
3. Selesaikan minimal **5 tantangan pertama**

> 💡 **freeCodeCamp menggunakan Gitpod/Replit**: Beberapa tantangan memerlukan environment online. Ikuti instruksi yang diberikan — semuanya gratis.

### Langkah 3: Kerjakan Modul Basic Node and Express
1. Lanjutkan ke bagian **Basic Node and Express**
2. Tantangan ini mengajarkan:
 - Membuat server Express sederhana
 - Routing (GET, POST)
 - Middleware
 - Serving static files
3. Selesaikan minimal **5 tantangan pertama**

### Langkah 4: Praktik Lokal (Opsional)
1. Buat proyek Express sederhana di komputer lokal:
 ```bash
 mkdir fcc-express-practice
 cd fcc-express-practice
 npm init -y
 npm install express
 ```
2. Buat file `server.js`:
 ```javascript
 const express = require('express');
 const app = express();

 app.get('/', (req, res) => {
 res.json({ message: 'Hello dari freeCodeCamp practice!' });
 });

 app.get('/api/timestamp', (req, res) => {
 res.json({ unix: Date.now(), utc: new Date().toUTCString() });
 });

 app.listen(3000, () => console.log('Server di port 3000'));
 ```
3. Jalankan: `node server.js`
4. Buka browser: `http://localhost:3000/api/timestamp`

---

## 🏁 Target Output

* ✅ Minimal **5 tantangan NPM** selesai di freeCodeCamp
* ✅ Minimal **5 tantangan Basic Node and Express** selesai di freeCodeCamp
* 📸 Tangkapan layar dashboard freeCodeCamp menunjukkan progress
* 📸 (Opsional) Tangkapan layar browser menampilkan JSON response dari server lokal

---

## 🔄 Fallback

Jika freeCodeCamp tidak bisa diakses:
1. Buka [The Odin Project — NodeJS Module](https://www.theodinproject.com/paths/full-stack-javascript/courses/nodejs)
2. Baca artikel pengenalan Node.js dan Express
3. Kerjakan praktik lokal di Langkah 4 di atas — ini bisa berdiri sendiri tanpa freeCodeCamp
