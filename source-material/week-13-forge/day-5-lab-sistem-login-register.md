# 🔨 Week 13 · Day 5: Lab & Weekly Mission Sistem Login/Register

> **Rank**: FORGE | **Minggu ke-13**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓░░] 80% — FORGE Rank (Minggu 4 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░] 54% — Hari 65 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → 🔄 FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu krusial telah tuntas. Engkau telah diinisiasi menyelami arsitektur persemayaman basis data permanen peladen beserta struktur pertahanan pengenal *API*:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | SQL Basics (Bagian 1) | Pijakan membangun (`CREATE`), menyuntik (`INSERT`), serta mengekstrak (`SELECT`) arsip Database relasional SQL. |
| Day 2 | SQL Basics (Bagian 2) | Modifikasi pembaruan dan penghapusan (`UPDATE/DELETE`) seraya menjahit relasi bersilangan (`JOIN`). |
| Day 3 | Database di Node.js | Pemasangan fungsi perantara operasional *Database Driver sqlite3*. |
| Day 4 | Auth & Password Security | Konsep arsitektur *Session* vs *JWT*, dilengkapi penerapan kriptografi pelindung kata sandi (*Bcrypt Hashing*). |

---

## 🧪 Hands-On Lab

### Prerequisites
- *Node.js* dan Editor kode (seperti VS Code) telah siap beroperasi.
- Modul pengujian API klien: **Postman / Thunder Client** terinstal.

### Misi Hari Ini: "Membangun API Sistem Otentikasi"

Segala teoretis telah engkau kuasai. Hari ini dirimu bakal mengukir perakitan puncak menyatukan kerangka *Express Backend API*, menjahitnya bersama penyimpanan *SQLite*, serta melapisnya dengan sistem perisai kriptografi *Bcrypt*! 

### Step 1: Inisiasi Direktori (Setup)

1. Deklarasikan ruang direktori `mkdir lab-auth-api`, kemudian akses navigasinya `cd lab-auth-api`.
2. Inisialisasi manifest proyek melalui: `npm init -y`.
3. Unduh dan instalasikan kompilasi pustaka andalan *Backend*:
```bash
npm install express sqlite3 bcrypt
```
4. Buat berkas peladen utama dengan nama `server.js`.

### Step 2: Arsitektur Persemayaman Server Komplit (The Masterpiece)

Salin struktur skrip peladen ini dan sisipkan ke perut `server.js`:

```javascript
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');

const app = express();
app.use(express.json()); // Penadah sandi payload bodi JSON

// ===============================================
// 1. PENYIAPAN DATABASE & TABEL (Auto-Create)
// ===============================================
const db = new sqlite3.Database('./brankas-agen.db');
db.serialize(() => {
 // Merakit kerangka tabel pengguna
 db.run(`CREATE TABLE IF NOT EXISTS users (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 username VARCHAR(50) UNIQUE,
 password_hash TEXT
)`);
});

// ===============================================
// 2. RUTE REGISTRASI (CREATE USER)
// ===============================================
app.post('/api/register', async (req, res) => {
 const { username, password } = req.body; // Ekstraksi data sandi dari permintaan klien
 
 if(!username ||!password) return res.status(400).json({pesan_status: "Error 400: Nama pengguna atau kata sandi tidak boleh kosong!"});

 try {
 // Fungsi Hashing Sandi (Tingkat salt: 10)
 const saltRounds = 10;
 const hashAbadi = await bcrypt.hash(password, saltRounds);

 // Sisipkan cincangan sandi (BUKAN teks aslinya!) ke Database
 const tembakanKueri = db.prepare("INSERT INTO users (username, password_hash) VALUES (?,?)");
 
 tembakanKueri.run([username, hashAbadi], function(err) {
 if (err) {
 return res.status(400).json({pesan_status: "Gagal, username tersebut sudah digunakan oleh pengguna lain!"});
 }
 res.status(201).json({pesan_status: "Registrasi Sukses! Akun Anda terdaftar dengan aman!"});
 });
 tembakanKueri.finalize();
 } catch (error) {
 res.status(500).json({pesan_status: "Kegagalan Peladen Internal (Internal Server Error)."});
 }
});

// ===============================================
// 3. RUTE LOGIN halaman (AUTENTIKASI)
// ===============================================
app.post('/api/login', (req, res) => {
 const { username, password } = req.body;

 // Lakukan pencarian awal di Database berdasarkan username
 db.get("SELECT * FROM users WHERE username =?", [username], async (err, hasilData) => {
 
 // Validasi apakah pengguna tersebut eksis
 if (!hasilData) {
 return res.status(401).json({pesan_status: "Akses Ditolak! Akun pengguna belum terdaftar."});
 }

 // Apabila eksis, sinkronkan kecocokan fungsi 'password' masukan dengan 'hash' di peladen
 const tebakanCocok = await bcrypt.compare(password, hasilData.password_hash);
 
 if (tebakanCocok) {
 res.status(200).json({pesan_status: `Verifikasi Login Berhasil! Selamat datang, ${username}!`});
 // Di arsitektur produksi nyata, di titik inilah server menerbitkan token JWT untuk diserahkan ke klien.
 } else {
 res.status(401).json({pesan_status: "Akses Ditolak (401)! Kata sandi yang Anda masukkan tidak tepat."});
 }
 });
});

// Jalankan Palang Radar Aplikasi!
app.listen(3000, () => console.log('Sistem API Otentikasi beroperasi mendengarkan koneksi di Port 3000.'));
```

