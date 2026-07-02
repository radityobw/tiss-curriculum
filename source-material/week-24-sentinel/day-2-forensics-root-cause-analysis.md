# 🛡️ Week 24 · Day 2: Forensics & Root Cause Analysis

> **Rank**: SENTINEL | **Minggu ke-24**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 24 · Day 2/5 | SENTINEL Rank (Minggu 5 dari 5) | Overall: 117/120 hari (97%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengekstrak** jejak peretasan atau *Indicators of Compromise (IOCs)* dari hasil manipulasi barang bukti forensik.
2. **Menganalisis** serta mengidentifikasi celah kerentanan sumber insiden (*Root Cause Analysis*).
3. **Memetakan** aktivitas bukti temuan analisis forensik ke dalam format hierarki klasifikasi kerangka matriks *MITRE ATT&CK* (TTPs).

---

## 📖 Materi Inti

### Capstone Fase 2: Ekstraksi Bukti Indikator Insiden (IOCs)

Melanjutkan tahapan investigasi simulasi insiden pada tahap sebelumnya (Di mana sistem *Web Server* 192.168.1.100 dan basis data *Database Server* 10.0.0.55 dieksploitasi), tim spesialis SOC telah mengisolasinya dari akses internet publik jaringan sistem korporat internal (Fase Mitigasi Jaringan *Containment*) serta duplikasi penyalinan artefak operasi sistem (Pelaksanaan *Forensic Imaging*).

Investigasi tingkat arsitektur laboratorium beralih kepada pencarian **Indicators of Compromise (IOCs)** dari berkas log tersebut. *IOC* merepresentasikan entitas bukti spesifik "sidik jari digital" dari operasi ancaman (contohnya perumusan parameter: IP pelaku, kalkulasi nilai Hash identitas Malware, atau parameter pelacakan perubahan konfigurasi OS peretas).

*Temuan Investigasi Forensik Anda:*
1. **Analisis Log IIS Web Server:** Analis menemukan eksekusi berulang terhadap alamat URL parameter `/login.php?user=admin' OR '1'='1` (IOC: Temuan parameter serangan Payload SQLi).
2. **Analisis Arsitektur Memori (RAM) Database Server:** Mengeksekusi perangkat antarmuka *Volatility*, analis menemukan beroperasinya sebuah skrip anomali bertopeng penamaan `svchost.exe` palsu (yang mempunyai hasil pengujian validasi Hash: `a1b2c3d4...`) di mana penyamaran OS peladen arsitektur tersebut terus memantulkan panggilan komunikasi rute transmisi IP eksternal dari Rusia secara konstan beridentitas `45.33.22.11` (IOC: Entitas penemuan Hash Malware serta identitas IP Malicious).

### Evaluasi Analisis Akar Insiden (Root Cause Analysis)

Tugas penganalisis bukan sebatas memitigasi insiden *malware*, tetapi inspeksi analisis menuju pemecahan **Root Cause** (Akar Penyebab / Identifikasi parameter celah pertama kali aktor peretas sukses menginfiltrasi sistem perlindungan). Apabila celah eksploitasi parameter akar tersebut tidak dievaluasi, aktor peretas akan menggunakan celah yang sama pada operasi mendatang!

*Alur Analisis Root Cause:*
File Malware arsitektur di Database (`svchost.exe` penyamaran) tidak dikirim secara otomatis tanpa vektor awalan. Peretas menginisiasi transmisi intervensi rute peretasan melalui antarmuka web dengan memanfaatkan (celah aplikasi kerentanan *SQL Injection*) guna mengambil alih akses data sandi otentikasi data *Database*. Berbekal eksploitasi data otentikasi tersebut, peretas berpindah menyamping dan memasang perangkat malware OS di peladen infrastruktur data DB.
Oleh karenanya, **Root Cause (Akar Penyebab Permasalahan Infiltrasi Sistem Utama)** insiden korporat tersebut merupakan eksistensi kerentanan kode (*Vulnerability sistem Web SQL Injection*) yang tidak direspons dengan pembaruan pengamanan (*Patch/Update* arsitektur perlindungan keamanan korporasi).

### Pemetaan ke Sistem Referensi TTPs (MITRE ATT&CK Mapping)

Demi memenuhi standar formal pelaporan komunikasi intelijen ancaman tingkat eksekutif instansi maupun organisasi tingkat global, analis harus merangkum seluruh metode arsitektur penyerangan pelacakan ini menggunakan sistem matriks taksonomi pelaporan **MITRE ATT&CK Framework**.

1. Tahap pelaku menginfiltrasi perlindungan ekosistem infrastruktur web instansi melalui celah web eksploitasi *SQLi*.
 👉 **Klasifikasi Taktik:** Initial Access (Metode perolehan akses pertama masuk) | **Klasifikasi Teknik:** Exploit Public-Facing Application (ID matriks mitigasi: T1190).
2. Peretas memproses eksekusi serangan propagasi eskalasi sistem peladen menyamping lintas zona peladen web jaringan mengarah ke peladen basis data peladen.
 👉 **Klasifikasi Taktik:** Lateral Movement | **Klasifikasi Teknik:** Pemanfaatan instalasi Remote Services arsitektur (T1021).
3. Peretas memastikan operasi perlindungan menanam instalasi `svchost.exe` file penyamaran skrip rute transmisi IP eksternal Rusia.
 👉 **Klasifikasi Taktik:** Command and Control (C2) | **Klasifikasi Teknik:** Masquerading / Metode pengubahan penamaan file (T1036).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi analisis *Root Cause*!

1. Siapkan aplikasi penulisan dokumen analisis *SOC*.
2. Anda bertugas menginspeksi ekosistem insiden siber yang ditandai dengan infeksi perangkat pengunci *(Ransomware)*.
3. *Temuan Log Sistem:* Deteksi *Ransomware* tercatat mulai mengunci file pada pukul 09:05 pagi waktu peladen. Dengan analisis runut waktu mundur, log inspeksi stasiun komputer menampilkan laporan pukul 09:00: seorang pegawai internal bernama Budi mengakses klien surel email dan mengunduh lampiran instalasi mencurigakan bernama `gaji.pdf.exe` lalu mengeksekusi instruksi pembukaannya secara sistem komputer.
4. **Misi Pengujian:** Formulasikan argumen pelaporan insiden memilah bagian manakah yang difungsikan sebagai *IOC* dan komponen manakah pelacakan status yang digolongkan sebagai penentuan krisis insiden *Root Cause*!
5. **Jawaban Analis :**
 - **Parameter IOC (Indikator Kompromi):** identitas nama file virus eksekusi (`insiden.exe` ataupun `gaji.pdf.exe`), serta identifikasi parameter surel pengirim lampiran tak wajar eksternal.
 - **Kesimpulan Root Cause (Akar Penyebab Permasalahan Utama Sistem Instansi):** Minimnya penerapan edukasi fungsi tingkat pemahaman *(Security Awareness)* pengguna korporat yakni staf internal instansi bernama Budi yang terjebak taktik pengelabuan surel tipuan sosial intelijen kejahatan komunikasi (*Phishing/Social Engineering *).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah penelusuran arsitektur jejak serangan, akronim baku apakah yang merujuk pada parameter "sidik jari taktis " pelaku peretas pelacakan insiden korporat (berupa IP pelaku kejahatan sistem peladen maupun identifikasi pelacakan nilai Hash dari file virus operasi)?</summary>

**Jawaban:** Pengawasan pelacakan *Indicators of Compromise / IOCs (Indikator Kompromi Peladen)*.
</details>

<details>
<summary>❓ Dalam terminologi standar pelaporan investigasi insiden siber forensik korporasi, frasa apakah yang merepresentasikan makna parameter penentuan "Celah Kelemahan Pintu Masuk Pertama/Awal Titik Infiltrasi Utama" yang secara mutlak perlu dianalisis mitigasi sistem agar fungsi penyusupan serupa bisa ditutup peladen korporat untuk perbaikan sistem instansi?</summary>

**Jawaban:** Kesimpulan analisis parameter taktis operasi Root Cause (Akar Penyebab Insiden Siber).
</details>

<details>
<summary>❓ Mengacu pada perumusan data ensiklopedia intelijen global operasi sistem peladen korporat taktis, bilamana spesialis SOC menemukan pelaporan perilaku pelaku peretas yang menyamarkan identifikasi skrip menjadi penamaan berkas resmi (seperti pengubahan nama identitas berkas file instalasi virus menjadi klasifikasi file nama resmi *svchost.exe* OS peladen korporat), ke dalam matriks referensi manakah rutinitas pemetaan taktis *TTPs* ini diwajibkan diklasifikasikan arsitektur komputasinya?</summary>

**Jawaban:** Integrasi fungsi matriks arsitektur standar ancaman siber sedunia, yakni operasi MITRE ATT&CK Framework.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami mekanisme identifikasi ekstraksi parameter forensik pelacakan *IOCs*.
- [ ] Saya menguasai mekanisme penyimpulan analisis identifikasi operasi *Root Cause Analysis*.
- [ ] Saya menguasai klasifikasi rutinitas fungsi pemetaan parameter temuan struktur laporan ke *MITRE ATT&CK*.
- [ ] Saya paham bahwasanya keberadaan serangan virus adalah ekses konsekuensi, bukanlah mitigasi penyebab mula peladen kerentanan masalah sistem utama.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [MITRE ATT&CK: Enterprise Techniques](https://attack.mitre.org/techniques/enterprise/) — Basis taksonomi pemetaan klasifikasi parameter intelijen kerangka perilaku *TTPs* grup peretas.

---

## ➡️ Besok

**Day 3: Eradication & Remediation** — Akar masalah (Root Cause) telah terdeteksi (Kerentanan SQLi). Bukti taktis jejak serangan instalasi pelaku peretas (*IOCs*) telah diakuisisi pencatatannya (IP Rusia & fungsi algoritma identifikasi *Hash* malware). Modul pada operasi pelacakan insiden korporasi esok hari bakal berpusat pada penanggulangan eksekusi pengamanan mitigasi di fase penanggulangan : **Eradication (Pemusnahan Berkas)**. Personel *SOC* akan dikonfigurasi pengerahan operasi parameter filter jaringan untuk menyetel implementasi pencegahan *IPS Suricata* guna mengeblok akses IP peladen Rusia secara struktural permanen, membuang fungsi skrip malware dari infrastruktur *storage* perusahaan, dan pengerahan perombakan penambalan peladen instalasi *Patching Remediation* agar rutinitas infiltrasi kerentanan tak dapat direplikasikan oleh pelaku lain!

---

*📅 TISS Null Teaming · Week 24 · Day 2 · SENTINEL Rank*
