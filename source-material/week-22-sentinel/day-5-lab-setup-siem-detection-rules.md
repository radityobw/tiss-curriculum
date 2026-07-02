# 🛡️ Week 22 · Day 5: Lab & Weekly Mission Setup SIEM & Detection Rules

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓░░░░] 60% — SENTINEL Rank (Minggu 3 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░] 91% — Hari 110 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → ✅ BREACH → 🔄 SENTINEL

---

## 📝 Rekap Minggu Ini

Penobatan dirimu mengendalikan tingkat tinggi otomasi SOC (SIEM & IDS) dicetak minggu ini:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | SIEM Concepts & Architecture | Membedah 5 tahap otomasi korporasi: *Collect, Normalize, Correlate, Alert, Store*. |
| Day 2 | Splunk Basics | Mengekstrak bahasa kueri pencarian *SPL* (`index`, `table`, `stats count`). |
| Day 3 | Splunk Dashboards & Alerts | Menerjemahkan kueri *SPL* menjadi *Dashboards* visual lantas menyetel pemicu (*Trigger*) peringatan sirine (*Alerts*). |
| Day 4 | IDS/IPS: Suricata & Snort | Meracik sintaks aturan (*Rules*) sensor pendeteksi (*Alert/Drop*) berdasarkan sidik jari paket data lalu lintas. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Komputer dengan peramban teks pengolah dokumen (*Notepad/Markdown*).
- Disarankan memiliki akses ke platform pembelajaran (seperti TryHackMe: Splunk Room atau instansi lab ELK), namun laboratorium ini sepenuhnya dapat dilaksanakan berlandaskan simulasi logika analitik rekayasa (*Detection Engineering*).

### Misi Hari Ini: "Membangun Dinding Pertahanan (Rules Engineering)"

Di sesi taktis ini, peran SOC tidak terbatas pada fungsi monitoring (pemantauan pasif), melainkan dituntut untuk mendemonstrasikan kompetensi sebagai *Threat Engineer* (Arsitek Deteksi). Latihan ini mendemonstrasikan perancangan logika jebakan, memadukan kepiawaian Kueri Splunk (SPL) dengan perancangan aturan mesin pencegat *IDS/IPS (Suricata)*.

### Step 1: Merakit Kueri SIEM Splunk (Pendeteksi Kegagalan Login RDP)
1. Asumsikan penganalisis mengawasi dataset Windows keamanan terpusat di `index=windows_sec`.
2. Analis mendeteksi ancaman indikatif di mana entitas eksternal melakukan upaya menebak paksa (brute force) otentikasi RDP sistem peladen korporat.
3. Tuliskan kueri SPL yang menyaring (filter) log galat otentikasi konektivitas RDP (EventCode 4625, Logon_Type 10), lantas mengeksekusi perhitungan statistik jumlah serangan (frekuensi peretasan) dari tiap sumber IP peretas (`src_ip`).
4. *Hasil Rakitan Kueri Taktis SPL:* 
 `index=windows_sec EventCode=4625 Logon_Type=10 | stats count by src_ip | where count > 20`
 *(Kueri perumusan ini siap diintegrasikan sebagai komponen pemicu otomatis Alert ketika kuantitas penyerangan dari IP tertentu telah melampaui limit 20 upaya).*

### Step 2: Merakit Kueri Web Log (Pendeteksi Indikator XSS)
1. Asumsikan penganalisis mengevaluasi lalu lintas log peladen web yang bersemayam pada repositori agregat `index=web_logs`.
2. Target perburuan (Threat Hunting) menelusuri siapa pun yang mensimulasikan injeksi eksploitasi bermuatan `<script>` pada variasi argumen antarmuka web rute (*URI parameter*) mana pun.
3. *Hasil Rakitan Kueri Taktis SPL:*
 `index=web_logs | search uri="*<script>*" | table _time, src_ip, uri, status`
 *(Kueri struktur data tersebut memproyeksikan transformasi representasi pelaporan ke dalam arsitektur komponen visual dasbor berwujud tabel komprehensif, menginformasikan rentang kronologis Timestamp waktu eksekusi insiden, asal koneksi IP, rute injeksi XSS spesifik, dan indikasi kode validasi status peladen).*

