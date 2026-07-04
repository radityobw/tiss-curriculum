# 🔨 Week 12 · Day 1: Apa itu Backend?

> **Rank**: FORGE | **Minggu ke-12**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 12 · Day 1/5 | FORGE Rank (Minggu 3 dari 5) | Overall: 56/120 hari (46%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** perbedaan fungsi antara sisi Klien (*Frontend*) dan sisi Server (*Backend*).
2. **Menjelaskan** alur komunikasi data (*Request-Response Flow*) pada aplikasi *web* modern.
3. **Mendefinisikan** apa itu *API (Application Programming Interface)* dan mengapa aplikasi modern sangat bergantung padanya.

---

## 📖 Materi Inti

### Mengungkap Tabir Klien (Frontend) vs Peladen (Server)

Semua implementasi teknis yang kamu bangun selama 2 minggu ke belakang (seperti struktur markah HTML, deklarasi gaya estetika CSS, serta manipulasi *DOM* menggunakan *JavaScript*) berlangsung seutuhnya di sisi **Frontend (Klien)**. 
Untuk menyederhanakannya, konsep ini dapat diibaratkan seperti sebuah operasional restoran modern:
- **Klien / Frontend**: Adalah area ruang jamuan makan para pelanggan (tamu). Ini merupakan tempat menampilkan buku menu interaktif (HTML/CSS) tempat pelanggan berkomunikasi melalui pramusaji untuk mengirimkan pesanan (JavaScript).
- **Server / Backend**: Merupakan representasi dari **Dapur Restoran**. Area tertutup yang sepenuhnya dikendalikan staf ahli; amat sibuk dan mengelola akses perihal bahan vital. Di sinilah bahan baku mentah (data dari *Database*) difilter, dikalkulasi, dan diolah menghasilkan data valid (*JSON/informasi*) sesuai standar operasional yang dituntut oleh permintaan pelayan.

Pengguna (*Frontend*) **TIDAK PERNAH** diizinkan memiliki akses langsung ke 'dapur' (*Database* dan *Logic Server*). Jika diizinkan, keamanan aplikasi akan terancam karena pengguna bisa memanipulasi atau mencuri data sesuka hati. Pemisahan batas inilah yang menjadi fondasi keamanan siber pada sebuah aplikasi.

### Request Flow: Siklus Perjalanan Sebuah Permintaan

Saat kamu menekan tombol "Login" di sebuah halaman *Frontend*, beginilah alur (*flow*) yang terjadi:
1. **Request (Permintaan)**: *Frontend* membungkus data (*username* & kata sandi) dan mengirimkannya melalui jaringan internet (biasanya menggunakan HTTP POST) ke *Server Backend*.
2. **Processing (Pemrosesan)**: *Server* (Dapur) menerima data tersebut, lalu memprosesnya (misalnya mencocokkan kata sandi dengan data di *Database*).
3. **Response (Balasan)**: Setelah diproses, *Server* mengirimkan balasan (*HTTP Response*) kembali ke *Frontend*. Balasan ini berisi status (misal: `200 OK`) dan data yang diminta (misal: data profil pengguna).
4. **Render (Tampilan)**: *Browser* di sisi *Frontend* membaca respons tersebut dan memperbarui tampilan layar, misalnya mengalihkan pengguna ke halaman *Dashboard*.

### API: Pelayan Jembatan Komunikasi

Zaman dulu, *Server* bertugas memproses data sekaligus membuat tampilan (mengirim *file* HTML utuh ke *browser* klien). 

Namun di era aplikasi modern (seperti aplikasi *mobile* Android/iOS, atau *framework* web modern seperti React/Vue), *Frontend* sudah bisa mengurus tampilannya sendiri. *Frontend* kini hanya membutuhkan kiriman **datanya** saja dari *Server*.

**API (Application Programming Interface)** adalah jembatan komunikasi yang tugasnya hanya mengirim dan menerima "Data Murni" ini antara *Frontend* dan *Backend* (tanpa mengirimkan desain atau kode HTML). Standar format data yang paling populer digunakan oleh API saat ini adalah **JSON** (*JavaScript Object Notation*).

```json
// Contoh Wujud Standar Transmisi Data Murni (JSON)
{
 "status_respons": "sukses",
 "identitas_pengguna": "AdminTISS",
 "hak_otoritas": "SuperAdmin",
 "session_token": "a8f9c1b2..."
}
```

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari kita lihat wujud asli dari respons *Public API* secara langsung.

1. Buka *browser* kamu, lalu kunjungi URL berikut: `https://pokeapi.co/api/v2/pokemon/pikachu`
2. Perhatikan tampilannya! Situs tersebut hanya menampilkan teks mentah tanpa desain visual, tanpa tombol interaktif, dan tanpa elemen HTML apa pun.
3. Teks yang diapit oleh kurung kurawal tersebut adalah format **JSON**. Begitulah cara *Backend API* merespons: murni hanya mengirim data.
4. Data JSON ini nantinya dapat dibaca oleh *Frontend* (baik itu *web* maupun aplikasi *mobile*) untuk kemudian dihias dan ditampilkan dengan desain visual yang cantik ke pengguna.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa memisahkan *Frontend* dan *Backend* sangat penting dalam pengembangan aplikasi modern, terutama dari segi keamanan?</summary>

**Jawaban:** Pemisahan ini (*separation of concerns*) penting agar kunci otentikasi *database*, sandi administratif, dan algoritma rahasia tidak terekspos di sisi *Frontend*. Jika *Backend* dan *Frontend* dicampur (semuanya berjalan di *browser* klien), siapa pun bisa melihat kode dan kata sandi rahasia tersebut melalui fitur *Inspect Element* di *browser*.
</details>

<details>
<summary>❓ Jika *Frontend* diibaratkan sebagai Ruang Makan Pelanggan di restoran dan *Backend* sebagai Dapur, maka siapa yang berperan sebagai "Pelayan" yang menjembatani pesanan di antara keduanya?</summary>

**Jawaban:** **API (Application Programming Interface)**.
</details>

<details>
<summary>❓ Apa kepanjangan dari **JSON**, format standar yang paling sering digunakan API untuk mengirimkan data (ditandai dengan struktur tanda kurung kurawal `{ }`)?</summary>

**Jawaban:** **JSON** singkatan dari **JavaScript Object Notation**.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami perbedaan peran antara *Frontend* (Klien) dan *Backend* (Server).
- [ ] Saya memahami alur komunikasi *Request-Response* dari *browser* hingga *server* membalasnya.
- [ ] Saya mengerti peran dan tujuan dari *API*.
- [ ] Saya sudah mencoba mengakses sebuah *Public API* dan melihat format JSON secara langsung di *Mini Lab*.
- [ ] Saya sudah menjawab semua pertanyaan di bagian *Quiz Kilat*.

---

## 🔗 Resources

- [MDN: Client-Server Overview](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Client-Server_overview) — Penjelasan detail komprehensif pedoman wewenang peranan pengerjaan *backend* bagi spesialisasi jaringan web.

---

## ➡️ Besok

**Day 2: Node.js Fundamentals** — Hari ini kamu telah mempelajari teori *Backend*. Besok, kita akan langsung terjun ke aspek teknis! Kita akan menggunakan **Node.js**, sebuah teknologi yang memungkinkan bahasa *JavaScript* (yang awalnya hanya bisa berjalan di dalam *browser*) untuk berjalan secara independen di sistem operasi sebagai peladen *Backend*!

---

*📅 TISS Null Teaming · Week 12 · Day 1 · FORGE Rank*
