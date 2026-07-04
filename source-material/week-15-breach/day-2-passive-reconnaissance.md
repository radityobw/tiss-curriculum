# 💀 Week 15 · Day 2: Passive Reconnaissance

> **Rank**: BREACH | **Minggu ke-15**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 15 · Day 2/5 | BREACH Rank (Minggu 1 dari 5) | Overall: 72/120 hari (60%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep *Passive Reconnaissance* (Pengintaian Pasif) untuk mengumpulkan informasi tanpa terdeteksi oleh target.
2. **Mengekstraksi** data kepemilikan domain dan infrastruktur menggunakan *WHOIS* dan *DNS lookup*.
3. **Mengeksploitasi** sumber data terbuka (OSINT) menggunakan teknik *Google Dorking* dan mesin pencari *Shodan*.

---

## 📖 Materi Inti

### Seni Mengintai Tanpa Menyentuh

Fase **Reconnaissance (Pengumpulan Intelijen)** terbagi menjadi dua: *Active* dan *Passive*.
Pengumpulan intelijen pasif (**Passive Recon**) berarti kita mencari informasi target menggunakan sumber publik yang sudah tersedia di internet (*Open Source Intelligence / OSINT*). 

Dalam fase ini, kita **tidak pernah** mengirimkan *request* atau paket jaringan secara langsung ke server target. Akibatnya, server target tidak akan mencatat alamat IP kita di log mereka, dan sistem keamanan target tidak akan membunyikan alarm peringatan.

Sebagai penguji penetrasi, kamu akan mencari data sensitif yang tidak sengaja terekspos ke publik oleh pihak developer atau administrator.

### Senjata Pengintaian Pasif

1. **WHOIS & DNS Lookup**
   Saat seseorang mendaftarkan *domain* (misalnya `target.com`), mereka harus menyertakan data administrasi seperti nama, email, dan nomor telepon. Kamu bisa melihat data ini menggunakan perintah `whois target.com` di terminal. Untuk mencari tahu alamat IP server atau rincian DNS (seperti server email), kamu bisa menggunakan perintah seperti `dig` atau `nslookup`.

2. **Google Dorking (Operator Canggih Mesin Pencari)**
   Google adalah salah satu alat OSINT terkuat jika kamu tahu cara menyusun kueri pencariannya (*Google Hacking Database / Google Dorking*). Kamu bisa menginstruksikan Google untuk memfilter dokumen rahasia, *file* konfigurasi, atau halaman *login admin* yang secara tidak sengaja terindeks.
   - `site:target.com` (Membatasi pencarian hanya pada domain spesifik tersebut).
   - `filetype:pdf` (Mencari file dengan ekstensi tertentu, misalnya PDF).
   - `inurl:admin` (Mencari URL yang memiliki kata "admin" di dalamnya).

3. **Shodan (Mesin Pencarinya Hacker)**
   Jika Google mencari dan mengindeks *website*, **Shodan** mengindeks perangkat keras yang terhubung ke internet. Shodan memindai *router*, kamera CCTV, server *database*, dan *web server* di seluruh dunia. Kamu bisa melihat port apa saja yang terbuka dan *software* versi berapa yang digunakan oleh target, tanpa perlu melakukan *scanning* sendiri secara langsung.

4. **theHarvester**
   Ini adalah alat bawaan *Kali Linux* yang secara otomatis menyisir mesin pencari (Google, LinkedIn, Bing, dll) untuk mengumpulkan ribuan alamat *email* karyawan dari domain target. Data *email* ini sangat berharga untuk tahap serangan rekayasa sosial (*phishing*).

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari mempraktikkan teknik pencarian *Google Dorking*!

1. Buka [Google](https://www.google.com).
2. Bayangkan kamu sedang mengaudit domain `tiss.or.id` dan ingin melihat apakah ada dokumen PDF yang terekspos. Ketikkan kueri ini:
   `site:tiss.or.id filetype:pdf`
   *(Catatan: Jika hasilnya kosong, kamu bisa mencoba dengan domain universitas atau instansi publik lainnya).*
3. Coba cari halaman *login* yang mungkin disembunyikan menggunakan kueri kombinasi:
   `site:target-kampusmu.ac.id inurl:login OR inurl:admin`
4. Selanjutnya, buka [shodan.io](https://www.shodan.io/). Di kotak pencarian, masukkan nama kotamu, misalnya `city:"Jakarta"`. Kamu akan melihat berbagai perangkat, server, dan *port* terbuka yang terindeks secara bebas di internet!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar antara <i>Passive Reconnaissance</i> dan <i>Active Reconnaissance</i>?</summary>

**Jawaban:** *Passive Recon* mengumpulkan informasi melalui sumber pihak ketiga (seperti Google dan WHOIS) tanpa mengirim *request* langsung ke server target, sehingga IP kita tidak tercatat. Sedangkan *Active Recon* berinteraksi dan mengirim paket jaringan secara langsung ke server target, yang dapat terekam oleh sistem keamanan target dan memicu alarm.
</details>

<details>
<summary>❓ Operator <i>Google Dorking</i> apa yang digunakan untuk membatasi pencarian hanya pada satu domain tertentu?</summary>

**Jawaban:** Operator `site:` (contoh: `site:tiss.or.id`).
</details>

<details>
<summary>❓ Mesin pencari apa yang digunakan secara khusus untuk memetakan perangkat IoT (seperti CCTV dan Router) serta infrastruktur <i>port/service</i> yang terhubung ke internet?</summary>

**Jawaban:** Shodan.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami konsep Pengintaian Pasif (*Passive Recon*) dan OSINT.
- [ ] Saya tahu cara menggunakan perintah `WHOIS` untuk mendapatkan informasi domain.
- [ ] Saya telah mempraktikkan *Google Dorking* menggunakan operator `site:`, `filetype:`, dan `inurl:`.
- [ ] Saya mengetahui fungsi mesin pencari *Shodan*.
- [ ] Saya telah menyelesaikan dan memahami jawaban dari *Quiz Kilat*.

---

## 🔗 Resources

- [Google Hacking Database (GHDB)](https://www.exploit-db.com/google-hacking-database) — Arsip lengkap berbagai *payload Google Dorking* untuk mencari celah dan file sensitif.
- [Shodan.io](https://www.shodan.io/) — Mesin pencari khusus untuk perangkat keras dan *port* yang terhubung ke internet.

---

## ➡️ Besok

**Day 3: Active Reconnaissance** — Setelah mengumpulkan informasi pasif dari sumber publik, besok kita akan beralih ke tahap **Active Reconnaissance**. Kita akan berinteraksi langsung dengan server target menggunakan alat andalan peretas: **Nmap**, untuk memindai port dan layanan yang terbuka. Selain itu, kita juga akan belajar menemukan *file* dan direktori yang disembunyikan di dalam *web server* menggunakan teknik *Directory Bruteforcing* (dengan *tools* seperti Gobuster atau Ffuf). Bersiaplah untuk serangan yang lebih agresif!

---

*📅 TISS Null Teaming · Week 15 · Day 2 · BREACH Rank*
