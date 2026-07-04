# 🔨 Week 14 · Day 3: Broken Access Control & IDOR

> **Rank**: FORGE | **Minggu ke-14**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 14 · Day 3/5 | FORGE Rank (Minggu 5 dari 5) | Overall: 68/120 hari (57%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara *Authentication* (Otentikasi) dan *Authorization* (Otorisasi).
2. **Mengenali** kerentanan IDOR (*Insecure Direct Object Reference*) atau *BOLA*.
3. **Membentengi** *backend* dengan kontrol akses dan otorisasi yang benar.

---

## 📖 Materi Inti

### Juara 1 OWASP: Broken Access Control

Saat ini, posisi puncak dalam *OWASP Top 10* diduduki oleh **Broken Access Control (BAC)** (Kegagalan Kontrol Akses).

Seorang pengguna mungkin sudah berhasil *Login* (Otentikasi). Tapi apakah dia *berhak* mengakses halaman admin? (Otorisasi).
BAC terjadi ketika sistem gagal memvalidasi wewenang atau hak akses pengguna. Akibatnya, pengguna biasa bisa mengakses fitur admin, atau pengguna A bisa melihat dan mengubah data milik pengguna B.

### Kerentanan Paling Umum: IDOR (BOLA)

Varian paling populer dari eksploitasi BAC adalah **IDOR (Insecure Direct Object Reference)**. Di pengembangan API modern, kerentanan ini sering disebut **BOLA (Broken Object Level Authorization)**.

Kerentanan ini sangat berbahaya karena **mudah dieksploitasi tanpa alat khusus**. 
Bayangkan kamu sedang melihat profil pengguna dengan ID `5` di sebuah situs:
`GET https://banktiss.com/api/transaksi/5`

Jika programmer di *backend* hanya mengecek apakah pengguna sudah *login* tanpa mengecek apakah pengguna tersebut *memiliki hak* atas data tersebut, seorang penyerang bisa dengan mudah mengganti angka `5` menjadi `6` di URL:
`GET https://banktiss.com/api/transaksi/6`

Dan *BOOM!* Penyerang berhasil melihat data transaksi milik pengguna ID 6. Server memberikan data tanpa bertanya: *"Apakah pengguna yang sedang login (ID 5) berhak melihat data pengguna ID 6?"*

### Mekanisme Pencegahan: Authorization Checks

Celah *IDOR* tidak bisa dicegah hanya dengan menginstal *library* keamanan. Ini membutuhkan perancangan **logika bisnis** yang benar.

Jangan pernah mempercayai parameter ID yang dikirim oleh klien (misalnya dari URL)! 
Selalu lakukan *Double Check* (Pengecekan Silang) antara:
1. ID objek yang diminta (Misal: dari `req.params.id`).
2. ID pengguna yang sedang login (Misal: dari *payload* JWT, `req.user.id`).

```javascript
// Contoh Backend Aman dengan Filter Otorisasi Ganda
app.get('/api/transaksi/:id', (req, res) => {
  const idYangDiminta = req.params.id;
  const idKlienYangLogin = req.user.id; // Didapatkan dari token JWT (misalnya)

  // Cek apakah pengguna yang meminta akses adalah pemilik data tersebut
  // (atau memiliki peran sebagai admin)
  if (idYangDiminta !== idKlienYangLogin && req.user.role !== 'admin') {
    return res.status(403).json({
      pesan: "Akses Dilarang! (HTTP 403 Forbidden). Anda tidak berhak mengakses data ini."
    });
  }

  // Jika otorisasi berhasil, kirim data transaksinya
  // ...
});
```

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari mensimulasikan mekanisme *IDOR* sederhana!

1. Bayangkan kamu sedang menggunakan portal kampus, mengklik menu "Unduh Raport", dan browser mengunduh dokumen dari URL:
   `https://kampus.ac.id/download/raport?mahasiswa_id=901`
2. Apa hal pertama yang akan dicoba oleh seorang *Bug Hunter*?
   **MENGGANTI ANGKA 901 MENJADI 902!**
   (Ubah parameter di URL dan tekan Enter).
3. Jika web kampus itu ternyata mengunduh raport milik mahasiswa lain, *selamat! Kamu baru saja menemukan kerentanan IDOR murni yang sering kali berhadiah di kompetisi Bug Bounty!*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar antara <i>Authentication</i> dan <i>Authorization</i>?</summary>

**Jawaban:** *Authentication* (Otentikasi) membuktikan **siapa kamu** (misal dengan *login* menggunakan *username* dan *password*). Sedangkan *Authorization* (Otorisasi) menentukan **apa yang boleh kamu lakukan** (misal apakah kamu punya akses sebagai Admin).
</details>

<details>
<summary>❓ Apa kepanjangan dari IDOR?</summary>

**Jawaban:** *Insecure Direct Object Reference*.
</details>

<details>
<summary>❓ Bagaimana cara terbaik mencegah IDOR pada Backend API?</summary>

**Jawaban:** Jangan mempercayai parameter input (seperti ID di URL). Selalu cocokkan dan validasi ID yang diminta dengan ID pengguna yang sedang *login* (misal dari token sesi). Tolak permintaan (berikan status 403) jika pengguna mencoba mengakses data yang bukan miliknya.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan antara *Authentication* dan *Authorization*.
- [ ] Saya mengetahui bahaya IDOR (BOLA) dan bagaimana serangannya dilakukan.
- [ ] Saya memahami logika pencegahan IDOR di *backend* (`req.user.id === req.params.id`).
- [ ] Saya telah menyelesaikan dan memahami jawaban dari *Quiz Kilat*.

---

## 🔗 Resources

- [PortSwigger: Access Control](https://portswigger.net/web-security/access-control) — Laboratorium eksplorasi mumpuni untuk mensimulasikan dan membongkar kelemahan *Access Control*.

---

## ➡️ Besok

**Day 4: Security Misconfig & Data Exposure** — Kita sudah membahas SQLi (Injeksi), XSS, dan IDOR (Otorisasi). Besok, kita akan mempelajari kerentanan yang muncul bukan karena *bug* pada kode, tetapi karena kesalahan konfigurasi server. Mulai dari token rahasia yang tidak sengaja ter-push ke GitHub, tidak adanya batas permintaan (*rate limiting*), hingga kurangnya perlindungan keamanan *header* aplikasi.

---

*📅 TISS Null Teaming · Week 14 · Day 3 · FORGE Rank*
