# 🎯 Week 11 · Day 6 (Bonus): Hands-On Learning

> **Rank**: FORGE | **Minggu ke-11** | Bonus Day

---

## 🌐 Platform Hari Ini

**[The Odin Project — JavaScript Exercises](https://www.theodinproject.com/lessons/foundations-fundamentals-part-1)**
Latihan JavaScript interaktif dari The Odin Project yang dikerjakan langsung di browser menggunakan Developer Tools console — tanpa perlu Node.js.

💰 **Biaya**: Gratis (100% open source)
⏱️ **Estimasi Waktu**: ~60 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Mempraktikkan variabel, fungsi, dan kondisional JavaScript di browser console
2. Menyelesaikan tantangan logika pemrograman dasar
3. Menggunakan Developer Tools console sebagai playground JavaScript

---

## 📋 Requirement

* Peramban web modern (Chrome/Firefox) — **hanya ini yang diperlukan!**
* Pemahaman dasar JavaScript dari Day 1-4 minggu ini

> ⚠️ **Tidak perlu Node.js.** Semua latihan hari ini dikerjakan di **browser console** (DevTools). Node.js baru diajarkan di Week 12.

---

## 📝 Prosedur

### Langkah 1: Buka Browser Console
1. Buka peramban Chrome atau Firefox
2. Tekan **F12** atau **Ctrl+Shift+I** (Mac: **Cmd+Option+I**)
3. Klik tab **Console**
4. Ini adalah JavaScript playground-mu hari ini!

### Langkah 2: Latihan Variabel & Tipe Data
Ketik dan jalankan kode berikut satu per satu di console:

```javascript
// 1. Deklarasi variabel
let nama = "Kader TISS";
const rank = "FORGE";
console.log(`Halo ${nama}, rank kamu: ${rank}`);

// 2. Operasi matematika
let a = 15;
let b = 4;
console.log("Tambah:", a + b);
console.log("Modulo:", a % b);
console.log("Pangkat:", a ** b);

// 3. Tipe data
console.log(typeof nama); // string
console.log(typeof a); // number
console.log(typeof true); // boolean
console.log(typeof undefined); // undefined
```

### Langkah 3: Latihan Fungsi & Kondisional
```javascript
// 4. Fungsi: Cek apakah angka genap atau ganjil
function cekGanjilGenap(angka) {
 if (angka % 2 === 0) {
 return `${angka} adalah GENAP`;
 } else {
 return `${angka} adalah GANJIL`;
 }
}
console.log(cekGanjilGenap(7));
console.log(cekGanjilGenap(12));

// 5. Fungsi: Hitung nilai huruf (grading)
function nilaiHuruf(skor) {
 if (skor >= 90) return "A";
 if (skor >= 80) return "B";
 if (skor >= 70) return "C";
 if (skor >= 60) return "D";
 return "E";
}
console.log(nilaiHuruf(85)); // B
console.log(nilaiHuruf(42)); // E

// 6. Arrow function
const kuadrat = (n) => n * n;
console.log(kuadrat(5)); // 25
```

### Langkah 4: Tantangan Mandiri
Kerjakan 3 tantangan ini di browser console. **Tulis sendiri tanpa melihat jawaban**:

**Tantangan 1**: Buat fungsi `hitungUmur(tahunLahir)` yang menghitung umur berdasarkan tahun sekarang.

**Tantangan 2**: Buat fungsi `balikKata(kata)` yang membalik string (misal: "TISS" → "SSIT").
> 💡 Hint: Gunakan `.split("")`, `.reverse()`, `.join("")`

**Tantangan 3**: Buat fungsi `fizzBuzz(n)` yang mencetak angka 1 sampai n, tapi:
- Jika habis dibagi 3, cetak "Fizz"
- Jika habis dibagi 5, cetak "Buzz"
- Jika habis dibagi 3 dan 5, cetak "FizzBuzz"

> 💡 **Jika stuck**: Baca kembali materi Day 1-2 tentang variabel dan logika JavaScript. Semua konsep yang dibutuhkan sudah dipelajari minggu ini.

### Langkah 5: Eksplorasi The Odin Project
1. Buka [The Odin Project — Foundations](https://www.theodinproject.com/paths/foundations/courses/foundations)
2. Buka bagian **JavaScript Basics**
3. Baca artikel dan kerjakan latihan-latihan yang tersedia
4. Bookmark halaman ini — ini akan menjadi referensi penting selama rank FORGE

---

## 🏁 Target Output

* ✅ Semua kode di Langkah 2 dan Langkah 3 berhasil dijalankan di browser console
* ✅ Minimal **2 dari 3 tantangan** mandiri berhasil diselesaikan
* 📸 Tangkapan layar browser console yang menampilkan output dari tantangan mandiri
* 📝 Kode solusi untuk setiap tantangan yang berhasil (simpan di file `.js` lokal)

---

## 🔄 Fallback

Jika The Odin Project tidak bisa diakses:
1. Buka [freeCodeCamp — JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/)
2. Kerjakan 10 tantangan pertama di bagian *Basic JavaScript*
3. Platform ini sepenuhnya browser-based dan tidak memerlukan instalasi
