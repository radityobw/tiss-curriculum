# 🛡️ Week 21 · Day 5: Lab & Weekly Mission Identifikasi Serangan

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓░░░░░░] 40% — SENTINEL Rank (Minggu 2 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░] 88% — Hari 105 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → ✅ BREACH → 🔄 SENTINEL

---

## 📝 Rekap Minggu Ini

Modul minggu ini berfokus pada kapabilitas deteksi dan penguasaan teknik pembacaan jejak di lingkungan OS/Server:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Apache/Nginx Log Format | Membedah 7 atribut log akses web (IP, Timestamp, Method, URI, Status Code, Size, User-Agent) dari standar format *Combined*. |
| Day 2 | Windows Event Logs | Analisis sandi numerik esensial OS (Event ID 4624 Logon, 4625 Failed, 7045 Service Creation) untuk audit otentikasi. |
| Day 3 | Linux Logs & Journalctl | Analisis penempatan standar repositori direktori `/var/log/auth.log` dan pemanfaatan perintah kueri ekstraksi modern `journalctl`. |
| Day 4 | Pattern Recognition | Mengenali indikasi parameter visual arsitektur anomali ancaman seperti peretasan *Brute Force, Vulnerability Scanning*, dan skenario pencurian data (*Data Exfiltration*). |

---

## 🧪 Hands-On Lab

### Prerequisites
- Komputer dengan sistem operasi Linux atau implementasi virtualisasi WSL (Windows Subsystem for Linux).
- terminal *command-line* dasar pengolahan data (*grep, awk, sort, uniq, head*).

### Misi Hari Ini: "Audit Investigasi Log Sentral (Log Analysis Data Processing)"

Praktikum integratif kali ini tidak menggunakan *dataset* terstruktur sederhana yang sudah disiapkan baris ringkasannya, melainkan menuntut Anda menggunakan terminal untuk mengelola ekstraksi puluhan ribu baris teks mentah berkas riwayat peladen web korporasi. pemrosesan perintah baris menjadi kunci kelangsungan identifikasi.

### Step 1: Ekstraksi IP Penyerang Utama (Top Talkers Extraction)
1. Inisiasi prosesor sesi lingkungan *bash shell/terminal*. Asumsikan ketersediaan *dataset log web* dengan konvensi penamaan `access.log`.
2. Prosedur audit awal dalam mencari parameter peretas yang mengeksekusi serangan eksploitasi otentikasi diukur melalui identifikasi rute alamat yang paling mendominasi permintaan *(Most frequent request IPs/Top Talkers)*. Implementasikan gabungan rantai eksekusi parameter perintah terminal berkelanjutan (metode *Piping* `|`):
 `awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 5`
3. *Penjelasan Kombinasi :* `awk` digunakan untuk mengambil ekstraksi hanya pada spasi kolom urutan ke-1 (yakni bidang khusus Alamat IP sumber). Rangkaian instruksi `sort` lalu parameter `uniq -c` mengakumulasikan seluruh alamat ganda menjadi agregasi kalkulasi statistik beruntun per jenis nilai rute alamat IP tersebut. Terakhir, `sort -nr` menata agregat prioritas dari data frekuensi terbesar (*reverse numeric*), sementara fungsi argumen perintah penyempitan terminal `head -n 5` mempresentasikan penyajian hanya untuk visual 5 keluaran teratas.
4. *Hasil Pemantauan Hipotetikal Terminal:* Keluaran layar melaporkan identifikasi tunggal anomali IP. Misal `IP 10.10.55.5` mendominasi dengan lebih dari 15.000 rentetan transaksi koneksi *Requests*. Verifikasi Triase: Ini indikator awal serangan.

### Step 2: Menyelidiki Pola Serangan (Filtrasi Ekstraksi Spesifik)
1. Berdasarkan hasil validasi indikasi, IP parameter penyerang terekstrak (`10.10.55.5`).
2. Isolasi file master log dengan menginisiasi pembuatan pelaporan khusus yang difilter dan dicetak menuju berkas baru khusus data ancaman:
 `grep "10.10.55.5" access.log > hacker_log.txt`
