# 🛡️ Week 20 · Day 4: Incident Response Lifecycle (PICERL)

> **Rank**: SENTINEL | **Minggu ke-20**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 20 · Day 4/5 | SENTINEL Rank (Minggu 1 dari 5) | Overall: 99/120 hari (82%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** siklus hidup kerangka operasional respons insiden keamanan (Incident Response Framework).
2. **Menjabarkan** 6 tahapan baku standar penanganan ancaman dari SANS Institute / NIST (PICERL).
3. **Membedakan** antara prosedur isolasi teknis (Containment) dengan mitigasi kerentanan (Eradication).

---

## 📖 Materi Inti

### Rasionalisasi Siklus Penanganan Insiden

Merespons sebuah anomali atau ancaman terkonfirmasi memerlukan prosedur yang terstandarisasi. Proses pengambilan keputusan teknis secara impulsif—seperti dengan langsung menghentikan instansi server yang bermasalah secara spontan tanpa dokumentasi bukti (logging)—bisa mengakibatkan kompromi terhadap bukti forensik digital atau malah memicu degradasi produktivitas ketersediaan sistem operasional jangka panjang yang keliru. 

Organisasi keamanan (SOC) yang matang selalu mengandalkan pedoman siklus hidup respons insiden yang distandardisasi oleh asosiasi seperti NIST (National Institute of Standards and Technology) atau SANS Institute. Salah satu model yang dominan di industri adalah kerangka fase 6 tahapan **PICERL**.

### 6 Tahapan Incident Response (PICERL)

Prosedur metodologi operasional ini disusun ke dalam 6 tahapan utama:

1. **Preparation (Persiapan):**
 Kegiatan dasar organisasi yang dieksekusi saat fase sistem masih normal (sebelum krisis). Meliputi penyusunan dokumen prosedural operasional keamanan (Runbook/SOP), program pendidikan kesadaran, pelaporan alat pengawasan sistem (SIEM), dan implementasi mekanisme perlindungan redundansi cadangan data rutin.
2. **Identification (Identifikasi/Deteksi):**
 Observasi saat peringatan terpicu. Analis mengkaji, melaksanakan validasi *Triase (Triage)*, hingga memverifikasi indikasi parameter ancaman spesifik (seperti IP anomali, deteksi muatan *payload* eksploitasi, hingga indikasi eksfiltrasi log jaringan) sehingga menetapkan *Security Event* tersebut tereskalasi menjadi valid *Security Incident*.
3. **Containment (Penahanan/Isolasi):**
 Aktivitas taktis darurat yang ditujukan demi mencegah kerusakan sistem menyebar dan melakukan pembatasan propagasi ancaman tanpa menghilangkan rekaman metadata investigasi peretasan. Contoh eksekusi: Menghentikan rute *interface* perangkat koneksi jaringan peladen web (memblokir internet) namun mesin tersebut wajib dibiarkan aktif bekerja guna dilakukan pengambilan sampel bukti RAM *memory* di proses forensik selanjutnya.
4. **Eradication (Pembersihan/Mitigasi):**
 Upaya proaktif remediasi dan restorasi terhadap asal muasal akses penyerang (kerentanan). Merupakan langkah perbaikan di lapisan arsitektur. Contoh eksekusi: Mengekstirpasi seluruh eksistensi instalasi *malware* (misal penghapusan *Web Shell*), eliminasi manipulasi kredensial peretas (*backdoors*), sekaligus mempublikasikan (*Patching*) versi kode/sistem yang aman (perbaikan terhadap kueri SQL rentan agar tidak dieksploitasi kedua kalinya).
5. **Recovery (Pemulihan):**
 Restorasi konfigurasi sistem operasional secara menyeluruh sesuai standar arsitektur bisnis organisasi. Langkah krusial ini memerlukan jaminan kepastian validitas dari tahapan *Eradication*, restorasi volume partisi *database* dari berkas cadangan (backup), sekaligus validasi parameter monitor operasional (selama periode tertentu) yang memastikan peretas tak mendisrupsi ulang target.
6. **Lessons Learned (Pelajaran Berharga / Evaluasi Pasca-Insiden):**
 Kajian post-insiden sistematis yang menelaah akar penyebab kerentanan struktural, merunut ulang proses respons teknis para staf SOC, serta pembuatan revisi konfigurasi pencegahan dan peningkatan kompetensi analis untuk merombak parameter pengawasan di periode fase *Preparation* (sebagai bentuk umpan balik).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melakukan identifikasi operasional tahapan respons penanganan insiden *PICERL*.

1. Diberikan suatu skenario insiden peretasan aplikasi Web dengan eksploitasi celah tipe *SQL Injection (SQLi)* yang mengubah integrasi data produk aplikasi perusahaan.
2. Deskripsikan aktivitas-aktivitas instruksi di bawah ini ke dalam terminologi fase respons kerangka kerja.
 - **Aktivitas 1:** Analis mengaudit rincian log Nginx dan menemukan anomali frekuensi pengiriman parameter kueri SQL berbahaya dari rentang IP asing menuju *endpoint* `/login.php`.
 - **Aktivitas 2:** Tim operasional *backend* memutakhirkan implementasi aplikasi dengan kode validasi kueri (menggunakan *Prepared Statements* dan mekanisme sanitasi *Input Parameter*) demi menutup *logic* serangan injeksi tersebut.
 - **Aktivitas 3:** Analis IT menyusun kebijakan simulasi prosedur cadangan server (DRP) setiap kuartal guna persiapan skenario peretasan server tingkat masif.
 - **Aktivitas 4:** Operator memblokir parameter masuk eksternal dari domain IP pelaku menggunakan *Web Application Firewall* (WAF) guna memutuskan koneksi peretas pada saat itu juga.

*Evaluasi Analisis Praktik:*
- Aktivitas 1: **Identification** (Analisis bukti korelasi parameter peringatan, penelusuran validitas log kejadian insiden).
- Aktivitas 2: **Eradication** (Menghilangkan komponen kelemahan yang dieksploitasi peretas (menambal celah injeksi SQL)).
- Aktivitas 3: **Preparation** (Menyediakan prosedur keamanan komprehensif, latihan teknis simulasi operasional).
- Aktivitas 4: **Containment** (Tindakan taktis darurat isolasi jaringan guna menghentikan penetrasi secara instan).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengacu pada terminologi standar industri mengenai kerangka metodologi siklus hidup peretasan insiden, apakah definisi dari akronim PICERL?</summary>

**Jawaban:** Preparation (Persiapan), Identification (Identifikasi), Containment (Penahanan/Isolasi), Eradication (Pembersihan/Remediasi), Recovery (Pemulihan/Restorasi), dan Lessons Learned (Evaluasi Pembelajaran).
</details>

<details>
<summary>❓ Dalam terminologi mitigasi taktis SOC, apa pembeda obyektif operasional dari fase teknis Containment dibandingkan fase teknis Eradication?</summary>

**Jawaban:** Fase *Containment* ditekankan pada implementasi aktivitas darurat sementara untuk mencegah perluasan eksfiltrasi data jaringan pada saat serangan berlangsung (misalnya memisahkan/memutus sambungan koneksi instansi jaringan secara isolasi fisik). Sedangkan fase *Eradication* mengacu kepada identifikasi perbaikan secara lebih mendasar melalui perombakan kode konfigurasi infrastruktur secara permanen untuk menutup akses celah agar penyusupan dari vektor tersebut tidak dapat dilakukan lagi.
</details>

<details>
<summary>❓ Pada tahap mana dari metodologi PICERL tim keamanan TI melakukan identifikasi evaluasi komprehensif tentang kekurangan/keberhasilan proses identifikasi dan respons, serta pemaparan prosedur revisi arsitektur keamanan?</summary>

**Jawaban:** Fase Lessons Learned (Pelajaran Berharga / Review Evaluasi Pasca-Insiden).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami struktur metodologi operasional siklus hidup insiden.
- [ ] Saya mampu menguraikan definisi dari masing-masing 6 tahapan (PICERL).
- [ ] Saya mengidentifikasi peran krusial perbedaan teknis pada langkah isolasi ancaman darurat (Containment) serta mitigasi perbaikan kerentanan dasar eksploitasi (Eradication).
- [ ] Saya telah melakukan penentuan tahapan prosedur dalam rincian latihan Mini Lab.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS Institute: Incident Handler's Handbook](https://www.sans.org/white-papers/33901/) — Publikasi panduan profesional ekstensif yang mendetailkan penerapan PICERL di lingkungan operasional SOC korporasi riil.

---

## ➡️ Besok

**Day 5: Lab & Mission: Analisis Access Logs** — Pada akhir sesi minggu ini, Anda akan melakukan simulasi analisis pemantauan. Pada lab integratif hari ke-5, kita akan menganalisis dataset *Access Log Web Server* guna mengidentifikasi *Incident* berupa vektor injeksi dan menerapkan dokumentasi respons kerangka teknis *PICERL*.

---

*📅 TISS Null Teaming · Week 20 · Day 4 · SENTINEL Rank*
