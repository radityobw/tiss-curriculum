---
type: quiz
week: 22
day: 3
title: "Quiz: Splunk Dashboards & Alerts"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam penyajian pelaporan keamanan siber, mengapa analis SOC harus menerjemahkan rentetan parameter kueri *SPL* ke dalam format representasi antarmuka *Dashboard* (seperti <i>Pie Chart</i> atau grafik garis)?
- [x] A. Karena pemangku kepentingan tingkat manajemen menuntut pelaporan identifikasi krisis secara instan dan komprehensif untuk dicerna, ketimbang disajikan layar hasil kueri pencarian baris teks mentah yang kompleks secara teknis.
- [ ] B. Agar eksekusi kueri SPL tersebut secara teknis tidak menghabiskan penggunaan alokasi RAM.
- [ ] C. Karena parameter *Dashboards* adalah standar prasyarat untuk aktivasi mesin perlindungan *Suricata*.
- [ ] D. Lantaran dasbor grafis mampu menahan parameter serangan eksfiltrasi secara otomatis tanpa mitigasi.

### Q2
**Type:** True/False
**Question:** Saat Analis SOC melakukan pengawasan berkelanjutan, fitur <i>Alert (Peringatan Terotomatisasi)</i> Splunk dikonfigurasi guna mendelegasikan pemantauan. Secara terjadwal sistem ini menyaring kueri SPL dan membangkitkan notifikasi operasional (alarm/email) HANYA apabila memenuhi kondisi yang ditentukan melebihi angka <i>Trigger Condition</i> (Ambang batas).
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Pada analisis laporan log *Splunk*, istilah baku apakah yang mengelompokkan koleksi panel metrik visual (berbentuk grafik atau angka) yang diselaraskan dan diekstrak berkelanjutan secara *Real-Time* dari kueri parameter SPL?
**Answer:** Dashboards (Dasbor GUI).

### Q4
**Type:** Short Answer
**Question:** Saat seorang teknisi merumuskan konfigurasi peringatan *(Alert)*, dan menentukan kriteria parameter logis: "Aktifkan notifikasi apabila jumlah gagal login *count* > 50", terminologi apakah yang disematkan untuk merujuk pada standar numerik pembatas " > 50" tersebut?
**Answer:** Trigger Condition (atau Threshold / Ambang Batas Logis).

### Q5
**Type:** Short Answer
**Question:** Dalam parameter eksekusi respon peringatan insiden, kapabilitas <i>Action</i> (Tindakan Eksekusi) pada komponen pengaturan peringatan *Splunk* dikonfigurasikan guna menghasilkan efek teknis apa setelah insiden tervalidasi?
**Answer:** Eksekusi otomasi respons taktis seperti transmisi pengiriman peringatan *Notifikasi/Email* ke analis terkait, hingga rutinitas penciptaan tiket mitigasi pada manajemen pelaporan tiket.
