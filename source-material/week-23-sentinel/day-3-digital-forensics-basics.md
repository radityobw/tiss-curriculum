# 🛡️ Week 23 · Day 3: Digital Forensics Basics

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 23 · Day 3/5 | SENTINEL Rank (Minggu 4 dari 5) | Overall: 113/120 hari (94%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** urgensi investigasi pasca-insiden (Digital Forensics) dalam proses penegakan hukum dan audit kepatuhan korporasi.
2. **Menerapkan** kaidah penanganan parameter integritas pelacakan barang bukti (*Chain of Custody*).
3. **Mengerti** proses penciptaan salinan identik perangkat (Kloning *Forensic Imaging / Hashing*).

---

## 📖 Materi Inti

### Metodologi Bukti Sistem Digital: Digital Forensics

Meskipun sistem agregasi pengawasan seperti SIEM memberikan visibilitas aktivitas jaringan yang kuat, representasi notifikasi peringatannya belum mencukupi standar regulasi (Compliance) untuk disajikan secara mutlak di muka meja persidangan peradilan. Ketika insiden menyangkut kerugian finansial material, organisasi harus beralih menuju metode formalitas pembuktian berstandar penegak hukum, yang direalisasikan pada disiplin ilmu: **Digital Forensics (Forensik Digital)**.

Digital Forensics memuat serangkaian proses disiplin ilmu yang terstandarisasi untuk mengamankan (*Preserve*), mengidentifikasi (*Identify*), mengekstraksi (*Extract*), dan mendokumentasikan *(Document)* parameter bukti material komponen elektronik (misal *Hard Disk* atau blok Memory RAM peladen peretas), dengan tujuan utama mempertahankan integritas bukti digital (*Admissibility of Evidence*).

### Rantai Kepatuhan Integritas Barang Bukti: Chain of Custody

Dalam ekosistem pelaporan audit dan hukum, keabsahan barang bukti dapat dengan seketika digugurkan apabila pembela pihak kompromi membuktikan adanya kelalaian prosedur pencatatan fisik sehingga menumbuhkan indikasi bahwa manipulasi barang bukti digital (*Data Tampering*) telah dilakukan selama masa penyitaan.

Sebagai tanggapan strategis mitigasi, spesialis forensik wajib mendayagunakan parameter dokumentasi historis log audit perlindungan berwujud **Chain of Custody (Rantai Kustodi)**.
Dokumen administrasi kontrol ini menyimpan kronologis pendataan mengenai prosedur penanganan bukti:
- Konfirmasi penanggalan (*Timestamp*) barang bukti (Contoh unit: *Laptop*).
- Indentifikasi personel spesifik (ID spesialis) yang menyentuh, mengoperasikan, memproses akses penyitaan material komputer, serta pihak yang membedah sistem terkait.
- Penjelasan alur fisik pengamanan pelacakan penyimpanan barang bukti (Sistem Brankas keamanan).
Bila terdeteksi indikasi ketiadaan pemantauan (*Gap*) dalam sistem penjagaan alur kronologi pencatatan pemindahan operasi (menandakan *Chain of Custody* telah putus), maka status barang bukti otomatis kehilangan bobot integritas legal hukum.

### Modifikasi Protektif Penyitaan Data: Forensic Imaging & Hashing

Di dunia forensik tingkat instansi, larangan terpenting yang tak bisa ditolerir analis adalah: **DILARANG MENGAKSES DAN MENYALAKAN KOMPUTER BARANG BUKTI SECARA LANGSUNG!**

Prosedur sekadar menyalakan sistem mesin (*Booting OS*) bakal secara otomatis memodifikasi ribuan rekam metadata parameter (Timestamps), menimpa pemblokiran klaster alokasi blok penyimpan operasi data log perangkat yang secara hukum bakal mendeklarasikan manipulasi dan kerusakan status material bukti.
Metodologi forensik mutlak yang sah adalah:
1. **Perangkat Blokir Akses Intervensi (Write Blocker):** Implementasikan jembatan *Write Blocker* berwujud perangkat *Hardware* sebelum peladen HDD tersambung menuju workstation PC analis forensik, menggaransi bahwa pencegahan lalu lintas eksekusi perintah perombakan tulis (Write Command) 100% diputus pada alat tersebut.
2. **Kloning Bit-Level (Forensic Imaging):** Menginisiasi proses penggandaan keseluruhan media tingkat duplikasi struktur arsitektur murni *Bit-stream copy* tanpa intervensi kompresi hilang (*Bit-by-bit Clone*, biasanya berformat *.E01* / *.dd*). Pembedahan forensik di tingkat investigasi mutlak HANYA bisa diselenggarakan penganalisis di berkas citra salinan kloning ini.
3. **Sistem Integritas Data (Hashing):** Mengukuhkan keabsahan teknis bahwa arsip salinan salinan berkas pelacakan identik sempurna berhadapan sumber aslinya mendayagunakan perhitungan nilai arsitektur algoritma *Hash (MD5 / SHA-256)*. Berkas salinan yang mempunyai pencocokan (Match) hash terhadap alat peladen merupakan garansi keamanan mutlak persidangan valid integritas bukti.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi konseptual arsitektur integritas forensik!

1. Anda bertugas mengevaluasi insiden sebagai spesialis forensik. Tim insiden baru saja mengakuisisi satu blok peladen peretas *Hard Disk Drive (HDD)* 1TB terkait peretasan infrastruktur.
2. Berpedoman pada langkah SOP keamanan standar pelacakan, analis menjalankan metode algoritma kriptografi validasi **SHA-256** ke unit sumber material HDD tersebut, lantas mengonfirmasi nilai pencetakan: `a1b2c3d4e5...`.
3. Pekerjaan dilanjutkan dengan memproses penyalinan eksekusi *Forensic Imaging* menuju sistem instalasi klaster *Lab Server*. Sehari kemudian, Anda memproses ulang eksekusi arsitektur algoritma perhitungan hash untuk file arsip *Image* hasil duplikasi tersebut.
4. *Pendeteksian Anomali :* Penganalisis menginspeksi hasil nilai keluaran *Hash* dari file rekaman *Image* tersebut, di mana angka struktural menunjukkan inkonsistensi keluaran nilai: `f9e8d7c6b5...`.
5. **Kesimpulan Validasi Spesialis Forensik:** Terdapat indikasi modifikasi (Korupsi arsitektur data)! Kegagalan integritas parameter ini (*Hash Mismatch*) menyimpulkan indikasi kemungkinan terjadinya interferensi fungsi kloning tak sempurna maupun terindikasi pelanggaran tanpa modifikasi pembukaan data *Image* tanpa pencegah. Kegagalan parameter ini membatalkan legalitas data sebagai barang material persidangan.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam regulasi pelacakan, berkas log pelaporan kronologi pengawasan yang mendokumentasikan log aktivitas mobilitas alat material bukti elektronik keamanan di sistem hukum penyitaan agar tak dianulir legitimasinya disebut?</summary>

**Jawaban:** Pengawasan *Chain of Custody (Rantai Kustodi)*.
</details>

<details>
<summary>❓ Pada eksekusi pengerahan operasi lapangan (*Incident Response*), mengapa tindakan menyalakan sistem secara pasca penyitaan komputer target secara berlebihan tidak direkomendasikan prosedur spesialis analis forensik?</summary>

**Jawaban:** Operasi menyalakan perangkat OS *(Booting)* secara inheren otomatis melaksanakan proses baca-tulis log *(Write Process)*, mengubah sistem metadata tanggal/waktu arsip (*Timestamp Modification*), serta menimpa sistem log file RAM perangkat operasi, di mana intervensi struktur material ini membatalkan legitimasi integritas status perangkat hukum.
</details>

<details>
<summary>❓ Membahas standar perlakuan duplikasi forensik, fungsi analitis kriptografi pelacak manakah (seperti algoritma <i>SHA-256</i>) yang senantiasa diproyeksikan berperan menjamin stempel integritas file bayangan arsip pelacak (Forensic Image) tak termodifikasi parameter data aslinya?</summary>

**Jawaban:** Penghitungan integritas *Hashing (Hash Calculation / Fungsi Algoritma Checksum)*.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami pengerahan standarisasi legalitas integritas *Digital Forensics*.
- [ ] Saya memahami implementasi formasi log pengawasan kronologis kelola pelacakan *Chain of Custody*.
- [ ] Saya mengetahui batasan krusial SOP penyitaan terhadap boot sistem perangkat.
- [ ] Saya paham konsep metode duplikasi pendataan arsitektur operasi integritas *Forensic Imaging/Hashing*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [NIST: Guide to Integrating Forensic Techniques](https://csrc.nist.gov/publications/detail/sp/800-86/final) — panduan referensi standar arsitektur operasi instansi *NIST* pelacak taktik forensik sistem korporasi operasi dunia.

---

## ➡️ Besok

**Day 4: Memory & Disk Forensics** — Setelah merampungkan prosedur pendataan log kloning perlindungan berkas bayangan *Forensic Imaging*, rutinitas beralih menelusuri penampang ekstraksi arsitektur *Disk Forensics* (pemulihan direktori bekas hapusan) dan pembedahan ekstraksi *Memory Forensics (RAM)* menggunakan perangkat infrastruktur analitikal perangkat perlindungan log *Volatility* guna menarik kata sandi yang disembunyikan peretas!

---

*📅 TISS Null Teaming · Week 23 · Day 3 · SENTINEL Rank*
