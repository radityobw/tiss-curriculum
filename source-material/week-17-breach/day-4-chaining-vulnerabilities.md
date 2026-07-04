# 💀 Week 17 · Day 4: Chaining Vulnerabilities

> **Rank**: BREACH | **Minggu ke-17**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 17 · Day 4/5 | BREACH Rank (Minggu 3 dari 5) | Overall: 84/120 hari (71%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** logika eksploitasi tingkat lanjut menggunakan metode Rantai Kerentanan (*Chaining Vulnerabilities*).
2. **Menggabungkan** dua atau lebih celah keamanan berskala kecil (seperti *XSS* & *IDOR*) menjadi satu serangan yang berdampak besar.
3. **Mengevaluasi** skenario eksploitasi gabungan yang dapat berujung pada *Remote Code Execution (RCE)* atau *Account Takeover (ATO)*.

---

## 📖 Materi Inti

### Rantai Kerentanan (Vulnerability Chaining)

Seringkali, seorang *Bug Hunter* atau *Pentester* menemukan celah berisiko rendah atau celah yang sulit dieksploitasi secara langsung. Contohnya adalah penemuan *Self-XSS* (skrip XSS yang hanya tereksekusi di browser penyerangnya sendiri) atau *Open Redirect* (kemampuan mengalihkan URL). Program *Bug Bounty* biasanya melabeli temuan terisolasi ini dengan tingkat bahaya terendah (*Low/Informational Severity*).

Namun, bagi pentester tingkat mahir, kerentanan yang terisolasi tersebut bisa digabungkan (dirantai atau *Chained*) untuk menghasilkan eksploitasi tingkat *High* atau *Critical*!

**Chaining Vulnerabilities** adalah teknik menggabungkan dua atau lebih kelemahan keamanan secara berurutan untuk mengeksekusi satu serangan fatal yang mampu membobol sistem secara menyeluruh.

### Contoh Skenario: SSRF + Local XSS

1. **Celah 1 (Low Severity):** Kamu menemukan kerentanan *SSRF* yang bisa dipakai untuk mengakses halaman dasbor admin internal (`127.0.0.1/admin`). Sayangnya, halaman itu hanya menampilkan teks laporan dan tidak ada tindakan sensitif yang bisa dilakukan.
2. **Celah 2 (Low Severity):** Di halaman profilmu sendiri, kolom *username* rentan terhadap *Stored XSS*. Karena kamu hanya pengguna biasa, *payload XSS* tersebut hanya tereksekusi di komputermu sendiri tanpa bisa menyerang pengguna lain atau Admin (*Self-XSS*).

**Saatnya Merantai (The Chain Execution):**
1. Kamu menyuntikkan *payload XSS* pencuri sesi ke input *Username* milikmu sendiri. (Saat ini, skrip tersebut tidak berbahaya bagi orang lain).
2. Lalu, kamu memanfaatkan celah *SSRF* tadi untuk memaksa *server* (melalui `127.0.0.1/admin`) memuat halaman profilmu dari dalam jaringan internal.
3. Karena *server* memuat halaman profilmu **secara lokal (menggunakan hak akses aplikasi/Admin internal)**, *payload XSS* yang bersemayam di profilmu akan otomatis tereksekusi dalam konteks *server*! Rentetan ini sukses mengeksekusi XSS terhadap sistem internal target.
4. *(Imbalan temuan yang tadinya berstatus Low Severity dapat meningkat tajam menjadi Critical!)*

### Contoh Skenario: CSRF + Account Takeover

Bagaimana jika penyerang tidak bisa mencuri kata sandi korban secara langsung?
Penyerang bisa menggunakan eksploitasi *CSRF* untuk **memaksa sistem mengubah Alamat Email korban** menjadi email milik penyerang tanpa sepengetahuan korban.

Begitu alamat email korban berhasil diubah di *database*, penyerang tinggal membuka halaman *Login*, lalu menggunakan fitur **"Lupa Password"**. Tautan pemulihan sandi (*password reset link*) akan otomatis dikirimkan ke kotak masuk email milik penyerang! Akun korban pun berhasil diambil alih secara penuh *(Account Takeover)*.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan nalar pengujian *Chaining* di dalam benakmu (*Mental Simulation*)!

1. Bayangkan kamu sedang menganalisis situs yang memiliki fitur *"Upload PDF Invoice"*.
2. Kamu menemukan fitur itu rentan terhadap *IDOR*. Jika kamu mengubah parameter URL `invoice_id=20`, kamu bisa melihat dokumen *Invoice* milik pengguna lain atau Admin.
3. Di sisi lain, kamu juga menemukan celah *Stored XSS* di nama file PDF tersebut (server akan mengeksekusi JavaScript jika nama file disisipi `<script>`).
4. **RANTAIKAN EKSPLOITASINYA!** Kamu unggah *Invoice* PDF palsu yang nama filenya telah ditanami *payload XSS* pencuri *Cookie*. Kemudian, kamu manfaatkan celah *IDOR* untuk mengirimkan tautan URL langsung (*direct link*) dokumen palsu tersebut ke Admin.
5. Saat Admin membuka URL nota tersebut, skrip XSS tereksekusi di browser Admin, dan *Cookie Login* Admin berhasil kamu curi!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa definisi teknis dari teknik Chaining Vulnerabilities?</summary>

**Jawaban:** Teknik menggabungkan dua atau lebih celah keamanan berskala kecil (berisiko rendah jika dieksekusi sendiri-sendiri) menjadi satu rentetan serangan yang menghasilkan eksploitasi fatal (seperti Account Takeover atau RCE).
</details>

<details>
<summary>❓ Bagaimana cara agar kerentanan Self-XSS (kerentanan XSS yang hanya menyerang pengunggahnya sendiri) bisa menjadi eksploitasi berbahaya?</summary>

**Jawaban:** Kerentanan tersebut dihubungkan (*chained*) dengan celah lain seperti *CSRF* atau *SSRF* untuk menjebak korban (seperti Admin atau Server internal) agar mengakses halaman yang memuat *payload XSS* tersebut.
</details>

<details>
<summary>❓ Ketika pentester sukses mengeksploitasi celah CSRF pada formulir "Ganti Alamat Email" korban, insiden berbahaya apa yang dapat terjadi selanjutnya?</summary>

**Jawaban:** Serangan perampasan akun *(Account Takeover / ATO)*, di mana penyerang bisa menggunakan fitur "Lupa Password" untuk mendapatkan akses login penuh ke akun korban melalui email penyerang.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami logika teknik *Chaining Vulnerabilities*.
- [ ] Saya fasih menjabarkan alur penggabungan *Self-XSS* dengan *SSRF*.
- [ ] Saya mengerti cara merangkai celah *CSRF* menjadi *Account Takeover (ATO)*.
- [ ] Saya paham bahwa celah keamanan skala rendah tidak boleh diabaikan karena dapat dirantai.
- [ ] Saya telah menjawab seluruh *Quiz Kilat* dengan benar.

---

## 🔗 Resources

- [HackerOne Hacktivity](https://hackerone.com/hacktivity) — Platform *Bug Bounty* publik tempat kamu bisa membaca laporan (*writeup*) tentang bagaimana *Bug Hunter* profesional merantai celah untuk mendapatkan temuan bernilai tinggi.

---

## ➡️ Besok

**Day 5: Lab & Mission: PortSwigger XSS/CSRF Labs** — Kamu telah belajar tentang celah *XSS*, *CSRF*, *SSRF*, celah *File Upload*, dan cara merantai (*Chaining*) kerentanan. Besok, kamu akan terjun langsung ke laboratorium simulasi *PortSwigger Web Security Academy* untuk menaklukkan tantangan kerentanan web. Siapkan metodologi pengujianmu dan selesaikan tantangannya!

---

*📅 TISS Null Teaming · Week 17 · Day 4 · BREACH Rank*
