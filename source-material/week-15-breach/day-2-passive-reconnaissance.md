# 💀 Week 15 · Day 2: Passive Reconnaissance

> **Rank**: BREACH | **Minggu ke-15**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 15 · Day 2/5 | BREACH Rank (Minggu 1 dari 5) | Overall: 72/120 hari (60%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep pengumpulan intelijen Pengintaian Pasif (*Passive Reconnaissance*) dalam rutinitas ekstraksi tanpa terdeteksi.
2. **Mengekstraksi** data catatan publik kepemilikan sasaran menggunakan *WHOIS* dan interogasi rekam logis *DNS*.
3. **Mengeksploitasi** identifikasi sumber data informasi terbuka bermodalkan arsitektur parameter *OSINT* (*Google Dorking* & mesin pencari *Shodan*).

---

## 📖 Materi Inti

### Seni Mengintai Tanpa Menyentuh

Fase **Reconnaissance (Pengintaian Intelijen)** dalam arsitektur operasional peretasan terbelah menjadi dua kategori utama eksekutor: *Aktif* dan *Pasif*.
Pengumpulan intelijen pasif (**Passive Recon**) ibarat mengumpulkan profil sasaran menggunakan ketersediaan arsip data publik yang terbuka dan terdokumentasikan secara eksternal (*Open Source Intelligence / OSINT*). Mesin server infrastruktur web sasaran target niscaya tidak akan pernah membunyikan alarm maupun mencatat jejak (log) alamat *IP address* milikmu, karena metode eksploitasi intelijen ini dilaksanakan mutlak tanpa pernah mendelegasikan pengiriman kueri atau parameter interaksi transmisi paket eksekusi langsung yang membentur alamat antarmuka peladen sasaran.

Sebagai penguji penetrasi yang mumpuni, kamu dituntut merangkai payload analisis kelemahan intelijen semata bermodalkan jejak dan remah informasi kelalaian eksposur payload dokumentasi yang dibiarkan terekspos berceceran bebas pada arsip ekosistem mesin pencari awan publik internet.

### Senjata Pengintaian Pasif

1. **WHOIS & DNS Lookup**
 Kala sebuah entitas mendaftarkan lisensi administrasi sewa tautan *Domain* (seperti konfigurasi `target.com`), pihak administrator dipersyaratkan melampirkan payload data otentik mencakup nama penyewa, surel korespondensi operasional, dan nomor fungsionalitas telepon. Kamu bisa mengekstrak ekspos detail kepemilikan tersebut via panggilan kueri `whois target.com` di layar peramban terminal! Untuk membedah peramban email maupun informasi arsitektur *server* alamat sasaran penyangga peladen mereka, penganalisis menyayat rekam konfigurasi parameter *DNS* menggunakan kueri instruksional seperti `dig` atau instruksi kueri `nslookup`.

2. **Google Dorking (Operator Canggih Mesin Pencari)**
 Mesin peramban indeks publik Google nyatanya merupakan salah satu senjata alat penganalisis *OSINT* paling mumpuni jikalau analis sanggup memformulasikan komposisi perakitan sintaks kueri *Google Dork* (*Google Hacking Database*). Kamu mampu memanipulasi pelacak untuk menemukan payload indeks direktori ekskavasi *file* laporan berformat arsip rahasia (semisal PDF), payload sandi koneksi *database* yang rentan terekspos, hingga kerentanan memori laman antarmuka portal *login* administrator tersembunyi kelalaian yang secara pasrah tidak dikonfigurasi proteksi pengecualian pengindeksan konfigurasi web direktori *robot.txt*.
 - `site:target.com` (Filter pembatas kueri secara spesifik cuma diarahkan penelusurannya di domain situs target yang disasarkan)
 - `filetype:pdf` (Membatasi rincian hasil unduhan agar semata memuat ekstensi dokumen publik laporan PDF)
 - `inurl:admin` (Memindai letak alamat URL peladen yang pada arsitekturnya mengandung kata *admin*)

3. **Shodan (Mesin Pencarinya Peretas Keras)**
 Jika arsitektur mesin peramban Google diarahkan murni meraba dan mengindeks dokumentasi teks konten eksternal web halaman situs, maka peramban instalasi basis data khusus bernama **Shodan** berfokus pada pelacakan operasi mesin fisik arsitektur internet! Shodan memindai peladen *router* jaringan instalasi peranti sasaran, sistem pemantauan pengikatan IP kamera CCTV terbuka, perangkat operasional peladen pengikatan *web server*, dan memajang rincian pemetaan terbuka port perangkat lunak konfigurasi servis komponen versi peladen yang kadaluarsa telanjang dada ke penjuru publik tanpa fungsi otentikasi login apa pun.

4. **theHarvester**
 bedil terminal pengikatan pelacak andalan yang terintegrasi di distribusi mesin OS *Kali Linux* ini bertugas secara siluman menyisir otomatis arsitektur repositori pencari pihak ketiga (Google, LinkedIn, Bing) demi menyaring dan memetakan ratusan penemuan alamat kontak surel email karyawan target korporasi! Direktori email inilah yang kelak dipilah guna dimanfaatkan penganalisis sasar peluncuran operasional serangan metode pemancingan fana manipulatif (*Social Engineering / Phishing*).

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Ayo mulai mengimplementasikan ekstraksi jubah intaian siluman penganalisis dan merangkai filter logis penelusuran via parameter sintaks *Google Dorking*!

1. Buka mesin indeks pencari [Google](https://www.google.com).
2. Bayangkan kamu ditugaskan selaku auditor keamanan domain target `tiss.or.id` guna menelusuri apakah peladen membiarkan dokumentasi arsip laporan PDF mereka tercecer ke publik indeks peramban. Ketikkan mantra kueri penelusuran Dork ini:
 `site:tiss.or.id filetype:pdf`
 (Catatan Logis: Jika penelusuran menyatakan nihil/kosong, coba implementasikan uji pemetaan instansi publik kampus luringmu sendiri, misal `site:ui.ac.id filetype:pdf confidential`).
3. Coba inisiasikan manuver perburuan penemuan rute letak laman portal otentikasi *login* administrator situs yang dibiarkan terekspos peramban tanpa sengaja:
 `site:target-kampusmu.ac.id inurl:login OR inurl:admin`
4. Jelajahi juga pengujian mesin peramban khusus instalasi [shodan.io](https://www.shodan.io/). Pada kotak antarmuka penelusurannya, isikan kueri nama wilayah kota lokasimu (misal `city:"Jakarta"`). Kamu akan disajikan pemaparan rincian port jaringan terbuka, kamera, serta servis rentan peladen di wilayah tersebut yang meronta telanjang dipetakan Shodan!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam terminologi pemisahan prosedur intelijen keamanan siber, parameter konseptual mendasar apakah yang secara empiris memisahkan kategori pendekatan ekskavasi Pengintaian Pasif (*Passive Recon*) bilamana dikomparasikan dengan klasifikasi eksekusi Pengintaian Aktif (*Active Recon*)?</summary>

**Jawaban:** Pada tahapan *Passive Recon*, penganalisis sebatas mengekstrak agregasi repositori profil intelijen target menggunakan kumpulan data pihak ketiga publik terbuka (Google, Shodan, WHOIS) secara mutlak tanpa mengirimkan *Request/Packet* ping secara langsung ke arah infrastruktur peladen aslinya, sehingga sistem keamanan sasaran niscaya nihil menyadari kedatangan penganalisis karena ketiadaan interaksi catatan log masuk IP pengunjung di mesin mereka. Sebaliknya, pendekatan payload *Active Recon* menghunjamkan eksekusi transmisi transmisi pemindaian (scan probe) yang murni menabrak serta berinteraksi logis dengan konfigurasi mesin *server* target secara langsung yang mana sangat rentan terekam pengamatan log pertahanan serta niscaya berisiko tinggi membangkitkan alarm pelaporan jaringan sasaran.
</details>

<details>
<summary>❓ Deklarasi payload instruksional operator filter sakti pemetaan arsitektur kueri pencarian ekstensif (*Google Dorking*) macam apakah pada algoritma fungsi mesin peramban Google yang diaplikasikan eksklusif guna memastikan pembatasan hasil pelaporan penelusuran informasi hanya dipusatkan secara eksklusif berorientasi mengerucut pada lingkup eksekusi satu alamat situs *domain* organisasi sasaran spesifik (sebagai contoh, murni memusatkan pencarian ke arsip direktori peladen situs jaringan target `tiss.or.id`)?</summary>

**Jawaban:** Penggunaan payload parameter kueri operator penyaring ekstensi penyaringan `site:` (contoh penulisannya: `site:tiss.or.id`).
</details>

<details>
<summary>❓ Ketika arsitektur penugasan algoritma peramban Google murni memusatkan fungsionalitasnya untuk menelusuri serta merayapi pengindeksan data teks tautan dan pelaporan situs antarmuka halaman web aplikasi awan semata, instalasi mesin peramban data perangkat peranti intelijen spesialis apakah yang lazim diandalkan jajaran penganalisis peretas *OSINT* guna mendedikasikan ekstraksi pengintaian logik letak pemetaan kerentanan pemindaian parameter konfigurasi interaksi mesin port peladen perangkat keras IoT nyata (laksana membongkar CCTV terbuka tanpa keamanan kata sandi, instalasi router rentan, dan memaparkan versi aplikasi server kadaluarsa yang dibiarkan terekspos terkoneksi daring sejagat ranah bumi eksternal internet)?</summary>

**Jawaban:** Shodan (Mesin spesialis data peramban *Search Engine for Internet of Things/IoT and Cyber Devices*).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya telah menyerap perumusan kerangka klasifikasi pemisahan Pengintaian Pasif (*Passive Recon*) dalam koridor peretasan etis
- [ ] Saya sukses mempraktikkan penarikan ekstraksi pemetaan informasi rekam administrasi empunya domain via kueri instruksi terminal *WHOIS*
- [ ] Saya mahir memformulasikan dan mengirimkan instruksi parameter sintaks kueri spesifik peramban *Google Dorking*
- [ ] Saya telah menuntaskan simulasi eksplorasi ekskavasi intelijen *Dorking OSINT* di instalasi panduan operasional kerangka parameter *Mini Lab*
- [ ] Saya sukses mengulas hasil pengujian rangkuman modul *Quiz Kilat* dengan penyerapan evaluasi yang representatif

---

## 🔗 Resources

- [Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database) — Gudang pusat dokumentasi repositori *Google Dorking* mutakhir yang dioptimalkan untuk membedah spesifikasi paparan fail sensitif peladen sistem.
- [Shodan.io](https://www.shodan.io/) — peramban OSINT referensi pemetaan rincian eksekutor mesin perangkat keras jaringan yang terhubung bebas ke awan internet.

---

## ➡️ Besok

**Day 3: Active Reconnaissance** — Selesai sudah alokasi tahap awal rutinitas pengumpulan parameter intelijen di mana kamu mengeksploitasi data OSINT publik dari jarak jauh tanpa terdeteksi! Esok hari, lepaskan sejenak atribut manipulasi mode senyapmu! Kita beralih mengeksekusi tahapan yang niscaya mendebarkan dan mengharuskan izin otorisasi legalitas mutlak; rutinitas perburuan yang sarat serangan bising menabrak target peladen, fase **Active Reconnaissance**. Kita akan mempersiapkan peluncuran parameter serangan deteksi eksploitasi peramban aktif murni menyapu ketersediaan layanan pada pintu port peladen arsitektur operasional bermodalkan bedil pemindai industri **Nmap**, serta turut menggempur paksa jalur arsitektur ekskavasi pembongkaran direktori iteratif paksaan (*Directory Bruteforcing*) untuk membedah penempatan fail URL tersembunyi (*Hidden Interface Asset URL File Path Extraction Attack Method Tool Execution Strategy Module Recon*) situs target merujuk penggunaan instalasi peramban alat *Gobuster* / *Ffuf*!

---

*📅 TISS Null Teaming · Week 15 · Day 2 · BREACH Rank*
