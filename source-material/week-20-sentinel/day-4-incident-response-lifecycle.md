# 🛡️ Week 20 · Day 4: Incident Response Lifecycle (PICERL)

> **Rank**: SENTINEL | **Minggu ke-20**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 20 · Day 4/5 | SENTINEL Rank (Minggu 1 dari 5) | Overall: 99/120 hari (82%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** siklus hidup kerangka kerja respons insiden keamanan (*Incident Response Framework*).
2. **Menjabarkan** 6 tahapan standar penanganan insiden dari SANS Institute / NIST (PICERL).
3. **Membedakan** antara prosedur penahanan sementara (*Containment*) dengan perbaikan mendasar (*Eradication*).

---

## 📖 Materi Inti

### Rasionalisasi Siklus Penanganan Insiden

Merespons sebuah ancaman keamanan memerlukan prosedur yang terstandarisasi. Mengambil keputusan secara impulsif—misalnya langsung mematikan server yang diretas tanpa menyimpan log—bisa merusak bukti forensik digital dan menghambat investigasi. 

Oleh karena itu, organisasi keamanan (SOC) yang matang selalu berpegang pada pedoman siklus hidup respons insiden yang distandardisasi oleh lembaga seperti NIST atau SANS Institute. Salah satu model yang paling sering digunakan di industri adalah kerangka kerja 6 tahapan **PICERL**.

### 6 Tahapan Incident Response (PICERL)

Prosedur penanganan insiden dibagi ke dalam 6 tahapan utama:

1. **Preparation (Persiapan):**
   Fase ini dilakukan sebelum insiden terjadi. Meliputi penyusunan dokumen Standar Operasional Prosedur (SOP/Runbook), pelatihan staf, konfigurasi alat pemantauan (SIEM/IDS), dan pembuatan sistem *backup* (cadangan data) yang rutin.
2. **Identification (Identifikasi/Deteksi):**
   Fase saat peringatan keamanan terpicu. Analis melakukan validasi (*Triage*) untuk memastikan apakah anomali tersebut merupakan *False Positive* atau benar-benar *Security Incident* yang nyata. Tahapan ini juga mencakup analisis log dan penelusuran ruang lingkup insiden.
3. **Containment (Penahanan/Isolasi):**
   Tindakan darurat jangka pendek untuk mencegah penyebaran kerusakan ke sistem lain. Contoh: Memutus koneksi internet pada server yang terinfeksi, atau mengisolasi komputer dari jaringan (tanpa mematikannya agar data di RAM tetap bisa diselidiki oleh tim forensik).
4. **Eradication (Pembersihan/Remediasi):**
   Upaya memperbaiki akar masalah secara permanen. Contoh: Menghapus *malware* atau *Web Shell* yang ditanam peretas, menghapus akun *backdoor*, dan menambal (*patching*) celah keamanan (misal: memperbaiki kode yang rentan *SQL Injection*).
5. **Recovery (Pemulihan):**
   Mengembalikan sistem yang terdampak agar bisa beroperasi kembali secara normal dan aman. Langkah ini meliputi pemulihan data dari *backup* (jika data utama rusak), serta memantau sistem secara ketat selama beberapa waktu untuk memastikan peretas tidak kembali masuk.
6. **Lessons Learned (Pelajaran Berharga / Evaluasi Pasca-Insiden):**
   Evaluasi yang dilakukan setelah insiden selesai ditangani. Tujuannya adalah membahas apa yang salah, apa yang berhasil, dan bagaimana memperbaiki dokumentasi *Preparation* serta konfigurasi keamanan agar insiden serupa tidak terulang di masa depan.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari berlatih mengklasifikasikan aktivitas penanganan insiden ke dalam tahapan PICERL.

1. Bacalah skenario insiden peretasan aplikasi web via celah *SQL Injection* di bawah ini.
2. Klasifikasikan setiap aktivitas ke dalam tahapan respons yang tepat.
   - **Aktivitas 1:** Analis memeriksa log Nginx dan menemukan anomali pengiriman kueri SQL berbahaya secara berulang ke *endpoint* `/login.php`.
   - **Aktivitas 2:** Tim *Developer* mengubah kode aplikasi dengan menggunakan *Prepared Statements* untuk menambal celah injeksi SQL secara permanen.
   - **Aktivitas 3:** Analis SOC menyusun jadwal simulasi respons insiden setiap kuartal dan memastikan prosedur cadangan server (DRP) telah diperbarui.
   - **Aktivitas 4:** Administrator jaringan memblokir alamat IP peretas menggunakan *Web Application Firewall* (WAF) untuk memutus serangan yang sedang berlangsung.

*Kunci Jawaban Analisis:*
- Aktivitas 1: **Identification** (Mendeteksi dan menganalisis log untuk memvalidasi insiden).
- Aktivitas 2: **Eradication** (Menghilangkan kelemahan sistem secara permanen dengan menambal celah *SQLi*).
- Aktivitas 3: **Preparation** (Menyusun prosedur latihan dan mempersiapkan strategi cadangan).
- Aktivitas 4: **Containment** (Tindakan taktis untuk menahan ancaman secara instan dengan memblokir IP).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengacu pada metodologi siklus hidup penanganan insiden dari SANS, apa kepanjangan dari akronim PICERL?</summary>

**Jawaban:** Preparation (Persiapan), Identification (Identifikasi), Containment (Penahanan/Isolasi), Eradication (Pembersihan/Remediasi), Recovery (Pemulihan), dan Lessons Learned (Evaluasi Pasca-Insiden).
</details>

<details>
<summary>❓ Apa perbedaan utama antara tindakan di fase <i>Containment</i> dengan fase <i>Eradication</i>?</summary>

**Jawaban:** Fase *Containment* bertujuan untuk menahan ancaman sementara (misal: mengisolasi jaringan) agar tidak menyebar selama insiden berlangsung. Sedangkan fase *Eradication* adalah tindakan perbaikan permanen untuk membuang ancaman dan menambal celah (misal: menghapus malware dan *patching* kerentanan).
</details>

<details>
<summary>❓ Pada tahap mana tim keamanan TI berkumpul untuk mendiskusikan apa saja hal yang bisa diperbaiki dari prosedur penanganan insiden mereka agar tidak terjadi kesalahan yang sama di masa depan?</summary>

**Jawaban:** Fase Lessons Learned (Pelajaran Berharga / Evaluasi Pasca-Insiden).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami struktur metodologi operasional siklus hidup insiden keamanan.
- [ ] Saya mampu menjelaskan ke-6 tahapan standar PICERL.
- [ ] Saya mengerti perbedaan taktis antara penahanan insiden (Containment) dan mitigasi permanen (Eradication).
- [ ] Saya telah berlatih memetakan skenario respons insiden di sesi Mini Lab.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS Institute: Incident Handler's Handbook](https://www.sans.org/white-papers/33901/) — Publikasi panduan profesional ekstensif yang mendetailkan penerapan PICERL di lingkungan operasional SOC korporasi riil.

---

## ➡️ Besok

**Day 5: Lab & Mission: Analisis Access Logs** — Pada akhir sesi minggu ini, Anda akan melakukan simulasi pemantauan keamanan (SOC). Pada lab hari ke-5, kita akan menganalisis *dataset Access Log* dari Web Server untuk mengidentifikasi keberadaan insiden keamanan, dan menerapkan alur pelaporan investigasi log secara profesional!

---

*📅 TISS Null Teaming · Week 20 · Day 4 · SENTINEL Rank*
