# 🔨 Week 11 · Day 2: Functions, Scope & Closures

> **Rank**: FORGE | **Minggu ke-11**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 11 · Day 2/5 | FORGE Rank (Minggu 2 dari 5) | Overall: 52/120 hari (43%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep Functions sebagai blok kode yang dapat digunakan kembali (*reusable*).
2. **Membedakan** berbagai jenis penulisan fungsi (Declaration vs Arrow Function).
3. **Menganalisis** aturan wilayah kekuasaan variabel (*Scope*) dalam JavaScript.

---

## 📖 Materi Inti

### Functions: Pabrik Otomatisasi Perintah

Pernahkah kamu menyadari bahwa kamu sering melakukan tugas berulang? Misalnya, memotong pajak 10% dari sebuah gaji. Daripada kamu menulis rumus matematika setiap kali menghitung gaji karyawan, kamu bisa membungkus rumusnya ke dalam sebuah **Function**.

Function adalah layaknya sebuah pabrik. Ia menerima **Bahan Baku (Parameter/Input)**, lalu memprosesnya di dalam pabrik, dan memuntahkan **Barang Jadi (Return/Output)**.

```javascript
// 1. Membuat Pabrik (Function Declaration)
function hitungGajiBersih(gajiKotor) {
 let pajak = gajiKotor * 0.1;
 let hasilBersih = gajiKotor - pajak;
 return hasilBersih; // Memuntahkan hasil ke luar pabrik
}

// 2. Menggunakan Pabrik (Function Call)
let gajiBudi = hitungGajiBersih(100000);
console.log(gajiBudi); // Menghasilkan: 90000
```

### Arrow Function (Cara Modern)

Di era modern (ES6), cara penulisan fungsi disingkat sedemikian rupa agar lebih ramping menggunakan "Panah" (`=>`). *Arrow Function* adalah gaya penulisan paling populer saat ini di React.js maupun Node.js.

```javascript
// Gaya Klasik
const sapaUser = function(nama) {
 return "Halo, " + nama;
};

// Gaya Modern (Arrow Function)
const sapaUserModern = (nama) => {
 return "Halo, " + nama;
};

// Bahkan jika hanya 1 baris, bisa Disingkat Ekstrem!
const sapaSingkat = nama => "Halo, " + nama;
```

### Scope: Wilayah Teritori Kode

Ini konsep yang sering menjebak *developer* pemula dan *hacker* junior! 
**Scope (Cakupan)** adalah aturan batas wilayah di mana sebuah variabel boleh dilihat dan digunakan.

Aturan Emas: **Variabel yang dibuat DI DALAM sebuah kurung kurawal `{ }` (seperti di dalam function), TIDAK BISA dipanggil dari LUAR kurung tersebut.** Namun sebaliknya, kode di dalam kurung BISA melihat variabel di luar (Global). Ini disebut **Local Scope**.

```javascript
let senjataUtama = "Nmap"; // Global Scope (Bisa dilihat siapa saja)

function mulaiPeretasan() {
 let senjataRahasia = "SQLMap"; // Local Scope (Hanya hidup di dalam fungsi ini)
 console.log("Memakai: " + senjataUtama); // BISA! Dia melihat ke luar.
}

mulaiPeretasan();
console.log(senjataRahasia); // ERROR! senjataRahasia is not defined. (Luar tidak bisa tembus ke dalam).
```

### Closures (Level Advanced Singkat)

Bagaimana jika ada fungsi *di dalam* fungsi? Fungsi anak akan SELALU MENGINGAT (mengunci) variabel dari fungsi induknya meskipun fungsi induknya sudah selesai dijalankan. Ini dinamakan **Closure**. Konsep ini banyak dipakai untuk menyembunyikan data sensitif di JavaScript (karena JS tidak punya sistem keamanan *private* bawaan).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Ayo uji pemahaman fungsimu di Console!

1. Buka kembali tab Console (F12) di peramban kosong.
2. Buat sebuah Arrow Function pelacak IP otomatis sederhana:

```javascript
const scanPort = (ipTarget, port) => {
 let status = "Open"; // Variabel lokal
 return "Scan pada " + ipTarget + ":" + port + " berstatus " + status;
};

// Panggil fungsinya
console.log(scanPort("192.168.1.1", 80));
console.log(scanPort("10.0.0.5", 443));
```

3. Coba panggil variabel `status` langsung dengan mengetik `console.log(status)` di bawah kode. Kamu akan mendapati hasil error! (Itulah *Scope*).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa kita repot-repot membuat Function daripada menulis kode berurutan dari atas ke bawah (linear)?</summary>

**Jawaban:** Untuk prinsip **DRY (Don't Repeat Yourself)**. Function membuat kode bisa digunakan ulang (*reusable*) ratusan kali tanpa harus menyalin ulang logikanya. Jika ada kesalahan logika, kita cukup membetulkannya di 1 tempat (di dalam function tersebut) saja.
</details>

<details>
<summary>❓ Jika kita memiliki variabel `const tokenRahasia = "XYZ"` di baris paling atas dokumen (di luar fungsi apapun), tipe Scope apakah ini dan siapa yang bisa membacanya?</summary>

**Jawaban:** Ini adalah **Global Scope**. Seluruh fungsi atau blok kurung kurawal di manapun di dokumen itu bisa membaca variabel ini secara bebas.
</details>

<details>
<summary>❓ Apa keunggulan penulisan Arrow Function (`=>`) ketimbang penulisan Function konvensional?</summary>

**Jawaban:** Arrow function menyuguhkan sintaks penulisan yang jauh lebih ringkas (bahkan bisa satu baris, hilangkan kata `return` dan kurung kurawal) dan sangat praktis, menjadikannya lebih rapi untuk program modern.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami logika Fungsi sebagai "Pabrik" yang butuh Input dan memuntahkan Output
- [ ] Saya bisa mengubah fungsi biasa menjadi Arrow Function
- [ ] Saya sangat memahami aturan tembok isolasi **Scope** (Local vs Global)
- [ ] Saya sudah menjalankan Mini Lab tanpa *syntax error*
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) — Panduan mendalam tentang ragam jenis deklarasi fungsi.
- [JavaScript Visualizer](https://ui.dev/javascript-visualizer/) — Alat visual animasi untuk memahami konsep rumit *Scope* dan jalannya tumpukan fungsi (Call Stack).

---

## ➡️ Besok

**Day 3: DOM Manipulation** — Dua hari ini kita hanya bermain JavaScript di terminal (Console) hitam legam. Besok, kita akan menggabungkan JS dengan halaman HTML agar JS bisa mengendalikan teks, kotak, dan warna layaknya sihir di perambanmu!

---

*📅 TISS Null Teaming · Week 11 · Day 2 · FORGE Rank*
