# 💀 Week 18 · Day 3: Burp Suite Scanner & Extensions

> **Rank**: BREACH | **Minggu ke-18**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 18 · Day 3/5 | BREACH Rank (Minggu 4 dari 5) | Overall: 88/120 hari (73%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** fitur penarik payload kueri otomatis (Burp Scanner).
2. **Membedakan** lisensi pembatasan antara versi *Community* versus *Professional*.
3. **Menerapkan** instalasi sandi ekstensi *BApp Store* demi menambah persenjataan (*Extensions & Macros*).

---

## 📖 Materi Inti

### Kemewahan Otomasi: Burp Scanner (Professional Edition)

Bila *Repeater* dan *Intruder* memaksamu mengotori tangan, fungsionalitas kasta tertinggi milik PortSwigger menyimpan senjata pemusnah otomatisasi: **Burp Scanner**.
*Scanner* ini mampu memindai (*Crawl & Audit*) situs dari ujung ke ujung semalaman, lantas memuntahkan lembar laporan yang membeberkan : *"Ada SQLi di URL A, ada XSS di URL B, ada CSRF di C"*.

**Kendala Lisensi:** Sayangnya, fitur *Scanner* yang maha otomatis ini **DIKUNCI KETAT **! Ia hanya hadir di versi *Burp Suite Professional* (Harganya selangit, $450/tahun).
Di versi *Community* yang kamu unduh gratis, tab *Dashboard Scanner* hanya bisa kamu ratapi (abu-abu alias diblokir). 

Tapi jangan putus asa, spesialis penganalisis *Bug Hunter* sejati memburu kerentanan jauh lebih buas bermodalkan tangan telanjang arsitektur *Repeater* ketimbang bermanja ria disuapi *Scanner* !

### Bursa Ekstensi : BApp Store (Extensions)

Sama seperti editor *VS Code* punya *Extensions*, *Burp Suite* dibekali sarang modifikasi pihak ketiga bernama **BApp Store (Burp App Store)**.

Peretas sedunia merakit bungkusan *plugin* Python/Java skrip dan merilisnya gratis di BApp Store untuk menambah kekuatan Burp! (Catatan : Butuh instalasi Jython jika mengunduh plugin Python).

**Ekstensi Maut Andalan:**
1. **Autorize:** Merajai peretasan *IDOR*! (Ini bakal jadi andalanmu kelak). Ia otomatis mengirimkan seluruh URL dengan kalung *Cookie* pangkat rendah demi mendeteksi kerentanan Otorisasi secara massal di latar belakang.
2. **Logger++:** Papan catatan (Log) terperinci yang membeberkan merekam sejarah seluruh rentetan hantaran HTTP tanpa ampun (Lebih komplit dari *HTTP History* bawaan).
3. **Turbo Intruder:** Senapan *Brute Force* yang melontarkan jutaan serangan kueri ratusan kali lebih kilat ganas ketimbang bawaan *Intruder* orisinal Burp!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Ayo rakit ekstensi peretasan di bursa *BApp Store*!

1. Gelar jendela rahim *Burp Suite Community Edition*.
2. Navigasikan tetikus menuju tab **Extender -> BApp Store**.
3. Di layar depan, disuguhi ratusan plugin *hacker* sedunia .
4. Cari ekstensi bertajuk **"Logger++"**. Klik lantas tekan tombol **Install** di panel bawah!
5. Pasca terinstal, tab baru *Logger++* akan nampang meronta di deretan menu atas Burp. Buka tab itu.
6. Mulai detik ini, *Logger++* bakal diam-diam merangkum mengekstrak merekam setiap serangan desahan paket data HTTP yang merangsek keluar masuk Burp-mu laksana mesin perekam CCTV abadi.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membuka kasta arsitektur peretasan Web, apa fitur sakral (Crawl & Audit otomatis) yang diharamkan dan dikunci gembok abu-abu pada lisensi <i>Burp Suite Community Edition</i>?</summary>

**Jawaban:** Fitur *Burp Scanner* (Vulnerability Scanner Otomatis).
</details>

<details>
<summary>❓ Ketika penganalisis meratapi kelemahan keterbatasan fitur bawaan *Burp Suite*, tab perbendaharaan bursa apa yang dituju demi mengunduh merakit *plugin* tambahan (Extensions) racikan *Hacker* sedunia?</summary>

**Jawaban:** Tab *BApp Store* (atau *Extender*).
</details>

<details>
<summary>❓ Di ranah ekstensi , embel ekstensi kasta apakah yang senantiasa digandrungi dipuja penganalisis guna menelusuri penemuan celah *IDOR (Broken Access Control)* secara otomatis masif di peramban Burp?</summary>

**Jawaban:** Autorize.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap dominasi letak *Scanner* otomatis *Professional Edition* - [ ] Saya fasih meratapi nasib bodi lisensi *Community Edition* - [ ] Saya menguasai titah instalasi ekstensi *BApp Store*
- [ ] Saya memahami kegunaan penyedot *Autorize* dan *Logger++* - [ ] Saya telah menjawab seluruh ulasan *quiz kilat* 
---

## 🔗 Resources

- [PortSwigger BApp Store Directory](https://portswigger.net/bappstore) — Kumpulan galeri pajangan seribu plugin Burp sedunia.

---

## ➡️ Besok

**Day 4: Other Tools (ZAP, ffuf, nikto)** — Lantaran *Burp Scanner* versi *Community* dikunci mati, haruskah menangis merana mencari otomasi? TIDAK! Esok hari, Web menuntut penganalisis menoleh pada barisan bedil *Open Source* gratisan! Kenalkan **OWASP ZAP** (Pemindai Web Otomatis Gratis!), pelacak kerentanan purba **Nikto**, dan perobek direktori **ffuf** di altar pengujian (*Alternative Tooling*)!

---

*📅 TISS Null Teaming · Week 18 · Day 3 · BREACH Rank*