### Step 3: Meracik Algojo Pencegah Intrusi Jaringan IDS/IPS Suricata (Pencegat Otomatis Mutlak)
1. Sebagai tim taktis pengamanan tingkat tinggi, operator sadar bahwa konfigurasi mitigasi insiden mengandalkan alarm notifikasi SIEM *Splunk* (di Step 2) bersifat reaktif dan mungkin mengonsumsi waktu insiden penelusuran. Oleh karena itu, pengamanan sistem preventif tingkat perimeter dikerahkan melalui arsitektur mesin pencegat keamanan terdepan *Suricata IPS* untuk mengeliminasi intrusi serangan tersebut sebelum peretas mampu berinteraksi menginfiltrasi konektivitas internal jaringan *Web Server* korporasi (`192.168.1.50`).
2. Konstruksikan rancangan parameter pendeteksi (Rule Syntax) Suricata untuk mengeksekusi fungsi instruksional mitigasi pemblokiran *menggugurkan (Drop)* struktur koneksi paket *TCP* taktis dari jaringan zona eksternal yang diarah kepada rute tujuan jaringan Web Server internal korporasi, asalkan parameter muatan inspeksi paket transmisi lalu-lintas data (Payload) dianalisis memuat eksistensi indikator karakteristik serangan sidik jari berwujud `<script>`.
3. *Hasil Rakitan Rule Proteksi IDS/IPS:*
 `drop tcp $EXTERNAL_NET any -> 192.168.1.50 80 (msg:"DROP XSS Attack Payload"; content:"<script>"; sid:90001; rev:1;)`

---

## 🎯 Weekly Mission

### Misi: "Buku Pedoman Arsitektur Pertahanan Sistem (Detection Engineering Playbook)"

**Deskripsi:** Aktivitas di atas merupakan metodologi penyajian dokumen bukti kepiawaian meracik arsitektur otomasi penangkal ancaman korporat keamanan terstandar. Personel analis SOC bertaraf spesialis sistem tidak secara reaktif menganalisis indikator insiden secara manual; personel *Detection Engineer* wajib mampu mengembangkan dan struktur aturan arsitektur penjaga keandalan pemantauan pengawasan keamanan berwujud jebakan deteksi aktif sistem (Rules).

**Tugas Mandiri:** Mengacu kepada wawasan struktur analitis latihan simulasi dari instruksi prosedur eksekusi praktik (Step 1 hingga 3 di ranah Hands-On Lab), delegasikan ringkasan informasi perancangan ketiga parameter struktur aturan (Rules) tersebut menuju dalam wujud artefak arsip dokumentasi teknikal pedoman instalasi penangkal ancaman SOC (Detection Rule Playbook).

**Deliverables:**
1. Produksi arsip dokumentasi format *Markdown* secara khusus dengan nama tajuk berkas `DETECTION_ENGINEERING_RULES.md`.
2. Struktur dokumen yang diarsipkan mutlak memuat pendeskripsian lengkap elemen pembentukan parameter pengaturan 3 (tiga) jenis deteksi:
 - **Rule 1 (Arsitektur SIEM Splunk):** Konstruksi rumusan algoritma pencarian kueri *SPL* pendeteksi indikator insiden keamanan eksploitasi otentikasi paksa *Brute Force RDP Windows* (Logon Type 10) beserta penempatan parameter fungsi limitasi (Threshold > 20).
 - **Rule 2 (Arsitektur SIEM Splunk):** Penyajian konstruksi perumusan operasi peramban SPL untuk mencetak dan mendisplai pelaporan tabel anomali indikator log peretasan transmisi penelusuran percobaan injeksi struktural muatan berbahaya *XSS Web*.
 - **Rule 3 (Infrastruktur Perlindungan IPS Suricata):** Penyajian rancangan sintaks konfigurasi algoritma arsitektur protektif penangkal rute dan pencegat paket data transmisi (Drop Command) serangan spesifik *XSS Payload string* dari perimeter rute jaringan terbuka menuju fasilitas server jaringan korporasi.

**Kriteria Sukses:**
- [ ] Terdapat dokumen pedoman kompilasi repositori `DETECTION_ENGINEERING_RULES.md` dalam pengerjaan misi mingguan SOC.
- [ ] Elemen penyusunan laporan kueri arsitektur Splunk mampu mempresentasikan pendayagunaan sintaks filter pemanggilan sumber basis `index`, penyesuaian perhitungan statistik agregat `stats count`, atau parameter tata bentuk visual pelaporan `table`.
- [ ] Atribut pembentukan penulisan rumusan sistem inspeksi pengamanan *Suricata* mampu dan mengonfirmasi penyertaan pendefinisian kapabilitas instruksi fungsi teknikal tindakan operasi pasif/aktif pencegahan pengguguran rute paket (`drop`), bukan hanya peringatan (`alert`).

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Mengurai mesin pemroses keamanan sentral (SIEM), selain sebagai platform pengumpulan metadata, platform ini beroperasi menerjemahkan komposisi format sintaks beraneka tipe sistem log mentah (seperti perbedaan susunan teks pelaporan Windows Events dan format file Apache Linux Logs) ke bentuk penyatuan metadata penamaan atribut lapangan pelaporan data (*Fields*) yang terstruktur konsisten dan seragam di semua lapisan sumber data. Apa tahapan arsitektur proses penyelarasan struktur pelaporan ini di sistem manajemen peramban sentral SIEM (5-Pillar proses SIEM)?</summary>