### Step 3: Pengecekan Daya Operasional Aplikasi Klien (Postman)

1. Nyalakan sirkuit peladen via instruksi `node server.js`.
2. Bidik eksekusi pengikatan POST memakai aplikasi klien penguji (*Postman / Thunder Client*) ke alamat rute API:
 `http://localhost:3000/api/register` (Sisipkan payload di *Body JSON* yang memuat atribut payload "username" dan "password").
3. Usai proses registrasi tercatat berhasil divalidasi, ujilah pengalihan lajur eksekusi menyasar metode rute `/api/login` dengan merancang parameter masukan berupa kombinasi sandi yang disengaja keliru (tinjau respons penolakan stempel `401 Unauthorized`).
4. Perbaiki input kombinasi sandi dengan teks autentik, luncurkan kuerinya dan nikmati status keabsahan `200 OK` yang mengesahkan validasi arsitektur keamanan absolut otentikasi logikmu!

---

## 🎯 Weekly Mission

### Misi: Mengevaluasi Keamanan Data Secara 
**Deskripsi:** Apabila dirimu menelaah arsitektur penyusunan struktur kerangka Database *SQLite* pada *folder* operasional lab hari ini, peladen telah secara diam-diam menghasilkan sebongkah ekstensi file biner `.db` (*brankas-agen.db*) di lokasi direktori luringmu. 

**Tugas Mandiri:** Lakukanlah inspeksi manual untuk memeriksa secara visual kondisi rekam penulisan *Database* tersebut langsung pada media antarmuka penyimpanan di komputermu (Anda bebas memanfaatkan fitur ekstensi VS Code *SQLite Viewer* atau mengoperasikan peranti aplikasi GUI khusus semacam *SQLite Studio*). Bukalah modul muatan isi struktur tabel dari berkas `brankas-agen.db`!

**Deliverables:**
1. Tangkapan layar (*Screenshot*) visual yang mengilustrasikan penampang susunan barisan tabel pada berkas Database `brankas-agen.db` tempat rekam catatan log entitas *user* Anda bertengger mengabstraksikan panjang acak deretan enkripsi pelindung fungsi *hash* pada kolom `password_hash` (yang sukses disuntikkan via prosedur pengerjaan pertahanan bcrypt).
2. Lampirkan berkas gambar dokumentasi pengujian tangkapan visual (*screenshot*) tersebut untuk diunggah melengkapi dokumen repositorimu.

**Kriteria Sukses:**
- [ ] Mampu berinteraksi mengakses berkas pembaca basis SQLite menggunakan antarmuka eksternal (*GUI*).
- [ ] Memvalidasi dan memastikan penampakan penyimpanan data *password* tidak lagi berbentuk *plaintext*, melainkan termutasi sepenuhnya menjadi struktur fungsi hash rahasia acak 60 abjad.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Mengingat parameter pengiriman sandi otentikasi peladen API otentikasi pada gerbang *Register/Login* membungkus parameter paket *JSON* berisikan data sandi amat sensitif, rutinitas metode HTTP apa yang diwajibkan untuk mengalokasi pengiriman alurnya (dan mengapa diharamkan menggunakan GET)?</summary>

**Jawaban:** Pengiriman otentikasi diwajibkan mutlak diselundupkan tersembunyi menumpang payload paket *body* dari HTTP metode pengiriman transmisi jenis *POST*. Metode *GET* diharamkan karena berisiko memaparkan informasi parameter sandi secara vulgar terlihat transparan menempel pada antarmuka alur tautan *URL Address Bar* (dan terkam riwayat histori *browser*).
</details>

<details>
<summary>❓ [MUDAH] Atribut konfigurasi pembatas tambahan apa yang wajib disematkan pada spesifikasi pengikatan konstruksi pembuatan kolom tabel laksana barisan pendefinisian kueri `username VARCHAR(50)...` guna menggaransi pertahanan penangkal database seandainya didapati pendaftar yang berniat meretas profil menyabotase serta mengklaim identitas kombinasi abjad akun *username* yang eksistensinya persis identik telah digunakan sebelumnya?</summary>

