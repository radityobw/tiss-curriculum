# 🛡️ Week 22 · Day 4: IDS/IPS (Suricata & Snort)

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 22 · Day 4/5 | SENTINEL Rank (Minggu 3 dari 5) | Overall: 109/120 hari (90%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** strategis sistem antara sensor deteksi (IDS) dan sensor pencegahan intrusi (IPS).
2. **Memahami** arsitektur kerja platform inspeksi lalu-lintas jaringan terbuka *Snort* dan perangkat lunak modern *Suricata*.
3. **Membaca** dan merumuskan elemen sintaks aturan keamanan (*Detection Rules*) pendeteksian taktis ancaman (Signature-based).

---

## 📖 Materi Inti

### Pertahanan Titik Temu Perimeter: IDS vs IPS

Perangkat pengawasan jaringan tradisional (*Firewall Layer 4*) hanya bertugas memblokir akses rute jaringan berdasar penomoran rute (Contoh pencegahan konektivitas: Blokir akses semua komunikasi Protokol SSH/Port 22 dari Internet Eksternal). Perangkat ini pada umumnya tidak mengukur muatan konten di dalam bingkai transaksinya. Bila terdapat skenario upaya serangan eksploitasi taktis bermuatan bahaya (Contoh *Payload Malware*) yang ditumpangkan pada jalur terbuka yang legal (seperti akses ke port 80/HTTP aplikasi web), *Firewall* tradisional secara alami meloloskan akses serangan tersebut.
analitik tingkat lanjut yang diwajibkan dalam hal ini disebut teknik **Deep Packet Inspection** (Pemeriksaan Isi Paket Medalam), kapabilitas tersebut diselenggarakan oleh teknologi perangkat **IDS / IPS**.

1. **Intrusion Detection System (IDS):**
 Klasifikasi sensor pengawasan pendeteksi pasif. Mesin IDS menganalisis duplikat salinan aliran aktivitas lintas data jaringan korporasi untuk inspeksi kecocokan parameter indikator eksploitasi muatan ancaman rahasia. Ketika menemukan muatan (Payload) indikasi serangan semisal injeksi SQLi, sistem menerbitkan catatan peringatan insiden pelaporan (Alert). Perlu digarisbawahi, IDS berfungsi menginspeksi tanpa intervensi pencegahan ; sehingga paket koneksi taktis peretas senantiasa lolos menuju perangkat akhir internal peretas.
2. **Intrusion Prevention System (IPS):**
 Klasifikasi sensor intervensi pertahanan aktif. Mekanisme perangkat IPS merespons ancaman tidak sebatas membuat dokumentasi *Alert* sistem peringatan. Mesin pengawas ini dirancang untuk segera mengeksekusi operasi penanggulangan proaktif yakni penghancuran intervensi transfer (Menggugurkan lalu lintas koneksi muatan jaringan tersebut melalui fitur *Drop / Reject connection*) saat insiden serangan sedang terlaksana. Mekanisme taktis pencegahan otomatis ini memastikan paket bahaya dihentikan sebelum paketnya bereksekusi di jaringan internal.

### Arsitektur Sensor Industri: Snort dan Suricata

Dalam pengerahan arsitektur keamanan tingkat lanjut pusat (SOC), perlindungan Perimeter Sistem diatur di dominasi sensor pengendus lalu lintas terbuka lintas sistem:
- **Snort:** Mesin pengembang sensor pionir pelacak sidik jari berbasis analisis teks (Signature-based) legendaris dari Sourcefire.
- **Suricata:** Platform generasi penerus permesinan inspeksi data yang berkinerja mutakhir karena rancangan pengembangannya diakselerasikan melalui pemrosesan distribusi aliran jaringan paralel (*Multi-threaded Architecture*), sanggup mengatasi inspeksi padat berkecepatan *Gigabit*.

### Konstruksi Aturan Pencegahan Jaringan: Sintaks IDS Rule

Keberhasilan alat sensor Suricata maupun platform Snort dalam mengenali bahaya berpedoman pada pengumpulan dokumentasi direktori parameter kriteria identifikasi (Dikenal sebagai *Rules* atau aturan sidik jari).

Mari kita analisis anatomi parameter aturan (Rules deteksi) eksploitasi kode berbahaya spesifik tipe peretasan XSS di atas muatan teks HTML Web:
`alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS $HTTP_PORTS (msg:"XSS Attack Detected"; content:"<script>"; sid:100001; rev:1;)`

Komponen Arsitektur Taktis Parameter:
1. **`alert` (Rule Action/Tindakan):** Elemen penetapan operasi penanganan jika peringatan terpicu (Contoh tindakan pasif adalah *Alert*. Tindakan proaktif menggunakan perintah aksi `drop` yang diaktifkan untuk sistem *IPS*).
2. **`tcp` (Protocol):** inspeksi konektivitas transmisi spesifik (Mendeteksi struktur protokol spesifik TCP).
3. **`$EXTERNAL_NET any ->` (Rute Sumber):** Menentukan arah analisis penyerang di wilayah eksternal atau publik menuju port asal eksternal taktis mana pun (`any`).
4. **`$HTTP_SERVERS $HTTP_PORTS` (Rute Tujuan):** Klasifikasi alamat *Endpoint* penerima target internal ke infrastruktur peladen Web serta port konfigurasi khusus protokol HTTP.
5. **`(msg:"...");` (Pesanan Log):** pesan peringatan dokumentasi nama judul peretasan yang akan dipancarkan di *dashboard log* peringatan SIEM/Analis.
6. **`content:"<script>";` (Inspeksi Indikator Deteksi Payload):** INILAH PARAMETER PENENTU SENSOR (Signature String)! Suricata diberi instruksi menelaah inspeksi struktur di seisi tubuh paket dan mencocokkan indikator rangkaian teks parameter spesifik string `<script>`. Apabila tervalidasi keberadaannya di lalu-lintas muatan data, peringatan diregistrasikan.
7. **`sid:100001;` (Signature ID):** Parameter pelabelan nomor pengenal unik referensi administratif manajemen pencatatan Aturan *(Rule Identifier)*.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melakukan rancang bangun simulasi sintaks pertahanan detektor (IDS Rule)!

1. Persiapkan aplikasi pemroses teks (Notepad). Asumsikan kedudukan teknikal simulasi: Kamu bertindak selaku insinyur perlindungan operasi jaringan tim SOC.
2. Instruksi insiden darurat diterima: *"Atasi eskalasi eksploitasi. Diperintahkan untuk menonaktifkan dan menolak seketika seluruh transfer lalu-lintas akses komunikasi tidak resmi yang bermanifestasi asal alamat IP 192.168.1.5 yang ditargetkan mengeksekusi layanan peladen database relasional kita (beralamat IP tujuan target 10.0.0.99) pada rute protokol MySQL port default 3306!"*
3. **Perumusan Misi Analis:** Rakit komponen pencegahan *Snort/Suricata Rule* terkait penanganan operasi peretasan tersebut (satu baris taktis).
4. **Konfigurasi :**
 - *Tindakan Ekseskusi (Rule Action):* Membutuhkan kemampuan aktif menolak operasi, maka instruksinya menggunakan perintah parameter `drop`.
 - *Rute Arah Parameter Sumber:* Instruksi berbunyi `192.168.1.5 any` (Akses rute eksternal valid, protokol TCP dan port peretas parameter variabel acak).
 - *Rute Arah Parameter Tujuan Target:* Berlokasi di parameter konfigurasi `10.0.0.99 3306`.
 - * Detail Log Pesan & ID Parameter:* Parameter teks `(msg:"Drop Malicious MySQL Connection"; sid:100002;)`
5. **Hasil Integritas Rakitan Final Kueri IDS/IPS Taktis:**
 `drop tcp 192.168.1.5 any -> 10.0.0.99 3306 (msg:"Drop Malicious MySQL Connection"; sid:100002;)`
6. Intervensi pelaporan sistem perlindungan selesai dieksekusi. Pelaksanaan intrusi penyerangan digagalkan *Intrusion Prevention System (IPS)* sebelum transmisi serangan mengancam instansi server penyimpanan relasional.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Menelaah perlindungan jaringan, parameter perbedaan filosofis teknis utama apakah yang mengklasifikasi platform sensor <i>IDS (Intrusion Detection System)</i> dengan perangkat sensor perlindungan aktif <i>IPS (Intrusion Prevention System)</i>?</summary>

**Jawaban:** Aplikasi sensor perangkat lunak *IDS* menjalankan fungsi peninjauan indikator pasif, yakni membedah anomali log dan menginisiasi penciptaan sinyal tanda peringatan *Alert* di platform penyimpanan, dengan parameter toleransi pembiaran paket jaringan transmisi lolos. Di sisi lain, perlindungan mesin *IPS* memproses kapabilitas proteksi reaktif/aktif; tidak sekadar menerbitkan peringatan, modul IPS mengeksekusi penghentian intervensi peretasan dan menghapuskan paket konektivitas tersebut (memblokir/Drop paket koneksi) untuk memastikan insiden dihentikan secara prematur di perimeter.
</details>

<details>
<summary>❓ Pada perkembangan kemutakhiran deteksi platform inspeksi pertahanan lalu-lintas jaringan terbuka korporat, aplikasi perangkat lunak generasi penerus apakah yang dikenal unggul merekayasa proses parameter <i>Multi-threading (memproses koneksi lalu lintas jaringan paralel berkecepatan tinggi)</i> dan kerap kali dikelompokkan selaku evolusi pengganti arsitektur platform legendaris pelacak paket data Snort?</summary>

**Jawaban:** Platform arsitektur deteksi keamanan *Suricata*.
</details>

<details>
<summary>❓ Dalam konfigurasi pembentukan aturan deteksi keamanan <i>IDS Snort</i>, apabila spesialis merangkaikan integrasi argumen komponen kueri `content:"/bin/bash";` di tubuh sebuah pengaturan, instruksi teknis spesifik apakah yang diwajibkan sistem arsitektur tersebut dari platform alat pengendus muatan jaringan perlindungan tersebut?</summary>

**Jawaban:** Komponen atribut `content` merupakan instruksi untuk detektor melakukan verifikasi dan interogasi struktural parameter di perut transfer payload data pelacak isi (Payload). Alat IPS diperintahkan memicu notifikasi valid alarm JIKA platform mendapati penyesuaian keberadaan string sidik jari mutlak berupa tulisan eksak `"/bin/bash"` tertera pada struktur transmisi komunikasi peladen (mengindikasikan tanda eksekusi paksa terminal peladen Linux eksternal).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya mengetahui fungsi pengawasan platform pengawasan dan fungsi pencegatan *IDS/IPS* perimeter keamanan.
- [ ] Saya menguasai teori perbedaan efisiensi pelacakan platform deteksi legendaris Snort dengan implementasi fungsi kapabilitas Suricata OS mutakhir multi-thread.
- [ ] Saya fasih membedah metode penetapan aksi teknikal tindakan taktis kueri deteksi (Atribut deteksi instruksi `Alert` vs taktik intervensi `Drop`).
- [ ] Saya paham mekanisme pengerahan perumusan rute sintaks parameter (Rules Detection Engine) dan perakitan penyusunan parameter peringatan *Message (msg)* detektor *Signature ID (SID)* taktis.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Suricata Rules Documentation](https://suricata.readthedocs.io/en/suricata-6.0.0/rules/) — Direktori dokumentasi resmi tata cara eksekusi penulisan dan pengonfigurasian kueri parameter deteksi arsitektur infrastruktur pelacakan Suricata sedunia.

---

## ➡️ Besok

**Day 5: Lab & Mission: Setup SIEM & Detection Rules** — Melengkapi kualifikasi kompetensi wawasan manajemen arsip log terpusat SIEM, pengoperasian kueri analitik berbasis SPL pada peramban data besar *Splunk*, dan arsitektur penguatan *IDS/IPS (Sensor Peladen Keamanan Suricata)*. Evaluasi praktek laboratotium (Lab Simulatif Sentral) di esok hari mewajibkan pengerahan implementatif arsitektur keterampilan teknikal kasta perlindungan keamanan yang ekstensif, di mana simulasi mendemonstrasikan pembuatan tiga pelaporan dokumentasi taktis sistem mitigasi *(Detection Rule Engineering)* penangkal serangan.

---

*📅 TISS Null Teaming · Week 22 · Day 4 · SENTINEL Rank*
