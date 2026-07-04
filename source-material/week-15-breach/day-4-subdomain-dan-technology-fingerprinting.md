# 💀 Week 15 · Day 4: Subdomain & Technology Fingerprinting

> **Rank**: BREACH | **Minggu ke-15**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 15 · Day 4/5 | BREACH Rank (Minggu 1 dari 5) | Overall: 74/120 hari (62%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memperluas** cakupan permukaan serangan (*Attack Surface*) melalui pencarian *Subdomain*.
2. **Mengoperasikan** alat bantu pencarian *Subdomain* seperti *Sublist3r* dan *Amass*.
3. **Mendeteksi** tumpukan teknologi yang digunakan oleh situs target (*Technology Fingerprinting*).

---

## 📖 Materi Inti

### Memperlebar Peta: Mengapa Memburu Subdomain?

Domain utama sebuah organisasi (misalnya `www.banktiss.com`) biasanya dijaga dengan pengamanan yang sangat ketat. Namun, sebuah organisasi sering kali memiliki *Subdomain* yang tersembunyi atau terlupakan (seperti portal *staging* di `dev.banktiss.com` atau layanan lama di `vpn-lama.banktiss.com`). Subdomain ini sering kali tidak terpantau, jarang di-*update*, dan menjadi titik masuk yang sangat rapuh bagi para peretas.

Aktivitas mencari dan mendaftar subdomain ini disebut **Subdomain Enumeration**, sebuah langkah fundamental dalam *Bug Bounty* maupun audit keamanan.

**Alat Pencari Subdomain:**
- **Sublist3r:** Alat klasik yang sangat cepat untuk mengekstrak subdomain menggunakan mesin pencari publik (Google, Bing, Baidu) dan sumber OSINT lainnya.
- **Amass:** Alat mutakhir buatan OWASP. Amass tidak hanya mencari melalui API dan mesin pencari, tetapi juga membedah sertifikat SSL dan DNS untuk menemukan subdomain yang sangat tersembunyi.

```bash
# Contoh penggunaan Sublist3r untuk mencari subdomain
sublist3r -d target.com
```

### Membedah Susunan Server: Technology Fingerprinting

Setelah menemukan *Subdomain* atau IP, langkah selanjutnya adalah mengetahui teknologi perangkat lunak (*tech stack*) apa yang digunakan target. Apakah server tersebut menggunakan *PHP* versi lama? Menggunakan kerangka kerja *React*? Atau dijalankan di atas *Nginx*?

Aktivitas mengidentifikasi perangkat lunak dan arsitektur yang digunakan oleh aplikasi target ini disebut **Technology Fingerprinting** (Identifikasi Sidik Jari Teknologi).

**Senjata Fingerprinting:**
1. **Wappalyzer (Ekstensi Browser):** Alat ini dipasang sebagai ekstensi di *Chrome* atau *Firefox*. Saat kamu mengunjungi sebuah situs, Wappalyzer akan secara otomatis mendeteksi dan menampilkan semua teknologi yang digunakan (contoh: "Situs ini menggunakan React, Express, dan Nginx").
2. **WhatWeb (Terminal):** Alat bawaan *Kali Linux* yang memiliki fungsi serupa dengan Wappalyzer, namun dijalankan melalui terminal dan sangat cocok untuk proses otomatisasi (*scripting*).
```bash
whatweb https://dev.target.com
```

Dengan mengetahui versi spesifik dari perangkat lunak (misalnya, target menggunakan *Apache 2.4.49*), kamu bisa langsung mencari kerentanan publik (*CVE - Common Vulnerabilities and Exposures*) dan kode eksploitasinya (Exploit) di internet. Hal ini sangat menghemat waktu dibandingkan mencoba eksploitasi secara acak.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari mempraktikkan *Technology Fingerprinting* menggunakan Wappalyzer!

1. Buka *browser* Google Chrome atau Mozilla Firefox.
2. Buka menu ekstensi (*Extensions/Add-ons*) dan cari lalu instal **Wappalyzer**.
3. Pastikan ekstensi tersebut aktif (ikon Wappalyzer akan muncul di bilah ekstensi).
4. Kunjungi situs publik mana saja, misalnya `academy.tiss.or.id` atau situs berita.
5. Klik ikon Wappalyzer. 
6. Perhatikan hasilnya! Semua teknologi yang membangun situs tersebut, mulai dari kerangka *Frontend* (UI), *Web Server*, hingga layanan analitik, akan terbongkar. Sekarang kamu tahu teknologi apa yang sedang kamu hadapi!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam kegiatan <i>Bug Bounty</i> atau <i>Pentesting</i>, mengapa penyerang sering kali lebih fokus mencari celah di <i>Subdomain</i> (seperti `dev.target.com`) daripada di domain utama?</summary>

**Jawaban:** Domain utama biasanya diawasi dengan ketat dan sering diperbarui. Sebaliknya, *subdomain* (seperti server pengembangan/staging) sering kali dilupakan oleh administrator, jarang mendapatkan *patch* keamanan, dan memiliki tingkat perlindungan yang jauh lebih lemah.
</details>

<details>
<summary>❓ Sebutkan dua alat (<i>tools</i>) populer yang digunakan untuk mencari dan mengumpulkan daftar <i>Subdomain</i>!</summary>

**Jawaban:** Amass dan Sublist3r.
</details>

<details>
<summary>❓ Apa keuntungan mengetahui versi spesifik dari teknologi server target (misalnya mengetahui bahwa target menggunakan Nginx 1.18.0) melalui proses <i>Technology Fingerprinting</i>?</summary>

**Jawaban:** Dengan mengetahui versi spesifiknya, kita bisa mencari kerentanan (*CVE*) yang memang secara khusus ada pada versi tersebut. Ini mencegah kita membuang-buang waktu mencoba metode serangan yang tidak relevan.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami pentingnya mencari *Subdomain* untuk memperluas permukaan serangan (*attack surface*).
- [ ] Saya mengenal *tools* pencari subdomain seperti *Sublist3r* dan *Amass*.
- [ ] Saya telah menginstal dan mencoba ekstensi *Wappalyzer* di *Mini Lab*.
- [ ] Saya mengerti apa itu *Technology Fingerprinting* dan fungsinya.
- [ ] Saya telah menyelesaikan dan memahami jawaban dari *Quiz Kilat*.

---

## 🔗 Resources

- [Wappalyzer Extension](https://www.wappalyzer.com/) — Ekstensi browser untuk mendeteksi teknologi pembentuk website.
- [OWASP Amass](https://github.com/owasp-amass/amass) — Repositori alat pencari subdomain yang sangat kuat buatan OWASP.

---

## ➡️ Besok

**Day 5: Lab & Mission: Full Recon Report** — Semua teknik pengumpulan informasi telah kamu pelajari: *Passive Recon* (WHOIS, Google Dork), *Active Recon* (Nmap, Directory Bruteforcing), *Subdomain Enumeration*, dan *Technology Fingerprinting* (Wappalyzer). Besok, kamu akan mempraktikkan semuanya dalam simulasi laboratorium resmi pertamamu! Kamu akan mengumpulkan semua informasi dan menyusunnya menjadi sebuah laporan *Reconnaissance* (Recon Report), layaknya seorang *Bug Bounty Hunter* profesional!

---

*📅 TISS Null Teaming · Week 15 · Day 4 · BREACH Rank*