**Jawaban:** Pengikatan pelibatan spesifikasi sintaks batas kekangan kendali validitas klausa pengingat konstrain atribut pembatas `UNIQUE`.
</details>

<details>
<summary>❓ [SEDANG] Di tengah mengoperasikan kelancaran rute rutinitas inspeksi penyelarasan alur skrip verifikasi fungsi *Login* merespons pemanggilan API dari peluncur, jikalau lajur verifikasi sistem klien tersebut terbukti menyuntikkan kesalahan tebakan parameter kata sandi atau nama akun di masukan kargonya, jenis pelaporan stempel identifikasi kode status HTTP (*balasan HTTP Error Codes ras 4xx*) manakah yang mesti dieksekusi dikirim merespons interupsinya?</summary>

**Jawaban:** Konfirmasi respons pelaporan parameter kegagalan validasi galat bernomor kode status 401 (Unauthorized / Penolakan Autorisasi Akses).
</details>

<details>
<summary>❓ [SEDANG] Menyasar analisis terhadap struktur fungsi persandian `bcrypt.hash(password, saltRounds)`, definisikan signifikansi paramater argumen variabel *saltRounds* (lazim bernilai 10) bagi efektivitas perisai pertahanan arsitektur keamanannya?</summary>

**Jawaban:** *Salt rounds* menentukan tingkat kompleksitas dan porsi parameter besaran biaya operasional logik pengacakan (*cost factor*) algoritma kriptografi dalam menjejal sirkuit memori. Makin masif pengesetan nilainya, kian tersita waktu peladen memproses eksekutor kalkulasi pencincangannya (sengaja dilambatkan secara ekstrem), fungsi ini krusial diandalkan guna menguras ketahanan sumber daya memori mesin peretas dalam upaya menangkal eksploitasi peretasan sandi masif sejenis metode instan *Brute-Force*.
</details>

<details>
<summary>❓ [SULIT] Ketika operasi sirkulasi sandi skrip rute *API Login* divalidasi kinerjanya; coba runutkan dua tahapan krusial alur pengujian operasional validitas *Server Backend* di sebalik kodingan, sebelum putusan pengesahan konfirmasi sandi kode balasan HTTP *200 OK* dirilis diterbitkan!</summary>

**Jawaban:** Tahapan Babak Pertama (Validasi Ketersediaan Ekstraksi Identitas Kredensial Basis Data): Peladen menelusuri memori basis SQL menggunakan kunci nilai variabel payload kolom nama akun `username` demi memverifikasi eksistensi kepemilikan akun tamu pengunjung (*jika hampa/tidak ada satupun indeks korelasi terkait yang menjahit, eksekutor bakal segera menerbitkan putusan penolakan peringatan status galat Unauthorized 401*). Babak Kedua (Konfirmasi Silang Ketahanan Pertahanan Kredensial Hash Cincang vs Sandi Tulen Masukan Klien Pendaftar): Ketika verifikasi baris validasi akun pengunjung eksis dijemput, barulah logik peladen mengekstrak simpanan rahasia parameter teks cincang *password_hash* di kumpulan database, mengadu memanggil pembenturan pengujian integrasi logik penyelarasan silang (via aktivasi parameter komparasi metode *bcrypt.compare*) untuk ditubrukkan diadu kekuatan mencocokkannya merespons kombinasi teks rahasia sandi murni tebakan pengunjung barusan (dikalkulasikan dan dicincang algoritma hash lagi saat di udara untuk dibandingkan kelop validitas logiknya). Bilamana rentetan dwi tahapan validasi arsitektur perisai itu sukses sinkron mutlak tanpa kecacatan verifikasi, barulah gerbang menerbitkan status pelaporan sah konfirmasi otorisasi penyematan label sandi keberhasilan respons 200 OK.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya fasih merencanakan arsitektur kerangka penyusunan relasional pembuatan tabel kueri SQL (`CREATE`) menyusup ekosistem SQLite.
- [ ] Saya telah menuntaskan pendemonstrasian praktik menjahit fungsi konektor integrasi eksekusi payload skrip perantara API peladen *Express Node.js* melawan struktur transmisi arsitektur penyimpanan basis data SQL permanen lokal.
- [ ] Saya menuntaskan penguasaan teoretis perihal siklus kriptografis perlindungan segenap rekaman sandi basis pengamanan database (terbantu fungsi algoritma pembalut *Bcrypt*).
- [ ] Saya berhasil mendirikan operasional rutinitas arsitektur API secara komprehensif, mencakup rute payload fungsi sistem *Register* dan sistem verifikasi verifikator *Login* terpadu (Arsitektur API *Backend Security Controller Parameter System*).
- [ ] Saya sukses mengaplikasikan pembongkaran pengkajian evaluasi peramban inspeksi direktori database memanfaatkan bantuan pembaca visual *SQLite GUI Editor Viewer Software App* pada modul pencapaian pengukuhan *Weekly Mission*.

