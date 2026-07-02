# 🔨 Week 12 · Day 2: Node.js Fundamentals

> **Rank**: FORGE | **Minggu ke-12**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 12 · Day 2/5 | FORGE Rank (Minggu 3 dari 5) | Overall: 57/120 hari (47%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menjelaskan** eksistensi platform Node.js dan pergeseran paradigma arsitektur pengembangan yang dibawanya pada ekosistem global penulisan *JavaScript*.
2. **Mengelola** dan menginisialisasi peranti instalasi kerangka pengembangan dependensi perpustakaan lewat pemanfaatan pengelola *Node Package Manager (NPM)*.
3. **Membedakan** struktur eksekusi penerapan mekanisme pengimporan kerangka fail arsitektur tata modul usang (*CommonJS*) dengan penyesuaian skrip pedoman deklarasi yang lebih kekinian (*ES Modules / ESM*).

---

## 📖 Materi Inti

### Evolusi Node.js: Mengeksekusi JavaScript di Luar Browser

Di dekade awal revolusi internet, cakupan implementasi skrip *JavaScript* sangat terisolasi mutlak. Lingkungan eksekusi satu-satunya adalah antarmuka klien *Browser* (misalnya penampang peramban Chrome, Safari, atau Firefox). Parameter isolasi ini mengebiri eksekutor fungsi JS dan merantai akses *logic*-nya, mencegahnya mengakuisisi operasi modifikasi baca/tulis ke modul *file system* sistem operasi komputer (*hard disk* laptopmu), tidak diperbolehkan mengoperasikan manajemen arus soket server peladen *database*, hingga secara kaku ditakdirkan berfungsi sebatas mengeksekusi transisi efek dan manipulasi ringan kerangka antarmuka *UI* pengguna pada jendela halaman laman *web*.

Namun semua paradigma keterbatasan tersebut dijebol pada peluncuran penemuan tahun 2009. Seorang perancang sistem, *Ryan Dahl*, berhasil membedah kerangka struktur arsitektur pelaksana program mesin kompiler spesialis skrip berlogo nama mesin eksekusi JavaScript **V8** (inti kecerdasan mesin penerjemah bawaan Google Chrome). Ia mencabut fungsionalitas inti *V8* tersebut keluar ekosistem peramban klien, mengonfigurasikannya ke dalam lapisan sistem operasional, dan merakit ulang fungsi-fungsi komputasinya ke tingkat bawah memori sistem. Hasil integrasi radikal yang melepaskan JavaScript sehingga ia kuasa dijalankan leluasa secara lokal () pada lingkungan perangkat Sistem Operasi OS Server mandiri (entah itu modul peladen di Linux, Mac, atau pun Windows) ini lantas dimasyhurkan sebagai lingkungan eksekusi sistem hibrid **Node.js**.

Disenjatai fondasi *Node.js*, kapabilitas dan skala parameter bahasa skrip JavaScript melesat pesat, berkembang seketika menjajaki posisi sejajar teknologi yang tangguh untuk membaca/menulis fail sistem, menyusun *web server*, serta mendirikan komunikasi perantara jaringan (*Backend Server*) bersaing secara kompetitif dengan ketangguhan pendahulu legendaris sekelas bahasa platform penulisan murni seperti Python, Ruby, C#, hingga skrip PHP.

### Ekosistem Alat Bantu: Node Package Manager (NPM) & package.json

Dunia arsitektur penulisan parameter layanan server lapis belakang (*backend*) umumnya amat kompleks, karenanya *developer* amat mustahil membangun segenap kerangka rute keamanan (*security*), fungsi penyandian koneksi, hingga skrip interaksi basis data mutlak 100% manual baris dari nol. Para pembuat aplikasi rutin bergantung penuh meminjam sumbangsih pustaka tambahan gratis (*dependencies* atau peranti logik *Library*) dari para pemrogram ulung mancanegara lain. Platform registrasi gudang perangkat sentral berskala sedunia untuk mendistribusikan, memverifikasi, serta mengunduh jutaan kode pelengkap program instan tersebut diwadahi sistem penata paket bernama **NPM (Node Package Manager)**.

Saat kamu memulai menginisiasi peluncuran embrio pengerjaan proyek fondasi *Node.js* baru dari awal, hal perdana yang selalu kamu luncurkan adalah mengetikkan perintah inisiasi instalasi pada *terminal CLI*:
`npm init -y`

Komando ini akan mengarahkan direktori untuk secara dinamis menghasilkan berkas konfigurasi penanda proyek yang berfungsi sebagai 'Buku Manual Identitas' bernama fail `package.json`. Segala fungsionalitas logik perangkat *library/modules* spesifik yang di masa depan rutin bakal kamu instal masuk integrasikan untuk mendukung peladen (misalnya: penambahan peranti kemanan *cryptography*, pengaturan rute peladen, konektor manipulasi penataan sandi masuk API sistem, serta komponen lain), seluruh versinya akan terdokumentasikan detail melintasi format objek registri daftar fail skrip *JSON* ini secara sistematis.

### Skema Arsitektur Modularisasi Proyek: Pembagian Modul Skrip JavaScript

Mengingat rutinitas penulisan skrip aplikasi *backend* profesional di perusahaan sanggup menyedot luapan kompilasi memori masuk ketebalan puluhan hingga ribuan baris, *developer* menyelenggarakan tata manajemen kode dengan menjabarkannya serta mengisolasinya menyebar terpisah membagi beban tanggung jawab skrip ke porsi berkas bagian file spesifik kecil (*components*), yang dikenal teknis penyebutannya merujuk istilah komponen pendelegasian tata **Modules**.
Dalam lingkungan pengembangan Node modern mutakhir, lazim ditemukan penerapan struktur pedoman kerangka relasi antar modul *file* dengan mengikuti penggolongan arsitektur ke 2 skema aliran ekosistem spesifikasi impor utama:

1. **Format Arsitektur CommonJS (CJS)** — Format bawaan klasik usang ala ekosistem turunan lawas *Node.js*, meski saat ini porsinya mayoritas masih dominan terpakai pada warisan peladen.
```javascript
// Memanggil / menginjeksi kepemilikan kapabilitas library modul pihak luar secara spesifik ke halaman fail operasional saat ini (impor)
const fs = require('fs');

// Membagikan / menyediakan otorisasi rancangan modul internal spesifik (mengekspor ) supaya mampu disedot fail peladen di luar sana
module.exports = fungsiKu;
```

2. **Format Arsitektur ES Modules (ESM)** — Standar evolusi adopsi spesifikasi *EcmaScript* masa depan tata kelola *JavaScript* secara menyeluruh di ranah global (serasi menggunakan pendekatan penulisan yang serupa 100% pada fitur modifikasi spesifik kerangka deklarasi sintaks perutean import fungsionalitas di arsitektur pustaka UI spesifik semacam kerangka *React.js*/*Frontend*).
```javascript
import fs from 'fs';
export const fungsiKu = () => {};
```

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari menulis *script* barisan pemrograman server peladen operasional mandiri (*Node.js*) pertamamu tanpa mediasi peramban klien! (Asumsi persyaratan pelengkap awal: Komponen dasar pelaksana memori spesifik perangkat *Node.js* wajib tertanam dan sukses diakses di tingkat lokal OS perangkatmu; jika *CLI Node* gagal/menolak instruksi eksekusi muatan terminal, harap *install* instalasi *installer Node* murni dari peladen situs resminya `nodejs.org`).

1. Buka antarmuka jendela Terminal *Command Line* di OS, buat serta deklarasikan pemusatan area eksperimen folder baru misal `mkdir lab-node`, dan masuki perbatasan kompartemen direktori *folder* itu dengan rute sandi spesifik (`cd lab-node`).
2. Cetak luncurkan perintah konfigurasi otentik pembukaan integrasi proyek *NPM* `npm init -y` (Sesaat kelar eksekusi tuntas, bakal lahir wujud rupa dokumentasi `package.json` secara dinamis di *folder* eksperimen lab tersebut).
3. Buat dan siapkan *file* pemrogram peladen berekstensi *script* bertitel peresmian fail sandi `server.js` serta rangkai kode arsitektur pembangun fondasinya menyalin kerangka *scripting* ini:
```javascript
// Melancarkan deklarasi impor panggilan pemanfaatan salah satu pustaka (library module built-in) sakti kepunyaan default 'os' (Operating System) peninggalan bawaan pustaka asli perakit instalasi Node.js
const os = require('os');

console.log("===============");
console.log("EKSEKUSI PEMBONGKARAN DATA SISTEM DIREKAYASA SKRIP NODE.JS");
console.log("Informasi Spesifikasi Basis OS Target : " + os.type());
console.log("Estimasi Spesifikasi Total Kapasitas Memori Random Access: " + (os.totalmem() / 1024 / 1024 / 1024).toFixed(2) + " GB");
console.log("===============");
```
4. Balik meninjau pergerakan antarmuka operasional terminal OS, dan ketik seraya pemicu instruksi perakitan peladen di bawah guna memaksa peranti eksekutor *Node* kompilator membedah arsitektur operasional muatan *script*-nya:
```bash
node server.js
```
5. Lihat tampilan respons penampang *log* layarmu sekarang! Skrip murni dari turunan arsitektur peramban *JavaScript* kini sukses mengintip menyelinap mengintervensi serta mengakses kapabilitas kerangka informasi mesin Sistem Operasimu secara tertutup secara di barisan belakang latar (*backend server*) di luar kendali dan perantaraan batasan dari program kurungan aplikasi piranti lunak *browser* mana pun!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Secara hakiki, apakah arsitektur eksekusi perangkat lunak *Node.js* dikategorikan spesifik untuk mengelompokan lahirnya ragam baru tipe atau standar referensi tata bahasa pemrograman mutakhir?</summary>

**Jawaban:** Tidak. *Node.js* bukanlah wujud bahasa pemrograman komputer. Klasifikasi mutlak yang sah untuk perangkat ini merujuk kepada pengoperasian perantara (*"Runtime Environment"*/Lingkungan Eksekusi) khusus peranti sandi kompilasi yang diotaki serta diberdayakan arsitektur kecerdasan inti perantara penganalisa V8 Chrome. Pelengkap mutasi fungsi mesin penerjemah tersebut mendongkrak keluwesan kerangka pemograman bahasa peramban *JavaScript*, sehingga alih-alih dikungkung spesifik terisolasi dalam *browser* klien UI penelusuran, skrip dapat leluasa diberdayakan beroperasi secara murni berdiri mandiri sebagai arsitektur pembangun gerbang peladen basis data sentral (*Backend*) pada tataran pelataran ekosistem piranti murni OS.
</details>

<details>
<summary>❓ Ekstensi berkas format pendata apa yang diatur dan lahir seketika secara serentak sesudah *Developer* merilis rute parameter eksekusi terminal `npm init -y` di direktori peladen instalasi *CLI*?</summary>

**Jawaban:** File `package.json`. Rekaman dokumentasi pustaka skrip ekstensif di file sentral inilah yang diestafetkan menduduki hak kepemilikan *Manuskrip Direktori Cetak Biru (Project Dependencies Blueprint)* perincian paket referensi alat ekosistem apa saja yang wajib dirakit menyatu demi mendukung keutuhan proyek peladen secara absolut dan terpadu.
</details>

<details>
<summary>❓ Atribut pemicu identifikasi kuncian spesifik nama instruksional deklarasi apa yang diterapkan merujuk rezim struktur penyusunan sekte impor kerangka *CommonJS* lawas ketika program menuntut memanggil pelibatan ekstensi kerangka perantara modul berkas rute komponen terpisah di direktori eksternalnya (*import*)?</summary>

**Jawaban:** Deklarasi panggilan metode pengangkutan `require()`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya fasih membedah serta menjelaskan peranan Node.js selaku agen krusial inovator pengangkatan JavaScript menjebol batasan arsitektur *web browser*.
- [ ] Saya tangkas menjabarkan fungsi dan menavigasikan pemanggilan wewenang manajemen perpustakaan global NPM (*Node Package Manager*).
- [ ] Saya memahami struktur arsitektur pendataan peran fail *manifest blueprint package.json*.
- [ ] Saya sukses mengaplikasikan pengerjaan penyusunan sirkuit ekstraksi intelijen perangkat sistem dari pengikatan pemanggilan referensi bawaan objek peladen `os` (di ruang sesi pengerjaan *Mini Lab*).
- [ ] Saya meluangkan momen konsolidasi analisis penuntasan soal pada rangkuman ringkas panduan *Quiz Kilat*.

---

## 🔗 Resources

- [Node.js Official Documentation](https://nodejs.org/en/docs) — fitur portal ensiklopedia ketersediaan integrasi modul dokumentasi arsitektur pedoman resmi perpustakaan pustaka dasar *API* bawaan *Node.js* (contoh modul peretas data pembongkaran direktori disk (`fs`), penarik deteksi tipe sistem piranti OS (`os`), pengelola ekstrak ranting pemetaan jalur sandi perantara alamat instalasi OS (`path`), dan lain sebagainya).

---

## ➡️ Besok

**Day 3: Express.js: Routing & Middleware** — Membangun struktur pengelola alamat peladen penelusur web HTTP dengan menggunakan komando primitif (*native API Module bawaan dari arsitektur platform Node.js*) sangatlah kompleks, berulang berpotensi menyerap ratusan pengerjaan perakitan siklus perutean penanganan koneksi panjang yang menghabiskan waktu, bak merancang konfigurasi transmisi mesin rumit presisi hanya sekadar dibekali sebatang obeng besi. Besok hari pendarasan kompetensimu di arena sandi jaringan beralih dimensi! Kita kelak mendalami struktur pengikatan instalasi arsitektur penyokong pihak pengaya ekosistem peladen sandi (yakni sebuah pustaka penunjang pengerjaan *Framework server-side* yang begitu dihormati arsitek piranti global) bermerek **Express.js**, di mana kerumitan instalasinya yang teringkas bakal mendongkrak kapabilitas produktivitas kecepatan penataan penyusunan *routing HTTP endpoint Server API Node* terakselerasi berlipat ganda nyaris seutuhnya instan dengan stabilitas memukau!

---

*📅 TISS Null Teaming · Week 12 · Day 2 · FORGE Rank*
