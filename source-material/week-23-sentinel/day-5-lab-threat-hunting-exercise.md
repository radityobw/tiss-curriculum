# 🛡️ Week 23 · Day 5: Lab & Weekly Mission Threat Hunting Exercise

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓░░] 80% — SENTINEL Rank (Minggu 4 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░] 95% — Hari 115 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → ✅ FORGE → ✅ BREACH → 🔄 SENTINEL

---

## 📝 Rekap Minggu Ini

Modul pada minggu ini berfokus pada transisi kompetensi dari pengawasan keamanan otomatis ke investigasi manual secara proaktif.

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Proactive vs Reactive Security | Membedah filosofi perburuan ancaman (Threat Hunting) menggunakan *Hypothesis-Driven Approach*. |
| Day 2 | MITRE ATT&CK Framework | Memetakan dan mengklasifikasi arsitektur perilaku serangan berdasarkan anatomi TTPs (*Tactics, Techniques, Procedures*). |
| Day 3 | Digital Forensics Basics | Menjaga kepatuhan legalitas integritas hukum *Chain of Custody* dan pembuatan kloning *Forensic Imaging / Hashing*. |
| Day 4 | Memory & Disk Forensics | Menelaah preservasi data *Volatile* (Order of Volatility) RAM serta analisis *Volatility Framework*. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Komputer dengan aplikasi pengolah dokumen (*Notepad/Markdown*).
- Koneksi internet untuk melakukan pemetaan referensi ekosistem data *MITRE ATT&CK Navigator*.

### Misi Hari Ini: "Membangun Pedoman Berburu (Hunting Playbook Engineering)"

Spesialis SOC tingkat lanjut tidak beroperasi berdasarkan laporan alarm (Alerts) semata. Mereka wajib memformulasikan prosedur tanggap terstandarisasi untuk mendeteksi ancaman spesifik yang canggih (APT). Pada sesi kali ini, praktikum difokuskan pada pengembangan arsitektur *Threat Hunting Playbook*. Dokumen panduan ini menstandarkan instruksi inspeksi tim *SOC* untuk melacak metode peretasan APT tertentu di jaringan peladen instansi.

### Step 1: Memilih Skenario (Technique MITRE)
1. Analisis tren keamanan mengindikasikan lonjakan penggunaan taktik pemeliharaan akses (*Persistence*), yakni upaya peretas menyusupkan skrip instalasi untuk menjaga agar akses tetap berjalan pasca sistem di-restart.
2. Anda melakukan verifikasi dan memilih taksonomi identifikasi teknik dari referensi matriks MITRE ATT&CK: **T1053 - Scheduled Task/Job**. (Pendekatan di sistem Windows yang menyalahgunakan layanan *Task Scheduler* untuk mengeksekusi beban muatan ancaman peretas secara terjadwal).

### Step 2: Merumuskan Hipotesis (The Hunter's Hypothesis)
1. Berdasarkan parameter klasifikasi matriks teknik (T1053) tersebut, rumuskan parameter asumsi awal atau hipotesis investigasi.
2. *Contoh Formulasi Hipotesis:*
 "Terdapat probabilitas bahwa elemen peretas *Advanced Persistent Threat (APT)* sedang menjaga status persistensi sistem peladen korporat. Skenario hipotesis memperhitungkan kemungkinan afiliasi pelaku telah menyalahgunakan aplikasi sistem *Windows Scheduled Tasks* (T1053), yang dikonfigurasi guna eksekusi skrip koneksi belakang *(Backdoor)* secara repetitif pada periode jam non- sistem."

### Step 3: Penetapan Parameter Sumber Log (Data Sources) dan Sintaks Kueri
1. Anda wajib menentukan sumber pelaporan parameter penciptaan penjadwalan fungsi pada arsitektur Windows OS.
2. Dokumentasi: parameter eksekusi pelaporan Windows Security Event (Beridentitas referensi Event ID **4698** - *A scheduled task was created*).
3. *Rancangan Dasar Kueri Splunk (SIEM Hunting Syntax):*
 `index=windows_sec EventCode=4698 | table _time, ComputerName, Task_Name, Task_Content`
 *(Parameter eksekusi sintaks ini menugaskan filterisasi terhadap penciptaan penjadwalan tak wajar dan menyajikannya ke wujud tabel kolom waktu eksekusi, identitas sistem komputer, serta detail aplikasi instruksi eksekusi penjadwalan yang termuat).*