---

## 💬 Diskusi Minggu Ini

1. Jika algoritma otentikasi cincang *Bcrypt Hashing Cryptographic Parameter* terbukti secara teknis memiliki jaminan parameter enkripsi yang mutlak ireversibel dan tidak sanggup diretas balikan secara ke bentuk murni (didekripsi ulang) lantas dipaksa direkayasa, maka secara praktis relevankah atau fungsionalkah peladen mewajibkan secara mutlak fungsi validasi pencegat persyaratan penempatan fungsionalitas panjang variasi ragam batasan format modifikasi karakter sandi minimum (semisal pengimplementasian validasi "Sandi Wajib Tersusun Minimal Atas 8 Kombinasi Karakter Spesifik + 1 Sisipan Simbol Tanda Baca Khusus + Kombinasi Huruf Kapital") ke seluruh pendaftar profil pengguna *web application* klien tersebut? Mengapa tidak melepaskan kebebasan pendaftar meski ia nekat mendaftarkan frasa sandi bodoh layaknya "123"?
2. Evaluasi pengerjaan rentetan parameter arsitektur kolaborasi integrasi asimilasi instalasi sandi antarmuka *Backend API Node Developer Backend Logic Interface (Framework `Express` + Permanen `SQLite` + Perisai Keamanan *Hashing Cryptosystem Module `Bcrypt`)*! Komparasikan kadar tingkat porsi kesulitan merakit perisai arsitektur *Backend* ini bilamana disandingkan dengan parameter fokus rutinitas modifikasi kosmetik pengerjaan logika sintaks kustomisasi tata letak arsitektur fungsi interaksi *Frontend (Desain `CSS` / Logika Manipulasi `DOM Application`)* di rute pengerjaan eksplorasi minggu materi terdahulu? Manakah sisi yang memacu dan melahirkan gejolak stimulasi penalaran kecenderungan peminatanmu secara krusial?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ THE GATEKEEPER │
│ Week 13 Complete │
│ "You have built the vault │
│ and forged the unbreakable key." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 14: Secure Coding & OWASP Top 10**

Sekian pekan lamanya, secara berturut-turut rutinitasmu diekspos terhanyut terbuai di alam zona aman perakitan pendirian parameter kerangka pembangun konstruksi aplikasi antarmuka *Full-Stack App Developer Parameter Backend Frontend Implementation Database Logic Node Infrastructure* memori logik sirkuit mandiri pada peranti *environment* isolasi tertutup ruang rahasiamu! Di minggu mendebarkan depan, saatnya membangkitkan rutinitas gejolak peralihan zona nyaman dari lena perancangan struktur semu semata tersebut. Esok harinya, perumusan logikmu dipaksa mengalami pergeseran radikal merentang lintas alam operasi! Kita bakal memusnahkan dan mengakhiri penugasan rute pemetaan struktur profil kognitif arsitektur perancang arsitektur pembangun aplikasi semata (*Yellow Team Defensive/Developer Posture System Architecture Software Design Creation Implementation Developer Architecture Application Parameter Web App Logic Dev Methodology Developer*). Momen ini adalah transisi drastis di mana penugasan pikiran logik peramban instingmu dilatih menceburkan diri berasimiliasi sepenuhnya mengadopsi insting nalar agresif dan manipulatif pergerakan sirkulasi Arsitek Pengeksploitasi Jaringan Penetrasi (Insting Analis Kritis Peretas /Intelejen Penetration Tester Analis Kerentanan Keamanan Serangan Manipulatif *Offensive Red Teaming Hacking Hacker Web Hacker App Sec Security Analyst Vulnerability Web Intrusion Pen Testing Security Bug Logic Penetration App App Exploitation Methodology Security Hacker Method Tester System Testing Security Hacker Tester Bug Bounty Hunter Web Hacking Logic Application Attack*). Kita lantas berorientasi fokus merajut menelusuri penelaahan pendeteksi ancaman mendebarkan membedah kelamnya sirkuit kerentanan dokumen arsitektur daftar **OWASP Top 10**—yakni himpunan konsorsium kompilasi standardisasi dokumen global penyusunan urutan peringkat daftar 10 pengklasifikasian arsitektur peretasan tipe kelemahan fungsi kelalaian *logic code bug vulnerability* eksploitasi parameter kerentanan rute injeksi celah jaringan peladen operasi sistem aplikasi berpotensi fatal paling krusial mendominasi dan mengerikan di penjuru muka bumi peramban jaringan peretasan web sejagat jaringan!

> 🚀 *"To defend the fortress, one must learn how to burn it down."*

---

*📅 TISS Null Teaming · Week 13 · Day 5 · FORGE Rank*
