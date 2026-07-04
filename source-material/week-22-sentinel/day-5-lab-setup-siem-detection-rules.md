# 🛡️ Week 22 · Day 5: Lab & Weekly Mission Setup SIEM & Detection Rules

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓░░░░] 60% — SENTINEL Rank (Minggu 3 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░] 91% — Hari 110 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → ✅ BREACH → 🔄 SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini, kamu telah mempelajari fondasi teknis otomasi pertahanan SOC:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | SIEM Concepts & Architecture | Memahami 5 tahap operasional SIEM: *Collect, Normalize, Correlate, Alert, Store*. |
| Day 2 | Splunk Basics | Menyusun bahasa kueri pencarian *SPL* (`index`, `table`, `stats count`). |
| Day 3 | Splunk Dashboards & Alerts | Menerjemahkan kueri *SPL* menjadi *Dashboards* visual dan mengonfigurasi otomatisasi *Alerts*. |
| Day 4 | IDS/IPS: Suricata & Snort | Merancang sintaks aturan (*Rules*) sensor keamanan untuk mendeteksi dan memblokir paket berbahaya. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Aplikasi teks editor (*Notepad, VS Code, dll.*).
- Latihan ini menggunakan simulasi perancangan deteksi (*Detection Engineering*), sehingga tidak diwajibkan memiliki akses langsung ke platform SIEM asli (seperti Splunk) jika tidak tersedia.

### Misi Hari Ini: "Membangun Dinding Pertahanan (Rules Engineering)"

Di sesi ini, kamu akan bertindak sebagai *Detection Engineer*. Tugasmu adalah merancang aturan deteksi (kombinasi kueri Splunk dan aturan Suricata) untuk menangani ancaman spesifik.

### Step 1: Merakit Kueri SIEM Splunk (Pendeteksi Brute Force RDP)
1. **Skenario:** Analis mengawasi dataset Windows di `index=windows_sec`. Dicurigai ada upaya serangan *Brute Force* (tebak sandi) pada layanan *Remote Desktop* (RDP).
2. **Tugas:** Tuliskan kueri SPL yang menyaring log kegagalan *login* RDP (EventCode 4625, Logon_Type 10), lalu menghitung frekuensi serangan dari tiap alamat IP (`src_ip`).
3. **Kueri Taktis SPL:** 
   `index=windows_sec EventCode=4625 Logon_Type=10 | stats count by src_ip | where count > 20`
   *(Penjelasan: Kueri ini akan menampilkan daftar IP penyerang jika mereka telah melakukan lebih dari 20 kali percobaan gagal).*

### Step 2: Merakit Kueri Web Log (Pendeteksi Indikator XSS)
1. **Skenario:** Analis mengawasi lalu lintas *server* web di `index=web_logs`.
2. **Tugas:** Cari log yang mengindikasikan adanya injeksi parameter teks `<script>` pada URL, yang merupakan ciri khas eksploitasi *Cross-Site Scripting* (XSS).
3. **Kueri Taktis SPL:**
   `index=web_logs | search uri="*<script>*" | table _time, src_ip, uri, status`
   *(Penjelasan: Kueri ini memfilter log yang mengandung tag `<script>` pada URI, lalu menampilkannya dalam format tabel rapi yang berisi waktu kejadian, IP penyerang, bentuk *payload*, dan status respons).*

### Step 3: Meracik Aturan IPS Suricata (Pemblokiran Aktif)
1. **Skenario:** Mengetahui serangan XSS sedang terjadi, mengandalkan *Alert* di Splunk (Step 2) dinilai kurang cepat. Tim SOC memutuskan untuk memblokir serangan secara langsung menggunakan *Suricata IPS* di perimeter jaringan.
2. **Tugas:** Buat aturan *Suricata* untuk menggugurkan (*Drop*) paket data *TCP* dari jaringan luar (Internet) menuju *Web Server* internal (`192.168.1.50` port `80`) JIKA *payload* muatannya mengandung string `<script>`.
3. **Rule Proteksi IDS/IPS:**
   `drop tcp $EXTERNAL_NET any -> 192.168.1.50 80 (msg:"DROP XSS Attack Payload"; content:"<script>"; sid:90001; rev:1;)`
   *(Penjelasan: Suricata akan membaca muatan data, dan otomatis membuang (*Drop*) koneksi tersebut sebelum berhasil menyentuh Web Server).*

---

## 🎯 Weekly Mission

### Misi: "Menyusun Detection Engineering Playbook"

**Deskripsi:**
Analis SOC tingkat lanjut tidak hanya membaca log, tetapi juga mampu membuat jebakan keamanan yang proaktif (*Detection Engineering*). Pada misi ini, kamu diminta mendokumentasikan aturan-aturan deteksi dari latihan di atas ke dalam sebuah buku pedoman pertahanan.

**Tugas Mandiri:**
Buatlah rangkuman dari latihan (Step 1 hingga 3 di atas) dan simpan sebagai pedoman aturan deteksi (*Detection Rule Playbook*).

**Deliverables:**
1. Buat *file* berekstensi *Markdown* bernama `DETECTION_ENGINEERING_RULES.md`.
2. Di dalam dokumen tersebut, tuliskan penjelasan lengkap untuk ketiga aturan deteksi berikut:
   - **Rule 1 (Splunk SPL):** Kueri pendeteksi *Brute Force RDP Windows* (Logon Type 10) dengan batasan *threshold* di atas 20 kejadian.
   - **Rule 2 (Splunk SPL):** Kueri pendeteksi serangan injeksi *XSS* pada aplikasi Web.
   - **Rule 3 (Suricata IPS):** Aturan deteksi yang proaktif *menggugurkan (Drop)* lalu lintas data bermuatan string *XSS* sebelum masuk ke dalam *server* web.

