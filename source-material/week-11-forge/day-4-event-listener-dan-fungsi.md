# 🔨 Week 11 · Day 4: Event Handling & Form Validation

> **Rank**: FORGE | **Minggu ke-11**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 11 · Day 4/5 | FORGE Rank (Minggu 2 dari 5) | Overall: 54/120 hari (45%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep *Event Listeners* yang mendeteksi dan mendengarkan interaksi pengguna.
2. **Merespons** aksi pengguna (seperti klik tombol atau menekan tombol *keyboard*) dengan mengeksekusi fungsi JavaScript yang dinamis.
3. **Mencegah** perilaku pengiriman bawaan (*default behavior*) formulir saat proses validasi dilakukan.

---

## 📖 Materi Inti

### Mendeteksi Interaksi: Event Listener

Halaman *web* modern dirancang untuk reaktif terhadap pengguna. Jika terdapat tombol "Hapus Data", tombol tersebut harus 'merespons' dan tahu kapan ia diklik. Di JavaScript, sistem pemantauan interaksi dinamik ini disebut dengan **Event Listener** (Fungsi Pendengar Kejadian).

Langkah penerapannya sederhana: Kita seleksi elemen sasarannya (seperti di Day 3), lalu kita pasangkan *Event Listener* pada elemen tersebut.

```javascript
// 1. Tangkap Elemen
const tombolMerah = document.querySelector('#btn-hapus');

// 2. Pasang Fungsi Pendengar (addEventListener)
tombolMerah.addEventListener('click', () => {
 // 3. Logika dieksekusi jika tombol menerima pemicu 'click'!
 console.log("Data berhasil terhapus!");
});
```

Terdapat ratusan tipe *Event* interaksi bawaan selain pemicu `click`, di antaranya:
- `mouseenter` : Aktif saat kursor (*mouse*) melayang/berada di atas area elemen.
- `keyup` : Aktif saat pengguna melepaskan tekanan pada tombol fisik *keyboard*.
- `submit` : Aktif spesifik pada elemen form `<form>` sesaat ia hendak mengirimkan data inputannya.

### Mengendalikan Perilaku Formulir (Event.preventDefault)

Kilas balik ke Week 10: Formulir penampang HTML memiliki sifat bawaan (perilaku *default*). Saat kamu menekan tombol bertipe pengiriman `<button type="submit">`, halaman web secara otomatis akan meluncurkan aksi memuat ulang halaman (*refresh*) dan berpindah rute URL (misal lewat aksi GET/POST).

Hal ini sering kali menjadi hambatan dalam merancang aplikasi *Web Modern* (seperti *Single Page Application*). Kita biasanya memerlukan JavaScript untuk memverifikasi atau memvalidasi kelengkapan *password* dahulu sebelum mengizinkannya terkirim secara nyata.
Solusinya? **Matikan Sifat Bawaan Pengiriman Formulir**.

Setiap pelaksanaan fungsi panggilan balik *Event Listener*, peramban selalu mengumpan masuk sebuah obyek data kronologis lengkap yang mendeskripsikan spesifik rincian dari peristiwanya. Obyek parameter pelaporan *event* ini sering kali direpresentasikan dengan variabel `event` (atau dipersingkat huruf `e`).

```javascript
const formLogin = document.querySelector('#form-login');

// Perhatikan kita menangkap objek parameter pelaporan kejadian ('e')
formLogin.addEventListener('submit', (e) => {
 // MATIKAN SIFAT BAWAAN FORMULIR (Mencegah peramban me-refresh laman URL)
 e.preventDefault(); 
 
 // Barulah jalankan logika eksekusi atau inspeksi autentikasi dari JS-mu...
 console.log("Memverifikasi inputan kata sandi di latar belakang...");
});
```

### Mengambil Data Inputan (Values)

Setelah prosedur formulir tidak lagi *refresh* otomatis (tercegah), dari manakah instruksi JS mengetahui secara pasti data teks informasi apa yang barusan diinputkan (diketik pengguna) di dalam kolom `<input>`? 
Gunakan penarikan atribut properti `.value`!

```javascript
const inputNama = document.querySelector('#username');
// Mengekstraksi dan mencetak apa pun rangkaian teks masukan formulir yang baru saja diisikan.
console.log(inputNama.value); 
```

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari gabungkan semua pemahaman! Kita akan merancang verifikasi validasi pada kolom formulir pengamanan rahasia:

1. Buat file berkas `index.html` dan ketik kerangka pemodelan di bawah ini (perhatikan letak keterpisahan antara markah penyusun penampang struktur *HTML* bersanding deklarasi skrip operasi *JS*-nya):

```html
<form id="kotak-masuk">
 <label>Sandi Rahasia:</label>
 <input type="text" id="sandi">
 <button type="submit">Akses</button>
</form>
<h3 id="pesan"></h3>

<!-- Implementasi Skrip JS disematkan melangsungkan validasi di halaman yang sama -->
<script>
 const form = document.querySelector('#kotak-masuk');
 const inputSandi = document.querySelector('#sandi');
 const teksPesan = document.querySelector('#pesan');

 form.addEventListener('submit', (e) => {
 // Cegah intervensi sistem OS dari siklus otomatis pelampauan (refresh page)
 e.preventDefault();

 // Validasi syarat pengkondisian menggunakan kerangka If-Else (Sama dengan logika pemograman Bash)
 if (inputSandi.value === "TISS2026") {
 teksPesan.innerText = "Akses Diberikan. Sistem telah terbuka.";
 teksPesan.style.color = "green";
 } else {
 teksPesan.innerText = "Sandi Salah! Penolakan akses sistem dikunci.";
 teksPesan.style.color = "red";
 }
 });
</script>
```
2. Buka berkas HTML tersebut di dalam peramban penampil halaman *web*.
3. Cobalah masuki dengan mengisikan serentetan ragam acak sembarang tebakan sandi yang salah, lalu cetuskan tombol eksekusi Akses. 
4. Lalu perbaikilah dengan memasukkan kunci sandi orisinal bertuliskan format kapital `TISS2026`. (Perhatikan bahwa transisi perpindahan respons status tersebut dikalkulasi terjadi seketika tanpa menuntut sedikit pun proses transisi siklus memuat ulang halaman/ *loading web refresh*, murni berkat fungsi `.preventDefault()`).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa eksekusi fungsi `e.preventDefault()` amatlah esensial dan lumrah disisipkan sebagai baris logika pencegatan yang pertama setiap kali JS merancang skema prosedur intervensi terhadap pengoperasian insiden *submit* suatu form?</summary>

**Jawaban:** Hal ini diperuntukkan menonaktifkan dan membekukan sementara waktu perilaku bawaan peramban HTML di kala elemen formulir berupaya mematuhi sifat alamiahnya mengarungi pengiriman data (*yang biasanya bakal mereload URL*). Interupsi pencegatan ini memungkinkan barisan skrip *JavaScript* bekerja secara *offline* membedah pengujian validasi atau autentikasi isi dari formulir payload tanpa terdisrupsi terputus lantaran *reload* muat ulang laman.
</details>

<details>
<summary>❓ Objek struktural apakah (biasanya ditandai paramater variabel `e` atau `event`) yang didelegasikan serta diteruskan secara bawaan sebagai parameter awal masukan argumen dalam *Arrow Function* oleh peladen sistem setiap terdapat tangkapan kejadian, contoh klik ataupun submit?</summary>

**Jawaban:** Objek *Event*. Objek ini menampung paket referensi log dari kejadian interaksi tersebut yang amat informatif; contohnya merekam data perihal titik sumbu X dan Y pada layar saat *mouse* diarahkan mengeklik (koordinat), parameter penanda jenis spesifik kancing *keyboard* manakah yang baru ditekan, beserta beragam konteks kejadian pelengkap pemicunya.
</details>

<details>
<summary>❓ Atribut properti apakah yang berfungsi menjaring (menarik keluar) ekstrak nilai susunan data karakter *string* masukan, apa pun kontennya, yang sedari awal sudah diketik oleh pengguna ke dalam sebuah rongga balok penampung isian HTML (misal `<input>`)?</summary>

**Jawaban:** Atribut `.value` (misalnya penulisan pada penggunaannya: `inputBarang.value`).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami logika operasional fungsi penangkap *Event Listener* menggunakan argumen `addEventListener`.
- [ ] Saya mampu mendefinisikan pencegatan eksekusi pemuatan ulang `e.preventDefault()`.
- [ ] Saya mahir memproyeksikan perolehan isian variabel ketikan pengguna dengan properti `.value`.
- [ ] Saya telah menuntaskan praktik kode interaksi formulir (Validasi Rahasia) dalam sesi *Mini Lab*.
- [ ] Saya sudah memeriksa pengerjaan pada rangkaian penguasaan kuis kilat di penghujung panduan.

---

## 🔗 Resources

- [MDN: Events](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events) — Dokumentasi fundamental (Materi Referensi Mutlak) dari ragam jenis kompilasi eksekusi aksi interaktif, mulai pergerakan pointer, gestur sentuh piranti, hingga modul peraba rotasi arah giroskop piranti genggam.

---

## ➡️ Besok

**Day 5: Lab & Mission: Aplikasi To-Do List** — Waktunya unjuk keterampilan di hari akhir Minggu ke-11! Pada esok hari, kamu akan menggabungkan implementasi keseluruhan porsi eksekusi dasar penyusunan Fungsi, modifikasi memori objek DOM, serta tangkapan pemicu pemantau interaksi (Event Listener) untuk merealisasikan secara utuh kreasi program peranti lunak berbasis aplikasi *To-Do List* (Catatan Target Tugas Harian) interaktif pertama-mu. Tambahan materi juga melingkupi pemahaman media perekaman data memori peramban (*LocalStorage*)!

---

*📅 TISS Null Teaming · Week 11 · Day 4 · FORGE Rank*
