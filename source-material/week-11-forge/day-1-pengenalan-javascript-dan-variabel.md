# 🔨 Week 11 · Day 1: Variables, Data Types & Operators

> **Rank**: FORGE | **Minggu ke-11**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 11 · Day 1/5 | FORGE Rank (Minggu 2 dari 5) | Overall: 51/120 hari (42%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep dasar memori komputer melalui Deklarasi Variabel di JavaScript.
2. **Membedakan** tipe data dasar (String, Number, Boolean) dalam JavaScript.
3. **Menggunakan** operator logika dan aritmatika untuk manipulasi data sederhana.

---

## 📖 Materi Inti

### Apa itu JavaScript? Otot dari Sebuah Web

Jika HTML adalah **Tulang** (kerangka) dan CSS adalah **Kulit/Baju** (desain visual), maka JavaScript (JS) adalah **Otot dan Sistem Saraf** dari sebuah website. JS memberikan *nyawa* dan *interaktivitas* agar website bisa bergerak, merespons klik, dan memproses data.

Hampir 99% website modern (termasuk yang sedang kamu buka ini) menggunakan JavaScript. Bagi seorang *pentester* (Red Team), memahami JS adalah kunci untuk menemukan celah keamanan mengerikan seperti XSS (Cross-Site Scripting).

### Variabel: Kotak Penyimpanan Memori

Bayangkan komputer adalah sebuah gudang. **Variabel** adalah "kotak kardus" yang kita beri nama, lalu kita masukkan barang (data) ke dalamnya agar mudah dicari lagi nanti.

Di JavaScript modern, kita menggunakan `let` dan `const` untuk membuat kotak:
- `let` : Kotaknya boleh dibongkar dan isinya diganti di masa depan.
- `const` : Kotaknya digembok permanen (*Constant*). Isinya tidak boleh diganti.

```javascript
let namaHacker = "ZeroCool"; // Isinya boleh diganti nanti
const tahunKelahiran = 1995; // Tidak bisa diubah, karena sudah masa lalu

namaHacker = "CrashOverride"; // Boleh!
tahunKelahiran = 2000; // ERROR! Const tidak bisa diubah.
```

> 💡 **Tips**: Dulu orang menggunakan `var`, tapi itu sudah kuno dan sering memicu *bug* aneh. Biasakan SELALU menggunakan `const` secara *default*, dan gunakan `let` HANYA jika nilainya pasti akan berubah (misal: skor dalam game).

### Tipe Data Dasar

Isi dari kotak (variabel) memiliki jenis (tipe). Ada 3 tipe yang paling sering kamu temui:
1. **String** (Teks): Harus selalu diapit tanda kutip (`"..."` atau `'...'`). Contoh: `"Halo Dunia"`.
2. **Number** (Angka): Boleh pecahan atau bulat. Dilarang memakai kutip! Contoh: `42`, `3.14`.
3. **Boolean** (Saklar): Hanya punya dua kondisi: `true` (benar) atau `false` (salah). Sangat sering dipakai untuk mengecek apakah user sudah login atau belum.

### Operator: Matematika & Logika

JS jago berhitung. Kamu bisa pakai `+`, `-`, `*` (kali), `/` (bagi).
Namun yang terpenting bagi *hacker* adalah **Operator Perbandingan** (Logika):
- `===` : Apakah SAMA PERSIS nilainya dan tipenya? (Selalu gunakan 3 sama dengan!)
- `!==` : Apakah TIDAK SAMA?
- `>` atau `<` : Lebih besar atau lebih kecil.

```javascript
let umur = 20;
let sudahDewasa = umur >= 18; // Hasilnya akan be Boolean: true
```

---

## 🧪 Mini Lab

**Durasi**: ~10–15 menit

Mari menulis kode JS pertamamu langsung di dalam Browser!

1. Buka Google Chrome atau Firefox (tab baru kosong).
2. Tekan **F12** untuk membuka Developer Tools, lalu masuk ke tab **Console**.
3. Tab Console ini adalah terminal JS-mu. Ketik kode berikut sebaris demi sebaris (tekan Enter per baris):

```javascript
let nama = "Agen Rahasia";
let target = "Sistem Utama";
let peluangSukses = 99.9;
const isHacked = true;

// Mari kita rangkaikan (concatenate) string tersebut:
console.log(nama + " sedang menyerang " + target + " dengan peluang " + peluangSukses + "%");
```

**Expected Output:**
```
Agen Rahasia sedang menyerang Sistem Utama dengan peluang 99.9%
```
*(Fungsi `console.log()` adalah perintah wajib untuk mencetak tu ke dalam layar Console. Ini adalah alat bantu *debugging* terbaikmu!)*

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa kita sangat disarankan memakai `const` daripada `let` selama hal itu memungkinkan?</summary>

**Jawaban:** Memakai `const` membuat kode lebih aman (*bug-free*) karena melindungi nilai variabel tersebut agar tidak sengaja tertimpa/terganti di kemudian hari oleh fungsi lain secara tidak sengaja.
</details>

<details>
<summary>❓ Apa yang terjadi jika angka diapit tanda kutip, misal `let umur = "25";` lalu kamu tambahkan dengan 5 (`umur + 5`)?</summary>

**Jawaban:** Hasilnya bukan 30, melainkan `"255"`. Karena angka yang diberi kutip dianggap sebagai **String** (teks). Operator `+` pada string berfungsi menyambung teks, bukan menjumlahkan angka secara matematis.
</details>

<details>
<summary>❓ Jika HTML dan CSS itu ibarat kerangka dan kulit manusia, maka posisi JavaScript adalah?</summary>

**Jawaban:** Sistem saraf dan otot, yang memberikan manusia kemampuan bergerak, bereaksi ketika disentuh, dan berpikir logika.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami analogi variabel sebagai kotak penyimpanan
- [ ] Saya tahu perbedaan krusial antara `let` dan `const`
- [ ] Saya bisa membedakan tipe data String, Number, dan Boolean
- [ ] Saya berhasil menjalankan perintah di tab Console (Mini Lab)
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [MDN: JavaScript Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics) — Penjelasan fundamental langsung dari kreator Firefox.
- [javascript.info: Variables](https://javascript.info/variables) — Penjelasan detail soal let, const, dan sistem memori.

---

## ➡️ Besok

**Day 2: Functions, Scope & Closures** — Hari ini kamu belajar memasukkan barang ke dalam kotak (Variabel). Besok, kita belajar membungkus *sekumpulan aksi perintah* ke dalam sebuah "Pabrik Mini" otomatis bernama **Function**!

---

*📅 TISS Null Teaming · Week 11 · Day 1 · FORGE Rank*
