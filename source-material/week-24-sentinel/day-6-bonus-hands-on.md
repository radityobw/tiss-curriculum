# 🎯 Week 24 · Day 6 (Bonus): Hands-On Learning — Final Mission

> **Rank**: SENTINEL | **Minggu ke-24** | Bonus Day (FINAL)

---

## 🌐 Platform Hari Ini

**[CyberDefenders — Endpoint Forensics Challenge](https://cyberdefenders.org/blueteam-ctf-challenges/)**
Challenge forensik endpoint gratis yang menguji kemampuan analisis artefak sistem (disk image, memory dump, registry) — puncak dari seluruh perjalanan 24 minggu.

💰 **Biaya**: Gratis (challenge gratis tersedia)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menganalisis artefak endpoint untuk menemukan jejak penyusup
2. Menggunakan tools forensik dasar (Volatility, FTK Imager, atau Autopsy)
3. Menulis **Incident Response Report (IRR)** yang merangkum seluruh temuan

---

## 📋 Requirement

* Akun CyberDefenders (sudah ada)
* Terminal Linux (VM/WSL)
* Tools forensik (salah satu):
 - **Autopsy** (gratis, GUI, lebih mudah) — [autopsy.com/download](https://www.autopsy.com/download/)
 - **Volatility 3** (gratis, CLI) — `pip3 install volatility3`
* Wireshark (sudah ada)

> ⚠️ **Jika tools forensik belum terinstal**: Ikuti langkah instalasi di prosedur di bawah. Kedua tool gratis dan open source.

---

## 📝 Prosedur

### Langkah 1: Pilih Challenge Endpoint Forensics
1. Login ke [cyberdefenders.org](https://cyberdefenders.org)
2. ke **Blue Team CTF Challenges**
3. Filter: Difficulty **Easy**, Category **Endpoint Forensics** atau **Digital Forensics**
4. Pilih challenge gratis yang tersedia
5. Baca skenario investigasi

### Langkah 2: Unduh dan Siapkan Evidence
1. Unduh file challenge
2. Ekstrak:
 ```bash
 mkdir ~/ctf-week24-final
 cd ~/ctf-week24-final
 unzip challenge-file.zip
 ls -la
 ```
3. Identifikasi tipe file evidence:
 ```bash
 file *
 ```
 Kemungkinan format: `.raw` (memory dump), `.E01` (disk image), `.evtx` (Windows event log)

### Langkah 3: Analisis Evidence

**Jika Memory Dump (.raw /.mem):**

Instal Volatility 3 (jika belum):
```bash
pip3 install volatility3
```

Analisis:
```bash
# Identifikasi OS
vol -f memory.raw windows.info

# Daftar proses yang berjalan
vol -f memory.raw windows.pslist

# Proses mencurigakan (parent-child relationship)
vol -f memory.raw windows.pstree

# Network connections
vol -f memory.raw windows.netscan

# Command line history
vol -f memory.raw windows.cmdline
```

> 💡 **Cari anomali**: Proses dengan nama aneh, proses yang spawn dari lokasi tidak biasa (misal: `C:\Users\...\AppData\`), koneksi ke IP external yang mencurigakan.

**Jika Windows Event Log (.evtx):**
```bash
# Gunakan python-evtx
pip3 install python-evtx
python3 -m Evtx.Dump Security.evtx | head 100

# Atau di Windows, gunakan Event Viewer bawaan
```

**Jika Disk Image:**
1. Buka **Autopsy** (GUI):
 - New Case → Add Data Source → pilih disk image
 - Tunggu proses indexing
 - Jelajahi filesystem, recent documents, browser history
2. Atau gunakan CLI:
 ```bash
 # Mount image (Linux)
 sudo mount -o loop,ro disk-image.dd /mnt/evidence/
 ls /mnt/evidence/
 ```

### Langkah 4: Jawab Pertanyaan Challenge
1. Gunakan bukti dari analisis untuk menjawab pertanyaan
2. Pertanyaan tipikal:
 - Proses malicious apa yang berjalan?
 - IP C2 apa yang terhubung?
 - File apa yang dieksekusi pertama kali?
 - Kapan timeline infeksi dimulai?

### Langkah 5: Tulis Incident Response Report (IRR) Final

Ini adalah deliverable puncak dari perjalanan 24 minggu. Tulis report komprehensif:

```markdown
# 📋 Incident Response Report (IRR)
## TISS Null Teaming Division — Final Assessment

### Informasi Umum
- Investigator: [Nama]
- Tanggal: [Tanggal]
- Challenge: [Nama Challenge CyberDefenders]
- Evidence: [Tipe dan ukuran file]

### 1. Executive Summary
[2-3 paragraf untuk audience non-teknis. Apa yang terjadi? Seberapa parah? Apa yang harus dilakukan?]

### 2. Timeline Insiden
| Waktu | Aktivitas | Bukti |
|-------|-----------|-------|
| [waktu] | Initial access via [vektor] | [bukti] |
| [waktu] | Malware execution | [proses/file] |
| [waktu] | C2 communication | [IP/domain] |
| [waktu] | Data exfiltration (jika ada) | [bukti] |

### 3. Indicators of Compromise (IoC)
| Tipe | Nilai | Konteks |
|------|-------|---------|
| IP Address | [IP] | C2 Server |
| Domain | [domain] | Phishing/C2 |
| File Hash | [MD5/SHA256] | Malware |
| File Path | [path] | Malware location |

### 4. Root Cause Analysis
[Bagaimana serangan dimulai? Apa akar masalahnya?]

### 5. Rekomendasi Remediasi
1. **Immediate**: [tindakan darurat]
2. **Short-term**: [perbaikan 1-2 minggu]
3. **Long-term**: [peningkatan arsitektur keamanan]

### 6. Lessons Learned
[Apa yang bisa dicegah? Apa yang perlu diperbaiki di proses/teknologi/people?]
```

---

## 🏁 Target Output

* ✅ Minimal **1 challenge Endpoint Forensics** selesai atau progress signifikan
* 📝 **Incident Response Report (IRR)** lengkap dengan 6 section di atas
* 📝 Tabel IoC (Indicators of Compromise) yang diekstrak
* 📸 Tangkapan layar tools forensik (Volatility output / Autopsy / Wireshark)

> 🏆 **Selamat!** Jika kamu berhasil menyelesaikan seluruh 24 minggu bonus Day 6, kamu telah membuktikan kemampuan hands-on di platform industri nyata — dari bahasa Inggris hingga forensik digital.

---

## 🔄 Fallback

Jika CyberDefenders tidak bisa diakses atau tools forensik gagal diinstal:
1. Buka **[Blue Team Labs Online](https://blueteamlabs.online/)** — cari challenge gratis bertema forensik
2. Atau gunakan **[Volatility CTF Challenges](https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples)** dari Volatility Foundation (sample memory dumps gratis)
3. Analisis menggunakan Volatility 3 dengan perintah di Langkah 3
4. Tetap tulis **IRR** berdasarkan temuan yang berhasil diekstrak