3. Telusuri taktik dengan memvalidasi anomali rekaman kegagalan *(Vulnerability Scanning/Directory Enumeration brute-force)*. Lakukan kuantifikasi status rekaman galat (misal, merinci parameter penolakan direktori tak valid):
 `grep "404" hacker_log.txt | wc -l`
 *(Parameter Hasil Hipotetis: Muncul metrik kalkulasi 14.500 baris rekaman penolakan)*. Analisis konklusi: Teridentifikasi eksploitasi *Port Scanning* dan pencarian rentetan kerentanan rute berkas.

### Step 3: Mencari Titik Kebobolan Keamanan (Identifikasi Insiden / True Positive)
1. Setelah peretas memindai kueri galat 404 secara sistematis dan menginjeksi direktori berulang kali, apakah di interval waktu berikutnya peretas mendapatkan celah respon penerimaan kredensial?
2. Analisis berlanjut dengan ekstraksi keberadaan konfirmasi penanda sukses (berdasarkan status balasan valid peladen yakni *200 OK*) pada rekaman peretas:
 `grep " 200 " hacker_log.txt`
3. *Simpulan Analisis Terverifikasi:* Terminal mengekstrak rekaman parameter indikasi koneksi `GET /admin_dashboard.php` terselesaikan dengan parameter status persetujuan respon `200`. Kesimpulan Triase Mutlak: Sistem berstatus teridentifikasi jebol, pelaku berhasil menerobos keamanan autentikasi rute aplikasi untuk berkuasa mendarat sah di halaman antarmuka administrasi sensitif. Insiden terklarifikasi ke status valid *True Positive*.

---

## 🎯 Weekly Mission

### Misi: "Laporan Perburuan Insiden Siber (Threat Hunting Report)"

**Deskripsi:** Memanfaatkan keahlian teknikal manipulasi *Piping* Linux seperti (*awk* dan *grep*) sudah tersimulasi dengan mantap. Tanggung jawab tingkat pelaksana Analis SOC tidak terlepas dari proses validasi dokumentasi analisis forensik perburuan jejak yang dapat diserahkan di tingkat manajemen taktis.

**Tugas Mandiri:** Merujuk pada pemahaman investigasi dan penyaringan terminal, dokumentasikan pola indikator perburuan yang mendemonstrasikan implementasi. Susunlah pelaporan *Summary Report Threat Hunting* perburuan jejak.

**Deliverables:**
1. Hasilkan laporan dalam format penyajian *Markdown* dengan *naming convention* `THREAT_HUNT_LOGS.md`.
2. Struktur dokumen wajib menjabarkan temuan 3 Klasifikasi (Atribut Indikator Pola/Serangan):
 - **Tipe Analitik Serangan:** (Contoh : Penelusuran Direktori/Vulnerability Scanning Web, Brute Force Windows).
 - **IP Pelaku & Rekam Cap Waktu Timestamp:** (Periode di mana lonjakan peretasan terindikasi pada titik fluktuasi anomali intensitas paling puncak).
 - **Bukti Log Mentah (Raw Log Evidence):** (Representasi faktual penyalinan ekstraksi baris format data log yang menampakkan pola otentikasi keberhasilan).
 - **Komentar Analisis Forensik (Threat Analyst Rationale):** (Jabarkan metodologi deskriptif mengapa rentetan teks tersebut divalidasi ke status *True Positive* peretasan indikator eksploitasi pola).

**Kriteria Sukses:**
- [ ] Tersedia repositori dokumen berkas `THREAT_HUNT_LOGS.md`.
- [ ] Berisikan 3 (Tiga) struktur spesifik pembedahan parameter tipe insiden pengintaian kerentanan (Pattern).
- [ ] Mewajibkan penyajian komando *Bash Linux CLI Utility* (seperti rute perintah pemanggilan *grep/awk/uniq*) yang mendemonstrasikan instruksi tata cara menyeleksi *insight* informasi data dari sampel log fiktif berukuran besar tersebut.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Demi mengeksekusi ekstraksi atau porsi spesifik dari penampang bidang struktur data log web yang masif dan panjang (contoh: secara presisi membuang sisa data untuk sekadar mengisolasi nilai kolom pertama yang berisi metrik IP Alamat Klien), instruksi basis terminal Linux manakah yang diaplikasikan SOC Analyst?</summary>

