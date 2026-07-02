# 🔨 Week 14 · Day 4: Security Misconfig & Data Exposure

> **Rank**: FORGE | **Minggu ke-14**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 14 · Day 4/5 | FORGE Rank (Minggu 5 dari 5) | Overall: 69/120 hari (58%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** celah keamanan akibat kelalaian tata letak peladen (*Security Misconfiguration*) & kebocoran rahasia (*Sensitive Data Exposure*).
2. **Mengelola** brankas variabel rahasia peladen bermodalkan fail `.env`.
3. **Menerapkan** benteng NPM *Helmet.js* serta pengaplikasian jaring *Rate Limiting*.

---

## 📖 Materi Inti

### Dosa Kelalaian Konfigurasi

Seringkali, *Backend API* berhasil dibobol peretas murni karena **Salah Penyesuaian Pengaturan (Misconfiguration)**.

Contoh kelalaian operasional massal:
1. Menjalankan *Database Server* (semacam MongoDB/Redis) namun administrator lalai menggemboknya menggunakan perlindungan sandi, sehingga basis data dibiarkan terbuka (default) dan dapat diakses publik secara awam.
2. Saat server menabrak galat operasional (*HTTP Error 500*), peladen memuntahkan pelaporan jejak penumpukan eksekusi kodingan (*Stack Trace*) yang merinci error ke layar klien. Penyerang kegirangan karena letak struktur direktori, referensi modul, dan versi kerangka terekspos secara detail ke ranah publik!

### Tragedi Kecerobohan (Sensitive Data Exposure)

Kerentanan lain: Ketika *developer* lalai merakit aplikasi, dia mengetikkan kata sandi Database atau Rahasia Token JWT secara mentah-mentah (*plaintext*) bersandar langsung di naskah fail proyek `server.js`, lalu di-*Push* ke *GitHub* secara publik. 
Pasukan pemindai Bot otomatis peretas seketika menangkap paparan kredensial tersebut dan berpeluang membobol server korporasi secara instan!

**Tameng Rahasia (.env):**
Segala variabel kunci sandi gaib wajib dipisahkan lantas disekap dalam bungkus berkas rahasia terisolasi bertitel `.env` (*Environment Variables*) yang **HARAM** dinaikkan atau terunggah ke repositori kendali versi (seperti Git)!

```text
# Contoh fail.env (Fail ini wajib diabaikan oleh filter.gitignore)
DATABASE_PASSWORD=rahasia_tiss_2026
JWT_SECRET=super_kunci_sakti_
```
Di ekosistem Node.js, kodingan merujuk variabel tersebut diam-diam lewat instalasi bantuan modul *dotenv*:
`const dbSandi = process.env.DATABASE_PASSWORD;`

### Memasang Rompi Tahan (Helmet.js & Rate Limiter)

1. **Helmet.js (Pelindung Header HTTP)**
Kerangka *Express.js* punya rutinitas murni memamerkan atribut cap identitas versinya (Misal memuntahkan parameter *header*: `X-Powered-By: Express`). Peretas niscaya dapat melacak jejak ini lalu mengeksploitasi celah arsitektur jika menggunakan *Express* usang. Implementasi *Helmet.js* mensterilkan kelakuan pamer ini otomatis!
`app.use(helmet());`

2. **Rate Limiting (Tameng Anti DDoS / Brute-Force)**
Bagaimana jika peretas membangun *Bot* yang memborbardir rute `/api/login` sejuta kali per detik untuk melumpuhkan peladenmu? Cegah dan batasi transmisi tersebut dengan modul pembatas kecepatan!
`app.use(rateLimiter({ windowMs: 15 * 60 * 1000, max: 100 })); // Membatasi peladen murni melayani maksimal 100 serangan per 15 menit.`

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari mempraktikkan pemasangan perisai *.env*!

1. Rakit direktori `mkdir lab-rahasia` dan masuki rutenya: `cd lab-rahasia`.
2. Inisiasi ekosistem NPM: `npm init -y`.
3. Pasok instalasi brankas rahasia: `npm install dotenv`
4. Ciptakan dua fail berdampingan: `.env` dan `.gitignore`.
5. Di fail `.env` ketikkan konfigurasi:
 `API_KEY=ZERO_COOL_HACKER`
6. Di fail `.gitignore` deklarasikan tulisan:
 `.env` (Mencegah mesin *Git* mengunggah fail `.env` ke portal publik).
7. Buat file `induk.js`, ketik sandi ekstraksi pustaka *dotenv*:
```javascript
// Memanggil modul dotenv menyusup melarutkan isi.env ke otak Node OS
require('dotenv').config();

console.log("Kunci Sakti Variabel Rahasia terekstrak: ", process.env.API_KEY);
```
8. Letuskan pemicu komando terminal eksekusi: `node induk.js`. Laskar kuncimu sukses diekstrak di log, dan dijamin tak bakal terdorong ke jangkauan ekspos *GitHub* berkat pagaran `.gitignore`!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Menelaah ancaman keteledoran paparan , apa tujuan utama mengkarantina payload parameter kunci sandi API ke sarang berkas <i>.env</i> alih-alih meletakkannya tersurat di baris skrip `server.js`?</summary>

**Jawaban:** Agar payload krusial kata sandi maupun aset *API Key* terisolasi dan disembunyikan kelak dari ancaman eksposur sewaktu proyek diunggah (*Push*) menuju penyimpanan sistem kontrol repositori luar semacam *GitHub*, berkat perlindungan pagar `.gitignore`.
</details>

<details>
<summary>❓ Pasca *Node.js* mengalami ralat eksekusi bersandi error 500, mengapa dilarang keras bagi peladen memuntahkan lapor rincian <i>Stack Trace</i> merah ke layar antarmuka peramban?</summary>

**Jawaban:** Karena *Stack Trace* pelaporan galat mentah memamerkan detail struktur jejak folder letak komputer peladen, versi modul konfigurasi terinstal, hingga rentetan arsitektur alur kueri *database*, yang sejatinya menyuguhkan pedoman eksploitasi bagi analis intelijen *hacker*.
</details>

<details>
<summary>❓ Perisai tameng modul *Helmet.js* yang diintegrasikan ke bodi gerbang *Express* murni ditugaskan untuk menangkis celah kerentanan ekspos pada komponen apa?</summary>

**Jawaban:** Melindungi dan mensterilkan kebocoran informasi pada lapis komponen atribut *HTTP Headers*, semisal menonaktifkan deklarasi parameter penanda bawaan pamer semacam `X-Powered-By`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap pengetahuan ancaman bahaya fatal dari eksposur *Security Misconfiguration*
- [ ] Saya paham fungsi kerangka variabel konfigurasi `.env` dan kaitannya dengan larangan `.gitignore`
- [ ] Saya mengetahui kegunaan tameng eksekusi perisai HTTP *Helmet.js* dan *Rate Limiting*
- [ ] Saya sukses mengeksekusi integrasi instalasi *dotenv* Kunci Rahasia di fitur *Mini Lab*
- [ ] Saya telah menyimak tuntas seluruh rangkuman ulasan parameter pengujian *Quiz Kilat*

---

## 🔗 Resources

- [Helmet.js Docs](https://helmetjs.github.io/) — Dokumen referensi operasional perlindungan lapis *HTTP Header* di ekosistem *Express Node*.
- [Dotenv NPM](https://www.npmjs.com/package/dotenv) — paket modul *Environment Variables Setup*.

---

## ➡️ Besok

**Day 5: Lab & Mission: Securing the API** — Babak pemuncak kurikulum *Forge Rank* menjelang tiba! Kawah eksperimen pamungkas menunggumu menyusun integrasi segenap parameter benteng sandi yang digabung komprehensif; merajut tameng Injeksi fungsi mutlak `?`, sanitasi, perlindungan otorisasi *IDOR*, aktivasi instalasi pelindung header *Helmet*, restriksi penolakan peramban pembatas *Rate Limit*, lantas integrasi konfigurasi isolasi variabel `.env`. Waktunya mengunci rapat seluruh kelemahan gerbang infrastruktur peladen API TISS dan melayakkan dirimu terakreditasi promosi menuju materi peretasan sabuk *Red Team*!

---

*📅 TISS Null Teaming · Week 14 · Day 4 · FORGE Rank*