**Jawaban:** Pengoperasian tahap arsitektur struktur Normalize (Normalisasi pelaporan).
</details>

<details>
<summary>❓ [MUDAH] Dalam mengoperasikan pencarian platform data besar sistem sentral *Splunk* korporat, apa sebutan bahasa sintaks kueri perumusan instruksi pencarian khusus peramban mesin yang diderivasi mutlak dianut (dan ditulis) oleh operator untuk mengontrol filter parameter Splunk (memiliki singkatan berwujud inisial SPL)?</summary>

**Jawaban:** Search Processing Language (SPL).
</details>

<details>
<summary>❓ [SEDANG] Berkaitan dengan kapabilitas mitigasi krisis instruksi fungsi otomatisasi peramban log sentral sistem operasi platform SIEM korporat tingkat lanjut, apa klasifikasi sebutan teknikal komponen fitur fungsi Splunk terintegrasi yang diamanahkan mengurus pendelegasian instruksi untuk menavigasikan rutinitas penjadwalan evaluasi penyisiran berkala pengawasan kueri secara sistematis (pencarian bekerja repetitif di latar belakang), lantas bertugas krusial dalam menyiarkan inisiasi notifikasi transmisi peringatan pelaporan taktis kepada jajaran analis insiden bilamana kuantitas anomali log terverifikasi melampaui pengaturan kuantitatif indikator kondisi batasan angka wajar insiden *(Threshold value)*?</summary>

**Jawaban:** Manajemen peringatan operasi fitur *Alerts* (Sistem Peringatan Otomatis/Alarm Terotomatisasi).
</details>

<details>
<summary>❓ [SEDANG] Di cakupan penerapan pertahanan garis depan sistem sensor pemantauan peladen jaringan terbuka batas arsitektur (Network Perimeter Sensors), identifikasikan di titik manakah letak indikator utama diferensiasi filosofis taktis penanganan intervensi serangan peretas antara pengerahan arsitektur spesifik sistem pelaporan detektor pasif *IDS (Intrusion Detection System)* jika berhadapan sistem komparatif klasifikasi perlindungan reaktif penangkal intrusi intervensi pelindung arsitektur *IPS (Intrusion Prevention System)* ketika modul-modul perlindungan mengawasi lalu-lintas muatan konektivitas inspeksi (Deep Packet Inspection) paket rute transmisi berbahaya serangan jaringan eksploitasi peretas?</summary>

**Jawaban:** Platform sensor pemantauan *IDS* dioperasikan untuk bertindak reaktif semata dalam memetakan aktivitas pengawasan jaringan beresiko, mengendus paket inspeksi parameter anomali berisiko, memproses data pencatatan, dan sebatas menyiarkan sistem sinyal pelaporan peringatan insiden pasif notifikasi (*Alert* log) belaka, sembari struktur konektivitas paket operasi serangan tetap bebas untuk melaju meneruskan transmisi intervensi menuju titik akhir internal sasaran (*Server* aplikasi) secara langsung tanpa pencegahan intervensi struktural apa pun. Sebaliknya, komponen perangkat infrastruktur permesinan pelindung *IPS* dimanifestasikan pada topologi yang diimplementasikan untuk menyajikan perlindungan proaktif reaktif intervensi pemutusan seketika mutlak. Secara sistematis, sistem *IPS* mengidentifikasi eksploitasi parameter anomali rute data penyerang lantas pencegatan transmisi dan memusnahkan (*Drop/Reject *) lalu lintas rute komponen transmisi paket bahaya jaringan terkait seketika (menghentikan intervensi intrusi serangan seketika sebelum entitas paket ancaman tersebut berkesempatan merambat masuk menggapai instalasi fasilitas *Endpoint* target sistem operasi peladen).
</details>