---

## 🎯 Weekly Mission

### Misi: "Buku Pedoman Perburuan (Threat Hunting Playbook)"

**Deskripsi:** Aktivitas di atas merupakan metodologi penyajian dokumen panduan. *Threat Hunter* bertugas memberikan peta penelusuran arsitektur ancaman kepada analis keamanan lapis utama agar operasi pemindaian jaringan dapat berjalan terukur.

**Tugas Mandiri:** Mengacu kepada wawasan dan alur pengerjaan pada rutinitas praktik (Step 1 hingga 3) di simulasi *Hands-On Lab*, transformasikan ketiga komponen arsitektur analisis tersebut ke dalam bentuk format pelaporan Buku Pedoman *(Hunting Playbook)*.

**Deliverables:**
1. Satu (1) buah artefak repositori dokumen penugasan berwujud berkas `THREAT_HUNTING_PLAYBOOK.md`.
2. Struktur komponen pelaporan operasi yang terdiri dari empat (4) parameter spesifik:
 - **Taktik & Teknik MITRE:** Penyertaan parameter identifikasi klasifikasi ID taksonomi (Misal: *T1053 Scheduled Task*).
 - **Hipotesis (Hypothesis):** Penulisan parameter narasi deskriptif konseptual investigasi dugaan indikasi serangan.
 - **Sumber Data (Log Sources):** pendataan spesifik tipe sistem *Event ID* (Atau klasifikasi file log pengawasan jaringan).
 - **Tindakan Lanjut (Triage/Mitigation):** Penjelasan langkah teknikal instruksional forensik jika hipotesis terkonfirmasi (Contoh langkah operasi: Eksekusi perintah pengisolasian akses *Containment* sistem koneksi jaringan lalu instruksikan pengamanan integritas akuisisi pembekuan fungsi parameter klaster *Volatility RAM Image Extraction*).

**Kriteria Sukses:**
- [ ] Tersedia pelaporan arsip instalasi korporasi `THREAT_HUNTING_PLAYBOOK.md`.
- [ ] Mampu memaparkan pencantuman referensi kode identifikasi operasi taktik serangan standar kerangka taksonomi *MITRE ATT&CK* matriks secara komprehensif.
- [ ] Mendemonstrasikan perumusan hipotesis sistem pengujian pendeteksian yang merujuk pada pengerahan data analisis pelaporan keamanan *(Log Analysis Event ID)*.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Mengacu pada pedoman standar industri arsitektur pencarian ancaman (Threat Hunting), istilah spesifik apakah yang digunakan untuk merujuk pada metodologi analisis di mana analis membentuk argumen asumsi pengujian serangan ("Peretas menyisipkan eksploitasi skrip Powershell") terlebih dahulu sebelum melaksanakan validasi penyisiran berkas log?</summary>

**Jawaban:** Pendekatan arsitektur Berbasis Hipotesis (Hypothesis-Driven Approach).
</details>

<details>
<summary>❓ [MUDAH] Di klasifikasi referensi parameter arsitektur pengamanan pelaporan ensiklopedia *MITRE ATT&CK*, singkatan istilah hierarki <i>TTPs</i> mewakili klasifikasi perilaku eksploitasi peretas yang merupakan akronim terminologi apa?</summary>

**Jawaban:** Representasi pengelompokan tingkatan Tactics, Techniques, dan parameter operasi Procedures (TTPs).
</details>

<details>
<summary>❓ [SEDANG] Berkaitan dengan kapabilitas prosedur forensik penegakan keamanan, mengapa penataan serta pengendalian tata tertib pembatasan dan perlindungan pelaporan riwayat parameter log dokumentasi *Chain of Custody* disyaratkan mutlak dalam proses akuisisi penyitaan barang elektronik kejahatan?</summary>

**Jawaban:** Tanpa parameter riwayat kontrol pengawasan (Log kronologis yang memuat data personil dan stempel parameter perpindahan akses), maka parameter legitimasi integritas validasi keamanan bukti tak dapat dikonfirmasi dan status validasi barang digital akan didiskualifikasi keberlakuannya oleh entitas otoritas badan peradilan instansi (sebagai data parameter korup/data tampering kompromi sistem).
</details>

