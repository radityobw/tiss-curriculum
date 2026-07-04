# 🛡️ Week 22 · Day 4: IDS/IPS (Suricata & Snort)

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 22 · Day 4/5 | SENTINEL Rank (Minggu 3 dari 5) | Overall: 109/120 hari (90%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** fungsi sistem deteksi pasif (IDS) dan sistem pencegahan aktif (IPS).
2. **Memahami** arsitektur *platform* inspeksi jaringan populer seperti *Snort* dan *Suricata*.
3. **Membaca** dan menulis aturan deteksi ancaman taktis (*Detection Rules* / *Signatures*).

---

## 📖 Materi Inti

### Pertahanan Perimeter: IDS vs IPS

*Firewall* tradisional (Layer 4) hanya bertugas memblokir akses koneksi berdasarkan Port atau IP (Contoh: Blokir Port 22/SSH dari jaringan luar). *Firewall* ini umumnya tidak menginspeksi isi (*Payload*) dari data yang lewat. Jika penyerang menyisipkan serangan (seperti injeksi SQL atau muatan *Malware*) melalui *port* yang diizinkan (seperti Port 80/HTTP), *Firewall* tradisional akan membiarkannya masuk.

Untuk menganalisis muatan data yang berbahaya, jaringan memerlukan teknik **Deep Packet Inspection** (Pemeriksaan Paket Mendalam). Fungsi ini dijalankan oleh teknologi **IDS / IPS**.

1. **Intrusion Detection System (IDS):**
   Ini adalah sistem pemantauan pasif. Mesin IDS menganalisis salinan (*mirror*) lalu lintas data di jaringan. Ia mencari kecocokan antara muatan paket data dengan *database* ancaman (*Signatures*). Jika IDS menemukan paket data yang berbahaya, ia hanya akan membunyikan alarm (*Alert*) untuk memberitahu Analis SOC. IDS **tidak** menghentikan atau memblokir serangan; serangan tersebut akan tetap berhasil masuk ke server tujuan.
2. **Intrusion Prevention System (IPS):**
   Ini adalah sistem pertahanan aktif. Mesin IPS ditempatkan tepat di jalur lalu lintas jaringan (*Inline*). Jika IPS mendeteksi paket berbahaya, ia tidak hanya membuat peringatan, tetapi secara proaktif langsung **memblokir dan menggugurkan (*Drop*)** paket tersebut sebelum paket itu sempat mencapai server internal.

### Arsitektur Sensor Industri: Snort dan Suricata

Dalam arsitektur *Security Operations Center* (SOC) tingkat lanjut, inspeksi jaringan dikendalikan oleh sensor perangkat lunak khusus:
- **Snort:** Mesin pendeteksi jaringan pionir legendaris dari *Sourcefire*. Memiliki basis data deteksi (*Rules*) yang menjadi standar industri.
- **Suricata:** Platform deteksi ancaman generasi modern. Ia unggul karena mendukung pemrosesan secara paralel (*Multi-threaded*), sehingga mampu menginspeksi lalu lintas data bervolume raksasa berkecepatan *Gigabit* secara efisien.

### Konstruksi Aturan Pencegahan Jaringan: Sintaks IDS Rule

Keberhasilan Snort dan Suricata bergantung pada kualitas kumpulan aturan pendeteksinya (Disebut *Rules* atau *Signatures*).

Mari kita analisis struktur aturan deteksi serangan XSS (*Cross-Site Scripting*):
`alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS $HTTP_PORTS (msg:"XSS Attack Detected"; content:"<script>"; sid:100001; rev:1;)`

**Komponen Arsitektur Rule:**
1. **`alert` (Rule Action):** Tindakan apa yang dilakukan jika kueri ini terpenuhi. (Gunakan `alert` untuk fungsi IDS pasif, dan `drop` jika ingin IPS memblokirnya).
2. **`tcp` (Protocol):** Protokol spesifik yang diinspeksi.
3. **`$EXTERNAL_NET any ->` (Source):** Menentukan bahwa asal serangan dari jaringan publik eksternal (IP apapun) melalui *port* manapun (`any`).
4. **`$HTTP_SERVERS $HTTP_PORTS` (Destination):** Rute tujuan ke *server* internal khusus web melalui port HTTP.
5. **`(msg:"...");` (Message):** Nama judul peringatan yang akan dikirimkan ke SIEM/Analis SOC.
6. **`content:"<script>";` (Payload Signature):** INI ADALAH PARAMETER INTI. Mesin IDS akan memeriksa isi paket data; JIKA ia menemukan string teks mutlak berupa `<script>`, peringatan akan segera dipicu.
7. **`sid:100001;` (Signature ID):** Nomor ID identitas aturan yang unik secara administratif.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi sintaks pertahanan sensor IDS/IPS!

1. **Skenario:** Anda bertugas di SOC. Terdapat laporan serangan darurat ke *database*. Anda diminta membuat aturan IPS (*Prevention*) untuk **memblokir/menggugurkan** semua lalu lintas data dari alamat IP peretas `192.168.1.5` yang menuju ke *database server* internal Anda (beralamat `10.0.0.99`) pada *port MySQL 3306*!
2. **Rencana Analis:** Merakit *rule* satu baris berformat Suricata/Snort.
3. **Perumusan Konfigurasi:**
   - *Tindakan (Rule Action):* Membutuhkan tindakan pemblokiran aktif, maka gunakan `drop`.
   - *Rute Sumber:* `192.168.1.5 any` (Dari IP peretas melalui port acak manapun).
   - *Rute Tujuan:* `10.0.0.99 3306` (Menuju IP *server* via *port MySQL*).
   - *Informasi Peringatan:* `(msg:"Drop Malicious MySQL Connection"; sid:100002;)`
4. **Hasil Final Kueri IDS/IPS Taktis:**
   `drop tcp 192.168.1.5 any -> 10.0.0.99 3306 (msg:"Drop Malicious MySQL Connection"; sid:100002;)`
5. *Rule* ini telah ditanam pada sistem! IPS sekarang akan langsung menggugurkan koneksi jahat tersebut sebelum menyentuh *server database*.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan utama antara perangkat <i>IDS (Intrusion Detection System)</i> dengan perangkat <i>IPS (Intrusion Prevention System)</i>?</summary>

**Jawaban:** IDS bersifat pasif; ia hanya menginspeksi lalu lintas dan membunyikan alarm peringatan jika mendeteksi ancaman, tetapi serangan tetap lolos. Sebaliknya, IPS bersifat proaktif; jika mendeteksi ancaman, ia akan langsung memblokir/menghentikan paket jaringan tersebut (*Drop*).
</details>

<details>
<summary>❓ Teknologi sensor jaringan *open-source* modern apa yang sangat unggul karena kemampuannya memproses paket secara berbarengan (<i>Multi-threading</i>)?</summary>

**Jawaban:** Suricata.
</details>

<details>
<summary>❓ Dalam aturan *IDS Snort/Suricata*, jika terdapat sintaks komponen kueri <code>content:"/bin/bash";</code>, apa tugas dari instruksi spesifik tersebut?</summary>

**Jawaban:** Memerintahkan sensor untuk membedah muatan isi (*Payload*) dari paket jaringan. Jika ditemukan string teks mutlak `"/bin/bash"`, maka sensor akan memicu peringatan.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya mengetahui perbedaan konsep pertahanan antara *IDS* (Deteksi) dan *IPS* (Pencegahan).
- [ ] Saya mengetahui efisiensi kemampuan *Suricata* (*Multi-threading*) berbanding *Snort* klasik.
- [ ] Saya memahami struktur pembuatan kueri taktis pendeteksian ancaman menggunakan *Rules*.
- [ ] Saya dapat menentukan argumen fungsi (`alert` vs `drop`), definisi protokol (*tcp*), serta parameter indikator `content`.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Suricata Rules Documentation](https://suricata.readthedocs.io/en/suricata-6.0.0/rules/) — Dokumentasi resmi dan standar referensi mengenai tata cara pembuatan aturan (*Rules*) deteksi ancaman pada Suricata.

---

## ➡️ Besok

**Day 5: Lab Setup SIEM & Detection Rules** — Melengkapi kualifikasi dasar *Blue Team*, besok kita akan melaksanakan laboratorium terpadu. Kita akan menggabungkan wawasan tentang log terpusat SIEM, pencarian SPL di Splunk, dan penguatan IDS/IPS. Dalam *Lab Simulasi Sentral* besok, Anda akan mempraktikkan proses perumusan sistem deteksi taktis (*Detection Rule Engineering*) guna memformulasikan mekanisme penangkal untuk 3 skenario serangan spesifik.

---

*📅 TISS Null Teaming · Week 22 · Day 4 · SENTINEL Rank*
