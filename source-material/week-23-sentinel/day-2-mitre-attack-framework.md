# 🛡️ Week 23 · Day 2: MITRE ATT&CK Framework

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 23 · Day 2/5 | SENTINEL Rank (Minggu 4 dari 5) | Overall: 112/120 hari (93%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** struktur kerangka kerja referensi intelijen *MITRE ATT&CK*.
2. **Menjabarkan** klasifikasi tingkatan perilaku serangan (TTPs: *Tactics, Techniques, Procedures*).
3. **Memanfaatkan** matriks *MITRE ATT&CK Navigator* sebagai pendukung dalam penyusunan hipotesis.

---

## 📖 Materi Inti

### Referensi Operasional : MITRE ATT&CK Framework

Spesialis *Threat Hunter* tidak menyandarkan penelusurannya hanya pada asumsi acak. Analis wajib berpedoman pada data intelijen tersentralisasi yang merekam seluruh taksonomi perilaku serta metode infiltrasi yang didokumentasikan dari operasi kejahatan kelompok peretas tingkat lanjut (*Advanced Persistent Threats* / APT) secara komprehensif. Matriks referensi intelijen global ini dikenal sebagai **MITRE ATT&CK Framework**.

Organisasi lembaga riset terkemuka MITRE merumuskan matriks **ATT&CK** *(Adversarial Tactics, Techniques, and Common Knowledge)* sebagai ensiklopedia pemetaan perilaku ancaman, mengklasifikasikan urutan fase manuver taktis, serta operasi infiltrasi spesifik yang berpotensi ditujukan terhadap sistem korporasi keamanan dan peladen infrastruktur jaringan.

### Klasifikasi Perilaku Peretas (TTPs)

MITRE ATT&CK mengkategorisasi tingkat eksekusi eksploitasi serangan (Model *TTPs*) ke dalam tiga jenjang granular analitis:

1. **Tactics (Taktik):** Menjawab *"Mengapa (Why) peretas mengoperasikan manuver teknis tersebut?"*
 Taktik memformulasikan tujuan utama (*Goal*) eksekutor serangan pada fase infiltrasi tertentu. Contoh parameter Taktik mencakup kategori: *Initial Access* (Titik masukan akses mula ke sistem peladen), *Privilege Escalation* (Aktivitas mengangkat tingkatan otorisasi), *Defense Evasion* (Praktik menyembunyikan log dari pendeteksian pengamanan jaringan), *Exfiltration* (Penarikan aset data korporat ke luar perimeter peladen).
2. **Techniques (Teknik):** Menjawab *"Bagaimana (How) peretas meraih target dari Taktik operasional tersebut?"*
 Teknik menjelaskan modus operasional metodologi serangan jaringan. Sebagai ilustrasi, apabila tujuan operasional Taktiknya adalah *Initial Access*, maka pemanfaatan Tekniknya bisa mencakup: metode *Phishing* (Taktik Email tipuan rekayasa logis) atau prosedur manipulasi rute eksploitasi peretasan perangkat lunak *Exploit Public-Facing Application* (Pemanfaatan keamanan peladen celah web sistem eksternal).
3. **Procedures (Prosedur):** Menjawab *"Apa implementasi perincian langkah taktis yang dikonfigurasikan secara spesifik?"*
 Prosedur menyajikan deskripsi implementasi arsitektur peretasan logis di tingkat terperinci (Contoh pendefinisian Prosedur: *Grup kelompok APT29* secara mendemonstrasikan distribusi dokumen Excel bermuatan perintah makro eksekusi sistem VBScript logis berstatus berbahaya).

### Penggunaan MITRE Navigator untuk 
Ketika divisi operasional keamanan mendeteksi intelijen bahwa afiliasi peretas terorganisir (misal *Grup APT Lazarus*) mengincar infrastruktur finansial, analis akan melakukan pemetaan matriks arsitektur ancaman (*Threat Mapping*) mendayagunakan platform antarmuka bernama **ATT&CK Navigator**.
Platform ini mengaplikasikan parameter visual pada matriks. Analis dapat membaca pola operasional intelijen: *"Afiliasi operasi Lazarus terekam memiliki kecenderungan mengeksploitasi teknik modifikasi persistensi Scheduled Tasks (T1053). Sebagai respon perlindungan, penyusunan fungsi perburuan log Windows ID 4698 akan dieksekusi."*

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melaksanakan pemetaan simulasi klasifikasi kasta TTPs!

1. Siapkan aplikasi penyusun teks laporan.
2. Analisis laporan insiden taktis berikut: *"Terdapat laporan bahwa jaringan telah terkompromi. Untuk memastikan eksistensi jahatnya tersembunyi dari parameter deteksi Antivirus sistem operasi korporasi, peretas memanipulasi aset eksekusi berkas sistem. Ia mendelegasikan perintah penggantian penamaan file malware eksekutabel eksternal menyamar menjadi identitas file `svchost.exe` (Meniru entitas perangkat Windows resmi)."*
3. **Misi Analisis:** Petakan laporan skenario tersebut menurut taksonomi logis struktur TTPs (Taktik dan Teknik)!
4. **Evaluasi Taktik (T parameter Pertama - *Why*):** Apa rasional tujuan manipulasi tersebut? Tujuannya adalah mereduksi peluang dideteksi sistem pengamanan (*Antivirus*). Berdasarkan taksonomi matriks MITRE, kategori Taktiknya adalah klasifikasi **Defense Evasion (Penghindaran Pertahanan keamanan)**.
5. **Evaluasi Teknik (T parameter Kedua - *How*):** Bagaimana metode peretas mengakali hal tersebut? Dengan modifikasi manipulatif merubah status penamaan berkas. Mengacu pada kerangka operasional matriks MITRE, fungsi Tekniknya masuk ke pengelompokkan taksonomi **Masquerading (Operasi Penyamaran Pengelabuan entitas File Sah)**.
6. Dengan berpedoman pada nomenklatur standar taktis mitigasi MITRE ini, personel *Threat Hunter* di setiap korporasi multinasional dapat bertukar pemetaan analisis menggunakan struktur format taksonomi logis yang seragam.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah infrastruktur intelijen ancaman keamanan, apa kepanjangan nomenklatur klasifikasi perilaku operasional <i>TTPs</i> yang digunakan sebagai basis arsitektur taksonomi pada kerangka kerja operasi <i>MITRE ATT&CK</i>?</summary>

**Jawaban:** Tactics, Techniques, and Procedures.
</details>

<details>
<summary>❓ Dalam implementasi analisis pemetaan TTPs, parameter klasifikasi manakah (antara Tactics atau Techniques) yang secara difokuskan untuk memecahkan rumusan objektif <i>"Mengapa (Why) entitas peretas mengimplementasikan eksploitasi serangan tersebut / Apa sasaran perolehan akhir yang dikehendaki"</i> (contoh taksonomi: <i>Privilege Escalation</i>)?</summary>

**Jawaban:** Tactics (Taktik Operasional).
</details>

<details>
<summary>❓ Pada spesifikasi perumusan matriks pemetaan pertahanan korporasi, bilamana analis keamanan (*Threat Hunter*) mengevaluasi parameter Taktik tingkat <i>Initial Access (Upaya Akses Mula)</i>, maka implementasi teknikal operasional peretasan berupa <i>"Distribusi surel lampiran bermuatan eksploitasi logis (Phishing)"</i> diklasifikasikan sebagai tingkatan apa pada pengelompokan hierarki taksonomi logis sistem TTPs?</summary>

**Jawaban:** Pengelompokan spesifikasi Techniques (Teknik).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami fungsi matriks intelijen *MITRE ATT&CK*.
- [ ] Saya menguasai perbedaan arsitektur parameter *Tactics* vs *Techniques*.
- [ ] Saya mengerti taksonomi detail teknikal penerapan parameter *Procedures*.
- [ ] Saya paham tata guna platform referensi visual *ATT&CK Navigator*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [MITRE ATT&CK Matrix for Enterprise](https://attack.mitre.org/matrices/enterprise/) — Tabel matriks ensiklopedia intelijen arsitektur referensi taksonomi *TTPs* grup ancaman tingkat keamanan global.

---

## ➡️ Besok

**Day 3: Digital Forensics Basics** — *Threat Hunting* umumnya dioperasikan saat merespons aktivitas peretasan yang masih berpotensi aktif di jaringan. Jika sistem peladen operasi sudah hancur akibat eksploitasi serangan terprogram, peran penelusuran dialihkan pada ranah disiplin : **Digital Forensics**. Sesi operasi mendatang akan menguraikan secara ekstensif standar kepatuhan regulasi operasi pengolahan penyitaan keamanan *(Chain of Custody)* beserta teknik penduplikasian perlindungan aset barang bukti sistem yakni operasi *Forensic Imaging*!

---

*📅 TISS Null Teaming · Week 23 · Day 2 · SENTINEL Rank*
