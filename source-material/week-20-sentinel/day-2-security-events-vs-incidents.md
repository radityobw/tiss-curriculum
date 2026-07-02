# 🛡️ Week 20 · Day 2: Security Events vs Incidents

> **Rank**: SENTINEL | **Minggu ke-20**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 20 · Day 2/5 | SENTINEL Rank (Minggu 1 dari 5) | Overall: 97/120 hari (81%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara *Security Event* (Peristiwa Keamanan) dan *Security Incident* (Insiden Keamanan).
2. **Memahami** proses klasifikasi dan eskalasi peringatan (alerts) dalam operasional SOC.
3. **Mengaplikasikan** konsep Triase (Triage) untuk memprioritaskan peringatan berdasarkan tingkat ancaman.

---

## 📖 Materi Inti

### Klasifikasi Aktivitas: Event vs. Incident

Dalam infrastruktur pemantauan SOC, terdapat jutaan data log aktivitas (aktivitas jaringan, akses aplikasi, eksekusi proses) yang tercatat setiap harinya. Analis membagi aktivitas-aktivitas tersebut menjadi dua klasifikasi utama:

**1. Security Event (Peristiwa Keamanan):**
Setiap kejadian (observasi) pada sistem atau jaringan yang terekam. Mayoritas peristiwa (event) bersifat rutin dan tidak membahayakan.
*Contoh Security Event:*
- Proses otentikasi (login) pengguna yang sukses.
- Peringatan pemblokiran *port* rutin oleh *Firewall*.
- Akses ke berkas administratif oleh staf TI yang berwenang.

**2. Security Incident (Insiden Keamanan):**
Suatu *Event* atau rangkaian *Event* yang berdampak negatif terhadap prinsip kerahasiaan, integritas, dan ketersediaan data (CIA Triad), atau secara nyata melanggar kebijakan keamanan organisasi.
*Contoh Security Incident:*
- Aktivitas akses *login* yang sukses setelah rentetan ratusan kegagalan *login* dari IP yang sama (indikasi serangan *Brute Force* yang berhasil).
- Enkripsi massal file di penyimpanan server oleh proses tidak dikenal (indikasi *Ransomware*).
- Indikasi transfer data berukuran sangat besar (GB) ke alamat IP yang tidak dikenal (indikasi eksfiltrasi data/Data Exfiltration).

> **Konsep Kunci:** Setiap *Incident* berawal dari *Event*, namun tidak semua *Event* merupakan sebuah *Incident*.

### Proses Triase (Triage) dan Klasifikasi Keamanan

Saat sistem pemantauan (SIEM/IDS) memberikan peringatan otomatis, Analis SOC bertugas memvalidasi peringatan tersebut lewat proses **Triase (Triage)** untuk mengklasifikasikan tingkat ancamannya:

1. **False Positive:** Peringatan dipicu oleh sistem, namun setelah divalidasi, aktivitas tersebut bersifat wajar dan sah. (Contoh: Notifikasi anomali pemindaian *port* yang ternyata merupakan aktivitas rutin pengujian *Nmap* oleh tim audit TI internal).
2. **True Positive:** Peringatan dipicu oleh sistem dan secara sah tervalidasi sebagai ancaman keamanan nyata.
3. **True Negative:** Aktivitas normal yang diabaikan secara tepat oleh sensor keamanan.
4. **False Negative:** Aktivitas peretasan atau ancaman nyata yang gagal dideteksi oleh sistem pengamanan (tidak ada peringatan/alert yang terpicu). Hal ini memerlukan audit atau analisis forensik log independen (Threat Hunting).

### Eskalasi Insiden

Apabila analis SOC Tier 1 memvalidasi peringatan sebagai ancaman (*True Positive*) atau berpotensi menjadi insiden, maka analis wajib melakukan proses **Eskalasi**. Proses eskalasi akan memindahkan kewenangan penyelesaian kasus kepada Tier 2 atau Tim Respons Insiden yang memiliki kemampuan mitigasi lebih mendalam.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari berlatih menentukan perbedaan klasifikasi Event dan Incident.

1. Bacalah ketiga skenario di bawah ini.
2. Tentukan klasifikasinya berdasarkan hasil evaluasi (*Event* vs *Incident*, dan *True Positive*, *False Positive*, *True Negative*, atau *False Negative*).

*Skenario A:* Perangkat IDS memicu peringatan (Alert) mendeteksi payload *SQL Injection* pada rute aplikasi `app.internal.corp`. Setelah dilakukan korelasi data, IP asal serangan tersebut adalah milik tim audit internal (*Penetration Tester*) yang sedang menjalankan pemindaian terjadwal.
*Skenario B:* Sensor tidak memberikan peringatan anomali lalu lintas apapun. Namun keesokan harinya, administrator sistem menemukan 50GB file log operasional telah dipublikasikan di domain eksternal.
*Skenario C:* Sistem Data Loss Prevention (DLP) mengirimkan peringatan karena mendeteksi bahwa akun `staff_keuangan` telah mengunduh rekap gaji bulan lalu ke perangkat penyimpanan eksternal, sesuai dengan siklus rekonsiliasi akhir bulan.

*Analisis:*
- Skenario A: Termasuk **Event**. Klasifikasi: **False Positive** (Aktivitas terdeteksi berbahaya namun memiliki otorisasi).
- Skenario B: Termasuk **Incident**. Klasifikasi: **False Negative** (Ancaman nyata berhasil dieksekusi tanpa deteksi sensor peringatan).
- Skenario C: Termasuk **Event**. Klasifikasi: **False Positive** (Aktivitas diidentifikasi melanggar oleh DLP, tetapi secara operasional merupakan kegiatan yang sah).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa definisi operasional yang membedakan antara *Security Event* dan *Security Incident*?</summary>

**Jawaban:** *Security Event* adalah segala kejadian yang tercatat pada log sistem (baik aktivitas rutin maupun anomali), sedangkan *Security Incident* adalah *event* spesifik yang tervalidasi berdampak negatif terhadap kerahasiaan, integritas, dan ketersediaan sistem atau melanggar aturan keamanan (pelanggaran aktual).
</details>

<details>
<summary>❓ Dalam terminologi pemantauan SOC, apakah istilah untuk suatu peringatan sistem (alert) yang mengindikasikan serangan , namun setelah proses verifikasi terbukti sebagai aktivitas administratif yang sah?</summary>

**Jawaban:** False Positive.
</details>

<details>
<summary>❓ Apa klasifikasi sensor peringatan pada kejadian di mana peretas sukses mengekstraksi data perusahaan tanpa memicu satupun peringatan atau notifikasi keamanan dari sistem IDS/IPS?</summary>

**Jawaban:** False Negative.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami definisi *Security Event* dan *Security Incident*.
- [ ] Saya mampu menjelaskan klasifikasi *False Positive*, *True Positive*, dan *False Negative*.
- [ ] Saya mengerti proses triase dan urgensi tahapan eskalasi.
- [ ] Saya telah menganalisis skenario validasi peringatan di sesi Mini Lab.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [NIST: Computer Security Incident Handling Guide (SP 800-61 Rev. 2)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf) — Panduan standar industri dari NIST untuk identifikasi dan klasifikasi insiden keamanan.

---

## ➡️ Besok

**Day 3: Log Sources & Syslog** — Setelah mampu mengklasifikasi insiden, tahap selanjutnya adalah mempelajari dari mana asal informasi (event/alert) tersebut. Besok, kita akan menganalisis komponen utama dalam visibilitas keamanan, yakni pengelolaan rekam jejak aktivitas (Logs). Kita akan membahas berbagai jenis log sistem, sumber log (Log Sources), dan pengenalan protokol *Syslog*.

---

*📅 TISS Null Teaming · Week 20 · Day 2 · SENTINEL Rank*
