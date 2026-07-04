# 🔨 Week 13 · Day 4: Authentication & Password Security

> **Rank**: FORGE | **Minggu ke-13**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 13 · Day 4/5 | FORGE Rank (Minggu 4 dari 5) | Overall: 64/120 hari (53%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** mekanisme otentikasi konvensional (*Session-based*) dengan token (*JWT*).
2. **Menerapkan** kriptografi (*Hashing*) satu arah untuk merahasiakan kata sandi menggunakan `bcrypt`.
3. **Menggambarkan** alur arsitektur keamanan sistem validasi login.

---

## 📖 Materi Inti

### Otentikasi: Manajemen Sesi pada Server

Protokol *HTTP* pada dasarnya bersifat *Stateless* (tidak merekam jejak riwayat/memori). Protokol ini tidak didesain untuk mengenali klien yang sukses melakukan login pada permintaan sebelumnya. Agar peladen (*Server*) bisa mengingat bahwa pengguna tersebut sudah terotorisasi saat berpindah halaman, server perlu memberikan "tanda pengenal" atau tiket otorisasi.

Di dunia pengembangan backend, terdapat 2 pendekatan utama untuk otentikasi:

**1. Session-Based Authentication**
Server mengelola daftar sesi (*Session Store*) di memori lokalnya, lalu memberikan ID (*Session ID*) yang disimpan di dalam *Cookie* peramban pengguna. Setiap klien mengirimkan permintaan baru, *Cookie* tersebut akan disertakan untuk dicocokkan dengan catatan *Server*.

**2. Token-Based Authentication (JWT)**
Server menggunakan arsitektur tanpa riwayat status (*Stateless*). Setelah login berhasil, Server membuat sertifikat token digital yang ditandatangani secara kriptografi (*JSON Web Token / JWT*). Token ini berisi pengenal spesifik (seperti ID pengguna) dan disimpan di peramban *Frontend*. Server tidak perlu menyimpan status sesi, ia cukup memvalidasi tanda tangan kriptografi dari token yang dikirimkan klien.

### Mencegah Kebocoran Kredensial: Hashing Kata Sandi (Bcrypt)

Sebagai pengembang *Backend*, **DILARANG KERAS** menyimpan kata sandi pengguna dalam format teks telanjang (*Plaintext*) di dalam *Database*. Jika basis data bocor, seluruh kredensial pengguna akan terekspos secara langsung!

Kita wajib menyamarkan kata sandi melalui fungsi Kriptografi (*Hashing*). Berbeda dengan *Enkripsi* (yang bisa didekripsi kembali ke bentuk asli asalkan memiliki kuncinya), *Hashing* dirancang berjalan **satu arah**. Sandi hasil *hashing* tidak bisa dikembalikan (di-*reverse*) menjadi teks aslinya.

Modul penyandian yang sangat disarankan pada *Node.js* saat ini adalah paket `bcrypt`.

**Lantas, Bagaimana Server Tahu Sandinya Cocok Kalo Gak Bisa Didekripsi?**
Sederhana! Saat pengguna mengetik sandi "R4hasi4" di halaman *Login*, server mengambil teks tersebut dan melakukan kalkulasi *hash* saat itu juga. Hasil *hash* ini kemudian dikomparasi: *"Apakah hash dari input baru ini sama persis dengan hash yang tersimpan di Database?"*. Jika cocok, akses masuk diberikan!

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari mempraktikkan proses perlindungan algoritma pengamanan sandi sistem *hashing* menggunakan `bcrypt`!

1. Buka Terminal, buat folder baru `mkdir lab-bcrypt`, lalu masuk ke folder tersebut `cd lab-bcrypt`.
2. Inisialisasi proyek Node.js dengan perintah `npm init -y`.
3. Instal pustaka `bcrypt`: 
```bash
npm install bcrypt
```
4. Buat file baru bernama `cincang.js`, lalu masukkan kode berikut:

```javascript
const bcrypt = require('bcrypt');

const sandiUser = "TissAcademy2026!"; // Kata Sandi Asli (Plaintext)
const kadarGaram = 10; // Salt rounds (Tingkat kompleksitas pengacakan algoritma)

// ===========================================
// 1. FASE REGISTRASI (Mencincang sandi sebelum disimpan ke Database)
// ===========================================
bcrypt.hash(sandiUser, kadarGaram, (error, hasilCincanganSandiUtama) => {
  console.log("Parameter Sandi Tulen Pendaftar:", sandiUser);
  console.log("Parameter Hasil Hash Cincang (Yg direkam ke DB):", hasilCincanganSandiUtama);
  
  // ===========================================
  // 2. FASE LOGIN (Pengecekan kecocokan sandi)
  // Ceritanya User mencoba Login kembali
  // ===========================================
  const ketikanSandiTamu = "TissAcademy2026!"; // Kamu bisa mengubah teks ini untuk mengetes fungsi penolakan!
  
  // Server memanggil perintah komparasi
  bcrypt.compare(ketikanSandiTamu, hasilCincanganSandiUtama, (err, validitasCocok) => {
    if(validitasCocok) {
      console.log("✅ STATUS VERIFIKASI : AKSES IDENTITAS SANDI COCOK!");
    } else {
      console.log("❌ STATUS VERIFIKASI : SANDI SALAH, AKSES DITOLAK!");
    }
  });
});
```

5. Jalankan skrip di terminal: `node cincang.js`.
6. Perhatikan terminalmu. Terdapat barisan teks acak yang panjang (*Hash*) tercetak di terminal. Mustahil bagi siapa pun untuk merancang formula khusus untuk mendekripsi deretan teks tersebut agar kembali menjadi "TissAcademy2026!".

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa pada otentikasi *JWT (Stateless)*, server tidak perlu menyimpan status login pengguna di dalam database *Session*?</summary>

**Jawaban:** Karena *JWT* bersifat *Stateless*. Token JWT yang disimpan di sisi klien (*browser*) sudah memuat klaim otorisasi yang sah beserta tanda tangan kriptografi dari server. Saat klien mengirim token tersebut, server cukup memverifikasi tanda tangannya tanpa perlu mencocokkan atau mencatat apapun ke memori/database internalnya. Hal ini meringankan beban operasional server.
</details>

<details>
<summary>❓ Apa perbedaan paling mendasar antara perlindungan sandi menggunakan metode *Hashing* dibandingkan *Enkripsi*?</summary>

**Jawaban:** *Enkripsi* bersifat dua arah (*reversible*); data yang dienkripsi bisa dibongkar (didekripsi) kembali menjadi teks aslinya jika kita memiliki kunci rahasianya. Sedangkan *Hashing* bersifat mutlak satu arah (*irreversible*); hasil pemrosesan algoritma *hash* tidak bisa dibongkar kembali menjadi teks aslinya menggunakan kunci apapun.
</details>

<details>
<summary>❓ Dalam modul `bcrypt`, parameter `Salt` (Garam) ditambahkan untuk menangkal serangan peretasan jenis apa?</summary>

**Jawaban:** `Salt` ditambahkan secara acak ke dalam kata sandi sebelum proses *hashing* untuk menggagalkan serangan seperti *Rainbow Tables* atau pola tebakan kamus yang sudah dipersiapkan sebelumnya (pre-computed hash). Dengan `Salt`, dua pengguna yang memiliki kata sandi yang sama persis (misal: "12345") akan menghasilkan cetakan *hash* yang sepenuhnya berbeda di database.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan antara *Session-based Authentication* dan *JWT Stateless Authentication*.
- [ ] Saya mematuhi standar keamanan absolut untuk TIDAK menyimpan kata sandi dalam bentuk teks murni (*Plaintext*) di database.
- [ ] Saya berhasil mendemonstrasikan keahlian mempraktikkan proses *hashing* dan pencocokan sandi (*compare*) menggunakan pustaka `bcrypt`.
- [ ] Saya telah menuntaskan praktik *Mini Lab*.
- [ ] Saya telah mereview pertanyaan pada sesi *Quiz Kilat*.

---

## 🔗 Resources

- [JWT.io Debugger](https://jwt.io/) — Tool esensial bagi pengembang web untuk membaca, memeriksa, dan membedah komponen di dalam struktur *JSON Web Token* (Header, Payload, Signature).

---

## ➡️ Besok

**Day 5: Lab & Mission: Sistem Login/Register** — Fondasi teoritis tentang arsitektur otentikasi web sudah kamu kuasai. Di sesi *Lab* besok, kamu akan membangun secara utuh sistem aplikasi peladen *Node.js* yang komprehensif! Kamu akan menyatukan kerangka arsitektur *Express.js*, mengintegrasikannya dengan database *SQLite*, dan menerapkan perlindungan *hashing* menggunakan *Bcrypt* untuk menciptakan fitur Registrasi Akun dan Login yang fungsional dan aman.

---

*📅 TISS Null Teaming · Week 13 · Day 4 · FORGE Rank*
