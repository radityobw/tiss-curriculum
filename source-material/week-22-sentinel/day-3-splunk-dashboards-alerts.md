# 🛡️ Week 22 · Day 3: Splunk Dashboards & Alerts

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 22 · Day 3/5 | SENTINEL Rank (Minggu 3 dari 5) | Overall: 108/120 hari (90%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menerjemahkan** hasil pencarian teks SPL menjadi antarmuka visual grafis (*Dashboards*).
2. **Menyusun** konfigurasi peringatan otomatis (*Alerts*) untuk mendeteksi insiden berdasarkan batasan (*Threshold*) tertentu.
3. **Memahami** nilai efisiensi otomatisasi pengawasan keamanan dibandingkan dengan inspeksi log manual.

---

## 📖 Materi Inti

### Pelaporan Eksekutif: Manajemen Visualisasi Dashboards

Dalam lingkungan kerja *Security Operations Center* (SOC) korporat, pihak manajemen (seperti CIO atau CISO) tidak perlu membaca ribuan baris teks kueri log mentah setiap harinya. Kebutuhan manajemen berfokus pada ringkasan pelaporan yang terstruktur, visual, dan mudah dianalisis secara instan.

Tuntutan tersebut dipenuhi melalui pembuatan antarmuka analitik bernama **Dashboards (Dasbor)**.
*Dashboards* adalah representasi visual (seperti grafik *Pie Chart*, diagram batang, atau indikator pengukur data) yang menyajikan hasil komputasi kueri SPL secara langsung (*Real-Time*). 

Dengan *Dashboards*, Analis SOC dapat menyematkan kueri seperti `index=web_logs status=401 | stats count by src_ip` ke dalam sebuah panel visual berlabel *"Top 5 IP Penyerang Terkini"*, yang kemudian dapat dipantau setiap saat di layar pusat ruang kendali SOC tanpa perlu mengetik ulang kuerinya.

### Automasi Pemantauan Insiden Siber: Splunk Alerts

Selain visualisasi, fungsi utama platform SIEM adalah mengeksekusi mekanisme notifikasi proaktif, sehingga Analis tidak perlu menatap monitor 24 jam penuh. Otomatisasi pengawasan ini diselenggarakan melalui arsitektur **Alerts (Peringatan Otomatis)**.

*Alert* adalah tugas pemantauan berkala yang berjalan di latar belakang, di mana kueri pencarian (SPL) dievaluasi dalam interval waktu tertentu (misalnya, setiap 5 menit). Apabila hasil pencarian mendeteksi bahwa jumlah anomali melebihi "Ambang Batas Wajar" (*Threshold*), maka sistem akan secara otomatis memicu peringatan/alarm.

**Komponen Konfigurasi Peringatan Taktis (Alert Architecture):**
1. **Search Query (Kueri Dasar):** Instruksi SPL yang digunakan untuk mencari insiden spesifik (Contoh: mencari alamat IP yang melakukan *Brute Force*).
2. **Schedule (Jadwal Evaluasi):** Pengaturan interval waktu bagi *Splunk* untuk menjalankan kueri tersebut (Contoh: Dievaluasi setiap 15 menit).
3. **Trigger Condition (Kondisi Pemicu / Threshold):** Menentukan batasan jumlah kejadian untuk membunyikan alarm. (Contoh: *JIKA jumlah hasil (Result Count) > 5 kejadian*).
4. **Trigger Action (Tindakan Respons):** Pengaturan tindakan otomatis yang dilakukan Splunk jika kondisi pemicu terpenuhi. (Contoh: Mengirimkan peringatan via Email ke tim respons insiden (SOC Tier 2), mengirimkan notifikasi *Webhook* ke Slack/Teams, atau membuat tiket insiden di Jira).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan konfigurasi pembuatan peringatan (*Alert Configuration*) di Splunk!

1. Anda bertugas membuat peringatan otomatis bernama "Pendeteksi Data Exfiltration (Pengurasan Data)" pada SIEM korporat.
2. **Tahap 1 - Pembuatan Kueri Deteksi (SPL):**
   `index=firewall action=allowed | stats sum(bytes_out) as total_out by src_ip`
   *(Penjelasan: Menjumlahkan seluruh ukuran transfer data keluar berdasarkan IP asalnya).*
3. **Tahap 2 - Penjadwalan Waktu Pemantauan (Schedule):**
   Kueri ini akan dikonfigurasi agar dievaluasi terus-menerus dengan interval setiap 1 Jam.
4. **Tahap 3 - Kondisi Pemicu (Trigger Threshold):**
   Evaluasi anomali. JIKA metrik `total_out` menunjukkan nilai > `5000000000` (setara dengan 5 Gigabyte transfer jaringan), maka bunyikan alarm.
5. **Tahap 4 - Penindakan Respons (Trigger Action):**
   `Send Email to SOC_Tier2@company.local` dengan judul peringatan: *"URGENT: Indikasi Pengurasan Traffic Outbound > 5GB!"*.
6. *Alert* telah aktif! Kini pemantauan pengurasan data dapat dijaga konsisten oleh sistem secara otomatis tanpa pemantauan manual.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam terminologi SIEM, modul antarmuka apa yang berfungsi untuk merangkum dan menyajikan hasil pencarian data log ke dalam bentuk grafik visual yang diperbarui secara *Real-Time*?</summary>

**Jawaban:** Dashboards (Dasbor UI).
</details>

<details>
<summary>❓ Fitur otomatisasi apa pada platform Splunk yang bertugas menjalankan kueri pencarian secara terjadwal, lalu mengirimkan notifikasi peringatan jika ada data yang melewati batas wajar keamanan?</summary>

**Jawaban:** Alerts (Peringatan Otomatis/Alarm).
</details>

<details>
<summary>❓ Saat mengonfigurasi *Alerts*, jika seorang Analis menetapkan aturan: "Kirim peringatan HANYA JIKA akumulasi jumlah hasil (<i>result count</i>) LEBIH BESAR DARI 50", sebutan teknis apa yang merujuk pada nilai batasan angka "50" tersebut?</summary>

**Jawaban:** Kondisi Pemicu atau Ambang Batas (*Trigger Condition* / *Threshold*).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami pentingnya mengonversi teks log kueri menjadi representasi visual.
- [ ] Saya menguasai konsep dan peran visualisasi pengawasan melalui *Dashboards*.
- [ ] Saya mengetahui cara kerja peringatan ancaman otomatis menggunakan *Alerts*.
- [ ] Saya memahami fungsi dari *Search Query, Schedule, Trigger Condition*, dan *Trigger Action*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Splunk: Alerting Manual](https://docs.splunk.com/Documentation/Splunk/latest/Alert/Aboutalerts) — Dokumentasi resmi dari Splunk mengenai standar pengembangan dan konfigurasi sistem peringatan (*Alerts*).

---

## ➡️ Besok

**Day 4: IDS/IPS (Suricata & Snort)** — Platform SIEM (seperti Splunk) terfokus pada pengumpulan dan pemantauan log terpusat setelah data tercatat. Namun, untuk memblokir serangan secara langsung saat paket ancaman mencoba memasuki jaringan, perusahaan memerlukan teknologi sensor inspeksi garis depan, yaitu **IDS/IPS (Intrusion Detection/Prevention System)**. Besok kita akan membedah cara kerja alat populer di industri, yaitu **Suricata** dan **Snort**, serta belajar bagaimana menulis aturan deteksi ancaman (*Rules*) untuk melindungi jaringan dari serangan eksploitasi.

---

*📅 TISS Null Teaming · Week 22 · Day 3 · SENTINEL Rank*
