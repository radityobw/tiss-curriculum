# 🔨 Week 11 · Day 5: Lab & Weekly Mission To-Do List

> **Rank**: FORGE | **Minggu ke-11**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓░░░░░░] 40% — FORGE Rank (Minggu 2 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░] 45% — Hari 55 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → 🔄 FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini kamu telah mempelajari dasar-dasar pemrograman logika interaksi JavaScript dari nol:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | Variabel & Tipe Data | Deklarasi penyimpan data: `let`, `const`, `string`, `number`. |
| Day 2 | Fungsi & Scope | Pembungkusan blok logika (`Function`), `Arrow Function`, serta ruang lingkup variabel lokal vs global. |
| Day 3 | DOM Manipulation | Konsep hierarki struktur elemen HTML dan penggunaan fungsi pencarian `querySelector`. |
| Day 4 | Event Handling | Menangkap interaksi dengan mendengarkan pemicu (*Event Listener*), serta mencegah perilaku pembaruan rute otomatis dari metode pengiriman halaman HTML. |

---

## 🧪 Hands-On Lab

### Prerequisites
- Editor VS Code
- Peramban web modern (Chrome/Firefox) dengan panggungan tab panel peranti pengembang (*Console Tools*) beroperasi.

### Misi Hari Ini: "Sistem Manajemen To-Do List Sederhana"

Hari ini, kita akan menyatukan konsep-konsep yang telah dipelajari untuk membuat *Web App* pertamamu: **To-Do List**. 
Program ini akan dirancang agar pengguna dapat menambahkan teks daftar tugas dan menampilkannya di halaman HTML secara dinamis. Kita juga akan menggunakan `localStorage` (memori penyimpanan bawaan *browser*), sehingga daftar tugasmu tidak hilang meskipun *browser* ditutup atau halaman dimuat ulang (*refresh*).

### Step 1: Merakit Kerangka Visual (HTML & CSS)

1. Buat file `index.html`. Ketikkan barisan blok kerangka kode pemodelan HTML berikut ini. (Kita akan menyisipkan format ringkas gaya *CSS Internal* untuk menyelaraskan komposisi estetikanya).

```html
<!DOCTYPE html>
<html lang="id">
<head>
 <meta charset="UTF-8">
 <title>Sistem Catatan TISS</title>
 <style>
 body { font-family: 'Courier New', monospace; background: #222; color: #0f0; padding: 20px; }
.container { max-width: 500px; margin: auto; background: #111; padding: 20px; border: 1px solid #0f0; }
 input, button { padding: 10px; border: 1px solid #0f0; background: #000; color: #0f0; }
 ul { list-style: none; padding: 0; }
 li { background: #333; margin: 5px 0; padding: 10px; display: flex; justify-content: space-between; }
.btn-hapus { color: red; cursor: pointer; font-weight: bold; }
 </style>
</head>
<body>
 <div class="container">
 <h2>[+] MANAJEMEN TUGAS TISS</h2>
 
 <!-- Formulir Input -->
 <form id="form-tugas">
 <input type="text" id="input-tugas" placeholder="Tambahkan daftar baru..." required>
 <button type="submit">Tambahkan</button>
 </form>

 <!-- Daftar Output -->
 <ul id="daftar-tugas">
 <!-- Tugas baru (tag li) akan dirender secara dinamis oleh skrip JS ke blok ini -->
 </ul>
 </div>
 
 <!-- Penempatan relasi rute perantara dokumen kode skrip JS -->
 <script src="app.js"></script>
</body>
</html>
```

### Step 2: Menambahkan Logika (JavaScript)

1. Buat berkas baru bertitel `app.js` yang posisinya persis setara di direktori yang serupa sejalan dengan *file* laman kerangka susunan panggungan (HTML)-mu.
2. Langkah pertama, deklarasikan objek-objek penangkapan selektor sasaran operasi (*DOM Selection*):

```javascript
const formTugas = document.querySelector('#form-tugas');
const inputTugas = document.querySelector('#input-tugas');
const daftarTugas = document.querySelector('#daftar-tugas');
```

3. Pasangkan modul pelacak interaksi (pengikatan *Event Listener*) atas kejadian ketika dokumen pengiriman form (`submit`) dilancarkan pengguna. Saat pemicu tersebut dipanggil, perintahkan kerangka peladen logik (*script*) untuk menciptakan objek elemen baru (yakni tag daftar cetakan `<li>`) secara dinamis, untuk menampung teks, kemudian merendernya disisipkan berdampingan ke wadah dalam format struktur panggung DOM *HTML* secara *real-time*.