<details>
<summary>❓ [SEDANG] Dalam penyelesaian parameter perolehan aset sistem forensik berwujud <i>Forensic Imaging</i>, algoritma kapabilitas verifikasi matematis integritas kriptografi (seperti <i>SHA-256</i>) memiliki status klasifikasi penyegelan yang biasa diistilahkan menggunakan sebutan fungsi analitis apa?</summary>

**Jawaban:** Implementasi fungsi kalkulasi arsitektur (Perhitungan *Hash* algoritma /Fungsi perlindungan fungsi Checksum).
</details>

<details>
<summary>❓ [SULIT] Dalam panduan perlindungan manajemen sistem insiden parameter prosedur penanganan sistem insiden taktis *Incident Response*, jika arsitektur sistem penyimpanan korporasi terinfeksi aplikasi ancaman *Ransomware*, prosedur pengerahan melarang operator keamanan memutus sumber daya instalasi kelistrikan (<i>Shutdown</i>) peladen; parameter rasional spesifik apa yang menyebabkan pembatasan akses mitigasi fungsi darurat tersebut?</summary>

**Jawaban:** Kebijakan intervensi keamanan mengacu pada arsitektur penyusunan retensi penyebaran parameter blok *Order of Volatility*. Perangkat ruang memori arsitektur *RAM* operasi OS komputer (yang senantiasa menampung status fungsi *Decryption Key / Kunci Dekripsi* arsitektur kriptografi Malware Ransomware OS saat OS komputer berjalan pasif maupun aktif) memiliki karakteristik penyimpanan *Volatile* (Mudah hilang/Menguap lenyap dengan siklus parameter listrik statis). Segala intervensi operasi pemutusan tegangan sumber OS atau perintah perombakan parameter log instruksi restart akan secara menghapus seluruh nilai instruksi dekripsi ini, sehingga restorasi arsip spesifik OS tak dapat dikembalikan lagi secara fungsi keamanan korporasi selamanya.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya menguasai pendayagunaan konsep pengerahan referensi fungsi taktis matriks TTPs perlindungan *MITRE ATT&CK Framework*.
- [ ] Saya memahami struktur prosedur hipotesis intelijen fungsi pengawasan *Threat Hunting Playbook*.
- [ ] Saya mengetahui dan memahami standar kepatuhan regulasi pencatatan instalasi dokumen kronologis *Chain of Custody*.
- [ ] Saya menguasai mekanisme perlindungan integritas sistem duplikasi pendataan parameter bayangan peladen *Forensic Imaging*.
- [ ] Saya sanggup membuktikan implementasi fungsi arsitektur pengerahan operasi pengamanan perumusan modul dokumen penugasan log `THREAT_HUNTING_PLAYBOOK.md`.

---

## 💬 Diskusi Minggu Ini

1. Selamat! Dirimu telah menyelesaikan materi intelijen dan forensik digital (*Threat Hunting & Digital Forensics*). Berdasarkan perbandingan antara sistem deteksi otomatis (SIEM/IPS) dan metode pelacakan proaktif manual (*Threat Hunting*), bagaimana pandanganmu tentang keseimbangan integrasi keduanya di dalam arsitektur SOC? Mengapa korporasi multinasional tidak bisa hanya mengandalkan otomatisasi untuk melawan ancaman *Advanced Persistent Threats (APT)*?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🕵️ THE CYBER DETECTIVE │
│ Week 23 Complete │
│ "Machines catch noise. │
│ Humans hunt the silence." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 24: Capstone — Full Cycle Defense & Graduation**

Kurikulum TISS Null Teaming telah mencapai kulminasi. Tidak ada lagi teori baru yang akan diperkenalkan. Esok hari, kamu akan dihadapkan pada ujian pamungkas : **Capstone Project & Graduation Ceremony**. Seluruh ilmu yang telah diserap—dari kriptografi, eksploitasi kerentanan aplikasi web (XSS/SQLi), pemindaian jaringan (*Nmap*), konfigurasi sensor dan pemantauan (*Splunk/Suricata*), hingga prosedur forensik dan *Threat Hunting*—akan diintegrasikan secara komprehensif. Kamu diwajibkan menyusun laporan teknis lengkap respons insiden (*Full Incident Response Triage Report*) sebagai syarat penyerahan kelulusan untuk menyandang gelar spesialis **SENTINEL**. Persiapkan dirimu untuk ujian simulasi akhir!

---

*📅 TISS Null Teaming · Week 23 · Day 5 · SENTINEL Rank*
