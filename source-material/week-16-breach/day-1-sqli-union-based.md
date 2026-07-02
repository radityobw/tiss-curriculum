# 💀 Week 16 · Day 1: SQL Injection UNION-based

> **Rank**: BREACH | **Minggu ke-16**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 16 · Day 1/5 | BREACH Rank (Minggu 2 dari 5) | Overall: 76/120 hari (63%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** anatomi arsitektur serangan parameter aplikasi web *SQL Injection* tingkat lanjut berbasis taktik manipulasi kueri sandi `UNION`.
2. **Mengekstraksi** data rahasia silang memori parameter basis data menggunakan pendekatan analisis *Column Enumeration*.
3. **Mensimulasikan** serangan manual penarikan struktur payload arsip tabel tersembunyi secara tanpa asistensi peranti pelacak penyerang otomatis.

---

## 📖 Materi Inti

### Memasuki Ruang Pembantaian (Web Exploitation)

Minggu sebelumnya Anda telah menuntaskan tahapan pengintaian letak pemetaan celah (*Reconnaissance*). Mulai tahap ini, kita mengeksploitasi arsitektur rentan tersebut! Kita menginisiasi eksekusi melalui vektor arsitektur kerentanan peladen fundamental: **SQL Injection (SQLi)**.

Pada modul pelatihan *Forge Rank*, Anda telah mempelajari simulasi eksploitasi parameter halaman *Login* berbekal muatan iterasi injeksi logika dasar `' OR 1=1 --`. Pendekatan eksploitasi parameter itu sekadar taktik pembuka konsep awal pemula. Hari ini, Anda ditugaskan membedah teknikal eksploitasi penetrasi tingkat lanjut: **UNION-based SQL Injection**. 

### Menggabung Tabel Paksa (UNION SELECT)

Asumsikan Anda menelusuri katalog peladen toko daring. Saat memilih parameter filter "Kemeja", URL aplikasi berinteraksi menjadi respons:
`https://toko.com/produk?kategori=kemeja`

Di belakang operasi sistem, peladen basis data mengeksekusi kueri pencarian arsitektur :
`SELECT nama, harga FROM tabel_produk WHERE kategori = 'kemeja'`

Jika peladen lalai karena membiarkan payload masukan pengguna (*user input*) melintas tanpa validasi penapisan karakter tanda kutip (*sanitization*), penganalisis dapat menyeludupkan kueri operator peladen SQL *UNION*. Perintah deklarasi *UNION* di arsitektur SQL mengemban krusial perintah struktural menggabungkan (*append*) ekstraksi dua antarmuka tabel independen ke dalam satu tampilan hasil visual.

Bagaimana jika kita menyelewengkan struktur tabel *Produk* guna mengangkut lantas memaparkan tabel rahasia *Sandi Pengguna (Users)*?

Penyerang menginisiasi parameter kueri muatan pada URL:
`https://toko.com/produk?kategori=kemeja' UNION SELECT username, password FROM users --`

Kueri pada SQL peladen akan dipaksa terangkai bertumpuk menjadi konfigurasi:
`SELECT nama, harga FROM tabel_produk WHERE kategori = 'kemeja' UNION SELECT username, password FROM users --'`

Seketika, antarmuka layar peramban aplikasi web niscaya tidak lagi sebatas memajang item Kemeja, melainkan memuntahkan paparan rekaman entitas tabel rahasia yang mencakup kompilasi sandi dan parameter *Username* milik jajaran administrator sistem ke hadapan publik!

### Syarat Struktural UNION (Column Enumeration)

Metode penetrasi injeksi sandi gabungan ini memiliki restriksi peladen mutlak. Syarat eksekusi peramban parameter komando sintaks fungsi tabel `UNION` adalah: **Kueri injeksi gabungan mutlak diwajibkan mengusung jatah ukuran dimensi jumlah kolom tabel yang sejajar dan presisi identik selaras dengan tabel eksekusi laman orisinal!**

Jika tabel kueri orisinal *produk* difungsikan memanggil konfigurasi dimensi data 2 kolom (*nama*, *harga*), maka sintaks injeksi parameter tebakan tebakan spesialis mutlak harus berukuran presisi 2 kolom.

Apabila jumlah kolom kueri target tidak diketahui, *hacker* mengeksploitasinya berbasis pengaplikasian metode tebakan enumerasi iteratif evaluasi **ORDER BY** atau pengerahan kueri injeksi hampa operator *NULL Enumeration*:
`' ORDER BY 1 --` (Peramban normal merespons aman)
`' ORDER BY 2 --` (Peramban respons normal aman)
`' ORDER BY 3 --` (Memantik respons galat *Syntax ERROR!* Berarti hitungan dimensi tabel aslinya sebatas memanggil 2 balok parameter kolom).

Sesudah hitungan dimensi dikonfirmasi 2 kolom, spesialis penganalisis langsung mengirimkan parameter muatan kueri payload pencaplokan ekstrak sasaran tabel :
`' UNION SELECT null, database() --` (Mengetahui identitas nama peladen basis data)
`' UNION SELECT username, password FROM users --` (Mengekstraksi utuh arsip sandi admin peladen).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan analisis kerentanan pemetaan jumlah dimensi tabel peladen kueri secara manual!

1. Kunjungi pelataran lingkungan lab kompetisi *Bug Bounty*: [PortSwigger Academy: SQL Injection](https://portswigger.net/web-security/sql-injection).
2. Anda menargetkan sebuah modul kueri rentan. Anda mendeteksi kerentanan aplikasi peladen pada injeksi parameter fungsi sandi kueri `id=1'`.
3. Anda melacak jumlah kolom peladen via *NULL Enumeration*:
 `id=1' UNION SELECT NULL--` (Situs respons ralat parameter Error)
 `id=1' UNION SELECT NULL,NULL--` (Situs respons ralat parameter Error)
 `id=1' UNION SELECT NULL,NULL,NULL--` (Situs Tampil Normal tanpa peringatan ralat kueri!)
4. Analisis penugasan tersebut menyatakan bahwa Anda sukses mendeduksi (*Enumeration*) parameter hitungan bahwa laman web peladen itu terkonfigurasi memanggil spesifik dimensi tabel berukuran tepat *3 kolom*.
5. Langkah krusial akhir berpusat pada pengeksekusian letupan parameter serangan ekstraksi sandi: `id=1' UNION SELECT username, password, email FROM users--`!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah anatomi sintaks kueri *SQL*, apakah fungsi penugasan komando deklarasi <i>UNION</i> pada sirkulasi bahasa peramban Basis Data?</summary>

**Jawaban:** fungsi sintaks SQL `UNION` ditugaskan demi menggabungkan lantas mencaplok (*append*) dua atau lebih bentangan layar pemaparan hasil tabel independen peramban kueri `SELECT` peladen (yang tidak terkait satu sama lain) ke dalam satu parameter antarmuka hasil laporan baris struktur visual tunggal (*Result Set*).
</details>

<details>
<summary>❓ Ketika meluncurkan serangan eksploitasi serangan kueri tingkat mahaguru tipe parameter serangan *UNION-based SQLi*, syarat fisik macam apa yang mutlak tidak boleh dilanggar pentester agar penugasan komando arsitektur kueri tabel gabungan *SQL* yang disisipkan tersebut tidak berakhir menabrak dan membenturkan peringatan deteksi ralat arsitektur respons *Syntax Error* peladen?</summary>

**Jawaban:** Formulasi injeksi tabel sisipan peretasan ekstensi (hasil deklarasi gabungan parameter kueri injeksi sasaran `UNION SELECT` milik penganalisis penyerang) dipastikan mutlak untuk pengaturan arsitektur parameter jatah hitungan dimensi kesetaraan **jumlah pemanggilan kolom yang presisi identik ukurannya** selaras meniru hasil keluaran ukuran cetakan baris tabel `SELECT` laman orisinal peladen target sasaran.
</details>

<details>
<summary>❓ Demi meraba-raba (*Enumeration*) kegelapan hitungan konfigurasi parameter sasaran penugasan payload letak dimensi dimensi jumlah payload ukuran tabel kuantitas tiang kolom peladen sasaran kueri mangsa, tebakan fungsi SQL spesifik jenis apakah yang diimplementasikan diluncurkan penyerang penganalisis secara beruntun lantas dimodifikasi terus perlahan membesar dengan pola iterasi sekuensial menebak urutan nilai pengindeksan hitungan parameter sandi indeks mulai dari pengikatan sandi parameter indeks angka batas dimensi hitungan indeks struktur *1*, lantas dinaikkan perlahan *2*, membesar ke indeks struktur hitungan indeks *3*, dan urutannya begitu seterusnya dipaksa menanjak secara dinamis hingga aplikasi web pada arsitektur mesin instalasi peladen mendadak mogok merespons terhenti lantas mutlak memuntahkan jeritan peringatan pemberitahuan ralat respons sandi *Error* peramban SQL?</summary>

**Jawaban:** Kueri analisis baris fungsi eksekutor instruksional pengurutan *ORDER BY* (dicontohkan melalui rangkaian injeksi berformat `' ORDER BY 1 --`, `' ORDER BY 2 --`, dan seterusnya).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap pengetahuan teknis identifikasi pembeda eksploitasi *Login Bypass SQLi* sederhana dengan analisis *UNION-based SQLi* yang mutakhir
- [ ] Saya fasih menjabarkan prasyarat kesetaraan jumlah kolom kueri sintaks *UNION*
- [ ] Saya sanggup menelusuri enumerasi pemetaan hitungan parameter arsitektur fungsi jumlah payload struktur baris tiang memori kolom tabel peladen (*Column Enumeration*) berbekal adopsi implementasi ekskavator utusan sandi tebakan fungsi *ORDER BY* maupun sandi fungsi sisipan data *NULL*
- [ ] Saya sukses memahami tahapan pembongkaran tebakan payload tabel arsip rahasia administrator instalasi *Mini Lab*
- [ ] Saya telah menuntaskan validasi evaluasi ulasan pelaporan *Quiz Kilat* dengan penyerapan materi memadai

---

## 🔗 Resources

- [PortSwigger UNION Attacks](https://portswigger.net/web-security/sql-injection/union-attacks) — Panduan lab komprehensif mengurai peretasan peladen arsitektur aplikasi berbasis *SQL UNION*.

---

## ➡️ Besok

**Day 2: SQL Injection Blind (Boolean & Time)** — Apa jadinya bila perlindungan situs membentengi paras layar halamannya sehingga hasil tebakan fungsi kueri modifikasi ekstraksi arsip tabel sasaran sintaks operasi eksploitasi peramban gabungan *UNION*-mu sama sekali TIDAK DITAMPILKAN di paras antarmuka layar pelaporan? Inilah jenis peretasan tingkat mahir yang diistilahkan **Injeksi Buta (Blind SQLi)**. Esok hari, Anda akan diajarkan fungsi parameter murni mengeksekusi ekstraksi pencurian arsip peladen data walau layar buta membisu, dengan meraba pelaporan mengandalkan evaluasi sinyal arsitektur tebakan instruksi penahanan algoritma jeda kelambatan peramban eksekutor peladen sasaran parameter *Time-based Blind*!

---

*📅 TISS Null Teaming · Week 16 · Day 1 · BREACH Rank*