<details>
<summary>❓ [SULIT] Dalam wacana metode pemrosesan pengamanan peracikan algoritma taktis konfigurasi penulisan identifikasi struktur tata nilai sintaks taktis peringatan ancaman pendeteksian pengamanan jaringan pada sistem platform mesin inspeksi aturan kontrol *Snort/Suricata Rule*, terangkan rasional urgensi analisis dari sudut pandang pembedahan mengapa pendefinisian instruksi konfigurasi perumusan indikator nilai taktis khusus elemen argumen `content:"<script>";` dipandang dan dianugerahkan secara esensial berfungsi sebagai struktur fundamental 'jantung sentral penentu krisis deteksi spesifik' dari keseluruhan anatomi komposisi deklarasi aturan operasi detektor pelacakan otentikasi taktis deteksi pengamatan tanda tangan ancaman perlindungan peringatan (Signature Engine) infrastruktur jaringan tersebut!</summary>

**Jawaban:** Keterikatan rasional sistematis ini berpedoman pada pengerahan elemen fungsi argumen `content`, di mana instruksi penetapan parameter komando spesifik komponen indikator deklarasi `content` tersebut berperan menugaskan secara absolut kepada modul algoritma teknikal platform mekanisme analisis fungsi pelacak pengendus muatan (modul sensor *Deep Packet Inspection/DPI* sistem perangkat lunak Suricata) agar membongkar struktur payload transmisi transfer jaringan dari hulu lapisan protokol pelacakan untuk memproses penggeledahan verifikasi operasi rute inspeksi ke kedalaman fisik atribut (tubuh Payload Data yang dikirim penyerang) yang bersemayam dalam bingkai jaringan peladen dan sedang melaju di transmisi transfer ekosistem lalu lintas korporasi yang sedang diawasi. Melalui operasi taktis verifikasi pengamatan tersebut, sistem algoritma mesin pelacak keamanan ini menelusuri secara, jika instruksi kriteria pengamatan tersebut mendapati (menemukan/mencocokkan) secara presisi ada wujud kombinasi penempatan susunan konstruksi perumusan penyelarasan parameter karakter teks deklarasi sidik jari indikator (string matching signature parameter eksak) berupa bentuk eksistensi urutan tulisan karakter spesifik nilai `<script>` (sebuah tag struktur elemen injeksi yang paling umum diandalkan dan disalahgunakan oleh ekosistem para eksploitator peretas taktis dalam kerentanan indikator pelaksanaan eksekusi transmisi penetrasi serangan skrip peretasan lintas aplikasi tipe *Cross-Site Scripting / XSS*), maka secara analitis taktis seketika platform infrastruktur sensor tersebut bakal segera mengeksekusi konfirmasi pengabsahan validasi indikator serangan peretasan ancaman (mengirimkan notifikasi peringatan insiden bahaya atau menolak operasi krisis hukuman pendeteksian) atas temuan parameter. Tanpa disediakannya deklarasi pendefinisian penyisipan rumusan atribut petunjuk sidik jari deteksi (*signature indicator rule* fungsi `content`) yang diinstruksikan dalam struktur komposisi operasi pengawasan taktis ini, modul mesin arsitektur peringatan deteksi tersebut sejatinya mengalami kebutaan analisis teknikal kognitif dan kehilangan parameter objektif validasi rumusan arah untuk bertindak mendeteksi, mengidentifikasi arsitektur muatan intervensi peretas klasifikasi (XSS) ataupun melakukan tindakan korelasi pencocokan verifikasi peretasan penyerang rute sistem di tengah arus transfer parameter padat payload data jaringan peretasan berisiko besar lainnya, secara pasif.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya mendaras pengoperasian arsitektur hierarki 5 fase siklus tata letak *SIEM*.
- [ ] Saya paham mempraktikkan struktur pengerahan metode kueri *SPL* Splunk dasar log.
- [ ] Saya fasih merajut pengembangan parameter visual taktis pengawasan Dasbor pelaporan dan formasi pengaturan pemantauan Pemicu log otomatis *Alert*.
- [ ] Saya meresapi penguatan penyusunan peracikan algoritma aturan instruksi sintaks taktis perlindungan blokir sensor *IDS/IPS* perimeter pertahanan.
- [ ] Saya sanggup membuktikan penugasan kompilasi arsip repositori pembentukan naskah arsitektur laporan pedoman operasi instalasi pertahanan taktis penangkal korporasi dokumen penugasan `DETECTION_ENGINEERING_RULES.md`.

---

## 💬 Diskusi Minggu Ini

