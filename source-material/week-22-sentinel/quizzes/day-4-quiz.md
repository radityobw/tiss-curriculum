---
type: quiz
week: 22
day: 4
title: "Quiz: IDS/IPS (Suricata & Snort)"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Menganalisis infrastruktur keamanan perimeter sistem korporat, di manakah letak diferensiasi arsitektur mendasar antara <i>IDS (Intrusion Detection System)</i> dan <i>IPS (Intrusion Prevention System)</i> dalam memproses muatan koneksi berbahaya?
- [x] A. Komponen *IDS* beroperasi sebagai alat pemantauan pasif; sistem mengidentifikasi muatan peringatan anomali (menciptakan indikator *Alert*), namun fungsi penerusan jaringan tetap membiarkan lalu lintas paket tersebut lewat. Di sisi sebaliknya, kapabilitas *IPS* beroperasi secara interaktif; selain meregistrasi temuan peringatan, ini langsung merespon untuk menggagalkan pemuatan transmisi serangan dengan eksekusi (*Drop/Reject*), mencegah paket tersebut menyentuh sistem peladen.
- [ ] B. *IDS* dikhususkan sebagai instalasi ekosistem Linux, sementara pemakaian perangkat lunak *IPS* wajib dijalankan di infrastruktur operasi *Windows*.
- [ ] C. Parameter instalasi *IDS* memanfaatkan perangkat lunak analitika log *Splunk*, sementara sistem operasi taktis *IPS* mengandalkan integrasi basis modul jaringan *Wireshark*.
- [ ] D. Tidak terdeteksi klasifikasi pembeda, kedua mesin identik mutlak serta merta dalam penerapan parameter eksekusi SPL.

### Q2
**Type:** True/False
**Question:** Pada pengujian implementasi sensor keamanan analitikal (Deep Packet Inspection) melalui alat *Suricata/Snort*, komponen definisi atribut `content:"<script>";` pada sintaks taktis *Rule* merupakan arahan parameter absolut untuk memandu instruksi deteksi dalam mencari eksistensi sidik jari struktural *(Signature string)* berupa identifikasi tipe penyerangan indikasi *XSS* di dalam muatan data jaringan.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Dalam ranah modernisasi deteksi pencegahan sistem terstruktur, apa nama perangkat lunak detektor sumber terbuka (yang dioptimalkan pemrosesannya untuk ekosistem *Multi-thread*) yang diakui sebagai sistem pewaris superior generasi terbaru <i>Snort</i>?
**Answer:** Suricata.

### Q4
**Type:** Short Answer
**Question:** Saat spesialis merumuskan penulisan struktur sintaks <i>Rule deteksi</i> pada pengaturan *Snort/Suricata*, komponen parameter (seperti pendefinisian kriteria taktis `alert` atau kueri `drop`) diposisikan pada area mana secara teknis di dalam urutan eksekusi penulisan satu baris pengaturan aturan tersebut?
**Answer:** Posisi terdepan pada elemen parameter eksekusi (merujuk pada penentuan *Action / Rule Action*).

### Q5
**Type:** Short Answer
**Question:** Di penelaahan pembedahan sintaks aturan deteksi *Rule* sensor *Snort*, apa definisi makna di balik penyematan fungsi referensi elemen singkatan kueri atribut `sid` (sebagaimana terlihat pada parameter spesifik `sid:100001;`) yang lazim ditulis pada akhir kueri instruksi tersebut?
**Answer:** Signature ID (Sebagai Identifikasi Pengenal Nomor Registrasi Standar Unik untuk konfigurasi Aturan Taktis).