```javascript
formTugas.addEventListener('submit', (e) => {
 // 1. Nonaktifkan fungsionalitas refresh siklus bawaan halaman peramban
 e.preventDefault();
 
 // 2. Akses serta alokasikan input data spesifik apa pun yang baru saja diketik pengguna
 const tugasBaru = inputTugas.value;
 
 // 3. Modifikasi memori dengan menginstruksikan JavaScript mencipta komponen kerangka blok <li> baru di RAM
 const li = document.createElement('li');
 
 // 4. Suntikkan (injeksi) rentetan konten teks dan modul tombol hapus sederhana ke perut tag elemen <li> ini
 li.innerHTML = `
 <span>${tugasBaru}</span> 
 <span class="btn-hapus">X</span>
 `;
 
 // 5. Perintahkan implementasi insersi, sematkan elemen bentukan <li> tersebut (appendChild) menyatu ke DOM elemen Induk
 daftarTugas.appendChild(li);
 
 // 6. Eksekusi pengosongan ulang rentang kotak field perantara isian agar kembali bersih menanti masukan tugas anyar
 inputTugas.value = '';
});
```

### Step 3: Fitur Menghapus Catatan (Event Delegation)

Bagaimana cara kita menghapus daftar tugas saat tombol 'X' diklik? Karena tombol 'X' (`.btn-hapus`) tidak ada di HTML sejak awal (dibuat secara dinamis oleh JavaScript), kita tidak bisa langsung memasang `addEventListener` padanya. Kita harus menggunakan metode **Event Delegation**. Artinya, kita memasang *Event Listener* pada elemen induk yang sudah ada sejak awal (`daftarTugas`), lalu mendeteksi apakah yang diklik di dalamnya adalah tombol 'X'.

4. Lengkapi kerangka instruksi *app.js* dengan koding deteksi penghapusan berbasis perantara *delegasi* di bawah:

```javascript
daftarTugas.addEventListener('click', (e) => {
 // Sistem menganalisis: Apakah rentang titik penunjuk area klik yang dipicu mendarat akurat pada class 'btn-hapus'?
 if(e.target.classList.contains('btn-hapus')) {
 // Jika kondisional pemicuan divalidasi tepat menyentuh target, matikan serta lenyapkan utuh hierarki elemen wadah induk penampungnya (yaitu bongkahan <li> utuh bersangkutan)
 e.target.parentElement.remove();
 }
});
```

5. Selamat! Simpan paripurna hasil skrip kodemu dan jalankan di *browser*. Uji coba menyisipkan serentetan 5 atau lebih pencatatan, lantas hapus silanglah satu per satu rentang data eksperimen tersebut melalui fungsi "X" barusan.

### 🔧 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Halaman situs masih otomatis memuat ulang (*Refresh URL*) sesaat aku klik enter di input form? | Validasi secara persis pemanggilan koding `e.preventDefault()`. Adakah kesalahan tipografi pada fungsi ini atau kelupaan penyematan referensi pengiriman variabel log `(e)`? |
| Baris elemen tugas `<li>` yang diketik tak kunjung tampil di bawah (Tidak ada pesan error)? | Pastikan untuk mengecek kesesuaian eksekusi penambahan *DOM* `appendChild()`, dan cermati kecocokan korelasi target blok variabel penampungan sasarannya. |

---

## 🎯 Weekly Mission

### Misi: "Penyimpanan Lokal Persisten (LocalStorage)"

**Deskripsi:** Aplikasi To-Do List yang kamu buat saat ini memiliki satu kekurangan: Jika pengguna memuat ulang halaman (*Refresh*), semua daftar tugas yang sudah ditambahkan akan hilang!
JavaScript menyediakan fitur bernama `localStorage` untuk menyimpan data secara permanen di *browser*.

**Tugas Mandiri:** Pelajari dokumentasi tentang `localStorage` di MDN (Mozilla Developer Network). Cobalah modifikasi kode JS-mu untuk menyimpan daftar tugas menggunakan `localStorage.setItem()` saat tugas ditambahkan, dan memanggil `localStorage.getItem()` saat halaman pertama kali dimuat agar daftar tugas yang tersimpan bisa ditampilkan kembali.

