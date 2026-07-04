# 🛡️ Week 23 · Day 1: Proactive vs Reactive Security

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 23 · Day 1/5 | SENTINEL Rank (Minggu 4 dari 5) | Overall: 111/120 hari (92%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara paradigma keamanan pasif (*Reactive Security*) dan keamanan aktif (*Proactive Security / Threat Hunting*).
2. **Memahami** konsep berburu ancaman menggunakan pendekatan hipotesis (*Hypothesis-Driven Approach*).
3. **Mengenali** peran penting insting analitis analis (elemen manusia) dalam mendeteksi anomali.

---

## 📖 Materi Inti

### Keterbatasan Keamanan Reaktif

Pada modul-modul sebelumnya, kamu telah mengonfigurasi *Splunk* untuk membunyikan *Alerts* dan memasang *Suricata* untuk memblokir serangan secara otomatis. Model pertahanan yang sepenuhnya bergantung pada sensor keamanan untuk memberitahu jika ada bahaya disebut sebagai **Reactive Security (Keamanan Reaktif)**. Analis di sini bertindak pasif menunggu peringatan muncul.

Masalahnya, kelompok peretas tingkat tinggi (*Advanced Persistent Threats* / APT) sering menggunakan teknik mutakhir yang tidak memicu sensor standar. Mereka seringkali membajak alat atau perintah sistem administrator yang sah (*Living off the Land*). Akibatnya, SIEM akan menganggap lalu lintas tersebut normal dan tidak membunyikan peringatan.

Oleh karena itu, organisasi tingkat lanjut beralih mengadopsi **Proactive Security (Keamanan Proaktif)** melalui praktik **Threat Hunting**.

### Apa itu Threat Hunting?

**Threat Hunting (Perburuan Ancaman)** adalah kegiatan investigasi secara proaktif dan iteratif mencari jejak serangan siber yang berhasil menyusup lolos dari sistem keamanan otomatis.

Di sinilah letak kelemahan Kecerdasan Buatan (AI) dan otomasi. Otomasi sistem itu kaku; mereka mendeteksi berdasarkan pola *Rules* lama. Sebaliknya, analis manusia memiliki insting deduktif dan analisis kontekstual untuk merasakan ada "sesuatu yang salah" meskipun sistem tidak membunyikan alarm.

### Hypothesis-Driven Approach (Pendekatan Berbasis Hipotesis)

Seorang *Threat Hunter* tidak akan melakukan pencarian data log secara membabi-buta (*blind search*). Mereka menggunakan kerangka metodologi yang disebut **Pendekatan Berbasis Hipotesis (*Hypothesis-Driven Approach*)**.

Tahapannya meliputi:
1. **Membuat Hipotesis:** Analis menyusun dugaan logis berdasarkan ancaman terkini. Misal: *"Ada laporan serangan Ransomware terbaru (Jenis X) yang memanfaatkan layanan Remote Desktop (RDP). Hipotesis saya, sistem RDP di server Keuangan kita mungkin telah diuji coba ditembus pada akhir pekan lalu."*
2. **Investigasi & Berburu:** Berbekal dugaan spesifik, analis mencari log *Splunk* khusus pada *Event ID 4624 (Logon Success)* untuk protokol RDP pada server Keuangan, spesifik di hari Sabtu dan Minggu malam.
3. **Menemukan Pola:** Analis mengevaluasi log dan mencari korelasi anomali, contohnya IP asing yang sering terhubung.
4. **Triage & Respons:** Jika dugaan tersebut terbukti benar dan terjadi serangan, analis menjalankan tanggap insiden dan segera membuatkan *Rule SIEM* baru untuk IP/Taktik tersebut (Mengubah metode perlindungan dari *Proaktif* menjadi otomatis *Reaktif*).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang sebuah hipotesis perburuan ancaman (*Threat Hunting Hypothesis*)!

1. **Skenario Laporan Intelijen:** Sebuah grup peretas 'DarkBear' diketahui mengirimkan email (*phishing*) berisi *file* PDF jebakan. Ketika PDF itu dibuka oleh pegawai, *file* itu diam-diam akan mengeksekusi terminal `powershell.exe` di latar belakang (tanpa disadari pengguna) untuk mengunduh *malware*.
2. **Rencana Operasional:** Rumuskan hipotesis taktis untuk memburu ancaman ini di jaringan Anda!
3. **Hipotesis yang Dihasilkan Analis:**
   *"Berdasarkan intelijen grup DarkBear, hipotesis saya adalah pegawai kita mungkin telah membuka PDF jahat tersebut. Saya akan mencari log aktivitas pembuatan proses Windows (Event ID 4688). Saya akan memfilter secara spesifik kejadian anomali di mana aplikasi pembaca PDF (`Acrobat.exe` atau `Foxit.exe`) bertindak sebagai proses induk (Parent Process) yang anehnya melahirkan anak proses berbentuk terminal `powershell.exe`."*
4. Anda baru saja melakukan *Threat Hunting* pola pikir! Anda mendeteksi potensi ancaman logis jauh sebelum SIEM mengetahui *malware* tersebut adalah ancaman.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar dalam alur kerja antara <i>Reactive Security</i> dengan <i>Proactive Security (Threat Hunting)</i>?</summary>

**Jawaban:** Keamanan Reaktif bersifat pasif, Analis menunggu peringatan (*Alert*) dari SIEM/IDS sebelum melakukan investigasi. Keamanan Proaktif bersifat proaktif, Analis secara aktif "berburu" melalui data log secara mandiri menggunakan asumsi dugaan serangan, tanpa menunggu sistem membunyikan alarm.
</details>

<details>
<summary>❓ Mengapa peran insting dan logika manusia (<i>Human Element</i>) sangat krusial dalam praktik <i>Threat Hunting</i> dibandingkan sekadar mengandalkan mesin SIEM/AI?</summary>

**Jawaban:** Mesin pengaman otomatis dan AI beroperasi secara kaku menggunakan pola serangan (*Rules* / *Signatures*) yang sudah diketahui sebelumnya. Peretas APT menggunakan taktik baru atau taktik "normal" yang disalahgunakan untuk mengelabui deteksi otomatis. Analis manusia dapat menggunakan intuisi analitis, pemahaman konteks bisnis, dan pemikiran lateral untuk mendeteksi anomali perilaku sistem yang tidak terdeteksi mesin.
</details>

<details>
<summary>❓ Jika Analis SOC mulai mencari log secara terarah berdasarkan asumsi: "Saya curiga *hacker* mengeksploitasi akses VPN di luar jam kerja minggu lalu", pendekatan metodologi pencarian apa yang sedang diterapkannya?</summary>

**Jawaban:** Pendekatan Berbasis Hipotesis (*Hypothesis-Driven Approach*).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami keterbatasan solusi otomasi pasif (*Reactive Security*).
- [ ] Saya mengetahui alur kerja perburuan ancaman proaktif (*Proactive Security / Threat Hunting*).
- [ ] Saya dapat merumuskan skenario metodologi pencarian berbasis hipotesis (*Hypothesis-Driven Approach*).
- [ ] Saya memahami mengapa keunggulan intuisi manusia diperlukan dalam menemukan peretas mahir.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [CrowdStrike: What is Threat Hunting?](https://www.crowdstrike.com/cybersecurity-101/threat-hunting/) — Referensi komprehensif mengenai konsep fundamental dan filosofi praktik operasional *Threat Hunting*.

---

## ➡️ Besok

**Day 2: MITRE ATT&CK Framework** — Menyusun hipotesis perburuan yang akurat membutuhkan acuan taktik peretas standar global. Besok, kita akan membedah salah satu dokumen intelijen terpenting di industri keamanan siber: **MITRE ATT&CK Framework**. Anda akan belajar mengenali tahapan taktis manuver penyerang (*Tactics, Techniques, and Procedures* - TTPs) dan bagaimana memetakannya di *ATT&CK Navigator*.

---

*📅 TISS Null Teaming · Week 23 · Day 1 · SENTINEL Rank*
