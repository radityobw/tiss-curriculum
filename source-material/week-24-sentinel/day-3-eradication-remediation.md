# 🛡️ Week 24 · Day 3: Eradication & Remediation

> **Rank**: SENTINEL | **Minggu ke-24**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 24 · Day 3/5 | SENTINEL Rank (Minggu 5 dari 5) | Overall: 118/120 hari (98%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengeksekusi** tahapan *Eradication* (Pemusnahan) guna membersihkan seluruh jejak dan perangkat peretas dari jaringan server.
2. **Meracik** aturan keamanan pada *IPS (Intrusion Prevention System)* seperti Suricata/Snort untuk memblokir alamat IP penyerang secara permanen.
3. **Menerapkan** tahap respons pasca insiden: *Recovery & Remediation* (Pemulihan operasional dan Penambalan celah keamanan).

---

## 📖 Materi Inti

### Capstone Fase 3: Pembersihan Ekosistem Korporat (Eradication)

Melanjutkan proses penanganan insiden kemarin (di mana peretas mengeksploitasi SQLi dan menanam *malware* duplikat `svchost.exe`), siklus PICERL kini memasuki fase teknis: **Fase Eradication (Pemusnahan / Penghapusan Indikator Kompromi)**.

*Eradication* adalah langkah strategis untuk menghapus bersih seluruh artefak berbahaya yang ditinggalkan oleh peretas (*malware*, akun *backdoor*, atau skrip jahat) agar infrastruktur tidak lagi memiliki celah tersembunyi yang bisa digunakan penyerang di kemudian hari.

*Langkah Teknis Eradication di Server yang Dikarantina:*
1. **Kill Process:** Menghentikan proses aktif (*Process termination*) dari `svchost.exe` palsu yang berjalan di RAM Server Database.
2. **Hapus File Malware:** Menghapus file skrip dan *malware* secara permanen dari *Hard Disk*.
3. **Reset Kata Sandi Korporat:** Karena peretas telah berhasil meretas kredensial otentikasi, seluruh kata sandi akun administrator dan *user database* diwajibkan untuk direset (*Password Reset*) secara menyeluruh!

### Restrukturisasi IOC ke Parameter Pertahanan (IPS Rule Mitigation)

Setelah memusnahkan *malware* dari sistem, *SOC Analyst* harus memitigasi risiko agar IP eksternal peretas (misalnya `45.33.22.11`) tidak bisa lagi mencoba menyusup ke jaringan. Insinyur keamanan bertugas memodifikasi aturan pencegahan jaringan (*IPS Rule*) berdasarkan data *Indicators of Compromise (IOC)* yang ditemukan saat proses forensik.

*Peracikan Sintaks Parameter Pencegahan (IPS Rule Logic):*
`drop ip 45.33.22.11 any -> $HOME_NET any (msg:"DROP Malicious Russian IP"; sid:999999; rev:1;)`
*(Penjelasan: Aturan ini menginstruksikan sistem IDS/IPS (seperti Suricata/Snort) untuk men-drop (menggugurkan/memblokir) seluruh lalu lintas paket data yang bersumber masuk dari alamat IP peretas tersebut).*

### Fase Recovery: Penambalan Celah Akar Permasalahan (Root Cause)

Fase *Recovery* (Pemulihan operasional bisnis) BUKAN sekadar menyambungkan kembali server dari status karantina ke jaringan internet publik. Jika Anda men-*online*-kan kembali server yang masih memiliki celah *SQL Injection* tanpa menambalnya terlebih dahulu, maka peretas dari belahan dunia mana pun dapat kembali meretas sistem tersebut dalam hitungan menit dengan cara yang sama!

*Tindakan Remediasi (Patching & Maintenance):*
1. Berkoordinasi dengan tim *Developer* untuk memperbaiki kode aplikasi web (menerapkan filter keamanan dan sanitasi input agar kerentanan SQLi tertambal sempurna).
2. Setelah *Vulnerability Scanning* memastikan celah sudah tidak bisa dieksploitasi lagi, barulah infrastruktur dinobatkan aman dan dapat disambungkan kembali ke internet publik *(Online)*.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi pengambilan keputusan pasca insiden (*Eradication & Recovery*)!

1. Anda sedang menangani insiden infeksi *Backdoor Malware* pada server perusahaan.
2. *Status Analitik Saat Ini:* Tim SOC mengonfirmasi bahwa file *malware* telah terhapus bersih (*Eradicated*) dari *Hard Disk*. Saat ini, server masih berstatus terisolasi dari internet (*Containment*).
3. **Misi:** Manajemen eksekutif mendesak Anda untuk segera menormalkan kembali akses layanan internet agar operasional bisnis tidak terganggu. Keputusan apa yang wajib Anda komunikasikan kepada manajemen?
4. **Laporan Jawaban Analis (Jawaban):**
   *"Saya TIDAK merekomendasikan pengaktifan layanan akses peladen saat ini juga! Walaupun malware telah dibersihkan (Eradicated), tim IT belum melaksanakan penambalan (Patching) terhadap akar kerentanan (Root Cause) yang menjadi pintu masuk malware tersebut. Mengeksekusi fase pemulihan (Recovery) dari isolasi tanpa melakukan perbaikan celah keamanan sama saja dengan membiarkan peretas lain untuk menyusup ulang lewat lubang kerentanan yang sama."*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam standar penanganan insiden PICERL, tahap operasional manakah yang bertujuan memusnahkan eksistensi malware, pengguna penyusup, maupun skrip jahat dari server korporat?</summary>

**Jawaban:** Fase Eradication (Pemusnahan).
</details>

<details>
<summary>❓ Saat tim spesialis mengonfigurasi aturan keamanan pada IPS korporat (Suricata / Snort), instruksi (berawalan huruf D) apa yang digunakan untuk langsung memblokir/menggugurkan paket dari IP peretas?</summary>

**Jawaban:** Instruksi `drop`.
</details>

<details>
<summary>❓ Mengapa analis SOC sangat menentang tahap pemulihan server ke internet publik (Recovery) jika perusahaan belum melakukan penambalan celah keamanan (Patching)?</summary>

**Jawaban:** Karena jika server disambungkan ke internet tanpa menambal *Root Cause* (akar celah kerentanan yang dipakai peretas menyusup), maka penyerang dapat dengan mudah mengeksploitasi ulang celah tersebut untuk menginfeksi server kembali.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami langkah-langkah dalam respons insiden fase *Eradication*.
- [ ] Saya fasih membaca aturan *IPS Rule (Drop)* dari temuan *IOCs* forensik.
- [ ] Saya menguasai urgensi penambalan kerentanan (*Remediation/Patching*).
- [ ] Saya paham bahwasanya fase *Recovery* mensyaratkan perbaikan celah agar peretas tidak menyusup kembali.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS: The 6 Steps of Incident Response](https://www.sans.org/white-papers/33901/) — Dokumentasi resmi SANS tentang pedoman 6 fase penanganan insiden siber standar industri *(termasuk fase Eradication & Recovery)*.

---

## ➡️ Preview Besok

**Day 4: Incident Report Writing** — Krisis telah berlalu dan ancaman telah dieradikasi. Server operasional bisnis berhasil dipulihkan (*Online*). Namun bagi tim *Blue Team*, tugas belum selesai sebelum semua terdokumentasi! Esok hari, kita akan berfokus pada **Penulisan Laporan Insiden Siber (Incident Report)**. Anda akan belajar mensintesis kronologi kejadian (*Timeline*), memaparkan akar masalah (*Root Cause*), serta menyusun rekomendasi perbaikan dan evaluasi pembelajaran (*Lessons Learned*) untuk presentasi ke manajemen eksekutif.

---

*📅 TISS Null Teaming · Week 24 · Day 3 · SENTINEL Rank*