**Kriteria Sukses:**
- [ ] Tersedianya *file* dokumen `DETECTION_ENGINEERING_RULES.md`.
- [ ] Dokumen mendeskripsikan secara jelas penggunaan perintah SPL Splunk (seperti `stats count` dan `table`).
- [ ] Dokumen mampu membedakan penggunaan parameter tindakan `drop` (pencegahan aktif) pada Suricata dibandingkan sekadar `alert` (peringatan pasif).

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Dalam arsitektur operasional SIEM (5 Tahap Pemrosesan), apa tahap yang berfungsi mengubah berbagai format log yang berbeda-beda (misal log Windows dan Linux) menjadi sebuah struktur data kolom (*Fields*) yang konsisten dan seragam?</summary>

**Jawaban:** Tahap Normalize (Normalisasi).
</details>

<details>
<summary>❓ [MUDAH] Saat melakukan pencarian dan analisis log di dalam platform Splunk, bahasa perintah khusus apa yang harus digunakan oleh Analis SOC?</summary>

**Jawaban:** Search Processing Language (SPL).
</details>

<details>
<summary>❓ [SEDANG] Fitur apa di dalam Splunk yang bertugas menjalankan kueri secara otomatis di latar belakang dengan interval waktu tertentu, dan mengirimkan peringatan kepada Analis jika jumlah *log* mencurigakan melampaui batas (*Threshold*) tertentu?</summary>

**Jawaban:** Alerts (Sistem Peringatan Otomatis).
</details>

<details>
<summary>❓ [SEDANG] Apa perbedaan utama dalam menangani ancaman keamanan antara perangkat *IDS (Intrusion Detection System)* dengan *IPS (Intrusion Prevention System)* di perimeter jaringan?</summary>

**Jawaban:** *IDS* bersifat pasif; sistem ini hanya mendeteksi dan mengirimkan peringatan (*Alert*) saat menemukan ancaman, namun serangan tetap lolos. Sedangkan *IPS* bersifat proaktif; jika menemukan ancaman, sistem ini akan langsung memblokir dan menggugurkan (*Drop*) koneksi tersebut sehingga serangan gagal mencapai target internal.
</details>

<details>
<summary>❓ [SULIT] Dalam penyusunan aturan (*Rule*) deteksi ancaman pada Suricata, mengapa parameter <code>content:"<script>";</code> sangat penting dan menjadi inti utama keberhasilan pendeteksian serangan XSS?</summary>

**Jawaban:** Parameter `content` menginstruksikan Suricata untuk melakukan inspeksi mendalam (Deep Packet Inspection) ke dalam isi muatan (*Payload*) data jaringan, bukan sekadar melihat alamat IP. Jika sistem menemukan kecocokan *string* teks secara persis (dalam hal ini `<script>`, yang sering digunakan dalam serangan XSS), maka Suricata dapat secara akurat memicu tindakan perlindungan. Tanpa parameter ini, sensor keamanan tidak akan dapat mengenali bentuk fisik muatan berbahaya dari sebuah eksploitasi peretasan.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya telah memahami 5 tahap siklus pemrosesan *SIEM*.
- [ ] Saya mampu mendemonstrasikan penggunaan kueri dasar *SPL* Splunk.
- [ ] Saya mengetahui fungsi penyusunan visual pelaporan (*Dashboards*) dan notifikasi (*Alerts*).
- [ ] Saya memahami struktur pembuatan aturan pertahanan aktif menggunakan sensor *IDS/IPS*.
- [ ] Saya telah menyelesaikan dokumentasi arsitektur mitigasi serangan pada tugas `DETECTION_ENGINEERING_RULES.md`.

---

## 💬 Diskusi Minggu Ini

1. Selamat, kamu kini telah menguasai konsep dasar arsitektur pusat keamanan SOC tingkat lanjut! 
Coba refleksikan peran kuat dari SIEM Splunk yang secara *Real-Time* mampu merangkum jutaan log rumit menjadi analisis peringatan instan, dipadukan dengan mesin *Suricata IPS* yang mampu memblokir paket serangan peretas secara otomatis dalam hitungan milidetik sebelum mencapai target.
Bayangkan betapa sulitnya tugas penyerang (*Red Team*) di lingkungan jaringan korporat nyata. Setiap pergerakan mereka harus menghindari jerat otomatisasi dari infrastruktur *Blue Team* yang sangat komprehensif ini.

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│                                     │
│     ⚙️ THE SIEM ARCHITECT         │
│          Week 22 Complete           │
│       "To master the logs,          │
│   is to control time and truth."    │
│                                     │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 23: Threat Hunting & Digital Forensics Intro**

Penguasaan SIEM dan IDS/IPS telah berhasil kamu delegasikan. Namun, infrastruktur keamanan pada dasarnya bekerja secara pasif (menunggu pemicuan parameter). Sensor konvensional seringkali gagal mendeteksi taktik *Advanced Persistent Threats (APT)*, yaitu kelompok peretas canggih yang bekerja layaknya aktivitas *user* biasa untuk menghindari radar peringatan.

Di tahap selanjutnya, kamu akan memasuki analisis puncak SOC: **Threat Hunting & Digital Forensics**.
Di level ini, kamu tidak lagi duduk menanti peringatan dari dasbor. Kamu akan dilatih untuk proaktif berburu anomali di sistem menggunakan panduan industri **MITRE ATT&CK Framework**, serta membedah teknik pengumpulan bukti dari penyimpanan *Disk* dan memori *RAM* melalui investigasi Forensik Digital.

> 🚀 *"The machine stops at alerts. The hunter begins in the silence."*

---

*📅 TISS Null Teaming · Week 22 · Day 5 · SENTINEL Rank*
