# 🎯 Week 21 · Day 6 (Bonus): Hands-On Learning

> **Rank**: SENTINEL | **Minggu ke-21** | Bonus Day

---

## 🌐 Platform Hari Ini

**[CyberDefenders — Log Analysis Challenges](https://cyberdefenders.org/blueteam-ctf-challenges/)**
Platform Blue Team CTF gratis yang menyediakan challenge berbasis analisis log nyata. Kamu akan menganalisis dataset log dan menjawab pertanyaan investigasi.

💰 **Biaya**: Gratis (registrasi gratis, banyak challenge gratis)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menganalisis log file menggunakan tools CLI (`grep`, `awk`, `sort`, `uniq`)
2. Mengidentifikasi indikator serangan dalam log web server
3. Menjawab pertanyaan forensik berdasarkan bukti di log

---

## 📋 Requirement

* Akun CyberDefenders (gratis)
* Terminal Linux (VM/WSL)
* Tools: `grep`, `awk`, `sort`, `uniq`, `cut` (sudah tersedia di Linux)
* Wireshark (jika challenge melibatkan PCAP)

> ⚠️ **Jika belum punya akun CyberDefenders**: Buka [cyberdefenders.org](https://cyberdefenders.org), klik **Register**, daftar dengan email. Gratis.

---

## 📝 Prosedur

### Langkah 1: Akses Platform & Pilih Challenge
1. Login ke [cyberdefenders.org](https://cyberdefenders.org)
2. ke **Blue Team CTF Challenges**
3. Filter berdasarkan:
 - Difficulty: **Easy**
 - Category: **Network Forensics** atau **Log Analysis**
4. Pilih salah satu challenge gratis (contoh: **"WebStrike"**, **"PacketMaze"**, atau challenge log lainnya yang tersedia)

> 💡 **Tips memilih challenge**: Pilih yang bertag *Log Analysis* atau *Web* — ini paling relevan dengan materi minggu ini.

### Langkah 2: Unduh Dataset
1. Klik challenge yang dipilih
2. Baca deskripsi skenario (siapa korban, apa yang terjadi)
3. Unduh file challenge (biasanya format ZIP)
4. Ekstrak file:
 ```bash
 unzip challenge-file.zip -d ~/ctf-week21/
 cd ~/ctf-week21/
 ls -la
 ```

### Langkah 3: Analisis Log
Tergantung tipe file yang diberikan:

**Jika file LOG (access.log / auth.log):**
```bash
# Lihat 20 baris pertama
head -20 access.log

# Hitung total request
wc -l access.log

# Temukan IP dengan request terbanyak
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head 10

# Cari indikator SQLi
grep -i "union\|select\|1=1\|or 1" access.log

# Cari indikator path traversal
grep "\.\.\/" access.log

# Cari response error (4xx, 5xx)
awk '$9 ~ /^[45]/' access.log | head 20
```

**Jika file PCAP:**
```bash
# Buka di Wireshark
wireshark challenge.pcap &

# Atau gunakan tshark di CLI
tshark -r challenge.pcap -Y "http.request" | head 20
```

> 💡 **Strategi analisis**: Mulai dari gambaran besar (siapa berkomunikasi dengan siapa, berapa banyak request), lalu zoom in ke anomali (request mencurigakan, payload berbahaya).

### Langkah 4: Jawab Pertanyaan Challenge
1. Kembali ke halaman challenge di CyberDefenders
2. Jawab setiap pertanyaan berdasarkan analisis kamu
3. Submit jawaban
4. Jika salah, baca ulang pertanyaan — mungkin ada format jawaban yang spesifik

### Langkah 5: Dokumentasi
Tulis SOC Shift Handover Log:
```markdown
# SOC Shift Handover Log — Week 21
- Challenge: [nama challenge]
- Analyst: [nama]

## Temuan Utama
1. IP penyerang: [IP]
2. Tipe serangan: [SQLi/XSS/Brute Force/dll]
3. Jumlah request mencurigakan: [angka]
4. Bukti: [perintah yang digunakan + output]

## Perintah CLI yang Digunakan
- `grep "xxx" access.log` → menemukan [temuan]
- `awk... | sort | uniq -c` → mengidentifikasi [temuan]
```

---

## 🏁 Target Output

* ✅ Minimal **1 challenge** CyberDefenders selesai (atau progress signifikan)
* 📝 **SOC Shift Handover Log** dengan temuan dan bukti
* 📝 Daftar perintah CLI yang paling berguna dari analisis hari ini
* 📸 Tangkapan layar terminal yang menampilkan hasil analisis log

---

## 🔄 Fallback

Jika CyberDefenders tidak bisa diakses:
1. Unduh sample access.log dari [SecRepo.com](https://www.secrepo.com/) (gratis)
2. Analisis log menggunakan perintah CLI yang sama:
 ```bash
 # Top 10 IP addresses
 awk '{print $1}' access.log | sort | uniq -c | sort -rn | head 10
 
 # Cari request mencurigakan
 grep -iE "(union|select|script|alert|../)" access.log
 
 # Distribusi status code
 awk '{print $9}' access.log | sort | uniq -c | sort -rn
 ```
3. Tulis laporan analisis berdasarkan temuan dari sample log
