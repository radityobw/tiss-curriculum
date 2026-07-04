# 🛡️ Week 23 · Day 2: MITRE ATT&CK Framework

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 23 · Day 2/5 | SENTINEL Rank (Minggu 4 dari 5) | Overall: 112/120 hari (93%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** struktur kerangka kerja referensi intelijen keamanan *MITRE ATT&CK*.
2. **Menjabarkan** klasifikasi tingkatan perilaku serangan (TTPs: *Tactics, Techniques, Procedures*).
3. **Memanfaatkan** matriks *MITRE ATT&CK Navigator* sebagai pendukung dalam penyusunan hipotesis.

---

## 📖 Materi Inti

### Referensi Operasional: MITRE ATT&CK Framework

Seorang *Threat Hunter* tidak menyandarkan penelusurannya hanya pada asumsi acak. Analis wajib berpedoman pada data intelijen yang merekam seluruh taksonomi perilaku serta metode infiltrasi yang pernah digunakan oleh kelompok peretas (*Advanced Persistent Threats* / APT). Basis pengetahuan global ini dikenal sebagai **MITRE ATT&CK Framework**.

Organisasi nirlaba MITRE merumuskan matriks **ATT&CK** *(Adversarial Tactics, Techniques, and Common Knowledge)* sebagai ensiklopedia global pemetaan ancaman. Matriks ini mengklasifikasikan urutan fase serangan serta metode spesifik yang sering ditujukan terhadap sistem korporasi dan infrastruktur jaringan.

### Klasifikasi Perilaku Peretas (TTPs)

MITRE ATT&CK mengkategorisasi cara kerja serangan (dikenal sebagai *TTPs*) ke dalam tiga jenjang spesifik:

1. **Tactics (Taktik):** Menjawab *"Mengapa (Why) peretas melakukan tindakan tersebut?"*
   Taktik adalah tujuan utama (*Goal*) peretas pada fase tertentu. Contoh Taktik: *Initial Access* (Mencari akses masuk awal), *Privilege Escalation* (Meningkatkan hak akses sistem), *Defense Evasion* (Menghindari deteksi keamanan), dan *Exfiltration* (Mencuri dan memindahkan data ke luar jaringan).
2. **Techniques (Teknik):** Menjawab *"Bagaimana (How) peretas mencapai tujuan dari Taktik tersebut?"*
   Teknik adalah metode operasional serangan. Sebagai ilustrasi, jika Taktiknya adalah *Initial Access*, maka Teknik yang digunakan bisa berupa: *Phishing* (Mengirim email tipuan) atau *Exploit Public-Facing Application* (Mengeksploitasi celah kerentanan web publik).
3. **Procedures (Prosedur):** Menjawab *"Apa implementasi langkah teknis yang dilakukan secara spesifik?"*
   Prosedur adalah detail observasi serangan di lapangan. Contoh Prosedur: *Grup APT29* mendistribusikan dokumen Excel yang disisipi makro berbahaya berformat VBScript.

### Menggunakan MITRE ATT&CK Navigator

Ketika divisi SOC menerima informasi intelijen bahwa grup peretas (misalnya *APT Lazarus*) sedang mengincar sektor finansial, analis akan melakukan pemetaan ancaman menggunakan platform antarmuka bernama **ATT&CK Navigator**.

Analis dapat melihat pola operasional: *"Grup Lazarus diketahui sering menggunakan teknik persistensi dengan memodifikasi Scheduled Tasks (T1053). Berdasarkan informasi ini, kita akan membuat hipotesis untuk memburu log Windows Event ID 4698 (Pembuatan Scheduled Task baru) pada server kita."*

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari melakukan pemetaan simulasi klasifikasi TTPs!

1. Siapkan aplikasi teks (Notepad).
2. **Skenario Insiden:** *"Sistem mendeteksi anomali. Untuk memastikan keberadaannya tersembunyi dari deteksi Antivirus, peretas telah mengganti nama file malware eksekusi mereka menjadi `svchost.exe` (Meniru nama proses sistem Windows yang sah)."*
3. **Misi Analisis:** Petakan laporan skenario tersebut menurut taksonomi struktur TTPs (Taktik dan Teknik)!
4. **Evaluasi Taktik (T Pertama - *Why*):** Apa tujuan dari penggantian nama tersebut? Tujuannya adalah agar tidak terdeteksi oleh Antivirus. Berdasarkan matriks MITRE, kategori Taktiknya adalah **Defense Evasion (Penghindaran Pertahanan)**.
5. **Evaluasi Teknik (T Kedua - *How*):** Bagaimana metode peretas mengakali hal tersebut? Dengan memanipulasi dan menyamarkan nama berkas. Mengacu pada kerangka operasional matriks MITRE, Teknik yang digunakan masuk ke kategori **Masquerading (Penyamaran)**.
6. Dengan menggunakan penamaan standar ini, seluruh personel *Threat Hunter* di seluruh dunia dapat saling bertukar analisis ancaman menggunakan istilah yang seragam.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah intelijen ancaman keamanan, apa kepanjangan klasifikasi <i>TTPs</i> yang digunakan sebagai arsitektur dasar pada kerangka kerja <i>MITRE ATT&CK</i>?</summary>

**Jawaban:** Tactics, Techniques, and Procedures.
</details>

<details>
<summary>❓ Dalam pemetaan TTPs, klasifikasi manakah yang berfokus untuk menjawab objektif <i>"Mengapa peretas melakukan tindakan tersebut / Apa tujuan utamanya"</i> (contoh: <i>Privilege Escalation</i>)?</summary>

**Jawaban:** Tactics (Taktik).
</details>

<details>
<summary>❓ Jika Analis SOC mengevaluasi Taktik <i>Initial Access (Akses Awal)</i>, maka aktivitas serangan berupa <i>"Distribusi email lampiran berbahaya (Phishing)"</i> diklasifikasikan sebagai tingkatan apa pada hierarki TTPs?</summary>

**Jawaban:** Techniques (Teknik).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami fungsi matriks referensi *MITRE ATT&CK*.
- [ ] Saya menguasai perbedaan parameter *Tactics* vs *Techniques*.
- [ ] Saya mengerti taksonomi detail penerapan *Procedures*.
- [ ] Saya memahami kegunaan platform visual *ATT&CK Navigator*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [MITRE ATT&CK Matrix for Enterprise](https://attack.mitre.org/matrices/enterprise/) — Tabel ensiklopedia intelijen arsitektur referensi taksonomi *TTPs* global.

---

## ➡️ Besok

**Day 3: Digital Forensics Basics** — *Threat Hunting* umumnya dioperasikan saat insiden masih aktif. Namun, jika serangan telah selesai dan server telah terkompromi, tanggung jawab beralih pada disiplin ilmu: **Digital Forensics**. Besok, kita akan mempelajari prinsip dasar penanganan bukti digital, aturan pengelolaan barang bukti (*Chain of Custody*), dan konsep duplikasi data investigasi.

---

*📅 TISS Null Teaming · Week 23 · Day 2 · SENTINEL Rank*
