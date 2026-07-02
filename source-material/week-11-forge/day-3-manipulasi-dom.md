# 🔨 Week 11 · Day 3: DOM Manipulation

> **Rank**: FORGE | **Minggu ke-11**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 11 · Day 3/5 | FORGE Rank (Minggu 2 dari 5) | Overall: 53/120 hari (44%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep Document Object Model (DOM) yang menghubungkan antarmuka JavaScript dengan elemen HTML.
2. **Menyeleksi** (menemukan) target elemen HTML secara presisi menggunakan fungsi JavaScript.
3. **Memodifikasi** konten teks, properti tampilan (CSS), dan struktur elemen secara dinamis (*frontend manipulation*).

---

## 📖 Materi Inti

### Menjembatani 2 Dunia: DOM

Selama ini, struktur HTML berdiri sendiri, dan eksekusi JavaScript (JS) bekerja di balik layar melalui *Console*. Bagaimana cara instruksi JS menjangkau dan mengubah elemen seperti `<p>` atau `<h1>` di dalam dokumen HTML?

*Browser* modern memfasilitasi interaksi ini melalui antarmuka yang dinamakan **DOM (Document Object Model)**.
DOM memodelkan seluruh halaman HTML-mu layaknya struktur pohon (*Tree Structure*).
- Elemen `<html/>` bertindak sebagai *root* (akar/induk utama).
- Elemen `<body/>` adalah turunan (*child*).
- Elemen `<h1>` dan `<p>` adalah turunan dari `<body>`.

JavaScript mengakses hierarki pohon ini melalui sebuah *object* global bawaan *browser* bernama: `document`.

### Membidik Target (Seleksi Elemen)

Sebelum sebuah skrip dapat memodifikasi komponen halaman, ia harus menemukannya (menyeleksi elemen tersebut) terlebih dahulu.
Metode standar industri yang paling modern dan efisien untuk mencari elemen DOM adalah:

```javascript
// Mencari 1 elemen pertama yang memiliki class="judul-merah"
const judul = document.querySelector('.judul-merah');

// Mencari elemen spesifik berdasarkan ID (ditandai dengan #)
const tombol = document.querySelector('#btn-login');

// Mencari SELURUH elemen paragraf (mengembalikan kumpulan node/NodeList)
const semuaParagraf = document.querySelectorAll('p'); 
```
*(Gunakan metode `querySelector`. Pola penargetannya sama persis dengan cara penulisan penyeleksi target di CSS)*

### Memodifikasi Target (JavaScript Manipulation)

Begitu suatu elemen berhasil diseleksi (misalnya dan ditampung ke dalam variabel `judul`), kamu memiliki privilese untuk memanipulasi nilainya:

**1. Mengubah Isi Teks (Aman):**
```javascript
judul.innerText = "Sistem Sedang Diperbarui!"; 
```

**2. Mengubah Struktur Kode HTML Asli:**
```javascript
judul.innerHTML = "Sistem <b>Diperbarui</b>!"; // Menyisipkan tag HTML tebal (bold)
```
> ⚠️ **HACKER ALERT**: Menggunakan modifikasi atribut `innerHTML` secara sembarangan sangat berbahaya, terutama jika teks modifikasinya berasal dari ketikan *input* pengguna yang tidak disaring. Praktik ini adalah akar penyebab kerentanan **DOM-based XSS (Cross-Site Scripting)**. Peretas (penyerang) dapat mengeksploitasi celah ini dengan menginjeksi muatan tag `<script>` berbahaya! Selalu gunakan atribut `innerText` atau `textContent` untuk merender masukan teks biasa.

**3. Mengubah Properti Gaya (CSS):**
```javascript
// JS menggunakan notasi camelCase untuk nama properti CSS
judul.style.color = "red";
judul.style.backgroundColor = "black"; // 'background-color' CSS ditulis 'backgroundColor' di JS
```

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari lakukan eksperimen *DOM manipulation* secara langsung! (Kita akan mencoba mengubah sementara tampilan halaman utama peramban Google).

1. Buka situs `https://www.google.com` (pastikan antarmuka menggunakan bahasa Inggris untuk memudahkan).
2. Tekan tombol **F12** untuk membuka fitur *Developer Tools*, lalu beralih ke tab **Console**.
3. Ketik perintah selektor berikut untuk menyeleksi gambar logo Google (dan tekan Enter pada setiap baris):
```javascript
const logo = document.querySelector('.lnXdpd'); // Class spesifik tag 'img' logo Google saat ini
// Catatan: Jika terjadi error atau class berubah, inspect logo tersebut secara manual untuk mendeteksi nama class terbarunya.
```
4. Mari kita ganti gambar sumber (properti `src`) fotonya:
```javascript
logo.src = "https://www.hackerone.com/sites/default/files/2021-08/H1_logo_black.png";
logo.srcset = ""; // Matikan penyesuaian resolusi bawaan Google agar gambar baru termuat
```
5. Mari ubah warna latar belakang (properti `backgroundColor`) halaman situs Google menjadi kelam:
```javascript
document.body.style.backgroundColor = "black";
```
Perhatikan layar Google-mu sekarang, tampilannya berubah menjadi gelap dengan logo peretas! (Ingat, ini hanyalah perubahan manipulasi DOM lokal sementara di layar perambanmu. Jika kamu menyegarkan (*refresh*) halaman *web* tersebut, konfigurasi aslinya akan dikembalikan seperti semula).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa kita sangat disarankan memakai metode mutakhir `querySelector` di masa kini, alih-alih metode lama seperti `getElementById` atau `getElementsByClassName`?</summary>

**Jawaban:** Karena `querySelector` mengadopsi standar sintaks tata letak (*selector*) yang ekuivalen persis seperti aturan penulisan *CSS* (menggunakan `#` untuk ID dan `.` untuk *Class*). Hal ini merampingkan alur pemograman karena *developer* tidak perlu menghafal beragam jenis sintaks pemanggilan secara spesifik, cukup menggunakan fundamental pemahaman gaya bahasa pemanggilan CSS yang sudah familier.
</details>

<details>
<summary>❓ Kerentanan/Vulnerability (*security vulnerability*) apa yang timbul bila pemrogram membiarkan masukan teks tak divalidasi dari *input* tamu web dicetak kembali (dirender) ke penampang laman situs melalui perintah manipulasi `.innerHTML`?</summary>

**Jawaban:** Memicu ancaman *Cross-Site Scripting* (XSS). Penyerang (*attacker*) bisa memanfaatkan fitur komentar atau *input* formulir guna menyisipkan baris peretasan berupa atribut `<script>kode_berbahaya();</script>`. Ketika situs menelan dan menampilkan *input* ini membonceng atribut fungsi `.innerHTML`, *browser* akan keliru menafsirkan *input* mentah tersebut sebagai skrip *HTML* aktif, bukan melukiskannya murni sebatas deretan teks tulisan tangan biasa; alhasil, mengeksekusi program serangan (*malware/payload*) milik pelaku.
</details>

<details>
<summary>❓ Apakah nama variabel perantara *Object* induk mutlak (bawaan *browser JavaScript*) yang berperan selaku entri poin awal/titik sentral untuk menjangkau ranting hierarki *HTML* pada situs?</summary>

**Jawaban:** Objek global bernama `document`.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya mengerti hierarki fundamental konsep struktur *Pohon DOM*.
- [ ] Saya piawai memanfaatkan perintah seleksi `document.querySelector`.
- [ ] Saya memahami perbedaan perlakuan antara penempatan atribut `.innerText` berbanding `.innerHTML` (dan memahami perikatan ancaman eksploitasi celah *XSS*).
- [ ] Saya sukses menjalankan simulasi injeksi lokal memodifikasi laman visual Google di *Mini Lab*.
- [ ] Saya telah meninjau kembali seluruh ulasan tes kemampuan pada kuis kilat di atas.

---

## 🔗 Resources

- [JavaScript HTML DOM (W3Schools)](https://www.w3schools.com/js/js_htmldom.asp) — Ensiklopedia mengenai referensi manipulasi fungsi DOM.
- [DOM XSS Prevention (OWASP)](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) — (Tingkat Menengah Lanjut) Dokumentasi formal *OWASP* bagi divisi keamanan dalam mitigasi dan mereduksi celah rekayasa peretasan fungsi berisiko *DOM innerHTML*.

---

## ➡️ Besok

**Day 4: Event Handling & Form Validation** — Fungsi penambahan *DOM* kita hari ini barulah terhitung *static* (disuntikkan manual via antarmuka *Console*). Esok hari, kita akan merevolusi rancangan situs kita menjadi laman REAKTIF! Apabila pengunjung (user) mengklik sebuah modul tombol konfirmasi pelaporan form atau mengetuk tuts keyboard, mesin pengawasan *JavaScript* situsmu bakal lekas merespons secara responsif dan otomatis!

---

*📅 TISS Null Teaming · Week 11 · Day 3 · FORGE Rank*
