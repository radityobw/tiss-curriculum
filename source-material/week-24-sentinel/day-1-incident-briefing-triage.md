# 🛡️ Week 24 · Day 1: Incident Briefing & Triage

> **Rank**: SENTINEL | **Minggu ke-24**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 24 · Day 1/5 | SENTINEL Rank (Minggu 5 dari 5) | Overall: 116/120 hari (96%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Merespons** laporan awal dari sebuah insiden keamanan (*Incident Briefing*) pada fase *Identification* (kerangka PICERL).
2. **Mengeksekusi** proses *Triage* (pemilahan log peringatan berdasarkan prioritas).
3. **Menentukan** *Scope* (ruang lingkup penyebaran) dari insiden siber yang terjadi.

---

## 📖 Materi Inti

### Capstone: Simulasi Respons Insiden Korporat

Selamat datang di tahap akhir pelatihan TISS Null Teaming! Selama 23 minggu, Anda telah membangun keahlian ofensif (*Red Team*) dan defensif (*Blue Team*). 

Modul minggu ini didedikasikan sepenuhnya untuk proyek akhir (*Capstone Project*). Mulai dari sesi ini, materi akan berjalan sebagai **simulasi satu siklus penanganan insiden skala korporat**, yang mengalir dari tahap identifikasi masalah di hari pertama, hingga perumusan laporan akhir di hari kelima.

### Fase 1: Incident Briefing (Laporan Awal Insiden)

Asumsikan waktu saat ini menunjukkan pukul 03:00 pagi. Anda bertugas sebagai analis SOC darurat (*On-Call*) dan menerima eskalasi dari tim IT:
> *"Tim IT melaporkan server Database Data Nasabah (IP 10.0.0.55) mendadak tidak responsif. Di waktu yang sama, sistem pemantauan Splunk mendeteksi lonjakan peringatan (Alerts) yang berasal dari Web Server publik (IP 192.168.1.100). Harap inisiasi proses investigasi darurat saat ini juga!"*

Sebagai komandan insiden (*Incident Commander*), langkah pertama Anda **bukan** mematikan atau mencabut kabel *server* secara reaktif (yang dapat merusak barang bukti). Langkah pertama yang benar adalah memvalidasi dan mengidentifikasi anomali tersebut secara teknis *(Fase Identification)*.

### Mengeksekusi Triage (Pemilahan Peringatan)

*Triage* adalah proses pemilahan kondisi darurat (diadaptasi dari dunia medis) ke dalam penanganan insiden siber. Analis memilah peringatan (*alerts*) berdasarkan tingkat ancaman untuk memprioritaskan peringatan mana yang harus dianalisis terlebih dahulu.

Saat layar *Splunk* menayangkan 5.000 peringatan, mana yang harus di-*Triage*?

1. **Titik Masuk (Initial Entry Point):** Analis memfilter log Web Server (`192.168.1.100`). Ditemukan ribuan percobaan koneksi berstatus *HTTP 404 (Not Found)*, yang diakhiri dengan satu transaksi berhasil (*HTTP 200*) pada URL `/login.php?user=admin' OR '1'='1`. Temuan ini memastikan adanya serangan *SQL Injection*.
2. **Pergerakan Menyamping (Lateral Movement):** Aktivitas aktor ancaman tidak berhenti di Web Server. Log mengonfirmasi bahwa setelah meretas Web Server (192.168.1.100), peretas menggunakannya untuk mencoba *Login RDP* (Event ID 4625) bergerak menyamping (*Lateral Movement*) menuju *server* Database (`10.0.0.55`).

### Menentukan Scope (Penetapan Ruang Lingkup Insiden)

Berbekal hasil *Triage* log di atas, analis kini mampu menetapkan batasan atau ruang lingkup (*Scope*) insiden.

*Penetapan Scope:* Insiden keamanan ini BUKAN infeksi *malware* massal yang menulari 500 komputer karyawan. Insiden ini secara spesifik berhasil dibatasi hanya di dua titik *server*: **Web Server (192.168.1.100)** dan **Database Server (10.0.0.55)**.

Dengan perumusan *Scope* yang akurat, tim SOC tidak perlu memutus seluruh jaringan internet perusahaan. Mereka cukup melakukan isolasi jaringan (*Containment*) khusus pada kedua *server* tersebut.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari mensimulasikan penetapan ruang lingkup (*Scope*) insiden!

1. Siapkan aplikasi catatan (Notepad/VS Code).
2. Anda menerima laporan: "Komputer Direktur HRD (IP 192.168.5.10) terkena *Ransomware* yang sedang aktif mengenkripsi dokumen."
3. Anda menganalisis log *Firewall* internal dan menemukan bahwa komputer HRD tersebut (192.168.5.10) terus-menerus memancarkan paket via port *SMB (Port 445)* ke komputer departemen Keuangan (192.168.5.11) dan departemen Marketing (192.168.5.12).
4. **Misi:** Formulasikan *Scope* penyebaran insiden ini!
5. **Formulasi Laporan Analis (Jawaban):**
   *"Scope (ruang lingkup) insiden keamanan siber ini terkonfirmasi menargetkan penyebaran di tiga komputer, yaitu: Komputer HRD (192.168.5.10), Komputer Keuangan (192.168.5.11), dan Komputer Marketing (192.168.5.12). Ketiga IP ini direkomendasikan untuk segera masuk ke tahap Containment (isolasi jaringan)."*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam siklus penanganan insiden, istilah apa yang merujuk pada aktivitas memilah dan memprioritaskan peringatan (Alerts) log mana yang harus dianalisis lebih awal?</summary>

**Jawaban:** Triage.
</details>

<details>
<summary>❓ Ketika tim mitigasi mengonfirmasi bahwa insiden hanya terbatas pada tiga <i>server</i> dan belum menyebar ke jaringan karyawan, istilah apa yang mendeskripsikan batasan area penyebaran tersebut?</summary>

**Jawaban:** Scope (Ruang Lingkup).
</details>

<details>
<summary>❓ Mengacu pada kerangka insiden PICERL, aktivitas menerima laporan <i>Incident Briefing</i> dan melakukan <i>Triage</i> dikategorikan ke dalam fase apa?</summary>

**Jawaban:** Identification (Identifikasi).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami cara merespons laporan awal (*Incident Briefing*).
- [ ] Saya fasih menjalankan logika pemilahan peringatan (*Triage*).
- [ ] Saya menguasai mekanisme penentuan batasan area insiden (*Scope*).
- [ ] Saya memahami bahwa tindakan darurat harus didasari oleh validasi log.
- [ ] Saya telah menjawab semua quiz kilat.

---

## 🔗 Resources

- [SANS: Incident Triage Lifecycle](https://www.sans.org/white-papers/33219/) — Pedoman standar industri dari SANS yang membahas proses pemilahan (*Triage*) insiden keamanan siber.

---

## ➡️ Besok

**Day 2: Forensics & Root Cause Analysis** — Ruang lingkup insiden telah ditetapkan (*Scope*). Evaluasi selanjutnya difokuskan pada disiplin ilmu forensik (*Digital Forensics*). Kita akan mengekstrak bukti indikator kompromi *(Indicators of Compromise / IOC)* dari *server* yang terinfeksi dan mencari *Root Cause Analysis* (Akar Masalah): "Dari mana peretas ini berhasil masuk pertama kali?".

---

*📅 TISS Null Teaming · Week 24 · Day 1 · SENTINEL Rank*