**Jawaban:** perintah *awk* (implementasi instruksi contoh: `awk '{print $1}'`).
</details>

<details>
<summary>❓ [MUDAH] Membuka rutinitas pemilahan informasi pada dasar manajemen terminal sistem operasi Linux, apakah nama komando yang senantiasa digunakan guna memfilter masukan teks, menyeleksi parameter dan cuma mencetak baris barisan log yang memiliki eksistensi karakter istilah (*pattern*) penelusuran tertentu (seperti mencari string numerik "404")?</summary>

**Jawaban:** Komando *grep*.
</details>

<details>
<summary>❓ [SEDANG] Berdasarkan praktik *Pattern Recognition*, apabila penganalisis mengekstrak log arsitektur peladen dan mendapati rekaman berupa ratusan notifikasi <i>HTTP Status Code 401 Unauthorized</i> terstruktur secara instan (bertubi-tubi) dengan tujuan mengincar <i>endpoint</i> otentikasi `/login.php`, lalu rentetan gagal itu terhenti mendadak seraya mencetak satu rekaman berstatus akhir indikasi <i>200 OK</i>, kesimpulan investigatif apa yang menasbihkan insiden tersebut?</summary>

**Jawaban:** Keberhasilan aktivitas otentikasi dari peretasan *Brute Force*. Indikasi berlanjut pada parameter *200 OK* menasbihkan peretas akhirnya sukses menemukan verifikasi parameter konfigurasi rahasia yang sah pasca penelusuran percobaan rentetan eksploitasi *Credential Guessing* ekstensif yang sebelumnya terekam gagal. 
</details>

<details>
<summary>❓ [SEDANG] Dalam hierarki *Piping* pengoperasian analisis di manajemen Linux terminal OS, operasi perintah lanjutan apalagi yang fardhu (wajib) diandalkan dan dipadukan menyusul implementasi perintah fungsi (*sorting* data log), di mana peran fungsionalisasinya adalah menghapus data nilai duplikasi baris dan merangkum akumulasi kuantitatif total data IP frekuensi alamat tersebut (`menghitung agregasi berulang/counting`)?</summary>

**Jawaban:** Instruksi komando *uniq* (khususnya dijalankan dengan parameter argumen kueri `uniq -c`).
</details>

<details>
<summary>❓ [SULIT] Jelaskan parameter di lingkup *Big Data Log Monitoring*, apa latar rasional teknikal arsitektur mengapa Analis mewajibkan pendayagunaan infrastruktur mekanika rantai <i>Piping</i> Linux (dengan menggunakan simbol rantai `|`) dalam mengelola ekstraksi, filtrasi dan pemantauan dataset data besar berkapasitas sangat raksasa hingga *10 Gigabyte*, alih-alih mengeksekusi *raw file* tersebut di lingkungan *Text Editor* sistem manajemen peladen secara statis standar?</summary>

