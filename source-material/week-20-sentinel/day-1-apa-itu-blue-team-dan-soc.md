# 🛡️ Week 20 · Day 1: Apa itu Blue Team & SOC?

> **Rank**: SENTINEL | **Minggu ke-20**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 20 · Day 1/5 | SENTINEL Rank (Minggu 1 dari 5) | Overall: 96/120 hari (80%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** peran fundamental dan tanggung jawab *Blue Team* dalam keamanan siber.
2. **Menjelaskan** konsep dan struktur *Security Operations Center* (SOC).
3. **Mendeskripsikan** alur kerja harian (daily workflow) seorang Analis SOC (SOC Analyst).

---

## 📖 Materi Inti

### Pergeseran Paradigma: Dari Penyerang Menjadi Pelindung

Setelah 5 minggu (Minggu 15-19) kamu mempelajari perspektif *Red Team* (penyerang) untuk mengeksploitasi sistem, kini kita akan beralih ke perspektif **Blue Team**. 
*Blue Team* adalah tim pertahanan. Tugas utama mereka adalah memantau, mendeteksi, mencegah, dan merespons upaya peretasan atau aktivitas mencurigakan. Jika *Red Team* berfokus pada menemukan celah eksploitasi, *Blue Team* berfokus pada pengamanan infrastruktur secara menyeluruh.

### Apa itu Security Operations Center (SOC)?

**Security Operations Center (SOC)** adalah fasilitas terpusat dalam sebuah organisasi tempat tim keamanan informasi (Information Security) secara terus-menerus memantau, mendeteksi, menganalisis, dan merespons insiden keamanan siber. 

**Tujuan utama SOC:**
- Memantau jaringan dan titik akhir (endpoints) 24/7.
- Mengidentifikasi anomali dan aktivitas mencurigakan.
- Merespons ancaman secara cepat (Incident Response).
- Melaporkan dan mendokumentasikan insiden.

### Tingkatan Analis SOC (SOC Tiers)

Organisasi SOC umumnya membagi personel ke dalam beberapa tingkatan (Tiers) berdasarkan pengalaman dan tanggung jawab operasional:

1. **Tier 1 (Triage Specialist / Alert Analyst):**
 - Personel pemantauan tahap pertama. Memantau dasbor dan peringatan (alerts) dari berbagai alat keamanan seperti SIEM, IDS, dan IPS.
 - Tugas utama: Melakukan klasifikasi awal (triage) untuk menentukan apakah peringatan merupakan ancaman nyata (True Positive) atau peringatan keliru (False Positive). Jika nyata, kasus akan dieskalasi ke Tier 2.

2. **Tier 2 (Incident Responder):**
 - Menerima eskalasi tiket dari Tier 1.
 - Melakukan investigasi mendalam (Deep Dive Analysis) untuk mengetahui bagaimana kejadian berlangsung, sumber masalah, dan sistem yang terdampak.
 - Melakukan tindakan penahanan (Containment) agar dampak insiden dapat dibatasi.

3. **Tier 3 (Threat Hunter / Lead Analyst):**
 - Personel senior. Bertugas melakukan analisis proaktif, tidak hanya bergantung pada peringatan sistem.
 - Tugas utama: Mencari ancaman (Threat Hunting) yang mungkin tidak terdeteksi oleh sistem otomatis (Advanced Persistent Threats/APT), serta melakukan analisis mendalam mengenai vektor serangan kompleks.

### Alur Kerja Harian (Daily Workflow) SOC Analyst Tier 1

Seorang Analis SOC Tier 1 biasanya memiliki rutinitas operasional berikut:
1. Mengawasi dasbor (Dashboard) SIEM.
2. Memproses peringatan (Alert) masuk.
3. Melakukan pemeriksaan (Triage): Misalnya memvalidasi aktivitas log dari IP eksternal pada waktu yang tidak wajar.
4. Mengumpulkan konteks (Context Gathering): Memeriksa riwayat log, reputasi alamat IP, dan pola aktivitas pengguna.
5. Memutuskan status: Menutup tiket bila teridentifikasi sebagai False Positive, atau melakukan eskalasi ke Tier 2 jika terindikasi True Positive.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari lakukan simulasi analisis peringatan (Triage) bagi seorang Analis SOC!

1. Siapkan catatan.
2. Posisikan diri Anda sebagai SOC Analyst Tier 1 di sebuah perusahaan e-commerce (dengan basis operasional di Indonesia).
3. Evaluasi 3 peringatan (alert) berikut dan tentukan apakah peringatan ini **False Positive (Abaikan/Log)** atau **True Positive (Eskalasi ke Tier 2)**:
 - **Alert 1:** Terdapat 5 percobaan login gagal berturut-turut pada akun admin dari alamat IP internal (192.168.1.15) pada pukul 09:00 WIB hari Senin.
 - **Alert 2:** Terdapat satu percobaan login berhasil pada akun admin web perusahaan dari alamat IP yang berlokasi di Rusia pada pukul 02:00 WIB.
 - **Alert 3:** Pemindaian antivirus mendeteksi file `laporan_keuangan.xlsx` mengandung skrip makro mencurigakan di komputer staf HR, namun langsung dikarantina dan dihapus oleh sistem pengamanan Endpoint.
4. **Analisis (Contoh):**
 - *Alert 1:* Kemungkinan kesalahan ketik oleh staf internal yang sedang bertugas. (False Positive / Memerlukan verifikasi singkat dengan pengguna bersangkutan).
 - *Alert 2:* **True Positive.** Indikasi anomali akses geografis (Geolocation Anomaly) dan waktu. Harus segera dieskalasi!
 - *Alert 3:* Ancaman nyata, namun status telah ditangani otomatis oleh sistem proteksi. (Dilakukan pencatatan log insiden; prioritas moderat/rendah untuk eskalasi lanjutan karena mitigasi sudah berjalan).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa definisi teknis yang membedakan operasional *Blue Team* dibandingkan dengan *Red Team* dalam sebuah organisasi?</summary>

**Jawaban:** *Blue Team* berfokus pada upaya defensif (pertahanan) seperti pemantauan, pendeteksian, dan mitigasi insiden, sementara *Red Team* berfokus pada pengujian ofensif, simulasi serangan, dan eksploitasi celah keamanan.
</details>

<details>
<summary>❓ Apa fungsi operasional dari seorang SOC Analyst Tier 1 (Triage Specialist)?</summary>

**Jawaban:** Memantau peringatan (alerts) sistem dan melakukan klasifikasi awal (triage) untuk membedakan antara peringatan valid (True Positive) yang perlu dieskalasi dengan peringatan keliru (False Positive).
</details>

<details>
<summary>❓ Pada tingkatan manakah seorang analis bertugas secara proaktif menganalisis dan mendeteksi ancaman tanpa menunggu munculnya peringatan otomatis (Threat Hunting)?</summary>

**Jawaban:** Tier 3 (Threat Hunter / Lead Analyst).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami fungsi operasional *Blue Team*.
- [ ] Saya mampu menjelaskan peran dan struktur operasional dari *Security Operations Center* (SOC).
- [ ] Saya dapat menguraikan tanggung jawab analis SOC pada Tier 1, Tier 2, dan Tier 3.
- [ ] Saya telah melakukan simulasi klasifikasi *Triage* sederhana pada Mini Lab.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [CrowdStrike: What is a SOC?](https://www.crowdstrike.com/cybersecurity-101/secops/security-operations-center-soc/) — Panduan komprehensif terkait struktur dan operasional SOC.

---

## ➡️ Besok

**Day 2: Security Events vs Incidents** — Setelah mempelajari fungsi SOC, Anda akan memperdalam pengetahuan tentang jenis-jenis peringatan yang dipantau. Besok, kita akan membahas perbedaan teknis antara *Security Event* dengan *Security Incident*, serta bagaimana menentukan prioritas penanganan berdasarkan klasifikasi tersebut.

---

*📅 TISS Null Teaming · Week 20 · Day 1 · SENTINEL Rank*
