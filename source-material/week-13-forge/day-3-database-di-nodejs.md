# 🔨 Week 13 · Day 3: Database di Node.js

> **Rank**: FORGE | **Minggu ke-13**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 13 · Day 3/5 | FORGE Rank (Minggu 4 dari 5) | Overall: 63/120 hari (52%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengkoneksikan** peladen antarmuka aplikasi *Node.js/Express* milikmu secara langsung ke gerbang *Database*.
2. **Mengeksekusi** pengiriman kueri operasi instruksional bahasa data SQL melalui perantara program skrip *backend*.
3. **Mengenal** sekilas penjabaran konsep dan fungsi arsitektur dari integrasi modul lapisan abstraksi *ORM (Object-Relational Mapping)*.

---

## 📖 Materi Inti

### Komunikasi Lintas Sistem: Driver Database

Node.js dan layanan penyimpanan Database SQL (seperti MySQL, PostgreSQL, maupun varian SQLite portabel) sejatinya merupakan dua arsitektur proses entitas program independen yang beroperasi terpisah di level sistem operasi komputermu. Node.js secara bawaan tidak mendesain dukungan logik guna mengenali dan membaca ataupun memproses sintaks eksekutor kueri *SQL* secara mandiri.
Agar kerangka server API berbasis *Node.js* sukses mentransmisikan surat payload kueri perintah operasi manipulasi basis data SQL menuju ke gerbang eksekutor *Database*, ia mutlak membutuhkan modul penghubung penengah (seorang perantara logik) yang didefinisikan secara khusus sebagai antarmuka pustaka **Database Driver** (maupun *Database Client Library*).

Untuk integrasi peladen basis data dengan fungsionalitas portabel ringan berjenis *SQLite*, kita akan mengeksploitasi fungsi perantara *Driver* SQL populer yang ditarik dari distribusi gudang modul pustaka *NPM* bernama `sqlite3`.

Alur kerangka konseptual mekanismenya beroperasi rasional dan tertata:
1. Skrip *Backend Node.js* memanfaatkan pustaka *Driver* untuk membangun koneksi perutean pipa memori ke *file database* di *storage OS*.
2. Skrip merakit kueri parameter pembentukan susunan spesifikasi SQL berbasis parameter format teks atau sintaks bahasa data (contoh pembentukan: `SELECT * FROM arsip_data`).
3. string kueri SQL tersebut lantas didelegasikan dan ditembakkan menyeberang via perantara koneksi eksekutor modul konektor *Driver*.
4. *Database Engine SQL* peladen sasaran yang mengeksekusinya akan otomatis memproses, menyortir rekaman pelaporan, kemudian meluncurkan balasan (yang diterjemahkan secara dinamis oleh *Driver* menjadi susunan tipe himpunan parameter fungsi logik tipe data struktur turunan *JavaScript: Array of Objects*). Array kembalian ini kelak akan ditangkap oleh fungsi Node, dibungkus secara otentik sebagai stempel format respon spesifik JSON, untuk lantas disuguhkan kepada layar peramban API pihak klien!

### Sintaks Eksekusi Kueri di Node.js

Berikut adalah penjabaran implementasi kodingan instalasi *Node.js* untuk menginisialisasi pengikatan basis data (menggunakan eksekutor *Driver sqlite3*):

```javascript
// 1. Memanggil dan Memuat Penghubung Modul Driver (Via Inisiasi NPM Module)
const sqlite3 = require('sqlite3').verbose();

// 2. Tancapkan fungsi pembukaan rute koneksi agar merujuk keberadaan letak file database pada storage harddisk direktori
const db = new sqlite3.Database('./fitur.db');

// 3. Mengeksekusi pengiriman pengiriman kueri pelacakan kueri pencarian SQL pada peladen memanfaatkan deklarasi rute panggil fungsi parameter array driver `.all`
db.all("SELECT * FROM arsip_data", [], (error, hasilTarikData) => {
 if (error) {
 throw error;
 }
 // Parameter tangkapan variabel 'hasilTarikData' (array) saat ini format rupa kembaliannya telah ditransformasikan tuntas menjadi kumpulan objek JavaScript Array murni bersarang siap diolah!
 console.log(hasilTarikData); 
});
```

### Lapisan Abstraksi Database: Pengenalan ORM (Object-Relational Mapping)

Di tingkatan operasional industri sistem rekayasa perangkat lunak sesungguhnya, rutinitas pengembang mengetik rentetan rincian rumit format mentah kueri panjang teks SQL di berbagai penjuru sebaran barisan komponen Node.js secara langsung rutin menimbulkan pemicu celah rawan ralat ketik yang memborbardir galat eror sintaks data. Belum lagi kueri string SQL murni umumnya cenderung sulit dipelihara dan di-refactor ulang pada skala aplikasi korporat raksasa.
Untuk mengatasi kemelut pengelolaan kueri, perancang melahirkan arsitektur jurus konversi abstrak berlapis yang dikenal sebagai peranti *ORM (Object Relational Mapper)* (contoh pustaka *NPM framework ORM* kelas global masyhur: *Prisma*, *Sequelize*, dan *TypeORM*).

Dibandingkan menulis fungsi modifikasi pemanggilan secara konvensional laksana string mentah ini:
`SELECT * FROM staf WHERE divisi_id > 20`

Arsitektur kerangka abstrak *ORM* memungkinkan pemrogram untuk mengalkulasi operasi pelacakan serupa secara elegan melalui panggilan susunan penulisan bahasa fungsi logik objek JS yang semata, semisal:
`Staf.findMany({ where: { divisi_id: { gt: 20 } } })`

struktur pustaka arsitektur operasi logik *ORM* kelak memfasilitasi peladen secara latar belakang (*under the hood*) bekerja menerjemahkan susunan fungsi logika spesifikasi log JS rapi elegan ini terotomasi merajut balutan perwajahan pembentuk perisai ke dalam kerangka bentuk komando kueri SQL tulen (*raw SQL queries*).

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari rancang rakit tautan database lokal mutakhir pertamamu di alam instalasi rute peramban skrip *Node.js*!

1. Buka rute jendela spesifikasi Terminal antarmuka peladen komandormu, lantas deklarasikan penciptaan sarang baru `mkdir lab-node-sql`, kemudian masuk navigasikan lajurnya `cd lab-node-sql`.
2. Gelar deklarasi rilis operasi eksekutor *package* repositori awal via `npm init -y`.
3. Pasang instalasi ekstrak pustaka penghubung konektor Driver database modul SQLite:
```bash
npm install sqlite3
```
4. Rakit fail *JavaScript* bernama spesifik `induk.js`, lantas sematkan padanan sandi pengikatan arsitektur operasi ini ke dalam parameternya:

```javascript
const sqlite3 = require('sqlite3').verbose();

// Tahapan memanggil dan merancang database (Sistem akan secara otomatis menyisipkan deklarasi kerangka cetakan penciptaan wujud file lokal berlabel nama 'rahasiatiss.db' jika penyimpanannya terbukti absen dari direktori!)
const db = new sqlite3.Database('./rahasiatiss.db');

// Rangkaian sandi deklarasi sirkulasi penyelarasan pengeksekusian pengikatan rentetan kueri secara runut beruntun (serialize)
db.serialize(() => {
 // Bangun Tabel data operasional payload db.run("CREATE TABLE IF NOT EXISTS pasukan (info TEXT)");

 // Suntik operasi rute memuat muatan array sisipan referensi payload (Parameterized Query / Prepared Statement)
 const pelatukInsersi = db.prepare("INSERT INTO pasukan VALUES (?)");
 pelatukInsersi.run("Anggota Tim Validasi");
 pelatukInsersi.run("Anggota Tim Auditor Jaringan");
 pelatukInsersi.finalize(); // Mengakhiri/meringkus pemicu sirkuit memori operasional Statement peluncur fungsi injeksi data memori RAM peladen

 // Mengekstraksi fungsi pelaporan rekam log lantas Tampilkan hasil sulingan muatan di layar tampilan konsol penampang output peladen Node
 db.each("SELECT rowid AS id, info FROM pasukan", (err, hasilData) => {
 console.log(`[LAPORAN REKAMAN EKSTRAKSI DATA BARIS SQLITE] ID Payload: ${hasilData.id} -> ${hasilData.info}`);
 });
});

// Menutup gerbang parameter pembukaan aliran sambungan komunikasi peladen ke memori database agar efisiensi terawat!
db.close();
```
5. Eksekusi penggerak lajur instruksi operasi terminal peladenmu: `node induk.js`
6. Penampang tampilan layarmu seketika niscaya menampilkan dan mendisplai log deretan umpan pelaporan payload balasan spesifik hasil pengolahan penyuntingan rekaman baris penulisan tabel di piringan Database SQLite lokal (*rahasiatiss.db* diproduksi, diisi tabel lantas dikueri dengan sempurna oleh Node)!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Ketika skrip antarmuka aplikasi operasional *Node.js Backend* menuntut pendelegasian otoritas untuk merilis pembukaan koneksi pertukaran perintah kueri menyambangi arsitektur pintu penyimpanan memori SQL (*SQL Database System*), modul peranti khusus berwujud apakah (yang lazim ditebus diinstal dari repositori bursa penyedia pasokan pusat perpustakaan peladen *NPM*) yang menduduki esensi jabatan guna menjembatani sarana transmisi jalur perintah komunikasi integrasi lintas antar kedua sistem arsitektur tersebut?</summary>

**Jawaban:** integrasi penyediaan jembatan ekstensi *Driver Database* (alias Pustaka *Database Connector Module*, misal referensi peranti pustaka fungsi arsitektur instalasi `sqlite3`, perantara driver logik koneksi perutean pustaka antarmuka `pg` untuk relasi pertautan integrasi pengolahan memori *PostgreSQL Engine Database Server*, atau modul pengaitan jembatan parameter eksekutor *Driver Application Node Programming Module Interface Data Fetching Connection Database Socket Interface Network Parameter Client MySQL Protocol Logic MySQL Module Adapter Logic SQL Database Backend MySQL Library Protocol Binding Database Connector* `mysql2`).
</details>

<details>
<summary>❓ Pasca pundi-pundi kumpulan parameter data peladen *SQL Database Engine Storage* memproses pengerjaan dan mengekstrak balasan tuntas untuk menanggapi pengikatan eksekusi kueri antarmuka instruksional pencarian data dari Node `SELECT`, wujud struktur abstraksi pengelompokan format pemetaan pengenalan data bawaan (secara konseptual pemrograman operasional *native data struct type* di mesin) berjenis apa yang niscaya sukses dihidangkan dikonversi mendarat ke variabel referensi tangkapan payload kembalian memori logik pelaksana fungsi peramban modul eksekutor *Driver Javascript Node*?</summary>

**Jawaban:** Transformasi data SQL ke bahasa Node (berwujud koleksi parameter pengelompokan struktur data) senantiasa secara standar dideklarasikan ke bentuk format himpunan berjenis ***Array of Objects*** (Di mana tiap objek JS tersebut merepresentasikan parameter pengikatan spesifik utuh atas satu *record* jejak rincian sel rekaman pelaporan spesifik di pelataran baris lajur fungsi kolom tabel).
</details>

<details>
<summary>❓ Apa padanan dari penamaan akronim logik operasional integrasi sirkulasi komponen arsitektur peladen berlabel *ORM*, di mana struktur *ORM* ini dihajatkan fungsinya secara spesifik menimpa kelamnya sintaks perutean penulisan penyusunan argumen kueri fungsi SQL statis untuk berganti wajah beralih fungsi direpresentasikan menjadi lapisan perumusan logika pemrograman elegan orientasi objek di sisi ekosistem perakitan modul proyek pemrograman peladen Backend mutakhir?</summary>

**Jawaban:** Konsep integrasi parameter objek perantara fungsionalitas tersebut merujuk pada pengalamatan identifikasi payload *ORM* merupakan sandi penyingkatan arsitektur dari penyusutan terma arsitektur klasifikasi antarmuka fungsi: **Object-Relational Mapping (ORM)**.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami relasi esensial fungsi logik peran instalasi dependensi perantara *Database Driver* yang menjembatani konversi instruksi interupsi lintas peladen SQL. 
- [ ] Saya sukses menguji serangan eksekusi *Request Payload Server Application Architecture System Execution Endpoint Connection Driver DB Driver Storage DB Initialization Command SQLite Architecture Parameter Command SQLite Driver Architecture Fetch Request Initialization* pada fungsi ekstraksi sintaks penelusuran ekstrak barisan operasional aplikasi perantara eksekutor pustaka fungsi komando instalasi log instalasi *NPM sqlite3 Module Node Middleware JS Syntax Database Configuration System SQLite Architecture Binding API Controller Node* dari *Node CLI*.
- [ ] Saya meninjau penjabaran ringkas perihal konsep perumusan struktur lapisan kerangka abstraksi relasi *ORM (Object-Relational Mapping Framework)*.
- [ ] Saya kelar menuntaskan rekam log instalasi modul eksekutor memori pemetaan rekam memori operasional database tabel *DB Engine Storage Engine SQL Data Creation Insertion Persistence Command Binding Initialization Module SQL Driver Query Result Binding Initialization Memory* parameter memori *SQLite DB Configuration Logic* dalam pengerjaan *Mini Lab Node-SQL*.
- [ ] Saya menyelesaikan pendalaman kaji ulas pendalaman arsitektur konsep penguasaan logik harian di pengujian evaluasi peramban singkat (*Quiz Kilat*).

---

## 🔗 Resources

- [NPM: sqlite3 Documentation](https://www.npmjs.com/package/sqlite3) — Dokumentasi ekstensif sah resmi penyediaan integrasi peramban operasional konfigurasi penataan instruksi *Node HTTP SQL Driver System Setup Network SQL Library Database Database API Query Binding SQLite Package Initialization Configuration Guide Application Syntax API Documentation* memfasilitasi parameter instalasi lajur pemanggilan sinkronis / asinkronis di dalam operasi paket pustaka log dependensi API pustaka `sqlite3`.
- [Prisma ORM Intro](https://www.prisma.io/) — (Pembacaan Alternatif Eksternal Opsional) Tilik serta selami arsitektur penulisan integrasi lapisan konseptual paras abstraksi kerangka *Software Database Relational Abstraction Mapping Software Framework Configuration Software Backend Logic Data Parameter Abstraction Library System Backend Infrastructure Abstraction API Software Model Data Architecture Middleware ORM Type Persistence Abstraction ORM Architecture Library Persistence Mapping System Backend Tool Developer System API* (Pustaka ORM) tersohor dan sangat modern implementasinya di berbagai *stack* proyek korporat rekayasa industri terkini.

---

## ➡️ Besok

**Day 4: Authentication & Password Security** — integrasi relasi penyimpanan payload tabel database arsip pengingat berhasil tuntas dirakit operasionalnya! Di eksekusi harian esok, tantangan pengikatan keamanan fungsionalitas perutean bakal membentang mendesak dituntaskan arsitekturnya. Kita menugaskan penyusunan parameter rekayasa proteksi operasi kontrol log peramban log perisai pengawasan fungsionalitas integrasi peladen (*Application Authentication System Request Control Endpoint Firewall Endpoint Parameter Web App Protection Authorization Layer Role Web Software Authorization App Web Interface Verification Auth Logic Logic*). Kita membedah dua varian mekanisme otorisasi perutean: Sistem *Session-based Memory Login Verification* eksekutor server log dan kerangka sistem modern antarmuka jaringan payload log fungsi identitas nir-status klien token API pertukaran parameter eksekutor *JWT Session ID API Parameter Application Security Verification Network Interface JWT Token Authorization Endpoint Server Backend Web App JWT Logic*. Tak tertinggal, merajut kelengkapan fitur pengerjaan parameter persandian perlindungan otentik lebur kriptografis cincang (*Hashing*) algoritma modul pertahanan memori pengaman peladen perutean sandi enkripsi rute jaringan arsitektur *Node Password Cipher Hashing Library Bcrypt API Configuration Application Hash Software Crypto Hashing Security*!

---

*📅 TISS Null Teaming · Week 13 · Day 3 · FORGE Rank*
