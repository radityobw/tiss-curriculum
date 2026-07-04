# 🛡️ Week 21 · Day 4: Pattern Recognition

> **Rank**: SENTINEL | **Minggu ke-21**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 21 · Day 4/5 | SENTINEL Rank (Minggu 2 dari 5) | Overall: 104/120 hari (87%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** pentingnya pengenalan pola anomali (*Pattern Recognition*) dalam metode analisis log skala besar (*Big Data Logs*).
2. **Mengidentifikasi** pola visual untuk serangan repetitif seperti *Brute Force* dan *Vulnerability Scanning*.
3. **Mendeteksi** parameter yang merepresentasikan insiden pencurian data (*Data Exfiltration*).

---

## 📖 Materi Inti

### Efisiensi Deteksi Ancaman: Logika *Pattern Recognition*

Dalam ekosistem *Enterprise* yang sebenarnya, Analis SOC tidak melakukan investigasi log dengan membaca setiap baris teks secara manual satu per satu. Hal ini tidak mungkin dilakukan karena *server* produksi skala besar dapat menghasilkan puluhan ribu baris log setiap detiknya.

Titik pembeda seorang Analis mahir terletak pada penerapan **Pattern Recognition (Pengenalan Pola)**. SOC *Analyst* yang terlatih tidak membaca teks secara keseluruhan, melainkan memfokuskan pemindaian visual pada deteksi lonjakan (*spike*), repetisi aneh, atau tren abnormal pada struktur data log.

### 3 Klasifikasi Pola Anomali Serangan Dasar

**1. Pola Serangan Tebak Sandi (Brute Force / Password Guessing)**
- *Ciri Visual:* Terjadi lonjakan ratusan atau ribuan log autentikasi dari satu IP eksternal yang sama dalam rentang waktu singkat (detik/menit). Barisan log ini secara konsisten menghasilkan status kegagalan (*Event ID 4625* di Windows atau *HTTP 401 Unauthorized* di Nginx).
- *Indikator Kesuksesan Serangan:* Jika rentetan log kegagalan tersebut mendadak berhenti dan diakhiri dengan SATU log keberhasilan (Status *HTTP 200 OK* atau *Event ID 4624 Logon Success*), ini mengonfirmasi bahwa penyerang telah berhasil menebak kata sandi dan berhasil masuk.

**2. Pola Pemindaian Kerentanan (Vulnerability Scanning / Web Directory Brute-Force)**
- *Ciri Visual:* Sebuah IP eksternal melakukan rentetan permintaan (*Request*) ke berbagai rute direktori *server* secara berurutan dan cepat (seperti `/.git/config`, `/.env`, `/backup.zip`, `/admin.php`). Indikator utama anomali ini adalah deretan status `404 Not Found`.
- Ini adalah tanda bahwa penyerang menggunakan alat pemindai otomatis (*Vulnerability Scanner* / *Directory Bruteforcer*) seperti *Nikto*, *Gobuster*, *Nmap*, atau *Ffuf* untuk memetakan infrastruktur aplikasi web.

**3. Pola Pencurian Data (Data Exfiltration)**
- *Ciri Visual:* Pola ini tidak ditandai dengan rentetan kegagalan, melainkan lonjakan drastis pada atribut ukuran pengiriman data (*Response Size* / *Bytes Out*).
- Secara normal, interaksi aplikasi web hanya menghabiskan puluhan *Kilobytes* (KB). Jika terdapat aktivitas jaringan keluar (*Outbound Traffic*)—misalnya via HTTP *POST* atau *FTP*—menuju IP asing dengan ukuran transmisi raksasa mencapai ribuan *Megabytes* (GB) pada jam tidak wajar (misal: pukul 2 pagi), maka ini adalah anomali *True Positive*.
- Pola lonjakan transfer data tak wajar ini mengindikasikan insiden pencurian aset/database (*Data Exfiltration*).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melatih kepekaan visual *Pattern Recognition* untuk 3 indikator anomali!

1. Amati ketiga kutipan log berikut dan identifikasi jenis ancamannya:
2. **Kategori A (Log Windows Event):**
   `14:00:01 | ID 4625 | User: Admin | IP: 10.0.5.5`
   `14:00:02 | ID 4625 | User: Admin | IP: 10.0.5.5`
   `14:00:03 | ID 4625 | User: Admin | IP: 10.0.5.5`
   *(Analisis: Pengulangan log kegagalan autentikasi (4625) dari IP yang sama secara cepat. Ini adalah indikator pola peretasan Brute Force).*
3. **Kategori B (Log Akses Peladen Web Nginx):**
   `GET /.git/config HTTP/1.1 | 404 Not Found`
   `GET /backup.sql HTTP/1.1 | 404 Not Found`
   `GET /phpinfo.php HTTP/1.1 | 404 Not Found`
   *(Analisis: Repetisi pencarian *file* rahasia yang menghasilkan 404. Ini merepresentasikan pola Directory Scanning / Vulnerability Scanning).*
4. **Kategori C (Traffic Jaringan Gateway Firewall Log):**
   `15:30:00 | SRC: Server_Database | DST: IP_Eksternal_Asing | Bytes Out: 8.5 GB`
   *(Analisis: Lonjakan transfer data keluar (8.5 GB) dari server *database* internal menuju IP publik asing adalah indikator kuat terjadinya Data Exfiltration).*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam pengawasan log web, jika terdapat puluhan log berstatus <i>HTTP 401 Unauthorized</i> atau <i>Event ID 4625 Logon Failed</i> secara beruntun dan cepat dari IP yang sama, indikasi ancaman pola apakah ini?</summary>

**Jawaban:** Indikasi serangan *Brute Force* (atau *Password Guessing* / Penebakan kata sandi terotomatisasi).
</details>

<details>
<summary>❓ Dalam analisis log <i>Firewall</i>, parameter anomali apa yang merupakan bukti krusial terjadinya pencurian data (<i>Data Exfiltration</i>) menuju server penyerang?</summary>

**Jawaban:** Lonjakan drastis pada ukuran lalu lintas keluar (*Outbound Traffic* / *Bytes Out*) yang tidak wajar (misal, bergiga-giga byte) menuju alamat IP/Domain eksternal yang tidak dikenal, terutama di luar jam kerja operasional.
</details>

<details>
<summary>❓ Dalam eksploitasi pencarian rute tersembunyi (<i>Vulnerability Scanning</i> atau <i>Directory Enumeration</i>), apa parameter log spesifik yang dihasilkan saat penyerang gagal mencari <i>file</i> rahasia di <i>server web</i>?</summary>

**Jawaban:** Rentetan balasan masif berupa log kode status *HTTP 404 Not Found*.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami konsep esensial investigasi berbasis *Pattern Recognition*.
- [ ] Saya mampu mendeteksi pola anomali repetitif seperti *Brute Force* dan pemetaan kerentanan (*404 Not Found*).
- [ ] Saya memahami cara membuktikan indikasi pencurian data melalui lonjakan metrik pengiriman log (*Bytes Out*).
- [ ] Saya mampu mengidentifikasi ancaman berdasarkan 3 klasifikasi Kategori Analitik pada Mini Lab.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS: Identifying Malicious Patterns in Network Traffic](https://www.sans.org/posters/windows-forensics-evidence-of/) — Referensi visual mengenai rekam jejak perilaku ancaman keamanan siber di infrastruktur perusahaan.

---

## ➡️ Besok

**Day 5: Lab & Mission: Identifikasi Serangan** — Setelah mempelajari metode analisis *Access Logs* Nginx, perburuan anomali OS Windows/Linux, dan konsep *Pattern Recognition*, sekarang tiba saatnya simulasi komprehensif! Esok hari, kamu akan melaksanakan praktikum yang menuntut keahlian manipulasi teks menggunakan antarmuka baris perintah Linux (kombinasi `grep`, `awk`, dan `sort`). Kamu akan ditantang untuk mencari IP penyerang dari puluhan ribu baris data log mentah dan memformulasikan hasil *Threat Hunting* tersebut.

---

*📅 TISS Null Teaming · Week 21 · Day 4 · SENTINEL Rank*
