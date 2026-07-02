# 🛡️ Week 23 · Day 4: Memory & Disk Forensics

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 23 · Day 4/5 | SENTINEL Rank (Minggu 4 dari 5) | Overall: 114/120 hari (95%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara klasifikasi penelusuran bukti *(Artifacts)* pada sistem Memori *(RAM)* berbanding infrastruktur Media Penyimpanan Disk *(Non-Volatile)*.
2. **Memahami** batasan ketersediaan waktu ekstraksi berdasarkan tingkat stabilitas penyimpanan *Order of Volatility*.
3. **Mengenali** pengoperasian *Volatility Framework* dalam pembedahan *Memory Forensics* infrastruktur peladen.

---

## 📖 Materi Inti

### Segmentasi Ruang Analisis: RAM vs HDD

Ketika penganalisis tim penyidik menjalankan operasi bedah digital pasca insiden peretasan peladen perusahaan, sumber ekstraksi material penelusuran bukti terklasifikasi menurut retensi data:
1. **Disk Forensics (Forensik Penyimpanan Jangka Panjang Non-Volatile):**
 Operasi investigasi penelusuran arsitektur penyimpanan (Hard Disk Drive / SSD). Di sinilah bertempatnya informasi log yang merekam *Event Viewer* OS peladen, daftar penjelajahan ekosistem *Browser History*, dan direktori file unduhan peretas eksternal. Ketika operasi aplikasi diinisiasi, dan pelaku sistem menekan hapusan sistem (Shift+Delete), secara fundamental klaster file tidak sepenuhnya dihilangkan seketika, dan umumnya spesialis bisa mendayagunakan fitur *Data Recovery* operasi OS pengarsipan untuk memperoleh bukti ini.
2. **Memory Forensics (Forensik Penyimpanan Dinamis Volatile / RAM):**
 Klasifikasi penyelidikan kelas lanjut infrastruktur ini berpusat di arsitektur *Random Access Memory (RAM)* peladen korporat tempat pemrosesan perintah terdistribusi. *RAM* merupakan kumpulan informasi mutlak yang pengoperasiannya memelihara indikator skrip penyusup *Malware Fileless* (virus tingkat lanjut peretas APT canggih yang dioperasikan untuk tak menjejak di ruang *Hard Disk* sistem), arsip fungsi keamanan entri parameter kata sandi tipe otentikasi *Clear-text*, serta memelihara ekstraksi referensi instruksi penanaman penahan enkripsi taktis kelompok *Ransomware* korporat saat itu juga.

### Hierarki Kehilangan Bukti Sesaat (Order of Volatility)

Kaidah primer akuisisi pengamanan insiden adalah penanganan pemrioritasan ekstraksi alat bukti berpedoman pada kaidah kelangsungan hidup data atau *Order of Volatility*.
Data residu memori OS di blok infrastruktur *RAM* mempunyai karakteristik tingkat pelaporan **Volatile (Sangat Rentan Kehilangan Parameter)**. Ketika perangkat komputer didaur ulang siklus daya boot atau kabel sumber kelistrikan dicabut, struktur alokasi ruang register jutaan *Bit* data di peramban perangkat lunak sistem di *RAM* peladen akan menghilang terhapus dari log seketika!

Karena parameter sistem inilah, seumpamanya Analis *SOC* atau instruktur penyidik tim insiden IT memantau sistem perusahaan sedang terinfeksi serangan peladen aktif serangan eksploitasi berbahaya, prosedur prioritas instruksi pengamanan adalah BUKAN menginstruksikan staf untuk sekadar mencabut sumber operasi tenaga suplai listrik sistem kelistrikan, namun hanya sebatas memotong jalur rute kabel komunikasi jaringan, disusul segera melakukan pengerahan "perekaman pembekuan data kloning citra salinan arsitektur ruang data memori aktif *Live Memory Capture*" perangkat peladen OS tersebut!

### Bedah RAM dengan Volatility Framework

Begitu sistem peramban spesialis analis SOC operasi penyidikan mengekstrak fail log bayangan duplikat (*Memory Dump File*, yang memiliki susunan tipe nama ekstensi seperti `.raw` atau berkas pelaporan file `.mem`), tampilan mentah data blok hanya memperlihatkan rentetan pengkodean heksadesimal acak fungsi parameter mesin. Maka analis memanggil perangkat kerangka referensi analisis perintah perangkat spesialis yang diakui dan digunakan komunitas industri pelacak yakni: **Volatility Framework**.

pelacakan platform CLI (Command Line Interface) Python operasi peramban ini memungkinkan tim penyidik mengeksekusi parameter analisis :
- `vol.py -f memory_dump.raw windows.pslist` : Kueri ini dikonfigurasi guna instruksi ekstraksi pembongkaran struktur seluruh direktori informasi operasi perangkat proses *Application Process* sistem yang sedang diinisiasi hidup *(termasuk eksistensi sistem parameter persembunyian skrip peretas Malware rahasia di log memori sistem RAM aktif)*.
- `vol.py -f memory_dump.raw windows.hashdump` : Operasi ini akan mengeluarkan fungsi ekstrasi arsip identitas (autentikasi Password Hashes korporasi pengawasan sistem akses hak) yang mengendap pada parameter ruang peladen memori sistem OS.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi konseptual penanganan insiden penyedotan memori!

1. Anda sedang bersiaga sebagai penganalisis utama *SOC* di operasi korporasi. Karyawan divisi SDM melaporkan insiden darurat setelah membuka lampiran surel palsu; layar peladen kerja stasiun kerjanya saat ini memproyeksikan instalasi perangkat tebusan *Ransomware* yang menampilkan pelaporan penuntutan kompensasi aset enkripsi.
2. *Misi Mitigasi Parameter Cepat:* Staf melaporkan kepanikan dan memberitahukan niat teknis menekan fungsi operasi tombol tenaga untuk me-restart *peladen komputer stasiun SDM operasi IT * OS tersebut.
3. **Instruksi Intervensi Analis SOC:** *"JANGAN MEMUTUS DAYA MESIN OS ATAU RESTART! Biarkan arsitektur komputernya terus menyala. Isolasi perangkat cukup diselenggarakan dengan sekadar prosedur memutus kabel rute akses komunikasi Ethernet jaringan"*
4. *Konklusi :* Tindakan peretasan perangkat lunak instruksional *Ransomware* umumnya menghasilkan kunci sistem sandi parameter kriptografi (*Decryption Key parameter file*) di mana proses dekripsi arsip data korporasi arsitektur penyelesaian peretasan operasi sandi tersebut berdiam hidup di sistem blok alokasi struktur *RAM OS *. Jika parameter eksekusi instruksional stasiun *reboot* peladen dieksekusi di OS stasiun sistem perangkat kerja tersebut, data rentan volatile operasi memori RAM ini (*Volatile RAM*) otomatis memusnahkan ketersediaan memori sandi operasi peretasan *Decryption Key*, yang kegagalan mutlak fungsi akses perbaikan parameter dekripsi dokumen selamanya.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam terminologi forensik digital sistem informasi arsitektur, apakah klasifikasi parameter letak diferensiasi fisik struktur <i>Disk Forensics</i> bila diperhadapkan pada penelusuran arsitektur perangkat <i>Memory Forensics</i> (OS RAM) peladen data?</summary>

**Jawaban:** *Disk Forensics* digunakan untuk mengevaluasi data perangkat keras non-volatile untuk rentang waktu jangka pelaporan jangka panjang *(Hard Disk/SSD)* OS. Parameter klasifikasi arsitektur *Memory Forensics* memusatkan ekstraksi analisis log data sistem OS dinamis *(Volatile Memory RAM OS)* yang pengawasan operasinya diproses langsung pada instansi aktif saat eksekusi berlangsung.
</details>

<details>
<summary>❓ Membahas standar mitigasi perlindungan darurat penanganan tanggap krisis <i>Incident Response</i> korporat jaringan, mengapa ekstraksi parameter penyitaan log data RAM diposisikan prioritas hierarki akuisisi perlindungan sistem bukti awal OS di atas pengamanan komponen perlindungan perangkat *Hard Disk OS* peladen korporat ?</summary>

**Jawaban:** Prosedur diprioritaskan mengacu aturan *Order of Volatility*. Perangkat memori (RAM) OS terstruktur sebagai parameter penyimpanan dinamis *(Volatile)* di mana arsitektur OS peladen tak akan merestorasi status keberadaan memori apabila struktur sistem arsitektur tersebut didaur ulang instruksi (*Restart*) atau sumber kelistrikan diputus secara pasif perangkat peladen, mengakibatkan hilangnya jejak instruksi aktivitas malware atau instruksional sandi *decryption key*.
</details>

<details>
<summary>❓ Di ekosistem analitik investigasi perangkat pendeteksian peretasan RAM peladen forensik korporat, apa perangkat fungsi alat aplikasi parameter sistem ekosistem perangkat lunak baris komando spesifik sistem (Python) yang kapabilitas penelusuran identitas pembelahan log *Memory Dumps* peladen?</summary>

**Jawaban:** perangkat pelacak Volatility Framework.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya mengetahui parameter urgensi perbedaan klasifikasi *Disk* dan parameter memori *RAM*.
- [ ] Saya menguasai metodologi *Order of Volatility* sistem peladen.
- [ ] Saya meresapi teknikal rasional pelarangan pelaporan aktivasi instruksi eksekusi sistem peladen *reboot* arsitektur di insiden *Malware/Ransomware*.
- [ ] Saya paham tata letak pengoperasian mesin instruksi perangkat arsitektur *Volatility Framework*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Volatility Foundation: Volatility 3](https://www.volatilityfoundation.org/) — Sumber dokumentasi komunitas sistem keamanan operasi arsitektur Volatility sistem bedah memori OS.

---

## ➡️ Besok

**Day 5: Lab & Mission: Threat Hunting Exercise** — Setelah penguraian parameter arsitektur instruksional penelusuran metode ekosistem fungsi log Sentinel *MITRE ATT&CK Framework*, penataan rantai dokumentasi prosedur *Chain of Custody* forensik korporasi, serta pelaporan taktis operasi identifikasi parameter *Volatility Memory Extraction*. Laboratorium pelatihan kualifikasi kasta SENTINEL esok harinya menuntut spesialis memformulasikan aplikasi praktik penyusunan buku modul penyidikan **Threat Hunting Playbook**. Latihan implementasi operasi ini akan menyeleksi arsitektur kecerdasan spesialis forensik korporasi TISS Null Teaming!

---

*📅 TISS Null Teaming · Week 23 · Day 4 · SENTINEL Rank*
