# 🛡️ Week 24 · Day 2: Forensics & Root Cause Analysis

> **Rank**: SENTINEL | **Minggu ke-24**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 24 · Day 2/5 | SENTINEL Rank (Minggu 5 dari 5) | Overall: 117/120 hari (97%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengekstrak** jejak peretasan atau *Indicators of Compromise (IOCs)* dari barang bukti forensik.
2. **Menganalisis** serta mengidentifikasi celah kerentanan yang menjadi akar masalah (*Root Cause Analysis*).
3. **Memetakan** aktivitas bukti temuan analisis ke dalam matriks *MITRE ATT&CK*.

---

## 📖 Materi Inti

### Capstone Fase 2: Ekstraksi Bukti Indikator Insiden (IOCs)

Melanjutkan tahapan investigasi simulasi insiden pada tahap sebelumnya (di mana *Web Server* `192.168.1.100` dan *Database Server* `10.0.0.55` terkompromi), tim SOC telah mengisolasi *server* tersebut dari jaringan (Tahap *Containment*) dan membuat salinan forensiknya (Tahap *Forensic Imaging*).

Investigasi kini beralih pada pencarian **Indicators of Compromise (IOCs)**. *IOC* adalah "sidik jari digital" dari aktivitas serangan (contoh: Alamat IP pelaku, nilai *Hash* dari *malware*, atau nama *file* spesifik yang dibuat oleh peretas).

*Temuan Investigasi Forensik Anda:*
1. **Analisis Log IIS Web Server:** Analis menemukan eksekusi berulang terhadap URL `/login.php?user=admin' OR '1'='1`.
   *(IOC: Bukti serangan Payload SQL Injection).*
2. **Analisis Memori (RAM) Database Server:** Mengeksekusi *Volatility*, analis menemukan sebuah proses bernama `svchost.exe` palsu (dengan nilai Hash: `a1b2c3d4...`) yang diam-diam memancarkan sinyal ke alamat IP eksternal dari Rusia (`45.33.22.11`).
   *(IOC: Nilai Hash Malware dan alamat IP Malicious).*

### Evaluasi Analisis Akar Insiden (Root Cause Analysis)

Tugas analis SOC bukan sekadar memburu dan menghapus *malware*, tetapi mencari **Root Cause** (Akar Penyebab), yaitu celah pertama yang dimanfaatkan peretas untuk masuk ke dalam sistem. Jika celah ini tidak ditutup, peretas akan kembali masuk keesokan harinya menggunakan rute yang sama.

*Alur Analisis Root Cause:*
*Malware* `svchost.exe` palsu di server Database tidak muncul dengan sendirinya. Peretas masuk ke jaringan publik melalui *Web Server* menggunakan celah *SQL Injection* untuk mencuri kredensial (kata sandi) administrator. Dengan kredensial tersebut, peretas bergerak menyamping ke server Database dan memasang *malware* jarak jauh.
Oleh karena itu, **Root Cause (Akar Masalah)** dari insiden ini adalah adanya celah *SQL Injection* pada web perusahaan yang belum diperbaiki (*unpatched*).

### Pemetaan ke MITRE ATT&CK (MITRE Mapping)

Untuk memenuhi standar formal pelaporan keamanan, analis merangkum metode serangan tersebut menggunakan matriks **MITRE ATT&CK Framework**.

1. Tahap peretas masuk ke *Web Server* menggunakan *SQLi*.
   👉 **Taktik:** Initial Access | **Teknik:** Exploit Public-Facing Application (T1190).
2. Peretas menggunakan kredensial hasil retasan web untuk *Login RDP* menyamping ke server Database.
   👉 **Taktik:** Lateral Movement | **Teknik:** Remote Services (T1021).
3. Peretas memasang skrip berbahaya dengan nama file proses Windows palsu (`svchost.exe`).
   👉 **Taktik:** Command and Control | **Teknik:** Masquerading (T1036).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi analisis *Root Cause*!

1. Siapkan aplikasi pengolah teks (Notepad/VS Code).
2. Anda sedang menangani insiden infeksi *Ransomware* di kantor.
3. *Temuan Log:* Deteksi *Ransomware* mulai mengunci *file* pada pukul 09:05 pagi. Anda memeriksa mundur ke pukul 09:00 dan menemukan log bahwa Budi, seorang pegawai, menerima email lampiran aneh bernama `gaji.pdf.exe` dan mengkliknya.
4. **Misi:** Identifikasi mana yang merupakan *IOC* dan mana yang merupakan *Root Cause*!
5. **Jawaban Analis:**
   - **IOC (Indikator Kompromi):** Nama *file* virus (`gaji.pdf.exe`) dan alamat email pengirim mencurigakan.
   - **Root Cause (Akar Masalah):** Rendahnya edukasi keamanan (*Security Awareness*) pada pegawai (Budi) sehingga ia menjadi korban manipulasi *Phishing/Social Engineering*.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam investigasi jejak serangan, apa singkatan (atau akronim) yang merujuk pada "sidik jari" bukti kejahatan peretas, seperti IP pelaku atau nilai <i>Hash malware</i>?</summary>

**Jawaban:** IOC (Indicators of Compromise).
</details>

<details>
<summary>❓ Istilah apa yang merujuk pada identifikasi "Celah Kelemahan Pintu Masuk Awal" yang menjadi penyebab pertama mengapa peretas bisa masuk ke dalam jaringan?</summary>

**Jawaban:** Root Cause (Akar Penyebab / Akar Masalah).
</details>

<details>
<summary>❓ Jika analis mendapati bahwa peretas menyamarkan nama <i>file malware</i>-nya agar terlihat seperti file sistem Windows resmi (misal: <code>svchost.exe</code>), ke dalam matriks standar global manakah perilaku taktis ini dipetakan?</summary>

**Jawaban:** MITRE ATT&CK Framework (Kategori Taktik: Masquerading).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami fungsi dari bukti jejak siber (*IOCs*).
- [ ] Saya menguasai mekanisme penarikan kesimpulan akar masalah (*Root Cause Analysis*).
- [ ] Saya mampu memetakan perilaku serangan ke dalam standar *MITRE ATT&CK*.
- [ ] Saya memahami bahwa infeksi *malware* hanyalah akibat, sedangkan celah keamanan adalah penyebab awalnya (*Root Cause*).
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [MITRE ATT&CK: Enterprise Techniques](https://attack.mitre.org/techniques/enterprise/) — Basis pengetahuan global untuk memetakan taktik dan teknik yang digunakan oleh grup peretas tingkat lanjut.

---

## ➡️ Besok

**Day 3: Eradication & Remediation** — Akar masalah (Root Cause) telah ditemukan (Celah SQLi). Bukti jejak peretas (*IOCs*) telah diamankan (IP Rusia & *Hash malware*). Besok, tim SOC akan melancarkan fase pembersihan: **Eradication & Remediation**. Kita akan mengonfigurasi IPS Suricata untuk memblokir IP Rusia secara permanen, memusnahkan *file malware* dari *server*, dan menambal celah aplikasi (*Patching*) agar peretas tidak bisa masuk lagi.

---

*📅 TISS Null Teaming · Week 24 · Day 2 · SENTINEL Rank*