1. Selamat! Dirimu kini menaiki posisi valid kualifikasi arsitektur penguasaan infrastruktur keamanan SOC level tingkat lanjut korporat (Arsitektur deteksi pasif log korporasi berskala raksasa *SIEM & pertahanan sensor mitigasi reaktif pengawalan koneksi jaringan infrastruktur otomatis perlindungan IDS/IPS Perimeter terdepan*). Di posisi penyelesaian penugasan titik taktis transisi pertengahan modul instruksi kasta SENTINEL ini, ketika merefleksikan fungsi eskalasi keagungan parameter arsitektur perangkat ekosistem pusat keamanan platform (SIEM Splunk) yang berkuasa utuh memproses mengawinkan penyederhanaan kalkulasi inspeksi parameter log secara *Real-Time* (Korelasi SPL Cerdas log sentral dari agregat tumpukan masif riwayat sistem jutaan data kotor harian korporasi dari penjuru OS endpoint terdistribusi dan *Server* perusahaan beraneka platform OS Linux log/Windows event), lalu dirangkaikan dan dipersenjatai kapabilitas penempatan implementasi modul mesin pembatas perlindungan sensor ekosistem sistem kontrol intervensi pencegatan aktif deteksi intrusi peretasan *Suricata IPS* (sebuah platform infrastruktur perimeter berarsitektur *multi-threaded* tingkat pengawasan arsitektur lalu lintas tinggi korporasi yang memiliki fungsi arsitektur analisis instruksi detektor cerdas pembongkar muatan (Payload payload berwujud bahaya serangan *XSS/Malware/SQLi*) mampu membunuh arsitektur komunikasi transmisi intervensi transmisi serangan eksploitasi jaringan berbahaya koneksi eksak khusus dalam ukuran rentang limit waktu sepersekian ukuran intervensi *hitungan mili/mikrodetik* kilat sebelum sempat dioperasikan peretas log), apakah dirimu kini mulai perlahan menguasai apresiasi analitikal dan memvalidasi kesadaran arsitektur persepsi menyadari sedalam apa parameter kerumitan limitasi posisi betapa luar biasa teramat *rapuhnya batas rasio keberhasilan fungsi peluang survival probabilitas nasib dan taktik bermanuver ruang lingkup akses aktor kelompok agresor penyerang (Aktor Tim Red Team Peretas Otoritas Ofensif)* di kancah struktur pengoperasian perang keamanan parameter dunia infrastruktur riil industri *Enterprise Network Cyber Architecture Deployment* yang sesungguhnya? Mereka setiap waktu, tanpa henti peretasan, selalu dipaksa mendayagunakan metodologi taktik dan skema operasi berisiko tinggi yang mensyaratkan parameter kehati-hatian siluman agar manuver mereka senantiasa lolos dari intervensi pengawasan jerat radar pengamanan instalasi mesin-mesin platform otomatisasi ekosistem pelaporan kecerdasan pendeteksi infrastruktur pertahanan aktif perlindungan infrastruktur *(The Invisible Omnipresent SOC Guardians)* tak kasat mata di jaringan arsitektur tingkat dewa ini yang mengintai setiap gerakan akses penyerangan taktis konektivitas rute mereka dengan tak terbatas?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ ⚙️ THE SIEM ARCHITECT │
│ Week 22 Complete │
│ "To master the logs, │
│ is to control time and truth." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 23: Threat Hunting & Digital Forensics Intro**

Penguasaan infrastruktur teknologi platform pemantauan log sentral (SIEM) serta formasi pengaturan sistem pertahanan perimeter (IDS/IPS) telah berhasil didelegasikan. Namun, mesin perlindungan keamanan pada dasarnya bersifat reaktif dan statis. Sensor keamanan tradisional tidak selalu mampu mendeteksi *Advanced Persistent Threats (APT)*, yakni manuver peretasan canggih yang tersembunyi dan mensimulasikan perilaku pengguna resmi untuk menghindari pemicuan *Alert* sistem konvensional.

Oleh karena itu, pada esok hari modul akan memasuki tingkat kompetensi analisis keamanan puncak: **Threat Hunting & Digital Forensics Intro**. Di tahap ini, kamu tidak lagi bertindak pasif menunggu peringatan dasbor, melainkan dilatih untuk memburu anomali secara proaktif. Kamu akan belajar mengoperasikan teknik isolasi artefak digital, mencabut dan merestorasi sisa-sisa memori (RAM) serta residu sistem *Magnetic Hard Disk Drive*, mengurai jejak anti-forensik, dan memetakan metode serangan menggunakan pedoman standar industri **MITRE ATT&CK Framework**.

> 🚀 *"The machine stops at alerts. The hunter begins in the silence."*

---

*📅 TISS Null Teaming · Week 22 · Day 5 · SENTINEL Rank*
