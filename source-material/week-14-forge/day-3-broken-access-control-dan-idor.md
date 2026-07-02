# 🔨 Week 14 · Day 3: Broken Access Control & IDOR

> **Rank**: FORGE | **Minggu ke-14**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 14 · Day 3/5 | FORGE Rank (Minggu 5 dari 5) | Overall: 68/120 hari (57%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara ranah Otentikasi (*Authentication*) dan Otorisasi (*Authorization*).
2. **Mengenali** anatomi kerentanan IDOR (*Insecure Direct Object Reference*) atau *BOLA*.
3. **Membentengi** kueri peladen *Backend* dengan lapis penyaring verifikasi wewenang absolut.

---

## 📖 Materi Inti

### Juara 1 OWASP: Broken Access Control

Bila tahun-tahun sebelumnya celah Injeksi selalu merajai panggung pemeringkatan, kini posisi puncak kemurkaan *OWASP Top 10* diduduki oleh **Broken Access Control (BAC)** (Kerusakan Kontrol Akses).

Seorang pengguna mungkin sudah sukses *Login* (Otentikasi). Tapi apakah dia *Berhak* mengakses rute atau fungsionalitas level administrasi? (Otorisasi).
BAC bermanifestasi ketika sistem gagal membentengi batasan Wewenang. Akibatnya, pengguna level standar bisa mengeksploitasi rute untuk melompat menjadi Admin, atau pengguna A sukses mengutak-atik sandi milik pengguna B.

### Monster Menakutkan: IDOR (BOLA)

Varian paling populer dari eksploitasi BAC adalah celah sederhana nan mematikan bertitel **IDOR (Insecure Direct Object Reference)**. Di kalangan peretas *API* modern, kerentanan ini lazim dijuluki **BOLA - Broken Object Level Authorization**.

Kerentanan ini teramat fatal sekaligus mengkhawatirkan karena **tidak mensyaratkan pemahaman bahasa pemrograman yang rumit**. 
Bayangkan kamu terdaftar sebagai pengguna di situs perbankan dengan profil ID `5`. Kamu melihat rute API di antarmuka peramban yang berbunyi:
`GET https://banktiss.com/api/transaksi/5`

Jika programmer di *Backend* bertindak ceroboh dan hanya mengecek: "Oh, pengguna tersebut sudah *Login*, bebaskan saja transmisi datanya", maka seorang peretas murni cukup iseng mengganti angka referensi `5` menjadi `6` di URL-nya:
`GET https://banktiss.com/api/transaksi/6`

Dan *BOOM!* Peretas sukses mengunduh rincian mutasi sensitif milik ID 6. Skrip server memuntahkan data secara vulgar tanpa pernah menginisiasi validasi silang, *"Tunggu, bukankah klien yang meminta akses ini mendaftar dengan identitas ID 5? Mengapa dia menargetkan penarikan data transaksi milik nomor 6?"*

### Tameng Pelindung (Authorization Checks)

Solusi penangkalan celah *IDOR* tidak bisa diatasi dengan peranti modul instalasi NPM otomatis semata. Kerentanan ini butuh perancangan logika bisnis kontrol akses manual dari arsitek API.

Di setiap rute peladen yang melayani permintaan aset sensitif, **jangan pernah hanya mendelegasikan kepercayaan pada angka argumen dari kueri URL!** 
Lakukan *Double Check* (Pengecekan Silang Ganda) antara:
1. Angka parameter ID referensi objek yang tercantum di URL (Misal: `req.params.id`).
2. Angka profil ID identitas sakti yang tertanam otentik di sertifikat memori JWT/Session klien yang bersangkutan (`req.user.id`).

```javascript
// Contoh Backend Aman dengan Filter Otorisasi Ganda
app.get('/api/transaksi/:id', (req, res) => {
 const idYangDiminta = req.params.id;
 const idKlienYangLogin = req.user.id; // Didapatkan hasil dekripsi verifikasi payload sesi (JWT)

 // Evaluasi Logik: Kalo bukan Admin, dan klien nekat menarik parameter ID milik orang lain:
 if(idYangDiminta!== idKlienYangLogin && req.user.role!== 'admin') {
 return res.status(403).json({pesan: "Akses Dilarang! (HTTP Error 403) Eksploitasi Otorisasi (IDOR) dicegah!"});
 }

 // Jika otorisasi selaras dan sukses divalidasi, serahkan data transaksinya!
});
```

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari mensimulasikan mekanisme eksploitasi peretasan otorisasi *IDOR*!

1. Biasanya praktikum ini dieksekusi di pelataran simulasi CTF (`https://tryhackme.com/`). Namun demi kepraktisan asimilasi logika, perhatikan simulasi parameter berikut:
2. Bayangkan dirimu mendarat di aplikasi portal kampus, mengklik menu "Unduh Raport Saya", lalu peramban mengunduh dokumen dari rute URL eksekutor:
 `https://kampus.ac.id/download/raport?mahasiswa_id=901`
3. Apa tindakan pertama yang niscaya dieksekusi oleh naluri penganalisis *Bug Bounty*?
 **MENGGANTI ANGKA REFERENSI 901 MENJADI 902!**
 (Tekan Enter dan luncurkan pemanggilan kuerinya).
4. Jika web kampus itu tiba-tiba merespons dan berhasil menyuguhkan unduhan dokumen Raport milik mahasiswa lain, *Selamat, kamu baru saja mendemonstrasikan eksploitasi 0-day kerentanan IDOR murni yang setara dengan validasi temuan bernilai hadiah di kompetisi Bug Bounty global!*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah jurang klasifikasi parameter akses aplikasi, apa esensi perbedaan terma <i>Authentication</i> (Otentikasi) disandingkan secara logis dengan <i>Authorization</i> (Otorisasi)?</summary>

**Jawaban:** *Otentikasi* sekadar menanyakan kepastian validitas identitas (*"Siapakah dirimu sesungguhnya? Buktikan kebenaran identitas profil Login-mu!"*). Sebaliknya, *Otorisasi* mendedahkan jaring kontrol penetapan wewenang akses hierarki izin (*"Baik, kau sudah terdaftar dan masuk, namun apakah derajat pangkat profilmu berhak merambah serta mengeksekusi operasi data krusial di fasilitas ruangan konfigurasi ini?"*).
</details>

<details>
<summary>❓ Akronim rincian kepanjangan klasifikasi ancaman siber kerentanan akses <i>IDOR</i> yang menggerogoti peramban objek API secara masif memuat kepanjangan terminologi apa?</summary>

**Jawaban:** Insecure Direct Object Reference.
</details>

<details>
<summary>❓ Ketika mengarsiteki tameng penangkal perlindungan <i>IDOR</i> di rute peladen *Backend API*, sepasang referensi parameter identitas ganda manakah yang mesti ditubrukkan dan diadu penyelarasan kontrol aksesnya agar rute beroperasi aman dalam memblokir eksploitasi peretas?</summary>

**Jawaban:** Kueri otorisasi peladen mesti mengadu dan membandingkan secara komparatif parameter nilai argumen spesifik referensi objek ID yang disuapkan klien di jalur alamat target permintaan (*seperti `req.params.id`*) disilang dengan ekstraksi parameter nilai validasi identitas sakti utuh profil ID klien (*macam `req.user.id` yang diusung oleh dekripsi token sesi JWT asli*). Jika parameter keduanya tidak ekuivalen klop tanpa dijustifikasi izin tingkat Admin, pemblokiran akses niscaya diletuskan.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya tangkas menelaah diskriminasi terminologi operasional *Authentication* vs *Authorization*
- [ ] Saya menyerap betapa masifnya celah manipulasi penggantian ekstrak angka identitas eksploitasi kerentanan *IDOR/BOLA*
- [ ] Saya memahami pengaplikasian logika validasi kontrol silang ganda arsitektur penangkalan `req.user.id === req.params.id`
- [ ] Saya meresapi pengadopsian insting simulasi eksploitasi *Bug Bounty* saat melakukan modifikasi injeksi payload nilai ID referensi
- [ ] Saya telah menelaah segenap pelaporan ulasan pembedahan evaluasi (*Quiz Kilat*)

---

## 🔗 Resources

- [PortSwigger: IDOR / Access Control](https://portswigger.net/web-security/access-control) — Laboratorium eksplorasi mumpuni untuk mensimulasikan dan membongkar kelemahan arsitektur akses pada level *Access Control*.

---

## ➡️ Besok

**Day 4: Security Misconfig & Data Exposure** — Dirimu sudah piawai menangkis Injeksi, mensterilkan XSS, dan mendobrak kelemahan IDOR. Esok hari, kita menelaah dosa aplikasi yang dilahirkan lantaran kelalaian administrasi setelan konfigurasi peladen. Pembocoran payload Rahasia Token disebar di Github, API yang dieksploitasi dihajar jutaan siklus serangan *bot* (Rate Limit), serta pembungkaman identitas peladen via cap *Helmet.js*. Kita lantas akan bersiap memasang serdadu perisai integrasi terakhir!

---

*📅 TISS Null Teaming · Week 14 · Day 3 · FORGE Rank*
