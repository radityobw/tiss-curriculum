# 🛡️ Week 24 · Day 1: Incident Briefing & Triage

> **Rank**: SENTINEL | **Minggu ke-24**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 24 · Day 1/5 | SENTINEL Rank (Minggu 5 dari 5) | Overall: 116/120 hari (96%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Merespons** laporan awal dari sebuah insiden keamanan (*Incident Briefing*) pada fase *Identification* (kerangka PICERL).
2. **Mengeksekusi** proses *Triage* (pemilahan prioritas mitigasi) dari hasil peringatan log SIEM.
3. **Menentukan** *Scope* (ruang lingkup) dampak penyebaran dari insiden siber yang terjadi.

---

## 📖 Materi Inti

### Capstone: Ujian Komprehensif Respons Insiden Korporat

Selamat datang di tahap akhir pelatihan TISS Null Teaming! Selama 23 minggu, Anda telah membangun keahlian ofensif (*Red Team*) maupun defensif (*Blue Team*). 

Modul minggu ini didedikasikan sepenuhnya untuk proyek akhir (*Capstone Project*). Mulai dari sesi ini, materi akan berjalan sebagai **simulasi satu siklus utuh penanganan insiden skala korporat**, yang mengalir dari tahapan identifikasi masalah di hari pertama, hingga perumusan laporan insiden akhir di hari kelima.

### Fase 1: Incident Briefing (Laporan Awal Insiden)

Asumsikan waktu saat ini menunjukkan pukul 03:00 pagi. Anda bertugas sebagai analis SOC darurat (*On-Call*) dan menerima eskalasi dari manajemen IT:
> *"Tim IT melaporkan server Database Data Nasabah (IP 10.0.0.55) mendadak tidak responsif. Di waktu yang sama, sistem pemantauan Splunk membangkitkan lonjakan peringatan (Alerts) yang berasal dari Web Server publik kita (IP 192.168.1.100). Harap inisiasi proses investigasi darurat saat ini juga!"*

Sebagai komandan insiden (*Incident Commander*), langkah pertama Anda **bukan** langsung mematikan atau mencabut kabel server secara reaktif (yang dapat menghilangkan barang bukti). Langkah pertama sesuai prosedur adalah memvalidasi dan mengidentifikasi anomali tersebut secara teknis *(Fase Identification)*.

### Mengeksekusi Triage (Pemilahan Peringatan)

*Triage* adalah konsep pemilahan kondisi darurat medis yang diadaptasi ke dalam penanganan insiden siber. Konsep ini mengharuskan analis untuk memilah peringatan log berdasarkan rasio bahaya guna memprioritaskan peringatan mana yang harus dianalisis terlebih dahulu.

Saat layar *Splunk* menayangkan 5.000 peringatan log aktivitas, mana yang harus di-*Triage*?

1. **Titik Masuk (Initial Entry Point):** Analis memfilter log Web Server (`192.168.1.100`). Ditemukan ribuan percobaan koneksi berstatus *HTTP 404 (Not Found)*, yang diakhiri dengan satu transaksi berhasil (*HTTP 200*) pada URL `/login.php?user=admin' OR '1'='1`. Temuan ini memastikan adanya serangan *SQL Injection*.
2. **Pergerakan Menyamping (Lateral Movement):** Aktivitas aktor ancaman tidak berhenti di Web Server. Log mengonfirmasi bahwa setelah meretas Web Server (192.168.1.100), peretas menggunakannya untuk mencoba *Login RDP* (Event ID 4625) bergerak menyamping (*Lateral Movement*) menuju server Database sensitif (`10.0.0.55`).

### Menentukan Scope (Penetapan Ruang Lingkup Insiden)

Berbekal hasil *Triage* log di atas, analis kini mampu menetapkan batasan atau ruang lingkup (*Scope*) insiden.

*Penetapan Scope:* Insiden keamanan ini BUKAN infeksi *malware* massal yang menulari 500 komputer karyawan. Insiden ini secara tegas berhasil dibatasi hanya di dua titik server: **Web Server (192.168.1.100)** dan **Database Server (10.0.0.55)**.

Dengan perumusan *Scope* yang akurat, tim SOC tidak perlu mengambil tindakan radikal seperti memutus seluruh jaringan internet perusahaan, melainkan cukup melakukan isolasi jaringan (*Containment*) khusus pada kedua server tersebut.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan penetapan ruang lingkup (*Scope*) insiden!

1. Buka aplikasi pencatatan (Notepad/VS Code).
2. Anda menerima laporan: "Komputer Direktur HRD (IP 192.168.5.10) terkena *Ransomware* yang sedang aktif mengenkripsi dokumen."
3. Anda menganalisis log *Firewall* internal dan mengonfirmasi bahwa komputer HRD tersebut (192.168.5.10) terus-menerus memancarkan paket via port *SMB (Port 445)* ke komputer departemen Keuangan (192.168.5.11) dan departemen Marketing (192.168.5.12).
4. **Misi:** Formulasikan draf penetapan *Scope* insiden perambatan ransomware ini!
5. **Formulasi Laporan Analis (Jawaban):**
   *"Scope (ruang lingkup) insiden keamanan siber ini terkonfirmasi menargetkan penyebaran di tiga stasiun perangkat, yaitu: Komputer HRD (192.168.5.10), Komputer Keuangan (192.168.5.11), dan Komputer Marketing (192.168.5.12). Ketiga IP ini direkomendasikan untuk segera masuk ke tahap Containment (isolasi jaringan)."*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam siklus penanganan insiden, istilah apa yang merujuk pada aktivitas memilah dan memprioritaskan peringatan (Alerts) log mana yang harus dianalisis paling awal?</summary>

**Jawaban:** Triage.
</details>

<details>
<summary>❓ Ketika tim mitigasi mengonfirmasi: "Infeksi ini hanya terbatas pada tiga server spesifik dan belum merambah ke jaringan pengguna", istilah teknikal apa yang digunakan untuk mendeskripsikan batasan area penyebaran tersebut?</summary>

**Jawaban:** Scope (Ruang Lingkup).
</details>

<details>
<summary>❓ Mengacu pada kerangka insiden PICERL, aktivitas menerima laporan <i>Incident Briefing</i> dan melakukan <i>Triage</i> log dikategorikan pada tahap awal apa?</summary>

**Jawaban:** Identification (Identifikasi).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami cara merespons laporan awal (*Incident Briefing*).
- [ ] Saya fasih menjalankan logika pemilahan peringatan (*Triage*).
- [ ] Saya menguasai mekanisme penentuan batasan zona paparan insiden (*Scope*).
- [ ] Saya paham bahwa pengambilan keputusan darurat harus berdasarkan validasi data log.
- [ ] Saya telah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS: Incident Triage Lifecycle](https://www.sans.org/white-papers/33219/) — Pedoman standar industri dari SANS yang membahas tentang proses pemilahan (Triage) insiden keamanan siber.

---

## ➡️ Besok

**Day 2: Forensics & Root Cause Analysis** — Ruang lingkup insiden telah ditetapkan (*Scope*). Evaluasi selanjutnya akan difokuskan pada ilmu forensik (*Digital Forensics*). Kita akan mengekstrak barang bukti indikator kompromi *(Indicators of Compromise / IOC)* dari komputer yang terinfeksi dan mengungkap *Root Cause Analysis* (Akar Masalah): "Dari mana pintu masuk awal peretas ini?".

---

*📅 TISS Null Teaming · Week 24 · Day 1 · SENTINEL Rank*
