# 🛡️ Week 22 · Day 3: Splunk Dashboards & Alerts

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 22 · Day 3/5 | SENTINEL Rank (Minggu 3 dari 5) | Overall: 108/120 hari (90%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menerjemahkan** hasil evaluasi pemrosesan teks instruksi SPL menjadi representasi pelaporan berwujud antarmuka grafis (Dashboards).
2. **Menyusun** konfigurasi otomasi peringatan keamanan deteksi insiden (Alerts) berdasarkan penetapan parameter <i>Threshold</i> SIEM.
3. **Memahami** nilai efisiensi eskalasi keamanan di atas prosedur inspeksi manual berkelanjutan.

---

## 📖 Materi Inti

### Pelaporan Eksekutif: Manajemen visualisasi Dashboards

Dalam lingkungan kerja *Security Operations Center* (SOC) korporasi, tingkat direksi manajemen (seperti CIO atau CISO) umumnya tidak memerlukan pembacaan teknikal kueri teks mentah atas rentetan kejadian *Logon Failed* harian. Kebutuhan manajemen mensyaratkan pemantauan pelaporan yang terstruktur dan mudah dianalisis seketika.

Tuntutan tersebut dipenuhi melalui pembentukan antarmuka analitik bernama **Dashboards (Dasbor)**.
Dashboards berfungsi sebagai integrasi visual *(seperti grafik Diagram Lingkaran Pie Chart, diagram grafik batang konstan, pengukuran kecepatan meteran data)*, yang metrik nilainya ditarik dan dikomputasi berkesinambungan secara wajar (*Real-Time*) hasil data dari rumusan pencarian SPL di lingkungan SIEM Splunk.

Melalui fasilitasi visual SIEM, SOC Analyst mengimplementasikan penataan kueri seperti `index=web_logs status=401 | stats count by src_ip` ditransformasikan menjadi parameter panel tampilan berwujud grafis dengan taksonomi penamaan seperti *"Top 5 IP Indikasi Peretasan Terkini"*, yang kemudian dimonitor konstan di terminal stasiun pemantauan ruang kendali pusat.

### Automasi Pemantauan Insiden Siber: Splunk Alerts

Selain representasi antarmuka pengawasan, utama platform sentral SIEM berkedudukan mengeksekusi mekanisme rutinitas notifikasi proaktif *(Alarm System)* tanpa memerlukan observasi pasif secara berkelanjutan di monitor. Otomasi proses pengawasan terpusat diselenggarakan melalui pengerahan arsitektur **Alerts (Peringatan Terotomatisasi)**.

*Alert* adalah eksekusi modul parameter pemantauan berkala (penjadwalan latar belakang), di mana kueri fungsi pencarian (SPL) dievaluasi dalam ritme siklus konstan (misalnya verifikasi dilakukan 5 menit sekali). Apabila nilai pencarian mendeteksi pelaporan yang mengindikasikan lonjakan kalkulasi matematis melebihi kondisi standar prasyarat toleransi atau "Ambang Batas Wajar" *(Threshold)*, rutinitas akan merespons pelaporan eksploitasi notifikasi alarm kejadian insiden.

**Komponen Konfigurasi Peringatan Taktis (Alert Architecture):**
1. **Search Query (Parameter Dasar):** Instruksi berbasis teks (SPL) khusus yang menganalisis serta mengisolasi jenis anomali kejadian (Contoh: Parameter mendeteksi alamat peretas sukses autentikasi rute administrator peladen eksternal).
2. **Schedule (Jadwal Evaluasi Intervensi):** Penetapan ritme parameter seberapa intens sistem *Splunk* mengkaji pencarian dan menganalisis log harian tersebut (Contoh: *Cron Schedule Evaluated Every 15 minutes*).
3. **Trigger Condition (Logika Pemicu):** Menentukan standar limitasi batasan eskalasi alarm dieksekusi. (Contoh parameter : *If Result Count > (Lebih Besar) daripada 5 entri indikator serangan*).
4. **Trigger Action (Tindakan Respons):** Pengaturan otomatis langkah tindakan eksekusi insiden. (Contoh: Menyiarkan peringatan pelaporan kepada alamat Surel/Email ke tingkat tim respon (*Incident Response Team*), mengirimkan modul skrip respon API (Webhook), hingga membentuk pelaporan sistem *Ticketing* mitigasi otomatis IT).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melakukan rancang bangun simulasi penataan struktur peringatan (Alert Configuration)!

1. Siapkan dokumentasi virtual Anda. Praktik menuntut operator untuk menyimulasikan konfigurasi pelaporan alarm bernama "Pendeteksi Data Exfiltration (Pengurasan Data)" pada arsitektur Splunk SIEM korporat.
2. **Tahap 1 - Formasi Kueri Deteksi:**
 (SPL) `index=firewall action=allowed | stats sum(bytes_out) as total_out by src_ip`
3. **Tahap 2 - Formasi Penjadwalan Waktu Pemantauan:**
 Konfigurasi rentang penelusuran (Misal: Kueri dievaluasi terus-menerus setiap durasi interval 1 Jam).
4. **Tahap 3 - Formasi Pemicu Parameter Kondisi (Trigger Threshold):**
 Evaluasi anomali wajar (Threshold Limit). JIKA parameter pencapaian besaran agregat metrik *total_out* menunjukkan eskalasi > (Lebih besar) dari nilai `5000000000` (atau ekuivalen 5 Gigabyte pertukaran transfer jaringan).
5. **Tahap 4 - Formasi Penindakan Darurat Otomatisasi (Trigger Action):**
 Terapkan pelaporan tanggap insiden (Emergency action). `Send Email to SOC_Tier2@company.local` disertai penamaan peringatan taksonomi pelaporan insiden: *"URGENT: Indikasi Pengurasan Traffic Outbound > 5GB!"*.
6. Formasi lengkap dan aktif! Kini penjadwalan pemantauan pengurasan dapat dijaga konsisten oleh kecerdasan sistem *Splunk*.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengurai otomasi visualisasi laporan pada SIEM, istilah terminologi apa yang digunakan untuk merujuk ke modul antarmuka yang membungkus kumpulan laporan data numerik (seperti Pie Chart, Bar Graph) yang diperbarui secara *Real-Time* mempresentasikan data hasil fungsi SPL Splunk?</summary>

**Jawaban:** Dashboards (Dasbor UI).
</details>

<details>
<summary>❓ Ketika mengaplikasikan manajemen SIEM cerdas, arsitektur Splunk apakah yang menyelenggarakan operasi pemeriksaan kueri secara terjadwal untuk mengamati sistem, dan mengaktifkan peringatan kepada pengguna apabila data masuk batas krisis insiden?</summary>

**Jawaban:** Alerts (Peringatan Otomatis/Alarm).
</details>

<details>
<summary>❓ Di eksekusi modifikasi pengaturan deteksi <i>Alerts</i>, apabila seorang analis mengonfigurasi batas regulasi kondisi: "Bentuk peringatan notifikasi HANYA JIKA akumulasi jumlah (<i>result count</i>) melampaui batasan nilai LEBIH DARI 50 kejadian", terminologi apa yang merujuk kepada klasifikasi batasan "angka 50" (atau titik krisis pemantik insiden) tersebut?</summary>

**Jawaban:** Pemicu Kondisi Limitasi (Trigger Condition / Threshold).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami urgensi konversi presentasi kueri log menjadi interpretasi visual.
- [ ] Saya menguasai pendefinisian elemen visualisasi pengawasan (*Dashboards*).
- [ ] Saya mengetahui kapabilitas penyusunan mekanisme parameter peringatan taktis SIEM (*Alerts*).
- [ ] Saya paham bahwasanya rutinitas pendeteksian dapat dialihkan pada kapabilitas jadwal *Alerts*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Splunk: Alerting Manual](https://docs.splunk.com/Documentation/Splunk/latest/Alert/Aboutalerts) — Dokumentasi standar pengembangan integrasi otomasi sistem peringatan taktis dari pengembang perangkat lunak platform Splunk SIEM.

---

## ➡️ Besok

**Day 4: IDS/IPS (Suricata & Snort)** — Mesin penganalisis seperti SIEM terfokus menangani peringatan visibilitas log korporasi yang terpusat. Untuk mencegah insiden secara simultan pada saat paket menyerang parameter halaman perusahaan, diperlukan infrastruktur inspeksi data real-time, yaitu teknologi detektor batas **IDS/IPS (Intrusion Detection/Prevention System)**. Mengetahui sensor inspeksi pertahanan terdepan **Suricata** dan alat **Snort** akan menjadi tujuan fokus esok hari. Anda akan difasilitasi instruksi teknik konstruksi arsitektur penulisan parameter deteksi ancaman taktis kueri aturan *(Rules)* yang berguna menolak penetrasi jaringan.

---

*📅 TISS Null Teaming · Week 22 · Day 3 · SENTINEL Rank*