**Jawaban:** Apabila penganalisis bersikeras memerintahkan pengolahan dokumen standar pembacaan (seperti menginisiasi Notepad/Gedit/Sublime Text editor antarmuka grafis statis) untuk membuka utuh *database* berkas sebesar 10 Gigabyte, arsitektur manajemen perangkat lunak di sistem operasi akan berupaya mengalokasikan (memuat/loading) eksekusi dari ukuran keseluruhan *file* tersebut ke dalam arsitektur penanganan *Random Access Memory (RAM)* dari peladen *backend*. Implementasi naif pengalokasian RAM seperti itu sangat memberatkan kapabilitas sumber sistem, memicu malfungsi berlebih hingga terjadi eksploitasi keruntuhan teknis OS (*Crash / System Freeze/Not Responding*). Di lain titik, strategi utilisasi struktur manajemen rantai terminal (seperti penerapan `cat access.log | grep "admin" | awk...`), merubah ekosistem dengan memecah instruksi pemrosesan *dataset* sehingga Linux OS hanya harus melaksanakan eksekusi muatan aliran penampang log per baris terkomputasi pada satu waktu (teknik pemrosesan konstan *Streaming Data Architecture Pipeline* tanpa penangguhan *memory*). Oleh sebab kapabilitas parameter metode inilah rutinitas manipulasi di *Terminal CLI Pipeline* diakui sistematis menjamin keamanan memori sistem stabil dan pengerjaan proses pelacakan berkinerja secara mutlak lebih optimal.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami instruksi eksekusi ekstraktif Linux seperti kueri data filter *awk* dan kapabilitas pencarian *grep*.
- [ ] Saya sukses melaksanakan integrasi operasi berantai (struktur mekanika manajemen *Piping*) untuk memproses rute log terminal secara berkelanjutan.
- [ ] Saya sukses mendemonstrasikan rumusan taktis eksekusi perburuan anomali *Top Talkers* log di simulasi peretasan.
- [ ] Saya fasih mendaras deteksi spesifik untuk memvalidasi rekaman sukses *200 OK* dalam riwayat anomali.
- [ ] Saya berkomitmen menghimpun laporan komprehensif pelacakan `THREAT_HUNT_LOGS.md` (Weekly Mission).

---

## 💬 Diskusi Minggu Ini

1. Anda baru saja menguasai kemampuan beradaptasi di ekosistem operasi penyusunan pelacakan data terstruktur dan pembedahan lalu lintas informasi *Log Analysis* format Apache web server, kapabilitas OS log Windows (via sandi ID referensi otentikasi), hingga metode kueri pemilahan Linux. Jika ditinjau dari kenyamanan manajemen *Threat Hunting*, metode penelusuran mana yang secara taktis Anda pandang lebih tangguh bagi pengawasan korporasi berskala raksasa? Secara personal teknikal, apakah Anda menilai rutinitas terminal (*Bash Linux CLI Piping* seperti operasi kueri parameter `grep/awk/uniq`) yang kompleks itu jauh lebih responsif dibanding visualitas sistem antarmuka interaktif UI grafis terotomasi korporasi di mana analisis dikomputasi pada tingkat dasbor GUI tanpa mewajibkan eksekusi arsitektur manual berbaris-baris pada lingkungan terminal? Paparkan rasional parameter argumen perbandingan metode perburuan jejak Anda!

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 👁️ THE PATTERN SEEKER │
│ Week 21 Complete │
│ "Numbers don't lie. │
│ They just hide in plain sight." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 22: SIEM & Monitoring Tools**

Setelah pembinaan investigatif Anda dengan mendaras keterampilan peretasan pencarian pengolahan perintah baris *grep/awk* berbasis CLI secara log secara komprehensif selesai, di korporasi kelas atas tingkat dunia rutinitas analisis ekstraksi berkas taktis murni manual saja secara strategis tidak mencukupi standar efisiensi SOC mutakhir untuk pengelolaan ratusan Gigabytes data harian yang membludak. Minggu lanjutan ini, ekosistem pemantauan keamanan korporasi membukakan babak eksekusi teknologi *Security Information and Event Management (SIEM)* mutakhir. Pada modul Week 22 Anda siap mengeksplorasi infrastruktur pemantauan dasbor korporasi terstruktur **Splunk**, menguasai teknik pemfilteran pencarian kueri standar (Search Processing Language/SPL), mempelajari teknik modifikasi grafik manajemen visual parameter pengawasan peringatan, serta mengintegrasikan rumusan perlindungan otomatis peredaman insiden intrusion peladen pada parameter penyelarasan deteksi Intrusion Detection Systems **IDS/IPS (Sistem perlindungan seperti Suricata & Snort)**.

> 🚀 *"Manual parsing is for the trenches. Splunk is the command center."*

---

*📅 TISS Null Teaming · Week 21 · Day 5 · SENTINEL Rank*