**Deliverables:**
1. Tambahan alur baris skrip *logic storage local* pelengkap (`localStorage`) pada file `app.js`.

**Kriteria Sukses:**
- [ ] Berkas masukan rekaman catatan sanggup memelihara ketahanan datanya tanpa degradasi kelenyapan, sekalipun peramban *web* dialihkan navigasinya atau ditutup paksa perjalanannya lalu di-refresh ulang dari awal.

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Apa sifat dari variabel yang dideklarasikan menggunakan `const`?</summary>

**Jawaban:** Variabel tersebut nilainya bersifat konstan (tetap) dan tidak dapat diubah (di-*reassign*) setelah deklarasi awal. Mencoba mengubah nilainya akan menghasilkan *error*.
</details>

<details>
<summary>❓ [MUDAH] Fungsi bawaan apa yang sering digunakan untuk mencetak informasi atau nilai variabel ke dalam tab *Console* di *Developer Tools* (F12)?</summary>

**Jawaban:** `console.log()`.
</details>

<details>
<summary>❓ [SEDANG] Fungsi *DOM Manipulation* apa yang digunakan untuk membuat elemen HTML baru di dalam memori JavaScript, sebelum elemen tersebut disisipkan ke halaman web?</summary>

**Jawaban:** `document.createElement('namaTag')` (misalnya `document.createElement('li')`).
</details>

<details>
<summary>❓ [SEDANG] Saat menggunakan `document.querySelector`, simbol awalan apa yang digunakan untuk mencari elemen berdasarkan ID (misal `id="sandi"`)?</summary>

**Jawaban:** Simbol pagar/hash `#` (ditulis menjadi `#sandi`).
</details>

<details>
<summary>❓ [SULIT] Apa perbedaan mendasar antara *Global Scope* dan *Local Scope* dalam JavaScript?</summary>

**Jawaban:** *Local Scope* adalah variabel yang dideklarasikan di dalam blok kurung kurawal `{ }` (seperti di dalam *function*), sehingga hanya bisa diakses dari dalam blok tersebut. Sedangkan *Global Scope* adalah variabel yang dideklarasikan di luar fungsi mana pun, sehingga dapat diakses dan digunakan secara bebas dari bagian kode mana saja.
</details>

---

## 📋 Weekly Checklist

- [ ] Saya telah memahami ekosistem pondasi interaksi pemograman web JavaScript.
- [ ] Saya memahami logika operasional serta ruang wilayah pembatas referensi penyusunan *Functions*.
- [ ] Saya memiliki pemahaman alur kerja dan mampu memperalat jembatan manipulasi antarmuka struktur dokumen (DOM).
- [ ] Saya sukses menjalankan pengerjaan tugas praktik (Misi Hands-On) implementasi penyusunan logika operasional memori peladen sistem (To-Do List).
- [ ] Saya (opsional sebagai tantangan ekstra berkelanjutan) berhasil merampungkan arsitektur penerapan daya ingat persistensi pengamanan sesi basis memori peranti (`LocalStorage`).

---

## 💬 Diskusi Minggu Ini

1. Setelah mempelajari logika JavaScript (*Logic Tier*), bagaimana penilaianmu terhadap tantangan belajarnya dibandingkan saat hanya menyusun struktur HTML (*Structure Tier*) minggu lalu?
2. Jika peretas berhasil menyuntikkan kode skrip berbahaya ke *browser* pengunjung (melalui celah XSS), menurutmu, mungkinkah mereka menggunakan manipulasi DOM untuk mencuri data sesi (*session*) atau kata sandi milik pengguna tersebut?

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ FRONTEND LOGICIAN │
│ Week 11 Complete │
│ "Your website now has a brain." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 12: Backend Basics — Node.js & Express**

Selama ini, kita berfokus pada tampilan antarmuka (*Frontend*) yang berjalan di *browser* pengguna. Aplikasi yang kamu buat sudah interaktif, tetapi belum memiliki pusat penyimpanan data sejati atau fungsi *Database*. Minggu depan, kita akan beralih ke belakang layar (*Backend*)! Kita akan mempelajari **Node.js** dan **Express** untuk membuat *server* kita sendiri, memungkinkan aplikasi web menjadi terpusat (*Server-Side Architecture*).

> 🚀 *"The client asks. The server dictates."*

---

*📅 TISS Null Teaming · Week 11 · Day 5 · FORGE Rank*
