# 🎯 Week 24 · Day 6 (Bonus): Hands-On Learning — Final Mission

> **Rank**: SENTINEL | **Minggu ke-24** | Bonus Day (FINAL)

---

## 🌐 Platform Hari Ini

**[CyberDefenders — Endpoint Forensics Challenge](https://cyberdefenders.org/blueteam-ctf-challenges/)**
Tantangan forensik *endpoint* gratis yang menguji kemampuan analisis artefak sistem (seperti *disk image*, *memory dump*, *registry*). Ini adalah ujian praktik dari seluruh materi yang dipelajari selama 24 minggu.

💰 **Biaya**: Gratis (tersedia tantangan gratis)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan *hands-on* ini, kamu akan mampu:
1. Menganalisis artefak *endpoint* untuk menemukan jejak penyusupan.
2. Menggunakan perangkat (*tools*) forensik esensial (seperti Volatility, FTK Imager, atau Autopsy).
3. Menulis **Incident Response Report (IRR)** yang merangkum seluruh temuan secara formal.

---

## 📋 Requirement

* Akun CyberDefenders (jika belum, silakan mendaftar).
* Terminal Linux (VM/WSL).
* *Tools* forensik (salah satu):
  - **Autopsy** (gratis, berbasis GUI, lebih intuitif) — [autopsy.com/download](https://www.autopsy.com/download/)
  - **Volatility 3** (gratis, berbasis CLI) — `pip3 install volatility3`
* Wireshark (sudah terinstal sebelumnya).

> ⚠️ **Jika tools forensik belum terinstal**: Ikuti panduan instalasi singkat di bawah. Keduanya adalah *tools* gratis dan *open source*.

---

## 📝 Prosedur

### Langkah 1: Pilih Challenge Endpoint Forensics
1. *Login* ke [cyberdefenders.org](https://cyberdefenders.org).
2. Masuk ke menu **Blue Team CTF Challenges**.
3. Gunakan filter: Difficulty **Easy**, Category **Endpoint Forensics** atau **Digital Forensics**.
4. Pilih tantangan gratis yang tersedia.
5. Baca skenario investigasi dengan teliti.

### Langkah 2: Unduh dan Siapkan Evidence
1. Unduh *file* bukti tantangan (*evidence*).
2. Ekstrak *file* tersebut:
   ```bash
   mkdir ~/ctf-week24-final
   cd ~/ctf-week24-final
   unzip challenge-file.zip
   ls -la
   ```
3. Identifikasi tipe *file evidence*:
   ```bash
   file *
   ```
   Kemungkinan format: `.raw` (*memory dump*), `.E01` (*disk image*), `.evtx` (Windows *event log*).

### Langkah 3: Analisis Evidence

**Jika berupa Memory Dump (.raw /.mem):**

Instal Volatility 3 (jika belum):
```bash
pip3 install volatility3
```

Proses Analisis:
```bash
# Identifikasi informasi OS
vol -f memory.raw windows.info

# Tampilkan daftar proses yang berjalan
vol -f memory.raw windows.pslist

# Analisis proses mencurigakan (melihat hierarki parent-child)
vol -f memory.raw windows.pstree

# Periksa koneksi jaringan
vol -f memory.raw windows.netscan

# Periksa riwayat command line
vol -f memory.raw windows.cmdline
```

> 💡 **Tips Pencarian Anomali**: Cari nama proses yang mencurigakan, proses yang berjalan dari lokasi yang tidak biasa (misalnya: `C:\Users\...\AppData\`), atau koneksi keluar ke IP eksternal yang tidak dikenal.

**Jika berupa Windows Event Log (.evtx):**
```bash
# Gunakan python-evtx
pip3 install python-evtx
python3 -m Evtx.Dump Security.evtx | head 100

# Atau gunakan aplikasi Event Viewer bawaan jika berada di Windows
```

**Jika berupa Disk Image:**
1. Menggunakan **Autopsy** (GUI):
   - Klik *New Case* → *Add Data Source* → pilih *disk image*.
   - Tunggu proses *indexing* selesai.
   - Jelajahi struktur direktori *filesystem*, dokumen terbaru, dan riwayat *browser*.
2. Menggunakan CLI Linux:
   ```bash
   # Mount image (Linux)
   sudo mount -o loop,ro disk-image.dd /mnt/evidence/
   ls /mnt/evidence/
   ```

### Langkah 4: Jawab Pertanyaan Challenge
1. Gunakan bukti-bukti dari analisis di atas untuk menjawab pertanyaan yang diajukan oleh tantangan.
2. Pertanyaan yang sering muncul:
   - Proses jahat (*malicious*) apa yang berjalan?
   - Alamat IP C2 (Command & Control) mana yang dihubungi?
   - *File* apa yang pertama kali dieksekusi oleh peretas?
   - Kapan rentetan infeksi (*timeline*) dimulai?

### Langkah 5: Tulis Incident Response Report (IRR) Final

Ini adalah hasil akhir (*deliverable*) utama dari pelatihan ini. Tulis laporan yang komprehensif:

```markdown
# 📋 Incident Response Report (IRR)
## TISS Null Teaming Division — Final Assessment

### Informasi Umum
- Investigator: [Nama Anda]
- Tanggal: [Tanggal]
- Challenge: [Nama Challenge CyberDefenders]
- Evidence: [Tipe dan ukuran file bukti]

### 1. Executive Summary
[2-3 paragraf singkat untuk pembaca non-teknis. Jelaskan secara ringkas apa yang terjadi, dampaknya, dan status akhirnya.]

### 2. Timeline Insiden
| Waktu | Aktivitas | Bukti |
|-------|-----------|-------|
| [waktu] | Akses awal (*Initial access*) via [vektor] | [bukti] |
| [waktu] | Eksekusi malware | [proses/file] |
| [waktu] | Komunikasi C2 | [IP/domain] |
| [waktu] | Pencurian data (jika ada) | [bukti] |

### 3. Indicators of Compromise (IoC)
| Tipe | Nilai | Konteks |
|------|-------|---------|
| IP Address | [IP] | Server C2 |
| Domain | [domain] | Phishing/C2 |
| File Hash | [MD5/SHA256] | Malware |
| File Path | [path] | Lokasi file malware |

### 4. Root Cause Analysis
[Jelaskan bagaimana serangan ini bermula dan apa celah utama (*root cause*) yang menyebabkannya.]

### 5. Rekomendasi Remediasi
1. **Jangka Pendek (Immediate):** [Tindakan darurat, misal pemblokiran IP]
2. **Jangka Menengah (Short-term):** [Perbaikan sementara, misal penambalan celah aplikasi]
3. **Jangka Panjang (Long-term):** [Peningkatan struktur keamanan dan pelatihan pengguna]

### 6. Lessons Learned
[Apa pelajaran yang dapat diambil dari insiden ini? Apa proses, teknologi, atau sumber daya manusia yang perlu diperbaiki?]
```

---

## 🏁 Target Output

* ✅ Menyelesaikan minimal **1 challenge Endpoint Forensics** (atau setidaknya mencatat progres yang signifikan).
* 📝 Menyusun **Incident Response Report (IRR)** lengkap yang memuat 6 bagian seperti format di atas.
* 📝 Melampirkan tabel *IoC (Indicators of Compromise)* yang berhasil diekstrak.
* 📸 Menyertakan tangkapan layar (*screenshot*) alat analisis (seperti output Volatility, Autopsy, atau Wireshark).

> 🏆 **Selamat!** Jika Anda berhasil menyelesaikan keseluruhan tugas pada Bonus Day 6 ini, Anda telah membuktikan kemampuan *hands-on* pada platform berstandar industri nyata — yang menguji logika investigasi, analisis forensik, hingga kemampuan pelaporan teknis Anda.

---

## 🔄 Fallback

Jika platform CyberDefenders tidak dapat diakses atau terjadi kendala instalasi perangkat:
1. Buka **[Blue Team Labs Online](https://blueteamlabs.online/)** — cari tantangan gratis bertema forensik (*Endpoint Forensics*).
2. Alternatif lain: Gunakan **[Volatility CTF Challenges](https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples)** dari Volatility Foundation (berisi sampel *memory dumps* gratis).
3. Analisis *file* tersebut menggunakan Volatility 3 dengan panduan perintah di Langkah 3.
4. Tetap kerjakan penulisan **IRR** berdasarkan temuan yang berhasil Anda ekstrak.
