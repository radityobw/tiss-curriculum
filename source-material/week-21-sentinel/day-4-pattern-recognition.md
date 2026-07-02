# 🛡️ Week 21 · Day 4: Pattern Recognition

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 21 · Day 4/5 | SENTINEL Rank (Minggu 2 dari 5) | Overall: 104/120 hari (87%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** nalar mengenai pentingnya pengenalan pola anomali visual (*Pattern Recognition*) dalam metode analisis lalu lintas (*Big Data Logs*).
2. **Mengidentifikasi** secara analitikal indikator serangan tipe repetitif seperti *Brute Force* dan pemindaian aplikasi web (*Vulnerability Scanning*).
3. **Mendeteksi** parameter kronologi yang merepresentasikan insiden pencurian transmisi data (*Data Exfiltration*).

---

## 📖 Materi Inti

### Efisiensi Deteksi Ancaman: Logika *Pattern Recognition*

Dalam ekosistem *Enterprise* yang sesungguhnya, staf (Analis SOC) tidak melaksanakan prosedur investigasi pemantauan log dengan menelaah seluruh metadata secara tekstual konvensional satu per satu, karena kapasitas muatan pencatatan sistem produksi terdistribusi sering kali bereskalasi hingga mencapai puluhan ribu baris log pada setiap detiknya. Menangani dataset yang luar biasa besar melalui metode visual statis biasa tidak mungkin dipertahankan secara.

Titik pembeda signifikansi kecepatan Analis tingkat mahir berada di implementasi identifikasi konseptual **Pattern Recognition (Pengenalan Pola)**. SOC *Analyst* terlatih mampu dengan sekilas mengekstraksi parameter yang terpusat melalui identifikasi ciri anomali repetitif visual: Analis tidak membaca konten teks keseluruhan, melainkan memfokuskan kemampuan pemindaian visual pada deteksi lonjakan pola atau *trend* abnormal pada baris struktur pencatatan log tersebut.

### 3 Klasifikasi Pola Anomali Serangan Dasar

**1. Pola Serangan Eksploitasi Kredensial Otentikasi (Brute Force / Password Guessing)**
- *Parameter Ciri Visual:* Teridentifikasi eskalasi signifikan dari agregat ratusan atau ribuan pemuatan rekaman log peladen dari parameter asal satu rute klien statis tunggal (1 Alamat IP) pada durasi rentang detik/menit terpusat. Secara eksklusif barisan pola masif tersebut menghasilkan atribut hasil validasi gagal/penolakan konstan (Status Kode *Event ID 4625* di Windows atau *HTTP 401 Unauthorized* di Nginx).
- *Eskalasi Krisis (Success Indicator):* Apabila pola rentetan log *Failed/401* tersebut secara mendadak berhenti dan pada menit kebersamaannya mencetak SATU indikator rekaman kode sukses akses (Status log otentikasi *HTTP 200 OK* atau *Event ID 4624 Logon Success*), ini terkonfirmasi eksploitasi serangan tebakan peretas sukses terlaksana dan berhasil melakukan login.

**2. Pola Penelusuran Kerentanan Aplikasi & Port (Vulnerability Scanning / Web Directory Brute-Force)**
- *Parameter Ciri Visual:* Sebuah alamat eksternal jaringan *(IP Asing)* melakukan repetisi koneksi *(Request)* bertubi-tubi dengan urutan yang sangat bervariasi pada pemetaan direktori *Endpoint* internal/administrasi di web server yang keberadaannya terselubung dan acak, seperti rute `/.git/config`, `/.env`, `/backup.zip`, `/admin.php`. Parameter utama dalam memverifikasi anomali adalah deretan mayoritas status `404 Not Found`.
- Ini adalah notifikasi indikator pengawasan visual kuat yang menunjukkan pemanfaatan senjata pengujian otomatis korporasi terotomatisasi *(Tool Scanning)* seperti *Nikto*, *Gobuster*, *Nmap*, *Ffuf*, yang memetakan infrastruktur aplikasi Anda.

**3. Pola Eksfiltrasi Pencurian Hak Ekspor Payload Data (Data Exfiltration)**
- *Parameter Ciri Visual:* Pola insiden tingkat lanjut tidak direpresentasikan pada parameter jumlah rekaman eskalasi penolakan gagal, melainkan diidentifikasi melalui fluktuasi/lonjakan anomali volumetrik di atribut ukuran besaran respons transfer balasan lalu lintas data *Size*.
- Secara lazim interaktif pertukaran HTML berkisar di ukuran puluhan Kilobyte (KB). Jika terdapat indikasi log lalu-lintas jaringan keluar (Outbound Traffic), entah menggunakan sarana *FTP*, *SSH*, atau HTTP *POST* menuju *IP* eksternal tak diidentifikasi, yang merangkum besaran alokasi pengiriman yang membengkak luar biasa hingga mencatatkan ukuran transmisi ribuan *Megabytes* hingga ratusan *Gigabytes*, lalu dipicu pada interval jam non- pengerjaan sistem staf korporasi (contoh pukul 2 pagi dini hari).
- Anomali masif pada pola visualisasi ekspor transfer volumetrik besar ini menasbihkan insiden pencurian komprehensif aset database (Perampokan *Data Eksfiltrasi* sistem).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melakukan validasi visual pada kapabilitas perangkaian parameter *Pattern Recognition* untuk 3 indikator anomali!

1. Amati konstruksi matriks log berikut, lantas tarik hipotesis rumusan insiden taktis dari masing-masing jenis kategori pola:
2. **Kategori Analitik A (Log Ekosistem Windows Event):**
 `14:00:01 | ID 4625 | User: Admin | IP: 10.0.5.5`
 `14:00:02 | ID 4625 | User: Admin | IP: 10.0.5.5`
 `14:00:03 | ID 4625 | User: Admin | IP: 10.0.5.5`
 *(Analisis Identifikasi: Indikasi pengulangan iterasi otentikasi login konsisten dari IP yang sama (4625), hipotesis taktis pola peretasan *Brute Force/Credential Stuffing*).*
3. **Kategori Analitik B (Log Akses Peladen Web Nginx):**
 `GET /.git/config HTTP/1.1 | 404 Not Found`
 `GET /backup.sql HTTP/1.1 | 404 Not Found`
 `GET /phpinfo.php HTTP/1.1 | 404 Not Found`
 *(Analisis Identifikasi: Repetisi akses terhadap rute *Endpoint* arsip infrastruktur secara paksa, merepresentasikan pola indikatif *Directory Scanning / Vulnerability Scanning*).*
4. **Kategori Analitik C (Traffic Jaringan Gateway Firewall Log):**
 `15:30:00 | SRC: Server_Database | DST: IP_Eksternal_Tak_Terdaftar | Bytes Out: 8.5 GB`
 *(Analisis Identifikasi: Eskalasi mutlak rute jaringan ukuran 8.5 GB dari simpul database *backend*—yang sejatinya merupakan ekosistem terisolir dan tak berlisensi berkomunikasi eksternal jaringan publik—merupakan pembuktian indikator valid *True Positive* perampokan transfer eksfiltrasi data (Data Exfiltration).*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Menguraikan pemahaman tentang metode inspeksi visibilitas *Pattern Recognition*, apabila log web korporat memberikan puluhan hingga ratusan berstatus *HTTP 401 Unauthorized* maupun *Event ID 4625 Logon Failed* dalam rentang waktu yang direpetisi berturut-turut cepat dan bersumber dari satu alamat rute klien, indikasi ancaman pola apakah ini?</summary>

**Jawaban:** Indikasi otentikasi rentetan repetisi iterasi eksploitasi *Brute Force* (atau *Password Guessing* / Penebakan kata sandi terotomasi).
</details>

<details>
<summary>❓ Dalam analisis pengawasan infrastruktur lalu lintas *Firewall Log*, apa parameter visual/ metrik anomali yang merupakan indikator primer (bukti krusial) yang memvalidasi terjangkitnya sistem terhadap insiden pencurian serta penyedotan aset *Data Exfiltration* menuju lingkungan penyerang?</summary>

**Jawaban:** Fluktuasi lonjakan perpindahan lalu lintas ukuran/volume besaran muatan data jaringan pengeluaran koneksi (Outbound Traffic) yang berekspansi di luar parameter ukuran batas normal (Contoh ukuran Gigabytes), di mana pengiriman transfer rute payload merujuk secara eksplisit menuju destinasi entitas rute alamat (IP/Domain Eksternal) luar, apalagi yang terlaksana di luar jendela periode jam waktu jam staf berbisnis.
</details>

<details>
<summary>❓ Dalam metodologi pengujian jejak kerentanan direktori log server Web (<i>Vulnerability Scanning</i> atau eksploitasi <i>Directory Enumeration</i>), apakah penanda (atribut parameter log teknis spesifik) pola utama dari serangan ini apabila peretas berupaya mengindeks rute nama fail rahasia atau *Endpoint* yang ditolak eksistensinya oleh web?</summary>

**Jawaban:** Rentetan balasan masif log *HTTP Status Code 404 Not Found*, yang menargetkan permintaan eksekusi penelusuran lokasi alamat path rute (/admin, /.git, /backup.sql). 
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap konsep esensial keilmuan investigasi *Pattern Recognition*.
- [ ] Saya mampu mendeteksi korelasi pola visual anomali berulang seperti otentikasi parameter *Brute Force* dan pola pemetaan kerentanan via anomali *404 Not Found*.
- [ ] Saya memahami pengamatan pembuktian lonjakan atribut muatan metrik respons log (Bytes Out / Data Exfiltration).
- [ ] Saya memiliki kapabilitas menerapkan inferensi analitik di tiga klaster Kategori Analitik di praktik Mini Lab SOC *Threat Detection*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS: Identifying Malicious Patterns in Network Traffic](https://www.sans.org/posters/windows-forensics-evidence-of/) — Poster dan material visual mengenai rekam jejak pola perilaku ancaman di korporat.

---

## ➡️ Besok

**Day 5: Lab & Mission: Identifikasi Serangan** — Setelah mempelajari metode analisa *Access Logs* Nginx, perburuan anomali OS Linux Windows dan kapabilitas meraba klasifikasi visibilitas *Pattern Recognition*, sekarang tiba saat penugasan simulasi komprehensif! Esok hari, Anda wajib melaksanakan praktikum integratif ekstensif yang menuntut kejelian kapabilitas terminal baris instruksi Linux (Piping `grep`, `awk`, dan `sort`). Anda ditantang mendeteksi serta memformulasi identifikasi IP penyerang krusial dari *Data Set Log* puluhan ribu entitas dan membuktikan rumusan identifikasi eskalasi (Threat Hunting). Bersiap menyusun pembuktian temuan peretasan teknis di sesi pelaporan akhir kasta *SENTINEL* minggu ke-dua ini!

---

*📅 TISS Null Teaming · Week 21 · Day 4 · SENTINEL Rank*
