# 💀 Week 15 · Day 4: Subdomain & Technology Fingerprinting

> **Rank**: BREACH | **Minggu ke-15**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 15 · Day 4/5 | BREACH Rank (Minggu 1 dari 5) | Overall: 74/120 hari (62%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memperluas** cakupan permukaan serangan (*Attack Surface*) melalui ekskavasi pemetaan turunan *Subdomain*.
2. **Mengoperasikan** perkakas penelusuran arsitektur *Subdomain* (*Sublist3r* & *Amass*).
3. **Mencetak-sidik** tumpukan arsitektur ekosistem perangkat teknologi situs (*Technology Fingerprinting*).

---

## 📖 Materi Inti

### Memperlebar Peta: Mengapa Memburu Subdomain?

Domain situs utama suatu organisasi (seperti `www.banktiss.com`) umumnya dipersenjatai dengan pengamanan arsitektur yang sangat tangguh. Namun di sisi lain, organisasi kerap membiarkan infrastruktur *Subdomain* tersembunyi (seperti portal *staging* `dev.banktiss.com` atau layanan usang `vpn-lama.banktiss.com`) beroperasi dengan minimnya pengawalan audit, menjadikan subdomain ini luput dari pembaruan modul aplikasi peladen sehingga berstatus sebagai sasaran eksploitasi peretasan yang rapuh.

Aktivitas memetakan daftar *Subdomain* ini dinamakan **Subdomain Enumeration**, sebuah tahapan penelusuran fundamental esensial dalam fase operasional rekognisi audit kompetisi keamanan *Bug Bounty*.

**Perkakas Ekskavator Subdomain:**
- **Sublist3r:** pencarian klasik namun tangguh yang mengekstrak jejak subdomain berbekal mesin peramban pencari terbuka OSINT publik (Google, Bing, Baidu).
- **Amass:** Perkakas mutakhir arsitektur keluaran OWASP. ini tidak sebatas menghimpun penelusuran API, melainkan juga menambang serta mengurai struktur arsip arsip sertifikat fungsi pelindung *SSL* dan *DNS*!

```bash
# Menembak peluncuran pencarian subdomain sasaran 
sublist3r -d target.com
```

### Membedah Susunan Tumpukan Peladen: Technology Fingerprinting

Pasca tahap penemuan sarang *Subdomain* atau ekstraksi IP dari Nmap, penganalisis kelak diwajibkan mengidentifikasi rincian tumpukan teknologi perangkat lunak (*tech stack*) arsitektur sasaran. Apakah peladen tersebut dirakit berbasis *PHP* usang? Ataukah menunggangi ekosistem konfigurasi antarmuka *Node.js Express*, atau kerangka kerja spesifik semacam *Laravel*?

Aktivitas mengidentifikasi wajah arsitektur instalasi perangkat lunak peladen *Backend* maupun antarmuka layanan web ini dinamai **Technology Fingerprinting** (Identifikasi Sidik Jari Teknologi).

**Senjata Fingerprinting:**
1. **Wappalyzer** (Pendekatan GUI Ekstensi Peramban): Peranti ini disematkan sebagai ekstensi pada peramban *Chrome*/*Firefox*. Penganalisis cukup mengeklik fungsionalitas fiturnya saat memuat sebuah situs, dan *Wappalyzer* akan seketika membongkar memaparkan seluruh entitas teknologi dan kerangka arsitektur situs tersebut (contoh laporannya: "Situs memuat kerangka *React, framework Express*, serta dilayani peladen *Nginx*").
2. **WhatWeb** (Pendekatan Kasta Terminal): bedil operasi bawaan distribusi lingkungan *Kali Linux* yang menunaikan fungsionalitas analisis pemetaan identik, namun memuntahkan laporannya secara ringkas ke antarmuka eksekusi layar konsol terminal .
```bash
whatweb https://dev.target.com
```

Dengan mengetahui versi spesifikasi perangkat lunak peladen (*misalnya penemuan deteksi instalasi Apache 2.4.49*), spesialis keamanan penganalisis dapat segera menelusuri penugasan referensi mesin pencari atau literatur data *CVE (Common Vulnerabilities and Exposures)* guna mendapati dokumen publik pelaporan kerentanan beserta senjata eksploitasi siap pakai arsitektur aplikasi tersebut tanpa pemborosan operasional deduksi manual yang sia-sia.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari mempraktikkan pelacakan instalasi alat sadap *Wappalyzer*!

1. Buka lingkungan instalasi operasi peramban Google Chrome atau Mozilla Firefox Anda.
2. Jelajahi menu ekstensi peramban (*Extensions/Add-ons*) dan instal perangkat ekstensi **Wappalyzer**.
3. Pastikan ekstensi tersebut telah aktif (ikon Wappalyzer akan tersemat di sudut atas peramban).
4. Kunjungi tautan situs publik semisal `academy.tiss.or.id` atau portal publik `tokopedia.com`.
5. Klik ikon Wappalyzer. 
6. Perhatikan pelaporannya! Seluruh arsitektur tersembunyi konfigurasi infrastruktur perangkat lunak web yang membangun situs terkait (mulai kerangka UI *Frontend*, server *Web Backend*, layanan peramban *Analytic*) niscaya terbongkar membeberkan spesifikasinya. Kini Anda menyadari persis nomenklatur arsitektur peranti lunak sasaran!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Menelaah eksekusi pendekatan strategis intelijen penganalisis keamanan kerentanan korporasi (*Bug Bounty*), alasan strategis logis apakah yang memotivasi penganalisis untuk mengalokasikan konsentrasi ekskavasi spesifik <i>Subdomain Enumeration</i> ketimbang mendedikasikan waktu sebatas menggedor keamanan situs utama?</summary>

**Jawaban:** Pintu benteng gerbang domain situs utama organisasi lazimnya diisolasi berlapis fungsionalitas pembaruan keamanan level prioritas. Sebaliknya, infrastruktur *Subdomain* semacam laman eksperimen (*dev/staging*) lazim terlantar fungsionalitas ketiadaan kontrol administrator dan jarang dilakukan peremajaan pembaruan patch (*update*), sehingga keberadaannya menjelma sebagai letak kerentanan permukaan serangan (*attack surface*) dengan resistansi perlindungan terlemah.
</details>

<details>
<summary>❓ Sebutkan titah nomenklatur dua peranti (<i>Tools</i>) primadona penganalisis intelijen *Red Team* yang kerap andal menyedot deteksi puluhan <i>Subdomain</i> rahasia!</summary>

**Jawaban:** Amass dan Sublist3r.
</details>

<details>
<summary>❓ Pasca pengoperasian penganalisis peramban arsitektur <i>Wappalyzer</i> lantas membentangkan penemuan sidik jari bahwasanya infrastruktur peladen memendam instalasi arsitektur <i>Nginx 1.18.0</i>, apa esensi signifikansi aktivitas pencetakan spesifikasi (<i>Technology Fingerprinting</i>) tersebut bagi persiapan operasi peretasan?</summary>

**Jawaban:** Mendeteksi tabir versi spesifik peladen memampukan penganalisis peretas mencari dan menelusuri literatur letak eksploitasi kerentanan perangkat keamanan *CVE (Common Vulnerabilities and Exposures)* pada pencarian yang memang menohok dan dipastikan secara logis hanya beroperasi mematahkan kerentanan aplikasi *Nginx 1.18.0*, menghindarkan penganalisis peretas dari eksekusi meluncurkan uji pelacakan payload eksekusi eksploitasi kerentanan yang tidak relevan (tidak *compatible*).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap pengetahuan strategis pemetaan pelacakan celah *Subdomain*
- [ ] Saya mengenali pemetaan pelacak ekskavasi ekstensi subdomain *Sublist3r* dan *Amass*
- [ ] Saya fasih mengoperasikan peranti ekstensi *Wappalyzer* dalam uji pembedahan operasional kerangka *Mini Lab*
- [ ] Saya tangkas menafsirkan perumusan faedah parameter *Technology Fingerprinting*
- [ ] Saya telah menyimak tuntas ulasan pelaporan penyerapan modul *Quiz Kilat*

---

## 🔗 Resources

- [Wappalyzer Extension](https://www.wappalyzer.com/) — Ekstensi peramban penganalisis pencetak arsitektur tumpukan web mutakhir.
- [OWASP Amass](https://github.com/owasp-amass/amass) — Repositori peramban andalan perburuan ekskavasi *Subdomain* rancangan OWASP.

---

## ➡️ Besok

**Day 5: Lab & Mission: Full Recon Report** — Segala pelacakan ekstraksi instalasi peramban intelijen logis (*Passive Reconnaissance: WHOIS, Google Dork*), fase pemetaan interaktif transmisi (*Active Recon: Nmap, Ffuf*), analisis enumerasi turunan sasaran (*Subdomain: Amass*), serta identifikasi tumpukan teknologi sasaran (*Technology Fingerprinting: Wappalyzer*) usai dikuasai! Esok hari, panggung *Lab* simulasi peretasan resmi pertamamu siap digunakan. Konsolidasikan segenap kerangka jurus parameter peramban penelusuran arsitektur ekskavasimu menjadi satu kompilasi laporan hasil intaian intelijen (*Recon Report*) layaknya operasional pengujian penganalisis kerentanan (*Bug Bounty Hunter*) profesional sejati!

---

*📅 TISS Null Teaming · Week 15 · Day 4 · BREACH Rank*
