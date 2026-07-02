# 💀 Week 18 · Day 4: Other Tools (ZAP, ffuf, nikto)

> **Rank**: BREACH | **Minggu ke-18**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 18 · Day 4/5 | BREACH Rank (Minggu 4 dari 5) | Overall: 89/120 hari (74%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** keberadaan alternatif di luar *Burp Suite*.
2. **Mengoperasikan** mesin pemindai otomatis web gratisan kasta *OWASP ZAP*.
3. **Mengeksploitasi** pelacak pemindai web purba *Nikto* dan *Ffuf*.

---

## 📖 Materi Inti

### Alternatif Pengujian Kategori Open Source

*Burp Suite* memang laksana logis utama bagi penganalisis peretas Web. Tapi lisensi *Scanner* profesionalnya yang masuk belasan juta rupiah terkadang menjadi rintangan bagi penganalisis pemula.
Sebagai penganalisis peretas ulung, Anda dituntut fleksibel . Dunia *Open Source* menjajakan balok perkakas kasta alternatif yang tak kalah mumpuni!

### 1. OWASP ZAP (Zed Attack Proxy)

ini merupakan kompetitor sejati *Burp Scanner*!
**ZAP** adalah *Scanner & Proxy* sumber terbuka (100% Gratis) gubahan ordo *OWASP*.
Seluruh fungsi pemindai otomatis (*Automated Vulnerability Scanner*) yang digembok di *Burp Community*, dibentangkan menganga gratis di arsitektur *ZAP*!
Penganalisis cukup memancangkan *URL* target, menekan tombol *Attack*, lantas *ZAP* bakal mengirimkan web menyuntikkan ribuan kueri *SQLi* dan *XSS* lantas memuntahkan laporan komplit (*Automated Scan*).

*Kenapa tak semua orang pakai ZAP?* Karena meski otomatisasinya buas, tata letak antarmuka (UI/UX) dan fitur manual *ZAP* terkesan kaku, dan lambat merespons bila disandingkan *Repeater* punya *Burp*. (*Pro-tip : Kombinasikan ZAP untuk Scan Otomatis, lantas eksploitasi manual di Burp!*).

### 2. Nikto: Mesin Pemindai Kerentanan Infrastruktur Web

Bila *ZAP* meraba celah, **Nikto** adalah senapan terminal purba (berbasis *Perl*) yang memburu mengendus kelalaian *Security Misconfiguration* .
*Nikto* bakal mengobrak-abrik menembak *server* (misal: peladen *Apache 2.4*), lantas menjerit melaporkan letak berkas `.git` yang terlantar, ketiadaan *Security Headers*, atau versi *PHP* yang sudah usang.
**Komando:** `nikto -h http://target.com` *(Catatan: Teramat Sangat Bising!)*.

### 3. Ffuf: Si alat Kecepatan Tinggi (Fuzzing)

(Anda telah meraba *Ffuf* di materi *Active Recon*). Tapi ketahuilah, **ffuf (Fuzz Faster U Fool)** tak sebatas pencari direktori tersembunyi!
Ditenagai bahasa *Golang*, *Ffuf* adalah payload tercepat untuk menggempur membantai (*Fuzzing*) parameter. Kamu meraba parameter `id=1`? *Ffuf* mampu menghantam parameter itu dengan sejuta payload *XSS* dalam hitungan detik!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Ayo unjuk kekuatan mengirimkan pemindai gratisan *Nikto*!

1. Buka pelataran balok Terminal *Kali Linux/Parrot OS*.
2. Pastikan `nikto` terpasang. (Biasanya bawaan orisinal instalasi distro keamanan siber).
3. Kita bidik server legal *scanme* :
 `nikto -h http://scanme.nmap.org`
4. Tatap rentetan tu serangan meriam yang mengalir di layar konsol terminalmu.
5. Dalam beberapa menit, *Nikto* bakal menjerit melaporkan absensi *Anti-clickjacking X-Frame-Options* header, membeberkan identitas `Apache/2.4`, dan menerawang keusangan instalasi. (Inilah senjata audit kelalaian miskonfigurasi!).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah anatomi peretasan alternatif, apa julukan gratisan gubahan ordo <i>OWASP</i> yang diagungkan laksana penantang dari belenggu mahalnya <i>Scanner</i> Burp Suite?</summary>

**Jawaban:** OWASP ZAP (Zed Attack Proxy).
</details>

<details>
<summary>❓ Ketika meluncurkan pemindaian mencari celah kelalaian tata letak (Security Misconfigurations) di OS terminal, utusan senapan purba apakah yang kerap diandalkan melacak versi usang dan ketiadaan Header?</summary>

**Jawaban:** Nikto.
</details>

<details>
<summary>❓ Di ranah pengujian kueri percobaan tebakan <i>Fuzzing</i>, bedil mutakhir apa (berbahasa Golang) yang menobatkan dirinya memegang gelar tercepat melontarkan serangan <i>Wordlists</i> membabi-buta parameter?</summary>

**Jawaban:** Ffuf (Fuzz Faster U Fool).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap dominasi peranti gratisan *OWASP ZAP* - [ ] Saya fasih membelah kasta peruntukan *ZAP* (Scan) dikawinkan *Burp* (Manual) - [ ] Saya menguasai titah serangan kueri purba bedil *Nikto* - [ ] Saya paham kebuasan kecepatan *Golang* membalut *Ffuf* - [ ] Saya telah menjawab seluruh ulasan *quiz kilat* 
---

## 🔗 Resources

- [OWASP ZAP Official](https://www.zaproxy.org/) — unduhan meriam pemindai otomatis gratis sedunia.

---

## ➡️ Besok

**Day 5: Lab & Mission: Full Pentest Machine** — Empat hari mendaras meraba memegang gagang peranti usai dilalui. Esok harinya, tibalah penobatan kasta *BREACH*! Dirimu ditantang menanggalkan teori dan merengkuh pedang *Burp Suite* di padang lab *TryHackMe* (Full Pentest End-to-End). Gunakan *Proxy, Repeater*, dan *Intruder* demi membedah menginjeksi mengoyak jiwa mesin uji tanpa ampun!

---

*📅 TISS Null Teaming · Week 18 · Day 4 · BREACH Rank*
