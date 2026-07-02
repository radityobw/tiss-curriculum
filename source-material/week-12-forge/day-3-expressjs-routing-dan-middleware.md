# 🔨 Week 12 · Day 3: Express.js, Routing & Middleware

> **Rank**: FORGE | **Minggu ke-12**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 12 · Day 3/5 | FORGE Rank (Minggu 3 dari 5) | Overall: 58/120 hari (48%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mendirikan** menara *Web Server* HTTP instan menggunakan *Framework* Express.js.
2. **Merancang** jalan rute penelusuran (Routing) untuk menampung *Request*.
3. **Memahami** konsep lapisan gerbang pencegat (Middleware).

---

## 📖 Materi Inti

### Express.js: Kerangka Perajut Server 

Membangun web server menggunakan perintah dasar Node.js (Native HTTP) ibarat membangun mobil langsung dari balok baja dan karet cair. Sangat melelahkan dan kodenya ruwet panjang.

Solusinya? Para *hacker* Node.js menciptakan **Framework (Kerangka Kerja) bernama Express.js**. Ini adalah pabrik perakitan instan. Cukup dengan segelintir baris kode, menara servermu siap mengudara menyambut *Request* dari seluruh dunia!

### Anatomi Rute Lalu Lintas (Routing)

Ketika (browser) berkunjung mengetik URL `/login`, atau `/profil`, server harus tahu apa yang mesti dijawab untuk spesifik gang rute tersebut. Inilah yang disebut **Routing**.

Sintaks dasarnya sungguh intuitif:
`app.METODE('ALAMAT_RUTE', (permintaan, jawaban) => {... })`

Contoh di kode Node.js:
```javascript
const express = require('express');
const app = express(); // Inisiasi mesin instan

// Mengatasi rute HTTP GET ke halaman beranda '/'
app.get('/', (req, res) => {
 res.send('Selamat datang di fitur Utama.'); 
});

// Mengatasi rute jika pengunjung ke URL '/profil'
app.get('/profil', (req, res) => {
 res.send('Ini adalah data rahasia Agen 007.');
});

// Nyalakan mesin server di pelabuhan (port) 3000
app.listen(3000, () => console.log('Server hidup di port 3000'));
```

### Pos Pemeriksaan Gerbang Utama: Middleware

Bagaimana jika pangkalanmu punya ratusan rute, lalu kamu butuh SATU satpam (logika) yang mengecek apakah pengunjung sudah punya kartu anggota (Login) sebelum boleh melewati rute mana pun?

Di Express, satpam penjaga gerbang transisi ini disebut **Middleware**.
Middleware adalah fungsi yang *mencegat* laju pesanan (Request) di tengah jalan, mengecek sesuatu, lalu memutuskan: "Boleh lanjut" (`next()`) atau ditolak mental.

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

Mari unduh peranti Express dari bursa global dan rakit server pertamamu!

1. Buka Terminal, buat folder baru `lab-express` dan masuk `cd lab-express`.
2. Inisiasi inventaris: `npm init -y`
3. Unduh payload sakti (Framework Express):
```bash
npm install express
```
4. Buat file `app.js` dan salin kode *Routing* dan *Satpam* dari bagian Materi Inti di atas ke dalam filenya. 
5. Nyalakan mesin server! 
```bash
node app.js
```
6. Buka peramban favoritmu (Chrome/Firefox), dan ketik alamat koordinat ini:
`http://localhost:3000`
7. Coba juga kunjung: `http://localhost:3000/profil`
8. Lihat di terminal aslimu, log satpam "Ada pengunjung mencurigakan..." akan dicetak saban kali browser melintasi rute tersebut!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Esensi utama mengapa pengembang Node.js berduyun-duyun berlindung mempercayakan pembangunan aplikasi di bawah perancah <i>Framework</i> macam Express.js?</summary>

**Jawaban:** Karena *Express.js* mendelegasikan penyederhanaan abstraksi kerumitan pembangunan rutinitas dasar pendirian peladen HTTP Native yang amat mengular kodenya, menjadikannya sebatas gubahan singkat ringkas sebaris dua baris demi manajemen rute (*Routing*) nan luwes elegan.
</details>

<details>
<summary>❓ Dalam terminologi alur sirkulasi *Backend Express*, sakral penyela transisi yang ditugaskan mencegat melintang payload lalu-lintas <i>Request</i> demi urusan semisal otentikasi login sebelum mengizinkannya tembus berlabuh pada ujung rutinitasnya adalah?</summary>

**Jawaban:** Middleware.
</details>

<details>
<summary>❓ Apa tuas komando mandat sakti penutup (diwakili embel-embel sebutir fungsi khusus) yang diselipkan dipanggil kelar tugas *Middleware* guna memberi palu restu perizinan jalan tol masuk rute selanjutnya?</summary>

**Jawaban:** Titah `next()`
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya cakap menguraikan andil esensial kedudukan Framework Express.js
- [ ] Saya menguasai fondasi arsitektur perakitan Rute Lalu Lintas (`app.get()`)
- [ ] Saya memahami logika delegasi pengamanan palang gerbang *Middleware*
- [ ] Saya berhasil mendirikan peladen HTTP `localhost:3000` di Mini Lab
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Express.js Basic Routing](https://expressjs.com/en/starter/basic-routing.html) — Lembar pedoman sah membedah lekuk-liku seni *Routing*.

---

## ➡️ Besok

**Day 4: REST API Design** — Kamu sudah bisa mencegat rute (Routing). Esok hari, kamu akan menyempurnakan bentuk struktur peruteanmu (CRUD Operations) mematuhi standardisasi pakem protokol komunikasi dunia: standar *REST API Design*, lengkap bermodalkan status perizinan sandi rahasia (`200 OK`, `404 Not Found`).

---

*📅 TISS Null Teaming · Week 12 · Day 3 · FORGE Rank*
