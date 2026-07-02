# 🔨 Week 10 · Day 4: CSS Fundamentals & DevTools

> **Rank**: FORGE | **Minggu ke-10**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 10 · Day 4/5 | FORGE Rank (Minggu 1 dari 5) | Overall: 49/120 hari (41%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedah** anatomi Box Model pada elemen HTML
2. **Mendesain** tata letak modern menggunakan CSS Flexbox
3. **Menggunakan** Developer Tools (Inspect Element & Network Tab) layaknya seorang profesional

---

## 📖 Materi Inti

### Box Model (Model Kotak) CSS

Jika HTML adalah tulangnya, **CSS (Cascading Style Sheets)** adalah kulit, pakaian, dan penampilannya.
Di dunia CSS, segalanya adalah **KOTAK (Box)**. Ingat prinsip ini baik-baik!

Setiap elemen HTML (`<p>`, `<h1>`, `<img>`) sejatinya adalah kotak tak kasatmata yang memiliki 4 lapisan dari dalam ke luar:
1. **Content**: Isi aslinya (teks atau gambar).
2. **Padding**: Bantal pelindung *di dalam* garis batas (jarak antara teks ke bingkai luar).
3. **Border**: Garis batas/bingkai yang mengelilingi elemen.
4. **Margin**: Jarak luar *setelah* garis batas (jarak untuk mendorong elemen lain agar tidak menempel).

### CSS Selectors (Cara Membidik Elemen)

Bagaimana cara kita menyuruh CSS untuk mewarnai paragraf tertentu? Kita membidiknya dengan Selektor.
- **Tag Selector**: Menembak semua tag sejenis. (Misal: `p { color: red; }` akan mewarnai merah *semua* paragraf).
- **Class Selector (`.`)**: Menembak elemen spesifik berkelompok. (Misal: `.penting { font-weight: bold; }`). Kamu dapat memasang `class="penting"` di banyak tempat.
- **ID Selector (`#`)**: Menembak SATU elemen paling spesial. Tidak boleh ada ID kembar di satu halaman. Kekuatannya mengalahkan (override) aturan Class biasa. (Misal: `#judul-utama`).

### Era Baru Tata Letak: Flexbox

Dulu, mengatur kotak agar berjejer rapi di web sangatlah sulit (menggunakan float/table). Sekarang, ada modul ajaib bernama **Flexbox (Flexible Box)**.
Dengan Flexbox, kamu cukup menyulap wadah induknya menjadi area fleksibel, maka isi di dalamnya akan berjejer dan meregang secara otomatis menanggapi ruang yang tersisa! Sangat adaptif dan responsif untuk layar HP!

```css
.wadah {
 display: flex;
 justify-content: center; /* Menengahkan elemen secara horizontal */
 align-items: center; /* Menengahkan elemen secara vertikal */
}
```

### Pisau Lipat Hacker: Developer Tools (F12)

Sebagai *builder* (Yellow Team) maupun *pentester* (Red Team), tab **Developer Tools** adalah senjata. Buka web apa pun, klik Kanan -> **Inspect** (atau tekan F12).

1. **Tab Elements**: Untuk mengutak-atik kode HTML/CSS secara langsung tanpa harus menyimpannya di file lokal (perubahan akan hilang jika web dimuat ulang). Ini alat luar biasa untuk bereksperimen dengan desain secara *real-time*.
2. **Tab Network**: Versi mini Wireshark di browsermu! Di sinilah *hacker* memata-matai arus pertukaran data (seperti formulir login yang kamu buat kemarin) yang mengalir diam-diam di belakang layar tanpa mengubah tampilan URL.

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari rapikan form dari Day 3 dengan kekuatan CSS Flexbox dan bedah menggunakan DevTools!

1. Buka file `index.html` dari kemarin.
2. Tambahkan baris kode ini tepat di atas tag `</head>`:
```html
<style>
 body {
 display: flex;
 justify-content: center;
 align-items: center;
 height: 100vh; /* Tinggi 100% layar */
 background-color: #2c3e50;
 font-family: Arial, sans-serif;
 }
 form {
 background-color: white;
 padding: 30px; /* Bantal dalam */
 border-radius: 10px;
 box-shadow: 0 4px 8px rgba(0,0,0,0.2);
 }
 button {
 background-color: #e74c3c;
 color: white;
 padding: 10px 15px;
 border: none;
 border-radius: 5px;
 cursor: pointer;
 }
</style>
```
3. Simpan dan buka di peramban. Form loginmu kini akan berada persis di tengah layar dengan tampilan elegan!
4. Tekan **F12**, masuk ke tab **Network**. Centang tu "Preserve log".
5. Isi form asal-asalan, lalu klik tombol Daftar. 
6. Lihat di tab Network! Surat pengiriman data (POST) milikmu tertangkap di sana!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa sistem rancang tata letak Flexbox jauh lebih digemari pengembang modern?</summary>

**Jawaban:** Karena Flexbox dirancang khusus untuk membagikan ruang di dalam penampung antar item meskipun ukurannya tidak diketahui atau dinamis. Hal ini membuatnya sangat tangguh untuk mendesain tata letak yang *responsive* (sanggup menyesuaikan diri di layar lebar maupun sempit) tanpa perlu berurusan dengan pengaturan matematika rumit.

</details>

<details>
<summary>❓ Berdasarkan konsep anatomi Kotak (CSS Box Model), lapisan apakah yang berfungsi memberi ruang kosong di luar garis pembatas (border) agar tidak menabrak elemen lainnya?</summary>

**Jawaban:** Lapisan **Margin**. Berbeda dengan Padding yang mengatur jarak *di dalam* kotak, Margin mendorong elemen lain dari *luar* garis batas.

</details>

<details>
<summary>❓ Di dalam Developer Tools, mengapa *pentester* web sering kali lebih lama memelototi tab "Network" ketimbang tab "Elements"?</summary>

**Jawaban:** Karena celah keamanan (bug) seringkali tidak bersembunyi di antarmuka desain visual (HTML/CSS), melainkan pada pertukaran data logika (API) dan Parameter yang sedang berlalu lalang di balik layar. Tab Network sanggup menangkap detail data sensitif ini.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami empat utama dalam anatomi Box Model
- [ ] Saya mengetahui hierarki selektor (Class `.` vs ID `#`)
- [ ] Saya memahami fungsi sakti dari `display: flex`
- [ ] Saya berhasil menangkap proses POST di tab Network via Mini Lab
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Flexbox Froggy](https://flexboxfroggy.com/) — Permainan seru (dan interaktif) paling legendaris untuk menghafalkan seluruh perintah ajaib Flexbox!

---

## ➡️ Besok

**Day 5: Lab & Mission: Halaman Profil & Hosting** — Tiba saatnya ujian mingguan! Kamu akan memadukan HTML, CSS (Box Model & Flexbox), Git, dan GitHub yang telah kita pelajari dari awal minggu ini. Misinya: membangun portofolio pribadi dan mengorbitkannya secara gratis ke internet agar dunia bisa melihatnya!

---

*📅 TISS Null Teaming · Week 10 · Day 4 · FORGE Rank*
