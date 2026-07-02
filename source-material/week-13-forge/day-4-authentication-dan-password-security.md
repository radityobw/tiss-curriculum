# 🔨 Week 13 · Day 4: Authentication & Password Security

> **Rank**: FORGE | **Minggu ke-13**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 13 · Day 4/5 | FORGE Rank (Minggu 4 dari 5) | Overall: 64/120 hari (53%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** mekanisme otentikasi manajemen sesi konvensional (*Session-based*) dengan pendelegasian status token berbasis identitas (*JWT Stateless Authentication*).
2. **Menerapkan** fungsionalitas algoritma kriptografi perlindungan (*Hashing*) satu arah untuk merahasiakan memori kata sandi memanfaatkan `bcrypt`.
3. **Menggambarkan** skema alur arsitektur sirkulasi keamanan sistem validasi jaringan login ekosistem peladen otentikasi.

---

## 📖 Materi Inti

### Otentikasi: Manajemen Sesi pada Server

Protokol operasional jaringan *HTTP* sifat dasarnya berstatus tanpa jejak riwayat memori (*Stateless*). Protokol arsitektur tersebut tidak didesain mengenali maupun merekam identitas klien yang sukses melalui gerbang verifikasi perutean fungsi login pada permintaan sebelumnya. Demi memastikan Peladen (*Server*) secara kontinu mengingat otorisasi pengguna pada perpindahan lintas rute pengaksesan, arsitek peladen perlu mendistribusikan "stempel karcis tanda pengenal" atau tiket otorisasi identitas usai validasi sandi pendaftar dinyatakan tuntas.

Di lingkungan eksekutor industri perancangan peladen, terdapat 2 kutub mazhab otentikasi :

**1. Session-Based Authentication (Otentikasi Berbasis Riwayat Sesi Klasik)**
Server mengelola daftar panjang tamu (*Session Store*) di memori lokalnya, lantas peladen mencetak delegasi stempel (berwujud *Session ID*) untuk didelegasikan agar diikat menyusup mendiami bungkusan fungsionalisasi penyimpanan payload *Cookie* peramban pengguna. Setiap klien meluncurkan transmisi eksekusi , *Cookie Session ID* tersebut disertakan untuk terus dikomparasi kecocokannya dengan daftar riwayat catatan *Server*.

**2. Token-Based Authentication (Otentikasi Berbasis Token API Modern: JWT)**
Server merilis manajemen arsitektur bebas pencatatan sesi riwayat, menanggalkan peranan fungsi **pencatatan riwayat** (*Stateless Architecture*). Pasca login terverifikasi akurat, Server memformulasikan sertifikat token digital khusus berlabel tanda tangan kriptografi enkripsi magis (*JSON Web Token / JWT*), diisi payload pengenal atribut spesifik (misal ID 5), dan diserahkan agar diselipkan dititipkan secara (di penyimpangan sisi) ke peramban *Frontend*. Server menaruh kepercayaan kepada sesi identitas klien selama klien tersebut responsif mendedahkan/mencantumkan deklarasi kemurnian token bertanda tangan absah racikan server terkait.

### Mencegah Kebocoran Kredensial: Hashing Kata Sandi (Bcrypt)

Sebagai pengembang *Backend*, **DILARANG KERAS** dan diharamkan mencatat kata sandi pengguna dalam format teks telanjang dan murni (*Plaintext*) di hamparan struktur pelaporan *Database*. Jika basis data diretas (skenario kebocoran basis log), seluruh kredensial sandi pengguna akan terekspos secara langsung!

Kita wajib menyamarkan data kata sandi murni melalui arsitektur pengikatan fungsi Kriptografi (*Hashing*). Berbeda jauh dengan teknik *Enkripsi* (bisa diputar/ditarik direkayasa divalidasi ke bentuk awal tulennya dengan memutar kunci dekripsi pembalik algoritmanya), fungsi kalkulasi matematis *Hashing* dirancang murni secara absolut berjalan **satu arah tunggal**. Sandi hasil hashing mustahil diretas kembali (di-*reverse*) menjadi wujud abjad murni asalnya.

Modul pustaka penyandian yang terjamin kualitasnya pada *Node Backend* kekinian adalah paket `bcrypt`.

**Lantas, Bagaimana Server Tahu Sandinya Cocok Kalo Gak Bisa Dibalikin (Di-dekrip)?**
Mudah! Saat pengguna memasukkan kembali inputan teks sandi "R4hasi4" saat menjalankan sirkuit *Login*, peladen segera mengambil teks masukan tersebut dan mencincangnya detik itu juga. Hasil perhitungan logik sandi *hash* teks tamu yang baru lantas dicocokkan *"Apakah payload *hash* kalkulasi serangan ini sama identik persis formatnya dengan hash yang tersimpan permanen di Database?"*. Jika nilainya divalidasi klop identik, status peramban login disahkan!

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari mempraktikkan proses perlindungan algoritma pengamanan sandi sistem *hashing* menggunakan `bcrypt`!

1. Bentangkan antarmuka OS *Terminal*, lalu cetak barisan sarang direktori eksperimen: `mkdir lab-bcrypt`, kemudian akses masuk `cd lab-bcrypt`.
2. Prakarsai registrasi berkas *Node API* dengan mengeksekusi inisiasi `npm init -y`.
3. Pasang instalasi perisai pustaka perlindungan sandi arsitektur fungsi *Bcrypt*: 
```bash
npm install bcrypt
```
4. Susunlah pelaporan fail baru bernama `cincang.js`, lalu sisipkan parameter deklarasi ini ke dalamnya:

```javascript
const bcrypt = require('bcrypt');

const sandiUser = "TissAcademy2026!"; // Konstruksi Sandi Tulen (Plaintext)
const kadarGaram = 10; // Salt rounds (Faktor parameter kalkulasi biaya kekebalan pengacakan enkripsi algoritmanya)

// ===========================================
// 1. FASE REGISTRASI (Perlakuan Mencincang Sandi Tulen Pengguna sebelum rekam tabel memori Database)
// ===========================================
bcrypt.hash(sandiUser, kadarGaram, (error, hasilCincanganSandiUtama) => {
 console.log("Parameter Sandi Tulen Pendaftar:", sandiUser);
 console.log("Parameter Hasil Hash Cincang (Yg direkam ke SQLite DB):", hasilCincanganSandiUtama);
 
 // ===========================================
 // 2. FASE LOGIN (Eksekusi Operasional Pengecekan kecocokan fungsi pengetikan Sandi)
 // Ceritanya User nyoba kembali Login dan mendaraskan tebakan entri sandi
 // ===========================================
 const ketikanSandiTamu = "TissAcademy2026!"; // Kamu dapat merombak teks ini nanti buat membuktikan uji tes penolakan sandi salah (Gagal validasi login error)!
 
 // Server memanggil perintah Adu komparasi
 bcrypt.compare(ketikanSandiTamu, hasilCincanganSandiUtama, (err, validitasCocok) => {
 if(validitasCocok) {
 console.log("✅ STATUS VERIFIKASI : AKSES IDENTITAS SANDI KLOP & COCOK MUTLAK!");
 } else {
 console.log("❌ STATUS VERIFIKASI : VALIDASI SANDI SALAH TOTAL, PENYUSUP DITOLAK!");
 }
 });
});
```

5. Ketik hulu perintah pemicu terminal untuk menerjemahkannya: `node cincang.js`.
6. Tarik napas saat Anda menatap penampang terminal. Terdapat barisan teks acak mencapai panjang parameter 60+ abjad (*Hasil Hash Cincangan Abadi*) tercetak murni. Mustahil Anda maupun peretas merancang formula khusus untuk menerjemahkan (mendekripsi) fungsi deretan teks pelaporan acak tersebut agar memeras balik maknanya wujud kembali rupa abjad "TissAcademy2026!".

---

## 💡 Quiz Kilat

<details>
<summary>❓ Ketika mendirikan peladen otentikasi login jaringan (*JWT Stateless Authentication*), mengapa arsitek peladen dibebaskan dari kewajiban berat untuk mengelola pencatatan status rekaman peramban jejak riwayat login pendaftar pengunjung di log memori penyimpanan database *Session ID Server*?</summary>

**Jawaban:** Dikarenakan hakikat pengoperasian eksekusi otorisasi parameter peladen peramban tipe JWT murni berbasis rancangan skema arsitektur nir-status (*Stateless Architecture*). Sebatas payload sertifikat token digital spesifik otorisasi yang disimpan di saku ruang penyimpanan lokal peramban itu sendirilah yang mandiri merepresentasikan profil klaim hak otoritas pendaftar (seusai Server sigap memverifikasi stempel kriptografi keabsahan digitalnya). Konsep struktur pendelegasian verifikasi di saku peramban tersebut secara revolusioner memerdekakan peladen basis data eksekusi untuk tak disibukkan operasi rutin sekadar buat mendokumentasikan serta mencatat rekaman status jejak kunjungan login sistem!
</details>

<details>
<summary>❓ Sasar rincian perbedaan konsep filosofis yang menjadi garis pemisah mutlak batasan pembelahan pemaknaan terminologi proteksi modifikasi keamanan sandi berbasis perlindungan *Hashing* dibandingkan penyamaran kata payload berwujud enkripsi modifikasi keamanan kriptografi perisai parameter perlindungan *Enkripsi* perlindungan kata sandi!</summary>

**Jawaban:** Arsitektur perlindungan manipulasi fungsi keamanan tameng operasi *Enkripsi (Encryption)* dirancang khusus untuk memfasilitasi kebutuhan perlindungan pertukaran payload pengikatan spesifikasi konversi parameter pergerakan sandi *dua arah (reversible)*; payload muatan parameter abjad fungsi perlindungan arsitektur sandi enkripsi (seperti rekaman fungsi teks terselubung) dirancang untuk bebas diekstraksi ditarik, dibongkar direkayasa dekripsinya kembali memulihkan rupa wujud parameter asli tulen jika dan hanya jika pengguna memiliki akses memori otentik kunci parameter (kunci deskripsi pelacak pembongkar rahasianya). Berbeda jauh dengan spesifikasi *Hashing*, yang mana operasional fungsinya terikat murni bertangan besi dalam sistem logik kalkulasi parameter matematis operasi penyandian statis satu arah (*satu arah / irreversible modification parameter calculation*); teks spesifikasi log yang usai tuntas diolah oleh rahim modul *hash* niscaya mustahil diretas, mustahil didekripsi (diurai dibongkar ditarik pemulihannya siuman) ke parameter abjad wujud penyusunan string pengetikan aslinya semula menggunakan rumusan kalkulasi logik parameter apa pun.
</details>

<details>
<summary>❓ Dalam bongkahan kerangka instalasi perisai penangkal arsitektur *Bcrypt*, parameter argumen sisipan bertitel 'Salt' (Kadar Garam / *Salt Rounds*) lantas bertugas secara spesifik ditambahkan membaur demi mempertebal perisai pertahanan kekebalan algoritma dari kerentanan bahaya insiden keamanan apa?</summary>

**Jawaban:** Paramater sisipan *Salt* (Garam / *String Modifier Randomized String Logic Parameter Injection Value Encryption Hashing Logic Integration Random Text Modification Element Configuration Application Algorithm Crypto Hashing Algorithm Randomization Value Addition String Hash Cryptographic Architecture Hash Algorithm Component Property*) berwujud ekstrak sisipan serpihan teks abjad modifikasi deret acak unik yang secara gaib otomatis tergenerasi diinjeksi diaduk diramu membaur mengkustomisasi logik rakitan *hash* tulen. Hal ini diinisiasi secara mutlak oleh logik program guna mengecoh, mengebiri serta menggagalkan operasi serangan serangan peretasan kamus tebakan referensial pembongkar basis peretasan sandi (*Rainbow Tables Application Attack / Array Dictionary Attacks Logic Dictionary Brute-Force Authentication Rejection Method Error Configuration Network Array Hacker Exploitation*), memastikan bahwa walau sepasang klien berbeda kompak mendeskripsikan penetapan logik payload nilai entri sandi kembar yang identik persis (umpama "12345"), parameter *output* arsitektur ukiran cetak hash rekaman keduanya di SQL database *backend server array* niscaya bakal melenceng dan berbeda bentuk tampilannya satu dan lain!
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya fasih membedah spesifikasi perbedaan prinsipil arsitektur manajemen sesi otentikasi memori otentikasi Server memori peladen terikat tabel *Session ID Storage Database Node Backend Token Application Memory Implementation Framework* berbanding perutean arsitektur *JSON Web Token API Stateless Logic Authentication Protocol Setup Implementation Parameters*.
- [ ] Saya menyerap konvensi saklek dan mematuhi kredo absolut pedoman parameter pelarangan integrasi perekaman sandi mentah rahim teks murni tak terlindungi sandi operasi aplikasi parameter *Plaintext Logic System Text Form Application Error Database Structure Code Injection* di peladen basis data.
- [ ] Saya berhasil mendemonstrasikan keahlian mengeksploitasi fungsi pencincang sandi (*hashing cryptosystem module algorithm architecture configuration tool node*) pustaka pelindung `bcrypt.hash` dan proses pencocokkan `compare`.
- [ ] Saya kelar menuntaskan rekam uji coba rutinitas instalasi aplikasi cincang sandi integrasi `bcrypt module Node integration module Node testing script function logic Node` di operasi terminal ruang *Mini Lab*.
- [ ] Saya menuntaskan pengujian ulasan referensi jawaban ringkasan evaluasi (*Quiz Kilat*).

---

## 🔗 Resources

- [JWT.io Debugger](https://jwt.io/) — radar sistem pembedahan inspeksi (*JSON Web Token Decoder Parser Visualizer Analyzer Inspector Security Test Integration Protocol Development Component Parameter Logic Parsing Security Component Interface Utility Software Tools Test Integration Debugger API Client API Testing API Architecture Authorization HTTP JWT Parsing Debugger Utility Testing Application Interface Security Software Inspection*) andalan spesialis pengembang web yang diandalkan untuk keperluan memecah membongkar mendaras mendeteksi rincian komponen bungkusan muatan pengiriman ekstrak klaim selimut payload informasi atribut pelaporan token otorisasi antarmuka klien API server otorisasi *JSON Web Tokens Payload Data Signature Header Parser Format Tools Decoder Visualization Component Tool Architecture Decoder Decoder JSON Tokens Payload Verification Component*.

---

## ➡️ Besok

**Day 5: Lab & Mission: Sistem Login/Register** — Seluruh fondasi pemodelan infrastruktur kelam gerbang pertahanan otentikasi arsitektur peramban fungsi telah tersedia komplet dibahas tuntas parameter teknikal arsitektur perakitan teoretis konseptual instalasi fungsinya di dokumentasi materi ekosistem kurikulum modul pengerjaan implementasi *Software Application Node Security Password Cryptographic Security Hash Logic Bcrypt Implementation Logic Server Router Security System Architecture Web Endpoint Router Routing SQL Node Controller User Middleware Form Node SQL Endpoint HTTP Database Form API Integration Security System Middleware Router SQLite DB Validation API Controller* selama 4 fase materi hari operasional minggu krusial ini! Di sesi pengerjaan laboratorium mutlak esok hari, Kawah Candradimuka perancangan utuh aplikasi basis server perutean fungsi login menunggu pengerjaan peretasan utuhmu menuntaskan parameter eksekutor rilis utuh fungsi perakitan sirkuit logik operasional fungsi rilis sirkuit pemrograman utuh logik murni memformulasikan rilis perakitan spesifikasi fungsi peladen proyek modul! Engkau akan menyatukan kerangka utuh perakitan *server* rahim API komplit meliputi sirkulasi spesifikasi gerbang arsitektur pembuatan klien Akun Registrasi Sistem API Klien (*User Register Account Application Data Creation System Controller Endpoint Route Logic User Validation SQLite Request Form Architecture Routing App Logic Node Endpoint*), serta mengintegrasikannya dengan fungsi halaman Otentikasi Masuk Sesi Akses Sistem Validasi Operasional (*Application User Login Auth Request Validator Form Controller Verification Architecture App SQLite Database Routing Parameter App User Route Logic Express HTTP Security API Server Application*) dengan mensinkronisasikan memadukan kolaborasi maut tri-komponen kerangka instalasi pustaka penyusunan aplikasi peladen utama (Kerangka gerbang fungsi *Express Server Router Node Node Interface Architecture HTTP Request Node Routing Method Router Implementation Routing Component Module Configuration Architecture App Node Module Node Logic Controller Backend Service HTTP Module Application Protocol Protocol Architecture Route Service Controller System Engine Framework System Method Data App Node App Middleware Request Handler Config Controller Endpoint Request* + Basis perakitan relasional *SQLite Architecture DB Table Parameter Request Component DB Architecture DB Driver Storage Persistence Data Module Network Form Integration Memory Data Architecture Integration Node SQLite Integration SQLite Config Storage SQL Engine DB Network Data Storage Module Command Initialization Logic Initialization Data Storage Implementation Engine Storage Network Database Storage Config Interface* + Seraya mengaktifkan pertahanan cincang kriptografis arsitektur pelindungan mutlak tameng perlindungan otentik otentikasi operasional sandi spesifikasi *Bcrypt Data Algorithm Hash Auth Cryptographic Storage Logic Password Logic Verification Module API Logic User Configuration Auth Integration Architecture Request Password Implementation Node Hashing Encryption Protection Hash Cryptographic Architecture Security Bcrypt Authorization Middleware User Identity Password Architecture Authentication Logic Access Component App Parameter Node Storage Middleware Form Config API Interface Encryption Controller Auth Backend Middleware Application Auth Security Tool Module Router Auth Verification Controller Auth Tool Security Framework Node Password* mutakhir)!

---

*📅 TISS Null Teaming · Week 13 · Day 4 · FORGE Rank*
