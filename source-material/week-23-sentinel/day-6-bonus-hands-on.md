# 🎯 Week 23 · Day 6 (Bonus): Hands-On Learning

> **Rank**: SENTINEL | **Minggu ke-23** | Bonus Day

---

## 🌐 Platform Hari Ini

**[CyberDefenders — Network Forensics Challenge](https://cyberdefenders.org/blueteam-ctf-challenges/)**
Challenge forensik jaringan gratis di CyberDefenders yang menguji kemampuan analisis PCAP file, identifikasi malware traffic, dan pelacakan Command & Control (C2) server.

💰 **Biaya**: Gratis (challenge gratis tersedia)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menganalisis file PCAP menggunakan Wireshark dan tshark
2. Mengidentifikasi komunikasi C2 (Command & Control) dalam network capture
3. Mengekstrak Indicators of Compromise (IoC) dari traffic analysis

---

## 📋 Requirement

* Akun CyberDefenders (sudah dibuat di Week 21)
* Wireshark terinstal (sudah ada sejak Week 6)
* Terminal Linux (VM/WSL)
* `tshark` (biasanya terinstal bersama Wireshark)

---

## 📝 Prosedur

### Langkah 1: Pilih Challenge Network Forensics
1. Login ke [cyberdefenders.org](https://cyberdefenders.org)
2. ke **Blue Team CTF Challenges**
3. Filter: Difficulty **Easy** atau **Medium**, Category **Network Forensics**
4. Pilih salah satu challenge gratis yang tersedia
5. Baca deskripsi skenario dengan teliti

### Langkah 2: Unduh dan Buka PCAP
1. Unduh file challenge
2. Ekstrak:
 ```bash
 mkdir ~/ctf-week23
 cd ~/ctf-week23
 unzip challenge-file.zip
 # Jika password-protected, gunakan password yang tertera di halaman challenge
 ```
3. Buka file PCAP di Wireshark:
 ```bash
 wireshark capture.pcap &
 ```

### Langkah 3: Analisis Bertahap

**Tahap 1 — Gambaran Besar:**
```bash
# Statistik koneksi
tshark -r capture.pcap -q -z conv,tcp | head 20

# Statistik protokol
tshark -r capture.pcap -q -z io,phs

# Daftar DNS queries
tshark -r capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name | sort -u
```

**Tahap 2 — Filter HTTP Traffic:**
Di Wireshark, terapkan display filter:
```
http.request
```
Perhatikan:
- URL apa saja yang diakses?
- Apakah ada download file mencurigakan?
- Apakah ada POST request ke domain aneh?

**Tahap 3 — Identifikasi Anomali:**
```
# Cari user-agent tidak biasa
http.user_agent contains "curl" or http.user_agent contains "wget" or http.user_agent contains "python"

# Cari komunikasi ke IP non-standard port
tcp.port > 8000 and tcp.port < 65535

# Cari DNS query ke domain mencurigakan
dns.qry.name contains ".xyz" or dns.qry.name contains ".tk" or dns.qry.name contains ".top"
```

**Tahap 4 — Ekstrak File (Jika Ada):**
1. Di Wireshark: **File** → **Export Objects** → **HTTP**
2. Lihat daftar file yang diunduh melalui HTTP
3. Simpan file mencurigakan untuk analisis lebih lanjut
4. Gunakan `file` command untuk mengidentifikasi tipe sebenarnya:
 ```bash
 file downloaded-file.exe
 ```

> 💡 **Jangan eksekusi file yang diekstrak!** Cukup analisis metadata-nya saja (nama, ukuran, hash).

### Langkah 4: Jawab Pertanyaan Challenge
1. Kembali ke CyberDefenders
2. Gunakan bukti dari analisis untuk menjawab pertanyaan
3. Format jawaban biasanya spesifik (IP address, domain, hash) — perhatikan format

### Langkah 5: Tulis Investigasi Report
```markdown
# Network Forensics Investigation Report — Week 23

## Skenario
[Ringkasan skenario dari challenge]

## Temuan Utama
| # | Indikator | Tipe IoC | Nilai |
|---|-----------|----------|-------|
| 1 | IP Penyerang | IP Address | [IP] |
| 2 | Domain C2 | Domain | [domain] |
| 3 | Malware Hash | SHA256 | [hash] |

## Timeline Serangan
1. [waktu] — Korban mengakses [URL]
2. [waktu] — File malicious diunduh
3. [waktu] — Komunikasi C2 dimulai ke [IP/domain]

## Rekomendasi
- Block IP [IP] di firewall
- Block domain [domain] di DNS filter
- Scan endpoint yang terinfeksi
```

---

## 🏁 Target Output

* ✅ Minimal **1 challenge Network Forensics** selesai atau progress signifikan
* 📝 **Investigation Report** dengan timeline serangan dan IoC
* 📝 Daftar Wireshark display filters yang paling berguna
* 📸 Tangkapan layar Wireshark menampilkan traffic mencurigakan yang ditemukan

---

## 🔄 Fallback

Jika CyberDefenders tidak bisa diakses:
1. Buka **[Malware-Traffic-Analysis.net](https://www.malware-traffic-analysis.net/)** (gratis)
2. Unduh salah satu exercise PCAP terbaru
3. Ekstrak dengan password: `infected`
4. Analisis menggunakan Wireshark dengan langkah yang sama di atas
5. Tulis investigation report berdasarkan temuan
