# 💀 Week 16 · Day 4: Authentication Bypass

> **Rank**: BREACH | **Minggu ke-16**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 16 · Day 4/5 | BREACH Rank (Minggu 2 dari 5) | Overall: 79/120 hari (66%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** batasan parameter antara serangan berbasis ekstraksi *SQLi* dibandingkan serangan penelikungan gerbang Otorisasi (*Authentication Bypass*).
2. **Mensimulasikan** taktik iterasi serangan tebakan parameter sandi masif (*Brute Force* & klasifikasi peretasan *Credential Stuffing*).
3. **Mengeksploitasi** kelalaian logika pemrograman arsitektur dalam memitigasi perlindungan kalung token sertifikat Sesi pengguna (*Session Attacks*).

---

## 📖 Materi Inti

### Mendobrak Gerbang Tanpa Modifikasi Kueri SQL (Auth Bypass)

Meskipun kerentanan Injeksi SQL pada peladen sasaran telah dimitigasi secara komprehensif (misalnya melalui adopsi *Parameterized Queries* seperti modul di *Forge Rank*), keamanan arsitektur aplikasi belum terjamin utuh mutlak seratus persen. Kelalaian logika implementasi pengembang peladen dalam menyusun validasi arsitektur sistem pengamanan **Otentikasi (Authentication)** kerap kali menyediakan payload letak celah kerentanan vektor serangan eksploitasi yang esensinya sama krusial dan fatalnya di mata penganalisis target peretas.

*Authentication Bypass* (Penelikungan/Bypass Otentikasi) merupakan kategori klasifikasi kerentanan ketika entitas penganalisis peretas berhasil eskalasi penetrasi meretas antarmuka validasi *Login* (memasuki panel akun pengguna sasaran atau mengambil alih otoritas Administrator) secara mutlak tanpa memvalidasi atau memegang payload input informasi parameter kredensial sandi otentik yang benar, melainkan semata-mata diinisiasi dengan cara memanipulasi serta mengeksploitasi kelalaian logika pemrograman peladen sasaran sasarannya.

### 1. Serangan Manuver Ekstraksi Sandi (Brute Force & Credential Stuffing)

Bila antarmuka instalasi aplikasi target **TIDAK MENGIMPLEMENTASIKAN PEMBATASAN KUERI ITERATIF** (sebagai contoh mutlak ditandai dengan nihilnya parameter proteksi semacam *Rate Limiting* batas log maupun tidak dioperasikannya mekanisme perlindungan verifikasi pengguna integrasi keamanan *CAPTCHA*), pentester dengan leluasa dapat letupan peluncuran eksekutor instalasi alat penetrasi otomasi peretasan (seperti *Hydra* atau penugasan modul *Burp Suite Intruder*) guna mengebom mengirimkan parameter antarmuka *Login* sasaran dengan percobaan iterasi kalkulasi repetitif ratusan hingga jutaan letupan tebakan kata sandi beruntun per detik bermodalkan kompilasi kamus daftar penugasan referensi tebakan umum (*Wordlists* arsip semacam pelaporan fail ekskavasi payload `rockyou.txt`).

- **Brute Force:** Mengeksekusi pengeboman kalkulasi probabilitas meraba 1 nama pengguna tunggal (misal `admin`) dikombinasikan dengan meluncurkan transmisi pengiriman iterasi beruntun tebakan jutaan variasi parameter sandi umum (contoh: kompilasi tebakan sandi `'123456'`, `'password'`, atau instalasi sandi `'admin123'`).
- **Credential Stuffing (Daur Ulang Arsip Kebocoran Lawas):** 
Penganalisis manuver taktis peretasan dengan cara memanfaatkan ketersediaan logika daftar perakitan kombinasi eksistensi parameter pasangan otentik sandi *email* dan rekaman kata sandi yang valid terekstrak dari hasil insiden kebocoran arsitektur data situs layanan publik pihak ketiga di masa lampau, lantas spesialis peretas menginisiasi simulasi mendaur ulangnya dengan menguji transmisi interaksi integrasi payload kredensial sandi spesifik tersebut secara otomatis ke antarmuka gerbang otentikasi situs sasaran peretasan aplikasi yang terpisah dan mutlak tidak berkaitan. (Taktik ini terbukti sangat krusial dan secara mematikan lantaran sasaran penganalisis mengeksploitasi fenomena kelalaian kebiasaan repetisi penggunaan variasi parameter sandi yang identik oleh mayoritas populasi pemilik antarmuka akun di berbagai arsitektur layanan web di bumi internet!).

### 2. Membajak Pengikatan Otentikasi Sandi Sesi (Session Hijacking & Fixation)

Pasca peramban seorang pengguna sah berhasil tervalidasi eksekusi login, peladen aplikasi web bakal menerbitkan sertifikat penanda otentikasi (semacam *Session Cookie* atau pencetakan token otorisasi parameter JWT). Jikalau antarmuka peramban klien terus-menerus melampirkan payload *Cookie* tersebut, maka peladen sasaran mengamini dan menganggap sesi akses penggunanya tetap berstatus masuk (terautentikasi) utuh tanpa dituntut parameter rutinitas peretasan login ulang manual.

Titik arsitektur kelalaian kerentanan pemrogram aplikasi:
- **Konfigurasi Sesi yang Dapat Diprediksi:** Mengonfigurasi pencetakan identitas Token Sesi yang berstruktur nilai statis dan persisten sehingga rentan ditebak secara iteratif! (Misal struktur pencatatan nama nilai `Cookie`: `session_id=admin_1`. Parameter sasaran tersebut teramat rentan diprediksi dan dimodifikasi spesialis penganalisis peretas diubah eskalasinya secara sepihak ke nilai parameter payload sandi `admin_2`).
- **Session Fixation:** Penyerang parameter memanipulasi taktik operasi penipuan psikologis untuk menjebak korban mangsa agar mengeklik payload instruksional tautan peramban pancingan peladen sasaran yang diam-diam telah sengaja memuat injeksi parameter sandi otentikasi fungsi *Cookie* bawaan spesifik modifikasi racikan penyerang. Niscaya berakibat krusial ketika pasca sasaran korban murni tersebut sukses tervalidasi mengeksekusi otentikasi *Login* aplikasinya, identitas login otorisasi admin komputasinya seketika dirampas karena secara utuh sandi luringnya terikat mutlak menyatu pada payload parameter fungsi kalung sesi peramban identitas *Cookie* sandi yang telah sedari awal dikendalikan secara mutlak penyerang di seberang!

### 3. Celah Logika Pengangkatan Paksa Parameter (Forced Browsing / Parameter Tampering)

Terkadang instalasi arsitektur aplikasi kerentanan suatu situs gerbang depan (*Login*) dirakit teramat tangguh, namun titik parameter kerentanan kelalaian justru direpresentasikan telanjang eksploitasi letak di balik panel antarmuka autentikasi sasaran! (Konseptual peretasan turunan dari pemanfaatan metodologi *IDOR / Broken Access Control*). Peretas menginisiasi akses pelaporan peramban masuk autentik dengan payload sebagai wujud otentikasi peramban *User Biasa*, lantas ia menyisipkan fungsi modifikasi mencegat pencatatan pertukaran parameter transkripsi bodi pengikatan *HTTP request*, menginterupsi lalu secara sepihak mengganti dan memodifikasi rekaman payload penanda atribut hak sasaran peran dari payload nilai pelaporan URL fungsi `"role":"user"` dirombaknya paksa ditambal modifikasi menjadi parameter nilai sandi eskalasi `"role":"admin"`. Peladen aplikasi yang rentan (lupa memvalidasi kontrol di fungsi *backend*) lantas otomatis mengeksekusi parameter sandi pengangkatan hak otonom tingkat administrator akun tersebut!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan pengalaman meluncurkan penetrasi tebakan serangan sandi *Brute Force* mekanikal di laboratorium peramban!

1. Kunjungi pelataran arsitektur ekosistem pengujian *PortSwigger Academy: Authentication*.
2. Asumsikan Anda sedang menargetkan formulir pengikatan *Login* sasaran yang murni dirakit memaparkan kerentanan alpa ketiadaan parameter *Rate Limiting*.
3. Buka peranti payload penganalisis *Burp Suite* (komponen detail fungsi pengujian penganalisis perangkat instruksional ini akan dikupas mendalam kelak pada silabus peretasan *Minggu 18*), lantas operkan tangkapan parameter kueri interaksi jaringan rekaman *Request Login* tersebut untuk dikonfigurasi ke rahim sandi eksekutor sandi *Burp Intruder*.
4. Pasang letak instruksi peramban penanda sasaran target eksekusi iterasi di letak kotak barisan isian parameter nilai kata sandi: pelaporan instruksional modifikasi `password=§FUZZ§`
5. Muat daftar dokumen parameter teks kamus tebakan referensi wordlist arsitektur memuat iterasi barisan rentetan sandi kebocoran. Letuskan fungsi pemicu tombol eksekusi serangan serangan peramban *Start Attack*!
6. Amati rentetan pencetakan pelaporan parameter pelaporan payload serangan. Hampir seluruh serangan merender pencetakan laporan kode balasan ralat konvensional *HTTP 200 OK* (yang di lab ini mengindikasikan fungsi penolakan *Gagal Login*, dibuktikan dengan pengukuran hitungan ukuran panjang parameter karakter halaman peramban yang berkapasitas dimensi kecil). Namun bakal tercetak paparan SEBUAH instruksi serangan sandi pelaporan yang melesatkan respons penandaan nilai pengikatan arsitektur sandi kode *HTTP 302 Found / Redirect* (Parameter bukti konfirmasi Dialihkan sukses masuk akses)! Anda mutlak berhasil mendobrak peretasan gerbang login sasaran bermodalkan pengujian kegigihan letupan tebakan repetitif percobaan payload otentikasi!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah anatomi klasifikasi definisi letak pembeda strategi pelacakan pendobrakan otentikasi login, apa definisi konseptual pembeda krusial taktik ekskavasi arsitektur <i>Credential Stuffing</i> jikalau diadu silang dibandingkan serangan eksploitasi peretasan membabi-buta acak iterasi tebakan jenis taktik parameter sasaran pengujian <i>Brute Force</i> biasa konvensional ?</summary>

**Jawaban:** Pada taktik parameter *Brute Force*, agen spesialis penganalisis mengirimkan letupan serangan kalkulasi sandi tebakan otentikasi kombinasi tebakan secara membabi-buta atau tebakan buta acak parameter (semata mengandalkan kalkulasi pelaporan probabilitas acak kombinasi tebakan umum matematis dari referensi *wordlist*). Sebaliknya, pada taktik eksploitasi parameter operasi peretasan *Credential Stuffing*, penganalisis penyerang dipersenjatai modal otentik daftar arsip data nyata kombinasi pasangan eksistensi *Email & Kata Sandi* orisinal yang berstatus divalidasi pernah terekstrak mutlak dari rekam jejak ekskavasi parameter kebocoran arsip situs pihak ketiga web eksternal massa lampau (sebagai contoh daftar pengikatan akun kebocoran situs web *Yahoo*), lantas spesialis peretas menginisiasi eksploitasi simulasi mendaur-ulangnya payload tersebut untuk digunakan mencoba mendobrak akses gerbang otentikasi web aplikasi sasaran target operasi yang sepenuhnya terpisah dengan landasan eksploitasi asumsi bahwa si pengguna korban niscaya cenderung terlalu malas dan lalai dalam mengubah variasi pengaturan rekaman pemakaian sandi yang identik tersebut.
</details>

<details>
<summary>❓ Ketika spesialis *Hacker* menyisipkan peramban modifikasi mencegat paket kiriman lalu lintas arsitektur *HTTP Request* peladen sasar (via *Intercept*), lantas penganalisis diam-diam memodifikasi lantas menggubah mencatatkan penyesuaian utusan modifikasi parameter sandi bodi pelaporan atribut payload pengenal pengikatan atribut *role=user* lantas di-edit secara paksa sandi di-edit silang dimanipulasi peramban dirombak sandinya menjadi parameter ekskalasi hak akses sandi *role=admin*, kerentanan kategori klasifikasi arsitektur peretasan operasi tipe peretasan jenis jenis apakah yang dipraktikkan eksploitasinya oleh penganalisis tersebut?</summary>

**Jawaban:** Parameter Tampering (atau eskalasi manuver klasifikasi ekskavasi kerentanan aplikasi *Privilege Escalation*).
</details>

<details>
<summary>❓ Identifikasikan nama nomenklatur klasifikasi kelalaian peramban arsitektur konfigurasi parameter pengamanan lapis peladen situs web apa yang sejatinya melonggarkan perizinan lantas melegalkan dibiarkannya akses pintu antarmuka otentikasi login aplikasi sasaran tersebut dieksekusi secara bebas sehingga situs sasar dirongrong payload eksploitasi serangan tebakan ratusan hingga frekuensi jutaan bot transmisi pelaporan tebakan *Brute Force* peramban detik tanpa adanya penahanan?</summary>

**Jawaban:** Ketiadaan pembatasan kecepatan pertukaran kueri transmisi arsitektur pembatasan fungsi parameter jaring perlindungan *Rate Limiting* (atau tidak dilengkapinya fungsi proteksi pengamanan pendeteksian pengujian validasi parameter CAPTCHA pada formulir sasaran).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap pengetahuan teknis identifikasi pembeda batasan operasi penembusan *SQL Injection* dibandingkan klasifikasi parameter *Authentication Bypass*
- [ ] Saya fasih membelah beda klasifikasi silang batasan konseptual arsitektur peretasan *Brute Force* dibandingkan peretasan fungsi *Credential Stuffing*
- [ ] Saya tangkas menafsirkan perumusan klasifikasi manuver fungsi peretasan penyalahgunaan maling token kalung identitas parameter peladen *Session Hijacking* & fungsi *Session Fixation*
- [ ] Saya memahami bahaya laten pencurian kekuasaan manipulasi peran *Parameter Tampering* 
- [ ] Saya telah membaca lantas mengeksekusi ulasan jawaban *Quiz Kilat* dengan penyerapan perumusan memadai

---

## 🔗 Resources

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) — Dokumen lembar panduan suci yang didedikasikan merangkum perumusan merajut benteng perlindungan otentikasi sistem login sasaran (atau bagi spesialis pentester: referensi meraba letak arsitektur dokumentasi lembar cek celah peretasan merobek keamanan!).

---

## ➡️ Besok

**Day 5: Lab & Mission: PortSwigger SQLi Labs** — Usai merampungkan materi teori eksploitasi kerentanan pengujian injeksi aplikasi *SQLi UNION*, fungsi sandi iterasi *Blind SQLi*, pemetaan otomatisasi bot eksekutor *SQLMap*, hingga serangan pembongkaran merobek panel gerbang otorisasi sandi *Login Bypass*. Esok harinya, altar gelanggang pengujian simulasi peretasan retas lingkungan mesin lab basis data arsitektur web sedunia, yakni *PortSwigger*, telah bersiap sedia menyambut pengerahan peluncuran operasi manuver penganalisis Anda! Selesaikan eksekusi simulasi penyusunan kueri lab demi pelaporan eksploitasi peretasan arsitektur injeksi web tanpa menyertakan penggunaan peluncuran bot otomatis kompromi peramban, lantas ukir pencatatan laporan manuskrip dokumentasi pelaporan pengujian parameter analisis kemenangan penganalisis mencetak hasil parameter gol target!

---

*📅 TISS Null Teaming · Week 16 · Day 4 · BREACH Rank*
