# 💀 Week 16 · Day 2: SQL Injection Blind (Boolean & Time)

> **Rank**: BREACH | **Minggu ke-16**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 16 · Day 2/5 | BREACH Rank (Minggu 2 dari 5) | Overall: 77/120 hari (64%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** karakteristik respons peretasan *SQL Injection UNION-based* dengan klasifikasi taktik operasi ekskavasi *Blind SQLi*.
2. **Mengeksploitasi** arsitektur *database* yang memblokir pencetakan layar menggunakan taktik evaluasi iteratif inferensi logika arsitektur kebenaran *Boolean-based Blind*.
3. **Mengekstrak** rahasia data payload peladen target lewat paksaan injeksi sandi peredaman perlambatan jeda (*Time-based Blind SQLi*).

---

## 📖 Materi Inti

### Meretas Dalam Kegelapan (Blind SQLi)

Berbeda dengan eksekusi vektor serangan arsitektur peladen *UNION-based* yang secara transparan memuntahkan payload ekstraksi pembongkaran arsip pelaporan basis *database* utuh ke paras layar visual antarmuka web orisinal, peladen aplikasi kerap dikonfigurasi untuk meredam respons sehingga arsitektur situs **TIDAK MENCETAK INDIKATOR APAPUN** meski dihajar rentetan percobaan eksploitasi parameter peretasan modifikasi sandi kueri *SQLi* penganalisis penyerang. 
Situs akan menolak membeberkan tampilan paparan galat pelaporan *Syntax Error*, namun di waktu bersaman peladen sasaran aplikasi juga meredam dan secara mutlak memblokir eksistensi parameter eksekutor fungsi pelaporan payload paparan tabel sandi rahasia basis data yang dicuri tebakan penyerang; menjadikannya sekadar meladeni interaksi dengan wujud menyuguhkan paras respons halaman peramban kosong konvensional biasa atau merespons pelaporan respons parameter standar *HTTP 200/500* semata.

Inilah konseptual implementasi taktik penetrasi arsitektur yang didefinisikan sebagai penetrasi klasifikasi **Blind SQL Injection (Injeksi Buta)**. Anda meluncurkan transmisi eksekusi injeksi kueri operasi, lantas pelaporan respons antarmukanya ditahan membisu sehingga Anda *buta* terhadap validasi hasil payload sandi temuan data spesifiknya di layar. Lantas, metodologi eksploitatif arsitektur apakah yang lantas diterapkan penganalisis guna mengekstraksi parameter rahasia dari instalasi peladen arsitektur peladen yang ditugaskan membisu di layar pelaporan peramban tersebut?
Penyelesaian arsitektur luringnya: **Mengadopsi ekskavasi inferensi logika berbekal penerapan taktik evaluasi parameter pengujian kueri pertanyaan Inferensi (Memaksa Peladen Menjawab Ya/Tidak lewat Perilaku).**

### 1. Boolean-based Blind (Evaluasi Sinyal Benar/Salah)

Alih-alih menugaskan sandi komando fungsi guna menyedot menguras isi tabel peladen sasaran payload secara masif utuh memborong langsung, *hacker* penganalisis beradaptasi memutar haluan lantas memformulasikan pelemparan tebakan algoritma sandi peretasan evaluasi pengindeksan payload ekstraksi secara meraba pelaporan karakter sandi target *huruf demi huruf*.
Asumsikan parameter URL rentan peladen target diidentifikasi penganalisis: `toko.com/produk?id=1`
Hacker mengirimkan sisipan peluncuran modifikasi kueri operasi parameter boolean penugasan evaluasi sandi :
`toko.com/produk?id=1' AND (SELECT substring(password,1,1) FROM users WHERE username='admin') = 'a' --`

*(Representasi translasi nalar komando kueri tersebut bermakna: "Instruksi kepada Database Peladen : Berikan pelayanan render menampilkan antarmuka data Produk ID 1 JIKA DAN HANYA JIKA huruf pengindeksan karakter sandi yang berada pada posisi peramban pertama sandi otentikasi login admin situs adalah abjad fungsi nilai 'a'.")*

Jika peramban arsitektur layar antarmuka halaman web produk tersebut lantas dicetak **MUNCUL** tampil secara wujud operasi peramban normal, berarti sistem evaluasi boolean peladen di belakang menyatakan logika tebakan huruf 'a' itu divalidasi kebenaran sibernya sehingga menghasilkan sinyal eksekusi **BENAR (TRUE / YA)**.
Jika paras layar peramban halaman web situs tersebut tiba-tiba hilang melenyapkan wujud konten komputasinya (**KOSONG/HILANG/HTTP ERROR/404**), berarti evaluasi parameter fungsi database menyatakan tebakannya **SALAH (FALSE / TIDAK)**.
Dengan bermodalkan kegigihan meluncurkan operasi tebakan iterasi meraba tebakan pengindeksan peramban sasaran hingga hitungan frekuensi yang dituntut menyentuh skala repetisi iterasi kalkulasi berjuta kali tebakan uji arsitektur sandi, penganalisis eksploitasi sasaran akhirnya mendulang pencapaian merangkai kepingan demi kepingan abjad sandi admin parameter rahasia arsitektur peladen tersebut tanpa membutuhkan secarik pun balasan layar ekskavasi peramban data secara harafiah!

### 2. Time-based Blind (Sinyal Deteksi Jeda Durasi Waktu)

Adakalanya instalasi parameter peladen meredam tuntas gelagat arsitektur pembacaan peramban sehingga parameter situs senantiasa direkayasa sekeras mungkin untuk menampilkan wujud pelaporan respons statis peramban aplikasi (*normal page rendering*) pada layar secara ajeg absolut dan persisten, baik ketika dibombardir lantas dijejali operasi parameter *Boolean* peretasan indikator respons fungsi kebenaran parameter *TRUE*, maupun ketika penganalisis membenturkannya ke kalkulasi respons boolean hampa nilai penugasan sandi pelaporan *FALSE*. Tidak ditemukan satu pun indikasi pembeda diferensiasi wujud rekam arsitektur diferensiasi perbandingan layar web visual pada kedua percobaan hasil pelaporan tebakan boolean penganalisis eksploitasi kueri tersebut.
Maka spesialis penganalisis penyerang mengadopsi pengerahan taktik pemungkas memanipulasi rentang kalkulasi kalkulasi batas dimensi waktu durasi eksekutor : **Memaksa penugasan peramban pembekuan *Delay Execution* agar peladen menunda eksekusi penyelesaian nafas peramban proses respons rendering lamannya! (Taktik metode Injeksi *Time-based Blind*).**

Hacker meluncurkan percobaan serangan:
`id=1' AND IF((SELECT substring(password,1,1) FROM users)='a', SLEEP(10), 0) --`

*(Representasi parameter nalar luringnya diartikan: "Apabila tebakan huruf karakter peramban indeks baris sandi sasaran admin sasaran yang pertama divalidasi kebenaran databasenya terkonfirmasi sama dengan abjad fungsi pelaporan 'a', maka BERHENTILAH lantas laksanakan fungsi pembekuan jeda penundaan pelayanan BEKERJA SELAMA SETIDAKNYA DURASI 10 DETIK. Jika kueri tebakan ini dikalkulasikan parameter salah (FALSE), maka terus jalankan fungsi respons eksekusi normal peladen tanpa penahanan sesaat pun.")*

Jika *Loading Browser* penganalisis tiba-tiba menahan rendering layar dan terjeda *muter-muter lambat* lantas menuntut alokasi waktu persis minimal setidaknya *10 detik* sebelum pada akhirnya menuntaskan perenderan penayangan paparan antarmuka operasi halaman layarnya, penganalisis murni sukses mendapati indikasi pembuktian konfirmasi bahwasanya ia sukses dan valid menebak parameter sandi admin diawali huruf 'a'—sebuah deduksi yang diperoleh mutlak semata-mata mengacu dari identifikasi observasi gelagat perlambatan respons durasi kalkulasi jeda waktu bernapas mesin peladen!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan kekuatan serangan parameter pembuktian muatan kueri *Blind SQLi* via modifikasi ekstensi sandi Cookie peramban!

1. Kunjungi lingkungan lab arsitektur kompetisi sasaran pengujian *PortSwigger: Blind SQL Injection*.
2. Asumsikan Anda bertugas menelusuri penemuan payload parameter kelemahan kerentanan di komponen variabel pencatatan antarmuka *Cookie TrackingId=xyz* sebuah aplikasi sasaran.
3. Anda diagendakan menguji pelacakan hipotesis ihwal apakah kueri basis data pengawalan payload komponen parameter pengikatan identitas payload tersebut dapat dieksploitasi kerentanannya terhadap peluncuran percobaan eksekusi manipulasi uji penahanan jeda waktu (*Time-based*).
4. Anda menyeludupkan serangan modifikasi peramban parameter struktur pengikatan kueri muatan pada komponen payload pelacakan cookie-nya direkayasa sandinya dimodifikasi formulasinya menjadi pelaporan injeksi parameter muatan kueri `TrackingId=xyz' || pg_sleep(10)--` *(Keterangan : penggunaan payload parameter instruksional pg_sleep() lazimnya dikhususkan bagi deteksi kerentanan arsitektur sandi PostgreSQL).*
5. Anda menginisiasi pengujian dengan menekan payload instruksional eksekutor parameter *Refresh* halaman. Laman peramban antarmuka seketika bengong macet memuat merender halaman pelaporan respons peladen secara presisi tepat tertahan operasionalnya melampaui kalkulasi hitungan *10 detik* lamanya.
6. Itu merupakan konfirmasi pembuktian validasi pelaporan sah bahwasanya peladen instalasi sasar basis data pelaporan di balik tirai memproses kueri Anda lantas murni mengamini kelemahan parameternya untuk dieksploitasi *Blind*!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah parameter klasifikasi konseptual peretasan arsitektur <i>Blind SQL Injection</i>, batasan struktural fisik respons peladen apa yang mendefinisikan pemisahan taktik tebakan eksploitasi parameter pelaporan ini bilamana parameter metodenya dipersandingkan melirik arsitektur kerentanan sasaran taktik <i>UNION-based SQLi</i>?</summary>

**Jawaban:** Pada taktik parameter operasi <i>UNION</i>, payload sandi ekstraksi curian dokumen arsip rahasia peladen (seperti isi pengungkapan pengindeksan parameter password target sasar) dimuntahkan diekstraksi ke antarmuka aplikasi sasaran secara komprehensif lantas tercetak dibeberkan memapar di layar paras depan Web. Sebaliknya, pada simulasi operasi pelacakan *Blind SQLi*, parameter server sasaran arsitektur sistem aplikasi target situs mutlak dikutuk pengamanannya menjadi meredam pencetakan informasi alias membisu (tidak mengekstraksi dan nihil mencetak data arsip rahasia apapun pada antarmuka / dan tidak akan mengaktifkan fungsi *Syntax Error*). Spesialis pentester dipaksa untuk mengekstraksi keberhasilan penemuan data sasaran semata-mata dengan merujuk pengumpulan via metode mengamati observasi respons gelagat sinyal pembacaan perbedaan respons sistem server sasaran aplikasi target antarmuka (memantau gejala payload operasi apakah layar hilang/tampil render *Boolean*, atau mengukur apakah layar mengalami durasi *loading* melambat *Time-based*).
</details>

<details>
<summary>❓ Ketika spesialis arsitektur peretasan meluncurkan pelaporan fungsi eksekusi eksploitasi peramban serangan serangan kueri klasifikasi tipe penganalisis operasi tipe tebakan arsitektur <i>Boolean-based Blind</i>, taktik matematis parameter evaluasi apakah yang ditunggangi <i>hacker</i> guna membedah dan lantas mendeduksi menerawang evaluasi fungsi tebakan ekstraksi pengindeksan wujud parameter rahasia pelaporan sandi instalasi peladen sasar target aplikasi web?</summary>

**Jawaban:** Hacker mengerahkan rentetan peluncuran analisis berfokus merumuskan serangan pertanyaan perumusan uji tebakan inferensi validasi logika matematis penentuan fungsi respons Boolean *TRUE/FALSE* satu per satu abjad huruf sandi (contoh evaluasi kueri pelacakan: apakah huruf pengindeksan peramban pertama sandi peladen target sasaran adalah 'a'?). Bilamana situs web sasaran fungsi target menanggapi tebakan peramban kueri percobaan penyerang tersebut dengan respons merender tampilan paras layar halamannya dengan wujud visual utuh konfigurasi standar normal, maka parameter tersebut mewakili respons pembuktian konfirmasi pelaporan sinyal sakti bahwasanya deduksi tebakan abjad tersebut adalah sah *TRUE (Benar)* keberadaan pengindeksan arsip arsitekturnya di database.
</details>

<details>
<summary>❓ Di ranah pembajakan operasi pelaporan penugasan arsitektur parameter <i>Time-based Blind SQLi</i>, serpihan fungsi deklarasi instruksional komando parameter jenis perintah apalah yang disuntikkan penganalisis ke peramban payload rahim SQL peladen demi menyediakan pembuktian konfirmasi kebenaran deduksi iterasi tebakan <i>hacker</i>?</summary>

**Jawaban:** Menginjeksi Fungsi operasi sandi parameter sandi instruksional fungsi peladen penjeda peramban kompilasi eksekutor, semacam penerapan payload deklarasi perintah operasi sandi parameter menunda durasi penugasan fungsi fungsi *SLEEP()* atau sandi *pg_sleep()*. (Tebakan parameter penganalisis penyerang yang secara struktural divalidasi dinilai benar akan otomatis memicu peladen menuruti titah fungsi instruksional sasaran pelaporan penahanan eksekusi bernapas / menyebabkan perenderan *loading* laman peramban antarmuka sasaran dipaksa mengalami durasi kelambatan waktu spesifik).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap arsitektur kesadaran deduksi ekstraksi sandi pada peladen bisu (*Blind SQLi*)
- [ ] Saya fasih menjabarkan mekanisme pembuktian sinyal respons parameter *Boolean-based Blind*
- [ ] Saya menguasai titah sintaks eksploitasi parameter penundaan respons peladen *Time-based Blind*
- [ ] Saya mengerti hambatan ihwal mengapa ekstraksi eksploitasi *Blind SQLi* dituntut kalkulasi waktu jauh lebih menahun bilamana dipersandingkan kecepatan kurasan ekstraksi pembongkaran instalasi arsitektur kueri *UNION*
- [ ] Saya mengulas jawaban pelaporan perumusan *Quiz Kilat* dengan penyerapan representatif

---

## 🔗 Resources

- [PortSwigger Blind SQLi](https://portswigger.net/web-security/sql-injection/blind) — Panduan referensi komprehensif mengkaji metode ekskavasi celah pada sistem peladen berkarakteristik meredam *verbosity*.

---

## ➡️ Besok

**Day 3: SQLMap (Automated Exploitation)** — Mengekstraksi struktur letak rahasia kata sandi sasaran menggunakan rutinitas eksploitasi evaluasi parameter peramban iterasi peretasan manual jenis *Blind SQLi* bermodalkan pendekatan tebakan kalkulasi parameter indeks pencocokan arsip karakter abjad per abjad arsitektur secara *manual* memboroskan esensi manajemen waktu krusial penganalisis industri. Esok hari, penganalisis akan menonaktifkan tahapan penugasan eksploitasi manual berdurasi kronis lantas mengadopsi kekuatan instalasi peramban perkakas mutakhir ekstraksi penarikan arsitektur penyedot peramban payload database sasaran terbesar di jajaran persenjataan otomatis profesional pelaporan : peramban instalasi otomasi **SQLMap**!

---

*📅 TISS Null Teaming · Week 16 · Day 2 · BREACH Rank*
