# 🛡️ Week 22 · Day 2: Splunk Basics (Search Processing Language)

> **Rank**: SENTINEL | **Minggu ke-22**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 22 · Day 2/5 | SENTINEL Rank (Minggu 3 dari 5) | Overall: 107/120 hari (89%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengenali** kapabilitas operasional dan arsitektur pengolahan data pada platform *Splunk*.
2. **Menyusun** tata cara pencarian data operasional log melalui instruksi kueri *Search Processing Language* (SPL).
3. **Mengekstraksi** data analisis memanfaatkan perintah penyaringan seperti `stats`, `table`, dan seleksi *fields*.

---

## 📖 Materi Inti

### Pengantar Fungsionalitas Splunk

Dari semua ekosistem SIEM tingkat *Enterprise*, **Splunk** merupakan salah satu solusi manajemen data log operasional terbesar dan paling dominan di arsitektur pertahanan bank multinasional dan perusahaan teknologi global. Kemahiran menyusun pencarian data (*Query*) di dalam Splunk adalah sertifikasi kompetensi mutlak bagi karir analis SOC operasional modern.

Splunk memiliki kemampuan indeksasi (Indexing) berkapasitas luar biasa, menjadikannya seakan perambah mesin pencari spesifik berkinerja tinggi terhadap data mesin dan data mentah yang tersentralisasi.

### Struktur Fundamental Kueri: SPL (Search Processing Language)

Pengoperasian pencarian log pada Splunk memanfaatkan bahasa kueri khusus yang disebut **SPL (Search Processing Language)**.
Struktur instruksional ini mengadaptasi secara erat mekanisme *Piping* yang ada di lingkungan terminal Linux, di mana satu instruksi kueri akan dirangkaikan berkesinambungan menuju tahap fungsi kueri operasional selanjutnya dengan penyisipan karakter simbol `|`.

**Contoh Struktur Fungsionalitas SPL Fundamental:**

1. **Kueri Pemilahan (Filtering) Parameter Dasar:**
 `index=web_logs sourcetype=access_combined status=404`
 *(Definisi Operasional: Melakukan pencarian dari struktur tempat data "web_logs", dengan kategori format file log Apache, serta menarik hasil baris secara eksklusif hanya untuk parameter respon status galat bernilai 404).*

2. **Organisasi Formasi Tabel (`table`):**
 `index=security_logs EventCode=4625 | table _time, user, src_ip`
 *(Definisi Operasional: Melakukan pencarian catatan kegagalan masuk (EventCode 4625), namun instruksi diproses untuk tidak menyajikan susunan teks lengkap melainkan menyaringnya menjadi tiga parameter tabel komprehensif berwujud: Cap Waktu, entitas akun User, serta Alamat IP klien peretas/pengguna).*

3. **Fungsionalitas Akumulasi Kuantitatif (`stats count`):**
 `index=web_logs status=401 | stats count by src_ip | sort - count`
 *(Definisi Operasional: Mengekstrak indikasi upaya akses ditolak (401), melaksanakan operasi matematis untuk menghitung agregat jumlah frekuensi kegagalan diurutkan menurut Alamat IP pelaku (`src_ip`), lalu mendayagunakan parameter urutan dari nominal intervensi dominan yang paling terbesar menuju ke frekuensi yang terkecil). Ini merupakan metodologi utama Analis SOC mengumpulkan bukti eskalasi peretasan Brute Force.*

### Abstraksi Parameter Ekstraksi (Fields)
Splunk secara dinamis dan otomatis (schema-on-the-fly) menyeleksi dan mengekstrak blok struktur teks mentah lalu menyematkannya menjadi parameter metadata yang bisa dicari, biasa dikenal sebagai **Fields**. Contohnya, meski data teks log aslinya tak memiliki susunan tabel, sistem *Splunk* mendelegasikan secara cerdas urutan karakter IP seperti `192.168.1.1` sebagai Fields beralias/variabel `src_ip`, memudahkan penyebutan nilai tanpa pengolahan rumit.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyusun konseptual simulasi bahasa parameter SPL!

1. Asumsikan perangkat latihan ini adalah platform simulasi kueri (Anda tidak memerlukan perangkat asli saat ini).
2. Anda bertugas mengatasi eskalasi operasional. Direksi SOC melaporkan indikasi lonjakan galat di koneksi fasilitas Remote Desktop Protocol (RDP) korporat dari luar jam kerja normal. Mereka mengharapkan konfirmasi identifikasi IP penyerang terkait.
3. **Rencana Eksekusi:** Menulis kueri ekstraksi SPL untuk mencari tahu entitas penyerang di dalam indeks penyimpanan `index=win_sec`.
4. **Instruksi Eksekusi 1 (Filter Parameter Peristiwa):**
 Mencari catatan percobaan penetrasi gagal. Kueri awal: `index=win_sec EventCode=4625 Logon_Type=10`
5. **Instruksi Eksekusi 2 (Kalkulasi Matematis):**
 Merangkai kalkulasi jumlah perulangan berbasis IP klien sumber dengan operator agregasi statistik:
 `| stats count by Source_Network_Address`
6. **Integrasi Eksekusi Kueri (Urutan Ekstraktif Valid):**
 `index=win_sec EventCode=4625 Logon_Type=10 | stats count by Source_Network_Address | sort - count`
7. Sistem SIEM akan mengeksekusi ekstraksi dan seketika menyajikan agregasi IP penyerang, yang mana entitas pelapor terekstrak telah mengeksekusi serangan 5.000 kali berturut-turut pada jam bersangkutan.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Menguraikan mesin *Splunk*, apa singkatan bahasa (be SPL) yang wajib dikuasai untuk melakukan analisis penyaringan pencarian log secara interaktif di platform SIEM tersebut?</summary>

**Jawaban:** Search Processing Language.
</details>

<details>
<summary>❓ Saat mengelola tata bahasa pencarian kueri *SPL*, apa kegunaan utama instruksi parameter `table` (misal diterapkan pada <code>| table _time, src_ip</code>)?</summary>

**Jawaban:** Berfungsi menghilangkan visualisasi penyajian format baris-baris teks mentah (raw log), lantas menata ulang data operasional tersebut menjadi antarmuka tabel kolom bersih yang spesifik memuat label argumen *field* terpilih.
</details>

<details>
<summary>❓ Apabila operator SOC merumuskan parameter instruksi SPL <code>| stats count by src_ip</code>, analitis apakah yang diselenggarakan algoritma platform Splunk?</summary>

**Jawaban:** Menghitung total jumlah (frekuensi kejadian akumulatif) dari log operasional tersebut yang spesifik dikategorisasikan berdasarkan variabel alamat *IP Asal (src_ip)*.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami peran dan keunggulan *Splunk* sebagai peramban data SIEM.
- [ ] Saya cakap mendemonstrasikan implementasi logika dasar kueri *SPL*.
- [ ] Saya mengetahui penerapan manajemen modifikasi presentasi menggunakan parameter fungsi *table*.
- [ ] Saya mengenal konsep pendataan taksonomi *Fields* (Ekstraksi metadata dinamis).
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Splunk SPL Quick Reference Guide](https://www.splunk.com/pdfs/solution-guides/splunk-quick-reference-guide.pdf) — Panduan sontekan kueri instruksi dasar pemrosesan SPL dari pengembang platform Splunk.

---

## ➡️ Besok

**Day 3: Splunk Dashboards & Alerts** — Rutinitas seorang analis keamanan operasional tidak sekadar merangkai teks kueri (Search String) berulang-ulang untuk menelusuri insiden keamanan. Memantau ancaman juga memerlukan optimalisasi penyampaian notifikasi otomatis operasional. Esok hari, pemantauan SPL akan difokuskan untuk ditransformasikan sebagai antarmuka representasi pelaporan metrik keamanan *(Dashboards)* serta penyusunan fungsi notifikasi pendeteksi pencegahan respons *(Alerts)* berkelanjutan.

---

*📅 TISS Null Teaming · Week 22 · Day 2 · SENTINEL Rank*
