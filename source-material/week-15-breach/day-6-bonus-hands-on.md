# 🎯 Week 15 · Day 6 (Bonus): Hands-On Learning

> **Rank**: BREACH | **Minggu ke-15** | Bonus Day

---

## 🌐 Platform Hari Ini

**[TryHackMe — Nmap Room](https://tryhackme.com/room/furthernmap)**
Room gratis TryHackMe yang mengajarkan penggunaan Nmap secara mendalam: scan types, scripting engine, dan teknik evasion. Sangat relevan dengan materi reconnaissance minggu ini.

💰 **Biaya**: Gratis (Free Room)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menggunakan berbagai tipe scan Nmap (SYN, TCP, UDP) di lingkungan lab
2. Memahami Nmap Scripting Engine (NSE) untuk deteksi kerentanan
3. Menjawab pertanyaan berbasis skenario reconnaissance nyata

---

## 📋 Requirement

* Akun TryHackMe (sudah dibuat di Week 1 Day 5)
* Peramban web modern (Chrome/Firefox)
* Koneksi internet stabil

> ⚠️ **Room ini menggunakan AttackBox** (mesin virtual di browser, gratis tapi terbatas 1 jam/hari). Alternatif: gunakan OpenVPN + Kali VM lokal untuk waktu tak terbatas.

---

## 📝 Prosedur

### Langkah 1: Akses Room
1. Login ke [tryhackme.com](https://tryhackme.com)
2. Buka URL: `https://tryhackme.com/room/furthernmap`
3. Klik **Join Room**
4. Klik **Start AttackBox** (tombol biru di atas) — tunggu mesin virtual terbuka di browser

> 💡 **AttackBox memerlukan waktu ~1-2 menit** untuk loading. Selama menunggu, baca materi Task 1.

### Langkah 2: Pelajari Nmap Scan Types (Task 1-5)
1. Baca penjelasan setiap tipe scan:
 - **TCP Connect Scan** (`-sT`)
 - **SYN Scan** (`-sS`) — *half-open scan*
 - **UDP Scan** (`-sU`)
2. Jawab pertanyaan interaktif berdasarkan materi
3. Praktikkan perintah di terminal AttackBox:
 ```bash
 nmap -sS [target-IP]
 nmap -sT [target-IP]
 nmap -sU --top-ports 20 [target-IP]
 ```

> 💡 **Target IP** akan ditampilkan setelah kamu deploy machine di dalam room. Cek instruksi di task yang meminta deploy.

### Langkah 3: NSE Scripts (Task 6-8)
1. Pelajari Nmap Scripting Engine (NSE):
 ```bash
 nmap --script=vuln [target-IP]
 nmap --script=default [target-IP]
 ```
2. Jawab pertanyaan tentang NSE scripts
3. Eksperimen dengan script categories: `safe`, `intrusive`, `vuln`

### Langkah 4: Firewall Evasion (Task 9-10)
1. Pelajari teknik evasion:
 - **Fragmentation**: `nmap -f [target-IP]`
 - **Decoy**: `nmap -D RND:5 [target-IP]`
 - **Timing**: `nmap -T0 [target-IP]`
2. Jawab pertanyaan terakhir
3. Pastikan semua task menunjukkan ✅

---

## 🏁 Target Output

* ✅ Room **Nmap** selesai 100% (semua task terjawab)
* 📸 Tangkapan layar profil TryHackMe yang menunjukkan room completed
* 📝 Cheatsheet: 5 perintah Nmap favorit beserta penjelasannya

---

## 🔄 Fallback

Jika TryHackMe tidak bisa diakses atau AttackBox sudah habis waktunya:
1. Praktikkan Nmap di **VM lokal** (Kali → scan Ubuntu VM):
 ```bash
 nmap -sV -sC [IP-Ubuntu-VM]
 nmap -p- [IP-Ubuntu-VM]
 nmap --script=vuln [IP-Ubuntu-VM]
 ```
2. Dokumentasikan output dari setiap scan
3. Identifikasi port terbuka dan layanan yang berjalan
